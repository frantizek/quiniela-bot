# Decision Log

## Status Definitions

- Accepted: confirmed product requirement or approved design.
- Proposed: recommendation awaiting approval.
- Open: insufficient information to decide.
- Superseded: replaced by a later decision.

Accepted direction does not mean implementation or environment
verification has occurred.

## D-001 — Administrative Authority Over Results

Status: Accepted

The owner/admin determines the advancing and eliminated teams.

The bot validates and records the action.
It does not calculate scores, interpret football rules, or verify fixtures.

## D-002 — Group-First Delivery

Status: Accepted

The MVP operates in Telegram groups.
Broadcast-channel support is deferred.

## D-003 — Registration and Assignment

Status: Accepted

Participant capacity equals team count.
One entry is allowed per Telegram user ID per quiniela.

There are no withdrawals or substitutions.
The final registration triggers an automatic random draw.
Persisted assignments cannot be rerolled or changed.

## D-004 — Language

Status: Accepted

Repository documentation, code identifiers, and developer comments
are English.

Actual Telegram messages and buttons are Mexican Spanish.
Documentation describes interface behavior in English.

## D-005 — Python and OCI

Status: Accepted

Use Python and the existing Oracle OCI infrastructure.

The new application must run independently from the existing bot.

Python version, deployment configuration, and resource capacity
remain open.

## D-006 — SQLite and Single-Process MVP

Status: Accepted

Use SQLite with explicit transactions and uniqueness constraints.
Start with one application process.

Reason:
Minimize infrastructure and operational complexity.

Revisit if multiple application instances become necessary or
measured workload exceeds the initial design.

## D-007 — Telegram-Native Authorization

Status: Accepted

Authorize the current Telegram group owner and all current administrators.
There is no separate bot-managed administrator list.

Check authorization for every privileged action and confirmation.
Reject unidentified actors and unverifiable authorization.

The bot requires administrator status with minimal necessary permissions.
Exact setup permissions remain to be validated.

## D-008 — No Match or Bracket Model

Status: Accepted

Store administrator-confirmed elimination outcomes.

Do not model match legs, scores, tournament rankings, or fixtures.
An outcome identifies an advancing team and an eliminated team.

The administrator is responsible for selecting a valid sporting outcome.

## D-009 — Transactional Announcements

Status: Accepted

Persist announcement intent with committed state changes
that require publication.

Send or retry announcements after commit.
Delivery failures must not repeat business actions.

Exactly-once message delivery is not guaranteed.

## D-010 — Initial Operational Delivery

Status: Accepted

Use long polling and a separate OCI service.

Use a separate token, environment, and database.
Do not deploy or modify infrastructure during documentation work.

Validate compatibility and capacity before deployment implementation.

## D-011 — Administrative Confirmations

Status: Accepted

Only the administrator who initiated a pending action may confirm it.
Check their current authorization again at confirmation.

Confirmations expire 10 minutes after creation.
Reject confirmation at or after the expiration timestamp.
Consumed confirmations cannot repeat a mutation.

A confirmation is stale when the quiniela's business-state version
differs from the version stored when the action was prepared.

Business-state changes include:
- Title or team-list changes.
- Lifecycle transitions.
- Successful registrations and the automatic draw.
- Confirmed outcomes.
- Cancellation.

The following do not change the business-state version:
- Creating a pending action.
- Viewing status.
- Recording delivery attempts.
- Retrying announcements.

Each successful transaction that changes existing quiniela business
state increments the version exactly once, even if it changes several
records.

Initialize a newly created quiniela at version 1.
Rejected, failed, rolled-back, or duplicate actions do not increment it.

Stale or expired actions must be initiated again.

These confirmation rules apply to:
- Opening registration.
- Recording outcomes.
- Cancellation.

Version initialization is a technical baseline clarification.
It does not change the approved confirmation policy.

## D-012 — Cancellation

Status: Accepted

Include cancellation in the MVP.

Current authorized administrators may cancel a quiniela in DRAFT,
OPEN, or ACTIVE after confirmation.

COMPLETED and CANCELLED quinielas cannot be canceled.

Preserve historical records.
Cancellation is not a withdrawal, substitution, correction, or redraw.
A new quiniela is a separate record and action.

## D-013 — Result Correction

Status: Accepted

Defer result correction from the first implementation.

Do not expose editing or undo of confirmed outcomes.
An incorrect confirmed outcome cannot be repaired in this version.

Before use with real participants, explicitly decide whether to:
- Accept this limitation for the initial release; or
- Implement a separately designed and tested correction workflow.

Cancellation does not repair an outcome.

## D-014 — Team Count

Status: Accepted

Support 2 to 32 teams inclusive.
Participant capacity equals team count.

Do not require powers of two.
Eight teams remain the primary acceptance scenario.

## Open Decisions

| ID | Decision | Required before |
|---|---|---|
| O-001 | Python version and Telegram library | Project scaffold |
| O-002 | OCI capacity and deployment supervisor | Deployment planning |
| O-004 | Accept correction limitation or design correction | Real-participant release |
| O-005 | Data retention and deletion | Real-participant pilot |
| O-006 | Final commands and button layout | Telegram adapter implementation |
| O-007 | Deadline and weekly availability | Delivery commitment |

Resolved open-decision IDs are not reused or renumbered.

## Document Boundary

This file records decisions.
Architecture details belong in docs/architecture.md.