# Test Plan

Status: Initial verification plan.
Framework and test commands remain to be selected.

## 1. Strategy

Use:
1. Domain unit tests without Telegram.
2. SQLite integration tests with temporary databases.
3. Telegram adapter tests with mocked API responses.
4. A private-group end-to-end rehearsal.

Use synthetic users and teams.
Do not use production databases or chat histories.

Use controllable clocks for expiration tests.
Use controllable randomness for deterministic fixtures.

Draw tests verify valid permutations and immutability.
They do not establish independent public verifiability or statistical fairness.

## 2. Core Behavior

| ID | Scenario | Expected result |
|---|---|---|
| T-01 | Different groups | Independent quiniela state |
| T-02 | Second non-terminal quiniela in one group | Rejected |
| T-03 | Team counts 1, 2, 3, 8, 32, 33 | Only 2 through 32 accepted |
| T-04 | Empty or duplicate normalized names | Rejected |
| T-05 | Team edits after opening | Rejected |
| T-06 | Duplicate user registration | No extra participant |
| T-07 | Same user in different groups | Allowed |
| T-08 | Concurrent final-slot requests | Capacity never exceeded |
| T-09 | Final registration | Complete unique assignments |
| T-10 | Draw transaction failure | No partial final registration or assignments |
| T-11 | Restart after draw | Original assignments preserved |
| T-12 | Repeated registration callback | No redraw |
| T-13 | Identical outcome teams | Rejected |
| T-14 | Foreign or eliminated outcome team | Rejected |
| T-15 | Valid outcome | One team eliminated |
| T-16 | Final valid outcome | Exactly one winner; COMPLETED |
| T-17 | Outcome outside ACTIVE | Rejected |
| T-18 | Cross-quiniela record references | Rejected |
| T-19 | Concurrent outcomes sharing a team | At most one valid mutation |
| T-20 | Full 32-participant draw | 32 unique assignments |

## 3. Authorization and Confirmation

| ID | Scenario | Expected result |
|---|---|---|
| A-01 | Current owner or administrator | Authorized |
| A-02 | Ordinary member performs privileged action | Rejected |
| A-03 | Unidentified administrative actor | Rejected |
| A-04 | Authorization lookup fails | No mutation |
| A-05 | Administrator loses role before confirmation | Rejected |
| A-06 | Different administrator confirms | Rejected |
| A-07 | Before expiration | Eligible if other checks pass |
| A-08 | At or after expiration | Rejected |
| A-09 | Business-state version changed | Stale; rejected |
| A-10 | Consumed confirmation reused | No repeated mutation |
| A-11 | Concurrent confirmation requests | At most one mutation |
| A-12 | Wrong group or quiniela callback | Rejected |

Apply confirmation checks to opening, outcomes, and cancellation.

## 4. Business-State Version

| ID | Scenario | Expected result |
|---|---|---|
| V-01 | Create quiniela | Version initialized to 1 |
| V-02 | Change title or team list | Increment once per successful transaction |
| V-03 | Open registration | Increment exactly once |
| V-04 | Register before capacity | Increment exactly once |
| V-05 | Final registration plus draw and ACTIVE transition | Increment exactly once |
| V-06 | Confirm ordinary outcome | Increment exactly once |
| V-07 | Confirm final outcome plus COMPLETED transition | Increment exactly once |
| V-08 | Cancel quiniela | Increment exactly once |
| V-09 | Create pending action | Version unchanged |
| V-10 | View status | Version unchanged |
| V-11 | Record delivery attempt | Version unchanged |
| V-12 | Retry announcement | Version unchanged |
| V-13 | Reject, roll back, or repeat action | Version unchanged |

Verify that V-09 through V-12 do not make an otherwise valid
confirmation stale.

## 5. Cancellation

- Succeeds from DRAFT, OPEN, and ACTIVE after valid confirmation.
- Rejects COMPLETED and CANCELLED.
- Preserves registrations, assignments, and outcomes.
- Rejects subsequent registration and outcomes.
- Allows a distinct new quiniela without overwriting history.
- Does not withdraw participants or trigger a redraw.

## 6. Excluded Actions

Verify that:
- No participant withdrawal or substitution command/callback exists.
- No assignment reroll or editing action exists.
- No confirmed-outcome correction, direct-edit, or undo action exists.
- Unsupported or fabricated callbacks do not mutate records.
- No sporting-result calculation or external sports lookup is invoked.

## 7. Persistence and Announcements

- Business mutation, audit, and announcement intent commit together.
- Failed transactions leave no partial mutation.
- Failed publication does not undo or repeat business state.
- Restart retries pending announcements.
- Interrupted sends with uncertain delivery do not repeat mutations.
- Backup restore preserves lifecycle, assignments, and outcomes.
- Consumed confirmations remain consumed after restart.

## 8. Interface

- Actual bot messages and buttons use Mexican Spanish.
- User-controlled names render safely.
- Capacity and no-withdrawal rules are clear.
- Outcome confirmation identifies both teams and participants.
- Rejection messages explain stale, expired, and unauthorized actions.
- Elimination never removes a participant from the group.

## 9. End-to-End Scenarios

### Eight-Team Primary Scenario

1. Configure eight teams.
2. Register eight distinct participants.
3. Verify eight unique assignments.
4. Restart and verify persistence.
5. Confirm seven valid outcomes.
6. Verify one winner and COMPLETED.
7. Restart and verify completed state.
8. Attempt repeated and unauthorized actions.

### Three-Team Non-Power-of-Two Scenario

1. Configure three teams.
2. Register three distinct participants.
3. Verify three unique assignments.
4. Confirm one valid elimination.
5. Confirm a second valid elimination between remaining teams.
6. Verify one winner and COMPLETED.

The bot does not require bracket rounds or power-of-two team counts.

### Cancellation Scenario

Rehearse cancellation separately in DRAFT, OPEN, and ACTIVE.
Verify preserved history and rejection of subsequent actions.

## 10. Release Gates

Before real-participant use:
- Critical automated checks pass.
- Private-group rehearsal passes.
- Backup restore is demonstrated.
- Deployment isolation is verified.
- Retention and deletion rules are approved.
- Correction limitation is explicitly accepted or correction is tested.
- No secrets or live records are committed.

Record checks as passed only after execution.

## Document Boundary

This document defines planned verification.
It does not claim that any test has already run.