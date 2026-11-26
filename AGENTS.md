# Agent Instructions

## Authority

Quiniela-Bot is a Python Telegram bot for recreational quinielas.

- docs/requirements.md defines product behavior.
- docs/decisions.md records accepted decisions.
- docs/tooling.md records the approved tooling baseline.
- docs/checkpoint.md summarizes current progress.

Report conflicts instead of silently choosing a new rule.

## Language

Use English for documentation, identifiers, and developer comments.
Use Mexican Spanish for actual Telegram messages and buttons.
Describe interface behavior in English in documentation.

## Scope

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
- Preserve cancellation history.
- No result editing or undo without an approved scope change.

## Authorization and Confirmation

- Current group owner and all current administrators are authorized.
- No separate authorized-user list.
- Require identifiable administrative actors.
- Check current authorization for every privileged action.
- Recheck authorization at confirmation.
- Fail closed if verification is unavailable.
- Only the initiating administrator may confirm.
- Expire confirmations after 10 minutes.
- Reject consumed, expired, or stale confirmations.
- Follow D-011 for business-state version behavior.

## Tooling

- Python 3.12.
- uv with pyproject.toml, uv.lock, and .venv.
- python-telegram-bot, initially pinned to 22.8.
- pytest and Ruff.
- Standard-library sqlite3 for persistence.
- One application process.
- Separate OCI service with long polling.

Do not independently maintain requirements.txt.
Do not change dependencies or the lockfile without an explicit task.

OCI paths, runtime user, capacity validation, and service configuration
remain unresolved. Do not infer deployment readiness.

## Working Rules

- Read only files relevant to the current task.
- Avoid repository-wide scans and agent fan-out.
- Complete one bounded task at a time.
- Split large tasks before implementation.
- State assumptions and blockers.
- Prefer simple code over speculative abstractions.
- Do not implement code during documentation-only tasks.
- Do not commit, push, deploy, or modify infrastructure without approval.
- Do not modify the existing bot or its runtime resources.

## Security

- Never read secrets, .env files, private keys, live databases,
  backups, or production logs.
- Use synthetic test data.
- Scope operations to the correct group and quiniela.
- Validate callbacks against stored state.
- Do not trust callback payloads as business records.
- Keep secrets and unnecessary personal data out of logs.

## Correctness

- Enforce uniqueness in storage.
- Commit final registration and assignments atomically.
- Handle repeated and concurrent actions safely.
- Persist state and announcement intent before sending messages.
- Recovery must not repeat draws or outcomes.
- Do not promise exactly-once Telegram delivery.
- Do not silently overwrite confirmed results.

## Local Checks

Run from the repository root:

- uv run --locked pytest -q
- uv run --locked ruff check quiniela_bot tests
- uv run --locked ruff format --check quiniela_bot tests

For collection diagnostics:
- uv run --locked pytest --collect-only -q

These commands passed for the initial three-test scaffold.

Implementation tasks require tests for changed behavior.
Never claim a check passed unless it was executed.

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