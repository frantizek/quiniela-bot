# Decision Log

## Status Definitions

- Accepted: confirmed product requirement or approved design.
- Proposed: recommended design awaiting approval.
- Open: insufficient information to decide.
- Superseded: replaced by a later decision.

## D-001 — Administrative Authority Over Results

Status: Accepted

The owner/admin determines the advancing and eliminated teams.

The bot validates and records the action.
It does not calculate scores, interpret football rules, or verify fixtures.

Reason:
Keep the MVP simple and usable for different elimination tournaments.

## D-002 — Group-First Delivery

Status: Accepted

The MVP operates in Telegram groups.
Broadcast-channel support is deferred.

## D-003 — Registration and Assignment

Status: Accepted

Participant capacity equals team count.
One entry is allowed per Telegram user ID per quiniela.
There are no withdrawals or substitutions.
The final registration triggers the automatic draw.
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

Python version, deployment method, and resource capacity remain open.

## D-006 — SQLite and Single-Process MVP

Status: Proposed

Use SQLite with explicit transactions and uniqueness constraints.
Start with one application process.

Reason:
Minimize infrastructure and operational complexity.

Revisit if deployment requires multiple application instances or
measured workload exceeds the initial design.

## D-007 — Telegram-Native Authorization

Status: Proposed

Authorize the current Telegram group owner and all current administrators.
Do not create a separate bot-managed administrator list.

Check authorization for every privileged action and confirmation.
Reject unverifiable or unidentified administrative actors.

The bot will require administrator status with minimal permissions.

Trade-off:
Every Telegram administrator can manage the quiniela.
A narrower authorization policy would require additional product rules.

## D-008 — No Match or Bracket Model

Status: Accepted

Store administrator-confirmed elimination outcomes.
Do not model legs, scores, tournament rankings, or scheduled fixtures.

A result contains an advancing team and an eliminated team.

## D-009 — Transactional Announcements

Status: Proposed

Persist announcement intent with each committed state change.
Send or retry announcements after commit.

Reason:
Telegram delivery failures must not change business outcomes.

Exactly-once message delivery is not guaranteed.

## D-010 — Initial Operational Delivery

Status: Proposed

Use long polling and a separate service on OCI.
Do not deploy or modify infrastructure during documentation work.

Validate compatibility with the existing environment before implementation.

## Open Decisions

| ID | Decision | Required before |
|---|---|---|
| O-001 | Python version and Telegram library | Project scaffold |
| O-002 | OCI capacity and supervisor | Deployment planning |
| O-003 | Maximum team count | Team configuration implementation |
| O-004 | Result-correction rules | Release scope approval |
| O-005 | Data retention and deletion | Pilot with real users |
| O-006 | Final commands and button layout | Telegram adapter implementation |
| O-007 | Deadline and weekly availability | Delivery commitment |
| O-008 | Cancellation inclusion and permissions | Backlog approval |