# Agent Instructions

## Authority

Quiniela-Bot is a Python Telegram bot for recreational quinielas.

- docs/requirements.md defines product behavior.
- docs/decisions.md records accepted decisions.
- docs/tooling.md defines approved tooling.
- docs/development-workflow.md defines branch, PR, and approval rules.
- docs/checkpoint.md summarizes progress.

Report conflicts instead of silently choosing a new rule.

## Language

Use English for documentation, identifiers, and developer comments.
Use Mexican Spanish for actual Telegram messages and buttons.
Describe interface behavior in English in documentation.

## Product Scope

- Owner/admin determines advancement and elimination.
- No score calculation, football rules, fixtures, sports APIs,
  payments, or runtime AI.
- One non-terminal quiniela per group.
- Support 2 to 32 teams, including non-powers of two.
- Participant capacity equals team count.
- One registration per Telegram user ID per quiniela.
- No withdrawals or substitutions.
- Draw automatically when full.
- Persist assignments; never redraw or edit them.
- Elimination does not remove participants from Telegram.
- Cancellation is allowed only in DRAFT, OPEN, or ACTIVE.
- Preserve canceled quiniela history.
- No result editing or undo without an approved scope change.

## Authorization and Confirmation

- Current group owner and all current administrators are authorized.
- No separate authorized-user list.
- Require identifiable administrative actors.
- Verify current authorization for every privileged action.
- Recheck authorization at confirmation.
- Fail closed when verification is unavailable.
- Only the initiating administrator may confirm.
- Expire confirmations after 10 minutes.
- Reject consumed, expired, or stale confirmations.
- Follow D-011 for business-state version behavior.

## Tooling

- Python 3.12.
- uv, pyproject.toml, uv.lock, and project-local .venv.
- python-telegram-bot initially pinned to 22.8.
- pytest and Ruff.
- Standard-library sqlite3 for persistence.
- One application process.
- Separate OCI systemd service with long polling.

Do not independently maintain requirements.txt.
Do not change dependencies or the lockfile outside an approved task.

OCI configuration and capacity validation remain unresolved.
Do not infer deployment readiness from local or CI success.

## Working Rules

- Read only files relevant to the current task.
- Avoid repository-wide scans and agent fan-out.
- Complete one bounded task at a time.
- Split large tasks before implementation.
- State assumptions and blockers.
- Prefer simple code over speculative abstractions.
- Do not implement code during documentation-only tasks.
- Do not implement directly on main.
- Confirm the current branch before making authorized edits.
- Do not modify the existing bot or its runtime resources.

Explicit approval is required for:
- Creating or switching branches.
- Committing.
- Pushing.
- Creating pull requests.
- Merging.
- Changing GitHub repository settings.
- Deployment or infrastructure changes.

Approval for code edits does not authorize these operations.
Approval for one Git operation does not authorize later operations.

## Review and Merge

Follow docs/development-workflow.md.

- Inspect the diff and actual check results.
- AI-assisted review is not independent human approval.
- Do not claim branch protection is enforced until verified.
- Do not bypass protections routinely.
- Do not enable automatic merging.
- Merging does not authorize deployment.

## Security

- Never read secrets, .env files, private keys, live databases,
  backups, or production logs.
- Use synthetic test data.
- Scope operations to the correct group and quiniela.
- Validate callbacks against stored state.
- Do not trust callback payloads as business records.
- Keep secrets and unnecessary personal data out of logs.
- Do not add deployment credentials to CI.

## Correctness

- Enforce uniqueness in storage.
- Commit final registration and assignments atomically.
- Handle repeated and concurrent actions safely.
- Persist state and announcement intent before sending.
- Recovery must not repeat draws or outcomes.
- Do not promise exactly-once Telegram delivery.
- Do not silently overwrite confirmed results.

## Local Checks

Run from the repository root:

- uv run --locked pytest -q
- uv run --locked ruff check quiniela_bot tests
- uv run --locked ruff format --check quiniela_bot tests
- git diff --check

For collection diagnostics:
- uv run --locked pytest --collect-only -q

Implementation tasks require tests for changed behavior.
Never claim a check passed unless it was executed.
Local checks do not prove GitHub CI passed.

## Release Gates

Before real-participant use:
- Approve retention and deletion.
- Demonstrate backup restore.
- Verify deployment isolation.
- Pass a private-group rehearsal.
- Accept the correction limitation explicitly or implement
  approved and tested correction behavior.

## Completion Summary

Report briefly:
1. Files changed.
2. Behavior or documentation added.
3. Actual checks and results.
4. Remaining blockers and next bounded action.