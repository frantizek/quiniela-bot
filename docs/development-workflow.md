# Development Workflow

Status: Verified workflow baseline; PR #1 remains open.

Workflow commit e2484b6 was pushed on chore/development-workflow.
GitHub CI check "Python quality" completed successfully.
Main protection was applied and verified.

This documentation update must be committed, pushed, and CI-rechecked
before requesting final human review. PR #1 has not been merged.

## 1. Purpose

Deliver small, tested changes through branches and pull requests.

The initial baseline was published directly as a one-time bootstrap.
Subsequent project changes use this workflow.

Merging does not deploy to OCI.

## 2. Branch Strategy

- main contains reviewed project changes.
- Use one short-lived branch per bounded task.
- Do not implement directly on main.
- Avoid unrelated changes in a single PR.

Examples:
- chore/development-workflow
- feat/config-validation
- feat/database-schema
- fix/registration-capacity

Before creating a new task branch:
- Finish or preserve current work.
- Update local main from origin/main.
- Create the branch from the updated baseline.

Do not discard another task's uncommitted changes.

## 3. Task Lifecycle

1. Select a bounded backlog task.
2. Define scope and acceptance tests.
3. Create the task branch.
4. Plan the implementation.
5. Implement and verify locally.
6. Review the diff.
7. Commit and push the branch after explicit authorization.
8. Open a PR targeting main.
9. Inspect GitHub CI and review findings.
10. Obtain required approvals.
11. Merge only after explicit owner authorization.
12. Update local main and begin the next task.

## 4. Local Quality Gate

Run from the repository root:

- uv run --locked ruff check quiniela_bot tests
- uv run --locked ruff format --check quiniela_bot tests
- uv run --locked pytest -q
- git diff --check

Tests must cover changed behavior.
Passing environment smoke tests alone does not verify product features.

## 5. CI Baseline

Workflow file: .github/workflows/ci.yml

Initial design:
- PRs targeting main.
- Pushes to main.
- Manual dispatch.
- One Linux job using Python 3.12.
- uv 0.7.9.
- Locked dependency synchronization.
- Ruff lint, formatting, and pytest.
- No secrets or deployment credentials.
- No automatic deployment.

Initial and verified check name: Python quality.

The GitHub CI check "Python quality" completed successfully for workflow
commit e2484b6. It is now a required main-protection check.
Future workflow changes require a fresh CI result.

Action revisions and tooling upgrades require review.

## 6. Review Policy

The author inspects the diff and actual test results.

An independent reviewer is a different eligible GitHub user.
The PR author cannot satisfy an independent approving-review requirement.

AI review is assistance, not a required human approval.

Current status: cibervicho and jfruvalc were invited.
Invitation acceptance and independent approval are not yet confirmed.

Until independent approval is granted:
- Record author review and AI-assisted findings.
- Do not claim independent approval.
- Do not bypass the configured approval requirement.

Once approval is granted:
- Record the approving reviewer.
- Resolve blocking findings before merging.

## 7. Verified Main Protection

Applied and verified on main:
- Required check: Python quality.
- Strict/up-to-date branch requirement enabled.
- One approving review required.
- Stale approvals dismissed.
- Conversation resolution required.
- Protection enforced for administrators.
- Force pushes and main deletion disabled.

Workflow files alone do not enforce branch protection.
Do not bypass or routinely override these protections.
Independent approval is configured as required, but no approval has
been recorded for PR #1.

## 8. Merge Policy

Prefer squash merging for bounded task PRs.
Do not enable automatic merging as part of this setup.

The owner explicitly authorizes merging after:
- Relevant local checks pass.
- Required CI passes.
- Blocking findings are resolved.
- Required human approvals are satisfied.

Never merge solely because an AI says the change is ready.

## 9. OpenCode Permissions

OpenCode may analyze or edit only the authorized task scope.

Separate explicit approval is required for:
- Creating or switching branches.
- Committing.
- Pushing.
- Creating PRs.
- Merging.
- Modifying repository settings.
- Deployment and infrastructure changes.

Do not read secrets or production records.
Do not perform unauthorized Git operations.

## 10. Deployment Boundary

CI verifies repository changes only.
It must not contain OCI credentials or deployment steps.

Deployment remains a separately approved operational task.

## 11. Current Setup Status

Historical setup:
- Public GitHub repository created.
- Initial baseline published.
- Workflow files prepared on chore/development-workflow.

Verified current status:
- Workflow commit e2484b6 was pushed.
- PR #1 is open and not merged.
- GitHub CI check "Python quality" completed successfully.
- Main protection was applied and verified; see section 7.
- cibervicho and jfruvalc were invited; acceptance is unconfirmed.
- Independent approval is not confirmed.

Pending for this documentation update:
- Commit, push, and CI recheck are required before requesting final
  human review.
- No configuration implementation or OCI deployment has occurred.

## Document Boundary

This document defines workflow rules and records verified setup.
Future repository enforcement and CI results must be verified separately.