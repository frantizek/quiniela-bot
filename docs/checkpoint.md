# Project Checkpoint

## Current Stage

The initial documentation and local scaffold are complete.

The baseline was published to GitHub.
Development workflow setup is in progress on its own branch.

No configuration-validation implementation, Telegram connection,
or OCI modification has been performed.

## Repository Baseline

- Repository: frantizek/quiniela-bot.
- Visibility: Public.
- Default intended branch: main.
- Published scaffold commit: d70a4d3.
- Current task branch: chore/development-workflow.

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

Introduce the development workflow through a pull request.

Files prepared:
- .github/workflows/ci.yml
- .github/pull_request_template.md
- docs/development-workflow.md
- Updated AGENTS.md.
- Updated docs/checkpoint.md.

The initial workflow-file review found no critical contradictions.
Its requested agent-instruction updates have been incorporated.

Current local checks and final documentation review remain pending.

## GitHub Verification

- Baseline push: Completed.
- Workflow branch created locally: Completed.
- Workflow branch push: Not performed.
- First workflow PR: Not created.
- GitHub CI execution: Not verified.
- Main branch protection: Not configured.
- Independent reviewer availability: Not confirmed.

Do not describe protection or CI success as established.

## Next Bounded Actions

1. Run local tests, lint, formatting, and whitespace checks.
2. Review the agent instructions and checkpoint changes.
3. Review and commit the workflow setup after explicit authorization.
4. Push the branch and create a PR after explicit authorization.
5. Verify the actual GitHub CI result and check name.
6. Configure and verify main protection through a separately approved step.
7. Resolve reviewer availability before requiring independent approval.
8. Merge only after explicit authorization and required checks.

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
- Repository review enforcement while no independent reviewer is available.

## Unperformed Verification

- Product acceptance tests.
- GitHub CI.
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