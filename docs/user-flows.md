# User Flows

Status: MVP interaction baseline.

Descriptions are English.
Actual Telegram messages and buttons use Mexican Spanish.
Exact commands and button layout remain open.

## 1. Shared Confirmation Rules

Apply these rules to opening registration, outcomes, and cancellation:

- Only the initiating administrator may confirm.
- Recheck current authorization.
- Expire confirmation 10 minutes after creation.
- Reject confirmation at or after expiration.
- Reject consumed confirmations.
- Reject a changed business-state version.
- Require re-initiation after staleness or expiration.

See D-011 in docs/decisions.md.

## 2. Create and Configure

Actor: Current group owner or administrator

1. Request creation.
2. Bot verifies authorization and absence of another non-terminal quiniela.
3. Administrator provides a title and team names.
4. Bot validates and displays the draft.

Reject:
- Unidentified or unauthorized actors.
- Unverifiable authorization.
- Another non-terminal quiniela in the same group.
- Empty or duplicate normalized team names.
- Team counts outside 2 to 32.

Powers of two are not required.
Registration is unavailable in DRAFT.

## 3. Open Registration

Actor: Current group owner or administrator

1. Request opening.
2. Bot displays the final teams, capacity, and no-withdrawal rule.
3. Administrator confirms using the shared rules.
4. Bot commits OPEN and locks the team list.
5. Bot publishes the registration message and Join button.

Canceling the pending confirmation leaves the quiniela in DRAFT.
Changing the draft invalidates an outstanding opening confirmation.

## 4. Join

Actor: Group member

1. Press Join.
2. Bot validates group, quiniela, state, identity, and capacity.
3. Bot registers the user once.
4. Bot confirms registration and updates the count.

Reject:
- Duplicate registration.
- Closed or full registration.
- Buttons for another or older quiniela.
- Canceled or completed quinielas.

Leaving the group does not release the slot.
No withdrawal or substitution exists.

## 5. Automatic Draw

Trigger: Final successful registration

1. Store the final participant and all assignments atomically.
2. Transition to ACTIVE.
3. Store announcement intent.
4. Publish the assignment list.

Each participant gets one team.
Each team gets one participant.

There is no approval or reroll action.
Retry failed publication using the stored assignments.

## 6. Record an Outcome

Actor: Current group owner or administrator

1. Request outcome entry in ACTIVE.
2. Select the advancing team.
3. Select a different active team to eliminate.
4. Bot displays both teams and assigned participants.
5. Administrator confirms using the shared rules.
6. Bot revalidates state and commits the outcome.
7. Bot publishes the update.

Reject:
- Unauthorized or unidentified actors.
- Unverifiable authorization.
- Confirmation by another administrator.
- Expired, consumed, or stale confirmation.
- Identical teams.
- Foreign or already eliminated teams.
- A quiniela that is not ACTIVE.

The administrator determines the sporting result.
The bot does not verify fixtures or calculate scores.

Elimination does not remove the participant from the Telegram group.

## 7. Complete

Trigger: A confirmed outcome leaves one active team

1. Commit completion with the final outcome.
2. Store winner-announcement intent.
3. Publish the winning team and participant.

Reject further outcomes and cancellation.
Announcement retries do not alter the winner.

## 8. View Status

Actor: Group member

Show:
- Before drawing: title, teams, registration count, and capacity.
- During play: assignments and active/eliminated status.
- After completion: winner.
- After cancellation: canceled status and relevant historical information.

Status views do not change the business-state version.

## 9. Cancel

Actor: Current group owner or administrator

Available only in DRAFT, OPEN, and ACTIVE.

1. Request cancellation.
2. Bot explains that the entire quiniela will close.
3. Administrator confirms using the shared rules.
4. Bot commits cancellation and announcement intent.
5. Bot publishes the canceled status.

Preserve historical registrations, assignments, and outcomes.

Cancellation is not a withdrawal, correction, or redraw.
A later quiniela is a separate record.

Reject cancellation of COMPLETED or CANCELLED quinielas.

## 10. Correction Limitation

No editing or undo of confirmed outcomes exists in the first implementation.

Before real-participant use:
- Explicitly accept this limitation; or
- Implement an approved and tested correction workflow.

Cancellation does not repair an outcome.

## 11. Restart and Recovery

1. Load committed state.
2. Resume interactions.
3. Retry pending announcements.
4. Reject expired, stale, or consumed confirmations.
5. Never recreate assignments or reapply outcomes.

Duplicate recovery announcements must not produce duplicate business actions.

## Document Boundary

These flows describe interaction behavior.
Final commands and message wording remain implementation decisions.