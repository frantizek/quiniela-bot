# User Flows

Status: Proposed interaction design.

All actual bot messages and buttons will use Mexican Spanish.
Descriptions and button concepts below are English.

Exact commands remain undecided.

## 1. Create and Configure

Actor: Authorized administrator

1. Request creation of a quiniela.
2. Bot checks authorization and absence of another active quiniela.
3. Administrator provides a title and team names.
4. Bot validates the list.
5. Bot displays the draft for review.

Failure cases:
- Unauthorized actor.
- Existing non-terminal quiniela.
- Empty or duplicate team names.
- Fewer than two teams.
- More teams than the eventual configured maximum.

No participant registration is available in DRAFT.

## 2. Open Registration

Actor: Authorized administrator

1. Request opening of registration.
2. Bot displays the final team list, capacity, and no-withdrawal rule.
3. Administrator confirms.
4. Bot locks the team list and transitions to OPEN.
5. Bot publishes a registration message with a Join button.

Canceling this confirmation leaves the quiniela in DRAFT.

## 3. Join

Actor: Group member

1. Press Join.
2. Bot checks the current quiniela and registration capacity.
3. Bot registers the user once.
4. Bot confirms registration and updates the participant count.

Failure cases:
- Already registered.
- Registration closed.
- Capacity exhausted.
- Button belongs to an older or canceled quiniela.

Leaving the Telegram group does not release the participant's slot.

## 4. Automatic Draw

Trigger: Final successful registration

1. Bot registers the final participant and stores all assignments
   in the same transaction.
2. Bot transitions the quiniela to ACTIVE.
3. Bot publishes the full participant-to-team assignment list.

There is no administrator approval or reroll action.

If publication fails, retry publication using the stored assignments.

## 5. Record an Outcome

Actor: Authorized administrator

1. Request outcome entry.
2. Select the advancing team from active teams.
3. Select a different active team as eliminated.
4. Bot displays both teams and their assigned participants.
5. Administrator confirms.
6. Bot checks authorization and current state again.
7. Bot stores the outcome and publishes the update.

Only the administrator who initiated the pending action may confirm it.

Failure cases:
- User is no longer authorized.
- Confirmation expired or was already consumed.
- Quiniela changed since the action was prepared.
- Either selected team is no longer active.
- Quiniela is completed or canceled.

The bot does not verify whether the selected teams played each other.

## 6. Complete the Quiniela

Trigger: A confirmed outcome leaves one active team

1. Bot records completion with the final outcome.
2. Bot publishes the winning team and participant.
3. Further outcome entry is rejected.

## 7. View Status

Actor: Group member

Before the draw:
- Title.
- Team list.
- Registration count and capacity.

After the draw:
- Participant assignments.
- Active and eliminated teams.
- Current quiniela state.

After completion:
- Winning team and participant.

## 8. Cancel the Entire Quiniela

Status: Should-have feature; inclusion pending.

Actor: Authorized administrator

1. Request cancellation.
2. Bot explains that the entire quiniela will be closed.
3. Administrator confirms.
4. Bot records cancellation and publishes the status.

Historical records remain stored.
Cancellation is not an individual withdrawal or a redraw.

## 9. Correct an Outcome

Not yet designed.

Do not provide direct result editing until correction rules,
dependent-outcome handling, and audit requirements are approved.

## 10. Restart and Delivery Recovery

1. Load committed state from storage.
2. Resume normal interactions.
3. Retry pending announcements.
4. Reject stale or consumed confirmation actions.
5. Never recreate persisted assignments or reapply stored outcomes.