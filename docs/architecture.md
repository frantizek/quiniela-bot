# Architecture

Status: Accepted MVP direction with unresolved environment details.

Product authority: docs/requirements.md.
Decision authority: docs/decisions.md.

## 1. Goals

- Keep the implementation small and understandable.
- Separate Telegram interactions from business behavior.
- Preserve state across restarts.
- Prevent duplicate registrations, draws, and outcomes.
- Deploy independently from the existing OCI bot.
- Avoid football-specific calculations.

## 2. Logical Structure

Telegram Group
    |
    v
Telegram Adapter
    - Commands and callbacks
    - Actor and group identification
    - Current-role authorization
    - Mexican Spanish interface
    |
    v
Application Services
    - Configuration and lifecycle
    - Registration and draw
    - Administrative confirmations
    - Outcomes and cancellation
    |
    v
SQLite Persistence
    - Business records
    - Pending actions
    - Audit events
    - Pending announcements

Core rules must not depend on Telegram handlers.

## 3. Lifecycle

DRAFT -> OPEN -> ACTIVE -> COMPLETED

DRAFT, OPEN, and ACTIVE may transition to CANCELLED.

- DRAFT: configure the title and teams.
- OPEN: teams are locked; registration is available.
- ACTIVE: assignments exist; outcomes may be recorded.
- COMPLETED: exactly one team remains active.
- CANCELLED: the entire quiniela is closed.

COMPLETED and CANCELLED are terminal.
One non-terminal quiniela is allowed per group.

Final registration and drawing transition OPEN directly to ACTIVE.
There is no separately committed DRAWING state.

## 4. Business-State Version

Initialize each new quiniela at version 1.

Increment the version exactly once per successful transaction that
changes existing quiniela business state.

Changes include:
- Title or team-list changes.
- Lifecycle transitions.
- Successful registrations and assignments.
- Confirmed outcomes.
- Cancellation.

Do not increment it for:
- Pending-action creation.
- Status views.
- Delivery attempts.
- Announcement retries.
- Rejected, failed, rolled-back, or duplicate actions.

A pending action stores the expected version.
A mismatch makes confirmation stale.

The authoritative policy is D-011.

## 5. Data Model

Exact schema, indexes, and migration scripts remain implementation tasks.

### Quiniela
- ID
- Telegram group ID
- Title
- State
- Business-state version
- Creator user ID
- Created and updated timestamps

### Team
- ID
- Quiniela ID
- Display name
- Normalized name

Names must be non-empty and unique within a quiniela.
Normalization ignores surrounding whitespace and letter case.
Support 2 to 32 teams.

### Participant
- ID
- Quiniela ID
- Telegram user ID
- Display-name snapshot
- Registration timestamp

Use Telegram user ID as identity.
Enforce uniqueness within the quiniela.

### Assignment
- Quiniela ID
- Participant ID
- Team ID

Each participant and team occurs once per quiniela.
Assignments are immutable.

### Outcome
- ID
- Quiniela ID
- Advancing team ID
- Eliminated team ID
- Confirming administrator user ID
- Confirmation timestamp
- Unique action identifier

A team is active if it has no committed elimination outcome.
Participant status follows the assigned team.

### Pending Action
- ID
- Quiniela ID
- Initiating administrator user ID
- Action type and payload
- Expected business-state version
- Expiration timestamp
- Confirmation status

### Audit Event
- ID
- Quiniela ID
- Action type
- Actor user ID
- Timestamp
- Minimal relevant details

### Pending Announcement
- ID
- Related event ID
- Destination group ID
- Message type and required rendering data
- Delivery state
- Retry metadata
- Telegram message ID when available

Constraints must prevent cross-quiniela references and duplicates.
Audit records must not contain secrets or full chat histories.

## 6. Authorization and Confirmation

Authorize the current group owner and all current group administrators.
Do not maintain a separate authorized-user list.

Reject unidentified administrative actors.
Fail closed if current authorization cannot be verified.

For opening, outcomes, and cancellation:
- Only the initiating administrator may confirm.
- Recheck authorization at confirmation.
- Expire the action after 10 minutes.
- Reject consumed or stale actions.
- Validate current state inside the write transaction.

Do not treat callback contents as authoritative business records.

## 7. Transactions

### Draft Creation and Editing

Creation:
- Enforce one non-terminal quiniela per group.
- Initialize the new quiniela at version 1.

Editing:
- Allow only in DRAFT.
- Validate title and team changes.
- Increment the version once per successful state-changing transaction.

### Opening Registration

After current authorization is verified:

1. Validate pending-action ownership, expiration, and expected version.
2. Require DRAFT and 2 to 32 valid teams.
3. Transition to OPEN.
4. Increment the version once.
5. Store audit and announcement intent.
6. Consume the pending action.
7. Commit atomically.

### Registration and Draw

Within one write transaction:

1. Require OPEN.
2. Reject duplicate users or exhausted capacity.
3. Insert the participant.
4. If capacity is reached, create one-to-one random assignments.
5. Transition to ACTIVE if assignments were created.
6. Increment the version once.
7. Store audit and required announcement intent.
8. Commit atomically.

Use an OS-backed random source.
Persisted assignments are authoritative.
A failed transaction must leave no partial final registration or draw.

### Outcome Confirmation

After current authorization is verified:

1. Validate the pending action.
2. Require ACTIVE.
3. Require two different active teams from the same quiniela.
4. Store the outcome once.
5. Transition to COMPLETED if one active team remains.
6. Increment the version once.
7. Store audit and announcement intent.
8. Consume the pending action.
9. Commit atomically.

### Cancellation

After current authorization is verified:

1. Validate the pending action.
2. Require DRAFT, OPEN, or ACTIVE.
3. Transition to CANCELLED.
4. Increment the version once.
5. Store audit and announcement intent.
6. Consume the pending action.
7. Commit atomically.

Preserve registrations, assignments, and outcomes.

## 8. Announcement Recovery

Store publication intent with the business transaction.
Send only after commit.

Retry pending announcements after delivery failures or restart.
Never repeat a draw, elimination, or cancellation to retry publication.

An interrupted send can leave delivery uncertain.
Exactly-once Telegram message delivery is not guaranteed.

## 9. Runtime Direction

- Python.
- SQLite.
- One application process.
- Telegram long polling.
- Separate OCI service, token, environment, and database.

Do not run multiple polling processes for this bot.
Python version, library, OCI capacity, and supervisor remain open.

## 10. Security and Operational Gates

- Keep secrets outside Git and AI context.
- Use synthetic development data.
- Use parameterized SQL.
- Escape user-controlled message content.
- Scope every action to its group and quiniela.
- Test migrations, backup, restore, and rollback before deployment.
- Approve retention and deletion before real-participant use.
- Resolve the correction release gate before real-participant use.

## 11. Exclusions

No score calculation, sports APIs, brackets, payments, withdrawals,
substitutions, channels, or runtime AI.

No result editing or undo in the first implementation.

## Document Boundary

This file describes architecture.
Accepted decisions are recorded separately in docs/decisions.md.