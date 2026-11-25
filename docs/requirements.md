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
Can configure the quiniela, open registration, and record outcomes.

### Bot
Validates actions, stores state, assigns teams, and publishes updates.

## 3. MVP Boundaries

- Group-based interaction.
- One active quiniela per group.
- Team count determines participant capacity.
- The primary acceptance scenario has eight teams.
- No football rankings, fixed brackets, or sport-specific rules required.
- No withdrawals, substitutions, or repeated draws.
- No payments or prize handling.

## 4. Functional Requirements

### FR-01 — Create a Quiniela
Priority: Must

An authorized administrator can create a draft quiniela with a title.

Acceptance:
- A second non-terminal quiniela cannot be created in the same group.
- Other groups have independent quiniela state.

### FR-02 — Configure Teams
Priority: Must

An authorized administrator can add and review teams before opening
registration.

Acceptance:
- At least two teams are required.
- Empty names are rejected.
- Duplicate names, ignoring surrounding whitespace and letter case,
  are rejected.
- Teams cannot be changed after registration opens.

### FR-03 — Open Registration
Priority: Must

An authorized administrator can open registration after confirming
the team list.

Acceptance:
- The bot publishes a Spanish registration message.
- The message displays available slots and the no-withdrawal rule.
- The message includes a "Participar" button.

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

### FR-05 — Draw Automatically
Priority: Must

The final successful registration triggers random team assignment.

Acceptance:
- Each participant receives exactly one team.
- Each team is assigned exactly once.
- Final registration and assignment persistence are atomic.
- Assignments cannot be rerolled or modified.
- Repeated actions or restarts do not create another draw.
- Assignments are stored before being announced.
- Failed announcements can be retried without changing assignments.

### FR-06 — Record an Outcome
Priority: Must

An authorized administrator identifies the advancing team and the
eliminated team after a completed elimination series.

Acceptance:
- Both teams belong to the current quiniela.
- Both teams are still active.
- The two selected teams are different.
- The bot displays the proposed outcome and requests confirmation.
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
- Before the draw: registration count and capacity.
- After the draw: participant-to-team assignments.
- During play: active and eliminated teams and participants.
- After completion: the winning team and participant.

### FR-08 — Complete the Quiniela
Priority: Must

The quiniela completes when exactly one team remains active.

Acceptance:
- The remaining team's participant is the winner.
- Further elimination actions are rejected.
- The final outcome is stored before the winner announcement.
- Announcement retries do not change the completed outcome.

### FR-09 — Cancel a Quiniela
Priority: Should

An authorized administrator can cancel the entire quiniela
after explicit confirmation.

Acceptance:
- Cancellation is distinct from participant withdrawal.
- Historical registrations and assignments remain stored.
- Further registrations and outcomes are rejected.
- Cancellation does not trigger a redraw.
- A new quiniela may subsequently be created.

### FR-10 — Correct an Administrative Mistake
Priority: Should

A controlled correction mechanism should be designed before release.

Acceptance:
- Previous results are not silently overwritten.
- Corrections are authorized, confirmed, and audited.
- The handling of dependent outcomes and completed quinielas
  must be explicitly decided before implementation.

Until a correction workflow exists, the bot must not expose an
unsafe result-editing action.

## 5. Non-Functional Requirements

### NFR-01 — Authorization
Validate the acting user's administrative authorization for every
privileged action.

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

Retention and deletion rules remain a release decision.

### NFR-06 — Spanish Interface
All user-facing messages and buttons use Mexican Spanish.

### NFR-07 — Operational Independence
Deployment must not modify or interfere with the existing OCI bot.

### NFR-08 — Maintainability
Separate Telegram interaction, application/domain behavior, and storage.

## 6. Out of Scope

- Sports-result APIs.
- Score aggregation and tie-breakers.
- Automatic bracket generation.
- Predictions or points-based rankings.
- Payments, betting, and prize management.
- Withdrawals and participant substitutions.
- Broadcast-channel support.
- Runtime AI.
- Web administration.

## 7. End-to-End Acceptance Scenario

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
- Outcome involving an already eliminated team.
- Repeated draw or outcome callback.
- Announcement failure after a committed state change.

## 8. Open Decisions

- Python version and Telegram library.
- Existing OCI capacity and deployment supervisor.
- Maximum supported team count.
- Detailed result-correction workflow.
- Data retention and deletion policy.
- Exact commands and administrator interaction flow.
- Delivery deadline and weekly development availability.