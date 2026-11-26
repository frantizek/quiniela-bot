# Product Requirements

## 1. Purpose

Manage recreational team-assignment quinielas in Telegram groups.

Participants receive randomly assigned teams.
The owner/admin determines advancement and elimination.
The bot manages registration, assignments, persistence, and announcements.

## 2. Actors and Authorization

### Group Member
Can register for an open quiniela and view public status.

### Group Owner or Administrator
Can configure quinielas, open registration, record outcomes, and cancel.

Authorization policy:
- Current Telegram group owner and all current administrators are authorized.
- No separate bot-managed administrator list.
- Administrative actions require an identifiable actor.
- Check current authorization for every privileged action and confirmation.
- If authorization cannot be verified, no state is changed.

### Bot
Validates actions, stores state, performs assignments, and publishes updates.

## 3. MVP Boundaries and Lifecycle

- Telegram groups.
- One non-terminal quiniela per group.
- Between 2 and 32 teams.
- Team count determines participant capacity.
- Powers of two are not required.
- One participant registration per Telegram user ID per quiniela.
- No withdrawals, substitutions, or repeated draws.

States:
- DRAFT: configure title and teams.
- OPEN: teams locked; registration available.
- ACTIVE: assignments committed; outcomes available.
- COMPLETED: exactly one active team remains.
- CANCELLED: entire quiniela closed.

COMPLETED and CANCELLED are terminal.

## 4. Functional Requirements

### FR-01 — Create a Quiniela

Priority: Must

An authorized administrator creates a draft with a title.

Acceptance:
- Reject a second non-terminal quiniela in the same group.
- Isolate different groups.
- Preserve historical quinielas.

### FR-02 — Configure Teams

Priority: Must

An authorized administrator configures teams in DRAFT.

Acceptance:
- Accept 2 to 32 teams inclusive.
- Do not require powers of two.
- Reject empty names.
- Reject duplicates ignoring surrounding whitespace and letter case.
- Reject team changes after registration opens.

### FR-03 — Open Registration

Priority: Must

An authorized administrator confirms the final team list.

Acceptance:
- Show teams, capacity, and the no-withdrawal rule before confirmation.
- Apply shared confirmation rules.
- Transition to OPEN and lock teams.
- Publish a Mexican Spanish registration message with a Join button.

### FR-04 — Register a Participant

Priority: Must

A group member claims one available slot.

Acceptance:
- Identify by Telegram user ID, not username.
- Duplicate registration does not consume capacity.
- Reject registration outside OPEN or when full.
- Never exceed team count.
- No withdrawal or substitution action.
- Leaving the group does not release a slot.
- Reject callbacks for the wrong group or quiniela.

### FR-05 — Draw Automatically

Priority: Must

Final successful registration triggers the draw.

Acceptance:
- Each participant receives one team.
- Each team is assigned once.
- Commit final registration, assignments, and ACTIVE transition atomically.
- Assignments are immutable.
- Repeated actions and restarts do not redraw.
- Store announcement intent before publication.
- Retry publication using stored assignments.

### FR-06 — Record an Outcome

Priority: Must

An authorized administrator selects the advancing and eliminated teams.

Acceptance:
- Require ACTIVE.
- Require two different active teams belonging to the quiniela.
- Display teams and assigned participants before confirmation.
- Apply shared confirmation rules.
- Eliminate only the selected losing team and its participant.
- Record the confirming administrator and outcome.
- Repeated confirmation does not repeat elimination.
- Never remove a participant from the Telegram group.

The administrator is authoritative about sporting results.
The bot does not model matches, verify fixtures, or calculate scores.

### FR-07 — Show Status

Priority: Must

Show:
- Before drawing: teams, registration count, and capacity.
- After drawing: assignments and active/eliminated status.
- After completion: winning team and participant.
- After cancellation: canceled status without deleting history.

### FR-08 — Complete the Quiniela

Priority: Must

Complete when exactly one team remains active.

Acceptance:
- Its assigned participant is the winner.
- Commit completion with the final outcome.
- Reject further outcomes.
- Store announcement intent before publication.
- Announcement retries do not change the winner.

### FR-09 — Cancel a Quiniela

Priority: Must

An authorized administrator confirms whole-quiniela cancellation.

Acceptance:
- Apply shared confirmation rules.
- Allow only in DRAFT, OPEN, and ACTIVE.
- Reject COMPLETED and CANCELLED.
- Preserve registrations, assignments, and outcomes.
- Reject subsequent registration and outcomes.
- Cancellation is not withdrawal, correction, or redraw.
- A later quiniela is a separate record.

### FR-10 — Result Correction Limitation

Priority: Deferred

No correction, direct editing, or undo of confirmed outcomes exists
in the first implementation.

Before real-participant use:
- Explicitly accept this limitation; or
- Implement an approved and tested correction workflow.

Cancellation does not repair an outcome.

## 5. Administrative Confirmation Rules

Apply to opening, outcomes, and cancellation.

- Only the initiating administrator may confirm.
- Recheck current authorization.
- Expire 10 minutes after creation.
- Reject at or after expiration.
- Reject consumed confirmations without repeating mutations.
- Reject changed business-state versions.
- Require re-initiation after expiration or staleness.

Initialize a quiniela at version 1.

Increment once per successful transaction changing existing business state:
- Title or team list.
- Lifecycle.
- Registrations and assignments.
- Confirmed outcomes.
- Cancellation.

Do not increment for:
- Pending-action creation.
- Status views.
- Delivery attempts or announcement retries.
- Rejected, failed, rolled-back, or duplicate actions.

## 6. Non-Functional Requirements

### NFR-01 — Authorization
Verify current administrative authority for privileged actions.

### NFR-02 — Isolation
Scope all operations to the correct group and quiniela.

### NFR-03 — Persistence
Committed state survives restarts.

### NFR-04 — Concurrency and Duplicates
Prevent extra registrations, redraws, and repeated eliminations.

### NFR-05 — Privacy
Store only necessary operational and audit data.
Do not store full chat histories.
Approve retention and deletion before real-participant use.

### NFR-06 — Language
Actual bot messages and buttons use Mexican Spanish.
Documentation and code identifiers use English.

### NFR-07 — Operational Independence
Do not interfere with the existing OCI bot.

### NFR-08 — Maintainability
Separate Telegram interaction, application behavior, and persistence.

### NFR-09 — Announcement Recovery
Store publication intent with relevant business transactions.
Retries must not repeat business actions.
Exactly-once Telegram delivery is not guaranteed.

## 7. Out of Scope

- Payments, betting, and prizes.
- Predictions and points-based scoring.
- Sports APIs, score calculations, and tournament-rule interpretation.
- Automatic brackets.
- Withdrawals and substitutions.
- Channels and web administration.
- Runtime AI.
- Result correction in the first implementation.

## 8. Acceptance Scenario

1. Configure eight teams.
2. Open eight registration slots.
3. Register eight distinct users.
4. Final registration creates eight unique persistent assignments.
5. Publish assignments.
6. Confirm seven valid elimination outcomes.
7. Announce exactly one winner.
8. Restart and verify preserved state.

Also verify:
- A complete three-team scenario.
- Duplicate and concurrent registration handling.
- Unauthorized, expired, stale, and repeated confirmations.
- Rejection of foreign or eliminated teams.
- Delivery failures without repeated business actions.
- Cancellation separately in each permitted state.

## 9. Open Decisions

- OCI capacity validation and systemd service configuration.
- Correction limitation acceptance before real-participant use.
- Retention and deletion.
- Final commands and button layout.
- Deadline and weekly development availability.

Python 3.12, python-telegram-bot, uv, pytest, Ruff, and systemd
are selected. See docs/decisions.md and docs/tooling.md.

## Document Boundary

This document defines required behavior, not implementation completion.