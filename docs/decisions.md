# Decision Log

## Status Definitions

- Accepted: approved requirement or design.
- Proposed: awaiting approval.
- Open: insufficient information.
- Superseded: replaced by a later decision.

Acceptance does not imply implementation, commit, or deployment completion.

## D-001 — Results Authority

Status: Accepted

The owner/admin determines advancing and eliminated teams.
The bot validates and records outcomes without sporting calculations.

## D-002 — Groups First

Status: Accepted

Support Telegram groups.
Defer broadcast channels.

## D-003 — Registration and Assignment

Status: Accepted

Capacity equals team count.
One registration per Telegram user ID per quiniela.

No withdrawals or substitutions.
Draw automatically when full.
Persisted assignments cannot be changed or rerolled.

## D-004 — Language

Status: Accepted

English documentation, identifiers, and developer comments.
Mexican Spanish bot messages and buttons.

## D-005 — Python and OCI

Status: Accepted

Use Python and existing OCI infrastructure.
Keep the new bot independent from the existing bot.

D-015 specifies development tooling.
Deployment configuration and capacity validation remain open.

## D-006 — SQLite and Single Process

Status: Accepted

Use SQLite with transactions and uniqueness constraints.
Run one application process initially.

Revisit based on measured workload or deployment needs.

## D-007 — Authorization

Status: Accepted

Authorize current Telegram group owner and all current administrators.
No separate authorized-user list.

Require identifiable actors.
Verify current authority for privileged actions and confirmations.
Fail closed when verification is unavailable.

The bot requires administrator status with minimal needed permissions.
Validate exact permissions before deployment.

## D-008 — No Match Model

Status: Accepted

Store advancing and eliminated teams.
Do not model scores, legs, rankings, fixtures, or brackets.

Administrators determine sporting validity.

## D-009 — Announcements

Status: Accepted

Store announcement intent with relevant business transactions.
Publish after commit.
Retries must not repeat business actions.

Exactly-once Telegram delivery is not guaranteed.

## D-010 — Deployment Direction

Status: Accepted

Use long polling and a separate systemd service on OCI.
Use a separate token, environment, and database.

systemd is selected.
Service configuration and capacity validation remain open.

No deployment is authorized by documentation or local setup.

## D-011 — Confirmation and Versioning

Status: Accepted

Only the initiating administrator may confirm.
Recheck current authorization.

Expire after 10 minutes.
Reject at or after expiration.
Reject consumed confirmations and stale business-state versions.

Initialize a new quiniela at version 1.

Increment exactly once per successful transaction changing existing:
- Title or teams.
- Lifecycle.
- Registrations or assignments.
- Outcomes.
- Cancellation.

Do not increment for:
- Pending-action creation.
- Status views.
- Delivery attempts or retries.
- Rejected, failed, rolled-back, or duplicate actions.

Require re-initiation after expiration or staleness.

Apply confirmation rules to opening, outcomes, and cancellation.

## D-012 — Cancellation

Status: Accepted

Allow confirmed cancellation in DRAFT, OPEN, and ACTIVE.
Reject COMPLETED and CANCELLED.

Preserve history.
Cancellation is not withdrawal, substitution, correction, or redraw.
A later quiniela is a separate record.

## D-013 — Correction Limitation

Status: Accepted

No outcome editing or undo in the first implementation.

Before real-participant use:
- Explicitly accept the limitation; or
- Implement an approved and tested correction workflow.

Cancellation does not repair results.

## D-014 — Team Count

Status: Accepted

Support 2 to 32 teams.
Do not require powers of two.
Eight teams remain the primary acceptance scenario.

## D-015 — Tooling

Status: Accepted

Use:
- Python 3.12.
- uv and project-local .venv.
- pyproject.toml and uv.lock.
- python-telegram-bot initially pinned to 22.8.
- pytest and Ruff.
- Standard-library sqlite3.

Repository policy requires tracking pyproject.toml, uv.lock,
and .python-version in Git.
This policy does not assert that current working changes are committed.

Do not independently maintain requirements.txt.
Generate an export if required.

Do not upgrade the existing bot.

The initial scaffold is unpackaged.
Verified versions and commands are in docs/tooling.md.

## Open Decisions

| ID | Decision | Required before |
|---|---|---|
| O-002 | OCI capacity validation and service configuration | Deployment |
| O-004 | Accept correction limitation or implement correction | Real-participant use |
| O-005 | Retention and deletion | Real-participant use |
| O-006 | Commands and button layout | Telegram integration |
| O-007 | Deadline and weekly availability | Delivery commitment |

O-001 is resolved by D-015.
Resolved IDs are not reused.

## Document Boundary

This file records decisions, not current implementation or commit status.