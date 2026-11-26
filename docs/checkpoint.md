# Project Checkpoint

## Current Stage

The initial documentation and local scaffold are complete.
The baseline was published to GitHub.

Workflow setup is verified on chore/development-workflow:
commit e2484b6 was pushed and PR #1 is open, not merged.
GitHub CI check "Python quality" completed successfully.
Main protection was applied and verified.

No configuration-validation implementation, Telegram connection,
or OCI deployment has occurred.

## Repository Baseline

- Repository: frantizek/quiniela-bot.
- Visibility: Public.
- Default intended branch: main.
- Published scaffold commit: d70a4d3.
- Current task branch: chore/development-workflow.
- Pushed workflow commit: e2484b6.
- Workflow PR: #1, open and not merged.

The current branch and working state must be verified locally
before subsequent operations.

## Previously Verified Local Results

For the initial scaffold:
- Python 3.12.10.
- python-telegram-bot 22.8.
- pytest 8.4.2.
- Ruff 0.17.6.
- Three environment tests passed.
- Source lint and formatting passed.
- .venv is ignored by Git.

These are environment checks, not product acceptance tests.
They do not establish the results of the current branch's checks.

## Current Task

Record verified workflow setup in documentation.

Workflow files were prepared on chore/development-workflow and proposed
in PR #1:
- .github/workflows/ci.yml
- .github/pull_request_template.md
- docs/development-workflow.md
- Updated AGENTS.md.
- Updated docs/checkpoint.md.

The initial workflow-file review found no critical contradictions.
Its requested agent-instruction updates were incorporated.
Workflow commit e2484b6 was pushed; GitHub CI check "Python quality"
completed successfully; main protection was applied and verified.

This documentation update must be committed, pushed, and CI-rechecked
before requesting final human review.

## GitHub Verification

- Baseline push: Completed.
- Workflow branch created locally: Completed.
- Workflow commit e2484b6: Pushed.
- First workflow PR: #1, open and not merged.
- GitHub CI check "Python quality": Completed successfully for e2484b6.
- Main branch protection: Applied and verified.
- Invited reviewers: cibervicho and jfruvalc.
- Invitation acceptance and independent approval: Not confirmed.
- CI recheck for this documentation update: Pending.

Do not describe PR #1 as merged or independent approval as obtained.

## Next Bounded Actions

1. Run local checks for this documentation update.
2. Review and commit this update after explicit authorization.
3. Push the update after explicit authorization.
4. Recheck GitHub CI after the push.
5. Request final human review only after the CI recheck.
6. Confirm invitation acceptance and obtain independent approval.
7. Merge PR #1 only after explicit owner authorization, required CI,
   and required approval.
8. After merge, create feat/config-validation through an approved Git
   operation.

## Next Product Implementation

After workflow setup is merged:
- Create feat/config-validation through an approved Git operation.
- Implement the approved configuration contract.
- Test without real secrets or Telegram connections.
- Complete the remaining configuration portion of F-03.
- Proceed to F-04 only after reviewing and merging that task.

No configuration implementation files currently exist.

## Remaining Decisions

- Final Telegram commands and button layout.
- OCI capacity validation and systemd service configuration.
- Retention and deletion.
- Real-participant acceptance of the correction limitation.
- Deadline and weekly availability.
- Invitation acceptance and independent approval for PR #1.

## Unperformed Verification

- Product acceptance tests.
- CI recheck after this documentation update.
- Deployment checks.
- Backup restore.
- Private-group rehearsal.

## Session Handoff

Update actual task progress and checks.
Keep historical results distinct from current verification.
Do not include secrets, live records, or full logs.
Do not invent commit identifiers or approvals.

## Document Boundary

This checkpoint summarizes progress.
Requirements, decisions, and workflow rules remain authoritative.