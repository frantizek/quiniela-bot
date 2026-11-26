# Quiniela-Bot

A Telegram bot for recreational team-assignment quinielas.

An administrator enters teams and opens registration.
When registration fills, the bot randomly assigns one team per participant.

The owner/admin records advancement and elimination.
The bot tracks the quiniela until one participant wins.

## Status

The initial local scaffold is implemented.

Verified:
- Python 3.12.10.
- Three environment smoke tests passed.
- Source lint and formatting passed.

Product behavior, persistence, Telegram integration, and deployment
are not implemented.

## MVP

- Telegram groups.
- One non-terminal quiniela per group.
- 2 to 32 teams, including non-powers of two.
- One participant per team.
- One registration per Telegram user ID.
- No withdrawals or substitutions.
- Automatic immutable draw when full.
- Administrator-confirmed elimination outcomes.
- Cancellation before completion, preserving history.
- Public status and winner announcements.
- Persistent state and recoverable announcements.

## Administrative Authority

Current group owner and all current administrators are authorized.
There is no separate bot-managed administrator list.

Require identifiable actors and current-role verification.

Administrators determine sporting results.
The bot does not calculate scores, interpret rules, generate brackets,
or consult sports APIs.

Opening, outcomes, and cancellation require:
- Initiator-only confirmation.
- Current authorization recheck.
- 10-minute expiration.
- Business-state version checks.
- Duplicate-action protection.

## Cancellation and Correction

Cancellation is allowed in DRAFT, OPEN, and ACTIVE.
It is not a withdrawal, correction, or redraw.

No result correction exists in the first implementation.
Before real-participant use, explicitly accept this limitation
or implement an approved and tested correction workflow.

## Language

- Documentation, identifiers, and developer comments: English.
- Actual Telegram messages and buttons: Mexican Spanish.

## Tooling

- Python 3.12.
- uv and project-local .venv.
- pyproject.toml and uv.lock.
- python-telegram-bot initially pinned to 22.8.
- pytest and Ruff.
- Standard-library sqlite3 for planned persistence.

Repository policy requires tracking uv.lock in Git.
Whether the current working changes are committed is determined
by local Git status and history.

Deployment direction: separate systemd service on OCI with polling.
Service configuration and capacity validation remain open.

Do not modify the existing bot.

## Local Checks

From the repository root:

    uv run --locked pytest -q
    uv run --locked ruff check quiniela_bot tests
    uv run --locked ruff format --check quiniela_bot tests

Initial environment creation was performed with:

    uv sync --python 3.12

Future synchronization should preserve the reviewed lockfile:

    uv sync --locked --python 3.12

No Telegram token is needed for current tests.
No bot startup command exists yet.

## Documentation

- AGENTS.md
- docs/requirements.md
- docs/architecture.md
- docs/decisions.md
- docs/user-flows.md
- docs/backlog.md
- docs/test-plan.md
- docs/risks.md
- docs/environment.md
- docs/tooling.md
- docs/runbook.md
- docs/checkpoint.md

## Exclusions

No payments, predictions, sports APIs, score calculations, brackets,
withdrawals, substitutions, channels, web dashboard, or runtime AI.

## Security and Release Gates

Never commit or submit secrets, live databases, backups,
participant records, or production logs to an AI provider.

Use synthetic data.

Before real-participant use:
- Pass product tests and private rehearsal.
- Demonstrate restore.
- Verify deployment isolation.
- Approve retention and deletion.
- Resolve the correction release gate.

Local scaffold success does not authorize deployment.