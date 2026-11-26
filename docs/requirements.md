# Product Requirements

## 1. Purpose

Provide a simple Telegram-group workflow for recreational quinielas
in which each participant receives a randomly assigned tournament team.

The owner/admin controls tournament outcomes.
The bot controls registration, assignments, persistence, and status updates.

## 2. Actors

### Group Member

Can join an open quiniela and view its public status.

### Group Owner or Authorized Administrator

Can configure the quiniela, open registration, record outcomes,
and cancel a non-terminal quiniela.

Accepted MVP authorization policy:
- The current Telegram group owner and current group administrators
  are authorized.
- There is no separate bot-managed administrator list.
- Telegram group-role changes determine authorization.
- Administrative actions require an identifiable acting user.
- Authorization is checked for each privileged action, including
  final confirmation.
- If authorization cannot be verified, no state is changed.

### Bot

Validates actions, stores state, assigns teams, and publishes updates.

## 3. MVP Boundaries

- Group-based interaction.
- One non-terminal quiniela per group.
- Support for 2 to 32 teams inclusive.
- Team count determines participant capacity.
- Powers of two are not required.
- The primary acceptance scenario has eight teams.
- No football rankings, fixed brackets, or sport-specific rules required.
- No withdrawals, substitutions, or repeated draws.
- No payments or prize handling.

Lifecycle:
- DRAFT: team configuration.
- OPEN: registration available.
- ACTIVE: assignments stored; outcomes may be recorded.
- COMPLETED: exactly one active team remains.
- CANCELLED: the entire quiniela has been closed.

COMPLETED and CANCELLED are terminal states.

## 4. Functional Requirements

### FR-01 — Create a Quiniela

Priority: Must

An authorized administrator can create a draft quiniela with a title.

Acceptance:
- A second non-terminal quiniela cannot be created in the same group.
- Other groups have independent quiniela state.
- A new quiniela does not overwrite historical records.

### FR-02 — Configure Teams

Priority: Must

An authorized administrator can add and review teams before opening
registration.

Acceptance:
- The team count must be between 2 and 32 inclusive.
- Powers of two are not required.
- Empty names are rejected.
- Duplicate names, ignoring surrounding whitespace and letter case,
  are rejected.
- Teams cannot be changed after registration opens.

### FR-03 — Open Registration

Priority: Must

An authorized administrator can open registration after confirming
the team list.

Acceptance:
- The bot displays the final team list and capacity before confirmation.
- Opening follows the shared administrative confirmation rules.
- The team list becomes locked.
- The bot publishes a Spanish registration message.
- The message displays available slots and the no-withdrawal rule.
- The message includes a Join button labeled in Mexican Spanish.

### FR-04 — Register a Participant

Priority: Must

A group member can claim one available slot.

Acceptance:
- Identity is based on Telegram user ID, not username.
- Duplicate registration does not consume another slot.
- Full or closed registration rejects new entries.
- Participant count never exceeds team count.
- No withdrawal or substitution action is available.
- Leaving the group does not free a registered slot.
- Buttons from another or older quiniela cannot register the user
  into the wrong quiniela.

### FR-05 — Draw Automatically

Priority: Must

The final successful registration triggers random team assignment.

Acceptance:
- Each participant receives exactly one team.
- Each team is assigned exactly once.
- Final registration and assignment persistence are atomic.
- Assignments cannot be rerolled or modified.
- Repeated actions or restarts do not create another draw.
- Assignments and announcement intent are stored before publication.
- Failed announcements can be retried without changing assignments.
- The quiniela becomes ACTIVE when assignments are committed.

### FR-06 — Record an Outcome

Priority: Must

An authorized administrator records one completed elimination outcome
at a time by identifying the advancing team and the eliminated team.

The bot does not model individual matches or series.

Acceptance:
- The quiniela must be ACTIVE.
- Both teams belong to the current quiniela.
- Both teams are still active.
- The selected teams are different.
- The bot displays the proposed outcome and affected participants.
- Recording follows the shared administrative confirmation rules.
- The advancing team remains active.
- The other team and its participant are marked eliminated.
- The confirming administrator and outcome are recorded.
- A repeated confirmation does not apply the outcome twice.
- Eliminated participants are not removed from the Telegram group.

The administrator is authoritative about sporting results.
The bot does not verify fixtures, scores, or tournament tie-breakers.

### FR-07 — Show Status

Priority: Must

Group members can view the quiniela state.

Acceptance:
- Before the draw: team list, registration count, and capacity.
- After the draw: participant-to-team assignments.
- During play: active and eliminated teams and participants.
- After completion: the winning team and participant.
- After cancellation: canceled status without deleting history.

### FR-08 — Complete the Quiniela

Priority: Must

The quiniela completes when exactly one team remains active.

Acceptance:
- The remaining team's participant is the winner.
- Further elimination actions are rejected.
- Completion and the final outcome are committed together.
- Announcement intent is stored before publishing the winner.
- Announcement retries do not change the completed outcome.

### FR-09 — Cancel a Quiniela

Priority: Must

An authorized administrator can cancel the entire quiniela
after explicit confirmation.

Acceptance:
- Cancellation follows the shared administrative confirmation rules.
- Cancellation is permitted only in DRAFT, OPEN, or ACTIVE.
- COMPLETED and CANCELLED quinielas cannot be canceled.
- Cancellation is distinct from participant withdrawal.
- Historical registrations, assignments, and outcomes remain stored.
- Further registrations and outcomes are rejected.
- Cancellation does not trigger a redraw or repair an outcome.
- A new quiniela may subsequently be created as a distinct record.

### FR-10 — Result Correction Limitation

Priority: Deferred

The first implementation has no correction, direct-edit, or undo action
for confirmed outcomes.

An incorrect confirmed outcome cannot be repaired in this version.
Cancellation is not a result correction.

Release gate:
- Before use with real participants, explicitly approve this limitation
  or implement a separately designed and tested correction workflow.

## 5. Administrative Confirmation Rules

These rules apply to registration opening, outcome recording,
and cancellation.

- Only the initiating administrator may confirm.
- Recheck current authorization at confirmation.
- Confirmations expire 10 minutes after creation.
- A confirmation is expired at or after its expiration timestamp.
- Reject consumed confirmations without repeating their mutation.
- Reject confirmations if the business-state version changed.
- Stale or expired actions must be initiated again.

Business-state changes include:
- Title or team-list changes.
- Lifecycle transitions.
- Successful registrations and the automatic draw.
- Confirmed outcomes.
- Cancellation.

Creating a pending action, viewing status, recording delivery attempts,
and retrying announcements do not change the business-state version.

A successful transaction that changes business state increments
the version once.

## 6. Non-Functional Requirements

### NFR-01 — Authorization

Validate the acting user's administrative authorization for every
privileged action and confirmation.

### NFR-02 — Isolation

Every operation must be scoped to the relevant group and quiniela.

### NFR-03 — Persistence

Committed registrations, assignments, and outcomes survive restarts.

### NFR-04 — Concurrency and Duplicate Handling

Concurrent requests and repeated Telegram interactions must not
produce extra participants, redraws, or repeated eliminations.

### NFR-05 — Privacy

Store only the data required to operate and audit the quiniela.
Do not store full chat histories.

Approve retention and deletion rules before a real-participant pilot.

### NFR-06 — Spanish Interface

All actual user-facing messages and buttons use Mexican Spanish.
Repository documentation and code identifiers use English.

### NFR-07 — Operational Independence

Deployment must not modify or interfere with the existing OCI bot.

### NFR-08 — Maintainability

Separate Telegram interaction, application/domain behavior, and storage.

### NFR-09 — Announcement Recovery

Committed state changes must include stored announcement intent
when publication is required.

Delivery retries must not repeat business actions.
Exactly-once Telegram message delivery is not guaranteed.

## 7. Out of Scope

- Sports-result APIs.
- Score aggregation and tie-breakers.
- Automatic bracket generation.
- Predictions or points-based rankings.
- Payments, betting, and prize management.
- Withdrawals and participant substitutions.
- Broadcast-channel support.
- Runtime AI.
- Web administration.
- Result correction in the first implementation.

## 8. End-to-End Acceptance Scenario

1. An administrator registers eight distinct teams.
2. Registration opens for eight participants.
3. Eight distinct users register.
4. The eighth registration creates one persistent random assignment.
5. The bot publishes all eight unique assignments.
6. The administrator confirms seven valid elimination outcomes.
7. Exactly one team and its participant remain.
8. The bot announces the winner.
9. A restart preserves the recorded state.

Negative scenarios:
- Duplicate registration.
- Concurrent attempts to claim the last slot.
- Unauthorized administrative action.
- Expired, stale, or consumed confirmation.
- Outcome involving an already eliminated team.
- Repeated draw or outcome callback.
- Announcement failure after a committed state change.

Rehearse cancellation separately from the completed-winner scenario.

## 9. Open Decisions

- Python version and Telegram library.
- Existing OCI capacity and deployment supervisor.
- Acceptance of the correction limitation or implementation of a
  correction workflow before real-participant release.
- Data retention and deletion policy.
- Exact commands and administrator interaction layout.
- Delivery deadline and weekly development availability.