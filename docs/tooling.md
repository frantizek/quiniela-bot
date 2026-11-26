# Development Tooling

Status: Approved baseline; initial local checks passed.

## 1. Python

Use Python 3.12 for development and deployment.

Verified local project interpreter: Python 3.12.10.
Reported existing OCI project interpreter: Python 3.12.13.

Exact patch-version alignment has not been established.
Deployment compatibility must be checked before release.

Do not replace global Windows Python or OCI system Python.

## 2. Dependency Management

Use:
- uv for project environment and dependency management.
- pyproject.toml for dependency declarations.
- uv.lock for resolved dependencies.
- .python-version for the project interpreter selection.
- .venv for the local environment.

Commit pyproject.toml, uv.lock, and .python-version.
Do not commit .venv.

Do not maintain requirements.txt independently.
Generate an export if another tool requires one.

## 3. Initial Dependencies

| Tool | Declared constraint | Locally resolved version |
|---|---|---|
| python-telegram-bot | ==22.8 | 22.8 |
| pytest | >=8,<9 | 8.4.2 |
| Ruff | >=0.11,<1 | 0.17.6 |

The lockfile is the authority for the complete resolved dependency set.

Use Python's standard-library sqlite3 module for the initial database
implementation. No separate SQLite package has been added.

Review dependency changes and rerun relevant checks before accepting
a lockfile update.

Do not upgrade the existing OCI bot through this project.

## 4. Project Layout

The initial application is an unpackaged project with:

- quiniela_bot/__init__.py
- tests/test_environment.py

No build backend or distribution configuration is required by the
current scaffold.

Application modules and product tests will be added incrementally.

## 5. Verified Commands

Run from the repository root in PowerShell:

- uv run --locked python --version
- uv run --locked pytest --collect-only -q
- uv run --locked pytest -q
- uv run --locked ruff check quiniela_bot tests
- uv run --locked ruff format --check quiniela_bot tests

Observed results:
- Python 3.12.10.
- Three tests collected.
- Three tests passed.
- Lint passed.
- Formatting passed.

## 6. Explicit Fix Commands

Use only when a relevant check reports a problem:

- uv run --locked ruff check tests/test_environment.py --select I --fix
- uv run --locked ruff format quiniela_bot tests

Review modifications after applying fixes.

## 7. Verification Boundaries

Current tests check:
- Python minor version.
- Application package import.
- Initial Telegram dependency version.

They do not verify:
- Configuration validation.
- Registration or drawing.
- Persistence or migrations.
- Authorization or confirmations.
- Telegram interaction.
- Deployment or recovery.

## 8. Deployment Direction

Use a separate systemd service on OCI.

Service configuration, runtime user, paths, and deployment commands
remain unresolved.

Local setup success is not deployment approval.

## Document Boundary

This document records tooling and observed local checks.
It does not claim product implementation is complete.