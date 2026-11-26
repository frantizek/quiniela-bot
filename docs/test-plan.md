# Test Plan

Status: Environment smoke tests passed; product verification remains planned.

## 1. Tooling and Commands

Use pytest, temporary SQLite databases, and mocked Telegram responses.

From the repository root:

- uv run --locked pytest --collect-only -q
- uv run --locked pytest -q
- uv run --locked ruff check quiniela_bot tests
- uv run --locked ruff format --check quiniela_bot tests

Current verification:
- Three environment tests collected and passed.
- Source lint passed.
- Source formatting passed.

No product acceptance tests have run.

## 2. Strategy

Use:
1. Domain unit tests without Telegram.
2. SQLite integration tests.
3. Mocked Telegram adapter tests.
4. Private-group rehearsal.

Use synthetic data and controllable clocks.
Use deterministic randomness fixtures where appropriate.

Verify valid, immutable assignment permutations.
Do not claim statistical fairness or independent public verifiability.

## 3. Environment Smoke Tests

Implemented in tests/test_environment.py:

- Project interpreter uses Python 3.12.
- Application package imports.
- Telegram dependency matches the initial 22.8 pin.

These tests do not validate business behavior.
Update the version assertion during an approved dependency upgrade.

## 4. Planned Core Tests

| ID | Scenario | Expected result |
|---|---|---|
| T-01 | Different groups | Independent state |
| T-02 | Second non-terminal quiniela | Rejected in the same group |
| T-03 | Counts 1, 2, 3, 8, 32, 33 | Only 2 through 32 accepted |
| T-04 | Empty or duplicate normalized names | Rejected |
| T-05 | Team edits after opening | Rejected |
| T-06 | Duplicate registration | No additional participant |
| T-07 | Same user in different groups | Allowed |
| T-08 | Concurrent final-slot requests | Capacity not exceeded |
| T-09 | Final registration | Complete unique assignments |
| T-10 | Draw transaction failure | No partial registration or draw |
| T-11 | Restart after draw | Original assignments retained |
| T-12 | Repeated callback | No redraw |
| T-13 | Identical outcome teams | Rejected |
| T-14 | Foreign or eliminated outcome team | Rejected |
| T-15 | Valid outcome | One team eliminated |
| T-16 | Final outcome | One winner and COMPLETED |
| T-17 | Outcome outside ACTIVE | Rejected |
| T-18 | Cross-quiniela references | Rejected |
| T-19 | Concurrent outcomes sharing a team | At most one valid mutation |
| T-20 | 32-participant draw | 32 unique assignments |

## 5. Planned Authorization Tests

- Current owner and administrators are authorized.
- Ordinary members cannot perform privileged actions.
- Unidentified actors and lookup failures cause no mutation.
- Lost administrator role prevents confirmation.
- A different administrator cannot confirm.
- Confirmations are eligible before expiration, subject to other checks.
- Confirmation at or after expiration is rejected.
- Stale or consumed confirmations do not mutate state.
- Concurrent confirmations produce at most one mutation.
- Wrong-group and wrong-quiniela callbacks are rejected.

Apply these checks to opening, outcomes, and cancellation.

## 6. Planned Business-Version Tests

- New quiniela initializes at version 1.
- Title and team changes increment once per successful transaction.
- Opening increments exactly once.
- Registration increments exactly once.
- Final registration, draw, and ACTIVE transition increment once together.
- Ordinary outcome increments exactly once.
- Final outcome and COMPLETED transition increment once together.
- Cancellation increments exactly once.

Version remains unchanged for:
- Pending-action creation.
- Status views.
- Delivery attempts.
- Announcement retries.
- Rejected, rolled-back, failed, or duplicate actions.

Non-mutating operations must not invalidate otherwise valid confirmations.

## 7. Planned Cancellation Tests

- Confirmed cancellation succeeds in DRAFT, OPEN, and ACTIVE.
- COMPLETED and CANCELLED reject cancellation.
- Historical records remain stored.
- Registration and outcomes are rejected after cancellation.
- A new quiniela does not overwrite history.
- Cancellation does not redraw or repair a result.

## 8. Planned Exclusion Tests

Verify no supported action exists for:
- Withdrawal or substitution.
- Assignment editing or reroll.
- Outcome correction, editing, or undo.

Fabricated callbacks must not mutate records.

Verify no sports lookup or sporting-result calculation is invoked.
Elimination must never remove a participant from Telegram.

## 9. Planned Persistence and Recovery Tests

- Business mutation, audit, and announcement intent commit together.
- Failed transactions leave no partial state.
- Failed publication does not undo or repeat business actions.
- Restart retries pending announcements.
- Uncertain delivery does not repeat mutations.
- Consumed confirmations remain consumed after restart.
- Backup restore preserves lifecycle, assignments, and outcomes.

## 10. Planned Interface Checks

- Actual messages and buttons use Mexican Spanish.
- User-controlled names render safely.
- Capacity and no-withdrawal rules are clear.
- Outcome confirmation identifies teams and participants.
- Rejection feedback explains the relevant failure.

## 11. End-to-End Scenarios

### Eight Teams

1. Configure eight teams.
2. Register eight distinct participants.
3. Verify eight unique assignments.
4. Restart and verify persistence.
5. Confirm seven valid outcomes.
6. Verify one winner and COMPLETED.
7. Restart and verify completed state.
8. Attempt repeated and unauthorized actions.

### Three Teams

1. Configure three teams.
2. Register three participants.
3. Verify three unique assignments.
4. Confirm one elimination.
5. Confirm an elimination between the remaining teams.
6. Verify one winner and COMPLETED.

No bracket rounds or power-of-two constraint are required.

### Cancellation

Rehearse cancellation separately in DRAFT, OPEN, and ACTIVE.

## 12. Release Gates

Before real-participant use:
- Critical automated tests pass.
- Private-group rehearsal passes.
- Restore is demonstrated.
- Deployment isolation is verified.
- Retention and deletion are approved.
- Correction limitation is accepted or correction is tested.
- No secrets or live records are committed.

## Document Boundary

Only the environment smoke tests and tooling checks are currently passed.
All product and operational checks above remain planned.