# Architecture

Status: Proposed MVP design.

Requirements authority: docs/requirements.md.
Decision status: docs/decisions.md.

## 1. Design Goals

- Keep the application small and understandable.
- Separate Telegram interactions from business rules.
- Preserve committed state across restarts.
- Prevent duplicate registrations, draws, and eliminations.
- Deploy independently from the existing OCI bot.
- Avoid football-specific calculations and external sports services.

## 2. Logical Structure

Telegram Group
    |
    v
Telegram Adapter
    - Commands and button callbacks
    - Actor and group identification
    - Authorization checks
    - Interface rendering
    |
    v
Application Services
    - Quiniela configuration
    - Registration and automatic draw
    - Outcome confirmation
    - Status and completion
    |
    v
Persistence
    - SQLite database
    - Audit events
    - Pending announcements

The Telegram adapter must not contain the core registration,
drawing, or elimination rules.

## 3. Quiniela Lifecycle

DRAFT -> OPEN -> ACTIVE -> COMPLETED

DRAFT, OPEN, or ACTIVE may transition to CANCELLED if the
cancellation feature is included.

Definitions:
- DRAFT: administrator configures teams.
- OPEN: team list is locked; participants may register.
- ACTIVE: all slots are filled and assignments are stored.
- COMPLETED: exactly one team remains active.
- CANCELLED: no further registration or outcomes are accepted.

OPEN transitions directly to ACTIVE when the final registration
and all assignments are committed.

There is no separately committed DRAWING state in the MVP.

Terminal states are COMPLETED and CANCELLED.
Each group may have only one non-terminal quiniela.

## 4. Proposed Data Model

### Quiniela
- ID
- Telegram group ID
- Title
- State
- Creator user ID
- Created and updated timestamps

### Team
- ID
- Quiniela ID
- Display name
- Normalized name

Normalized names ignore surrounding whitespace and letter case.
Names are unique within a quiniela.

### Participant
- ID
- Quiniela ID
- Telegram user ID
- Display-name snapshot
- Registration timestamp

Telegram user IDs are unique within a quiniela.
Usernames are not identity keys.

### Assignment
- Quiniela ID
- Participant ID
- Team ID

Each participant and team appears once per quiniela.
Assignments are immutable.

### Outcome
- ID
- Quiniela ID
- Advancing team ID
- Eliminated team ID
- Confirming administrator user ID
- Confirmation timestamp
- Unique action identifier

An active team is a team without a committed elimination outcome.
Participant elimination status follows the assigned team's status.

### Pending Action
- ID
- Quiniela ID
- Initiating administrator user ID
- Proposed action payload
- Expected quiniela version
- Expiration time
- Confirmation status

Pending actions allow confirmation without treating button contents
as authoritative state.

### Audit Event
- ID
- Quiniela ID
- Action type
- Actor user ID
- Timestamp
- Minimal relevant details

Do not store credentials or full chat messages.

### Pending Announcement
- ID
- Related event ID
- Destination group ID
- Message type and required rendering data
- Delivery state
- Retry metadata
- Telegram message ID, when available

## 5. Critical Transactions

### Registration and Draw

Within one database write transaction:

1. Verify that registration is open.
2. Reject duplicate registration or exhausted capacity.
3. Insert the participant.
4. If capacity is reached, create random one-to-one assignments.
5. Set the quiniela to ACTIVE.
6. Record audit and pending-announcement entries.
7. Commit.

Any failure rolls back the whole transaction.

Randomness must use an OS-backed random source.
Persisted assignments are the authority after commit.
Never recompute them to retry an announcement.

### Outcome Confirmation

Within one database write transaction:

1. Validate the pending action and current quiniela state.
2. Verify both teams belong to the quiniela and remain active.
3. Reject identical advancing and eliminated teams.
4. Insert the outcome once.
5. Complete the quiniela if one team remains active.
6. Record audit and pending-announcement entries.
7. Mark the pending action consumed.
8. Commit.

Administrative authorization must be checked before this transaction.
Confirmation must reject stale or already consumed actions.

## 6. Authorization

Proposed policy:
- Current Telegram group owner and administrators are authorized.
- No custom administrator list.
- Authorization is checked on initiation and confirmation.
- Administrative actions require an identifiable actor.
- Verification failures cause rejection without mutation.

The bot is proposed to operate as a group administrator with
minimal required permissions.

Exact Telegram setup permissions remain to be validated.

## 7. Announcement Recovery

Store state changes and announcement intent before sending messages.

After restart, retry pending announcements.
A failed send must never trigger a new draw or another elimination.

Do not promise exactly-once Telegram delivery.
An interrupted send may leave uncertainty about whether a message
was delivered. Duplicate announcements are preferable to corrupted state.

## 8. Runtime Direction

- Python.
- SQLite.
- One application process initially.
- Long polling proposed for Telegram updates.
- Separate token, environment, database, and service from the existing bot.

Python version, Telegram library, hosting capacity, and supervisor
remain undecided.

## 9. Security and Operations

- Secrets remain outside Git and AI context.
- Validate all callback data against stored state.
- Scope every operation to its group and quiniela.
- Use parameterized database queries.
- Escape user-controlled text when rendering Telegram messages.
- Use synthetic development data.
- Document backups, restore, migrations, and rollback before deployment.

## 10. Deferred Features

- Result correction until its safety rules are approved.
- Channels.
- Sports APIs and score calculations.
- Automatic tournament brackets.
- Payments.
- Multiple active quinielas in one group.