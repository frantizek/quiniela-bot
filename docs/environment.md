# Environment Inventory

Status: Operator-reported infrastructure inventory and locally
verified development setup.

## 1. Purpose

Record the development and deployment environments without exposing
credentials or modifying the existing OCI bot.

Accepted product decisions remain in docs/decisions.md.
Approved tooling details are recorded in docs/tooling.md.

## 2. Development Machine

| Item | Value | Evidence |
|---|---|---|
| Operating system | Windows 10 Pro; version reported as 2009 | Operator report |
| Global Python | 3.13.17 | Operator report |
| Project Python | 3.12.10 | Local command output |
| Git | 2.56.1.windows.1 | Operator report |
| uv | 0.7.9 | Operator report |
| Available terminals | PowerShell and Git Bash | Operator report |
| Terminal used for setup | PowerShell | Local command output |
| Development separate from OCI | Yes | Operator confirmation |
| Project environment | .venv | Local setup output |
| Dependency declaration | pyproject.toml | Scaffold |
| Dependency lock | uv.lock | Local setup output |

The project interpreter is separate from the globally installed Python.
No global interpreter replacement was required.

## 3. Existing OCI Bot

| Item | Reported value |
|---|---|
| Telegram library | python-telegram-bot |
| Declared dependency | >=21.3 |
| Locked library version | 21.11.1 |
| Project Python | 3.12 |
| Reported environment Python | 3.12.13 |
| Dependency management | uv and uv.lock |
| Supervisor | systemd |
| Update delivery | Long polling |
| Runtime invocation | uv run python bot.py |
| Deployment approach | Manual Git update, uv sync, service restart |
| CI deployment job | None reported |

These details describe the existing bot, not Quiniela-Bot.

No dependency upgrades, service changes, or database changes have
been performed on the existing bot.

## 4. OCI Host Snapshot

| Item | Reported value |
|---|---|
| Operating system | Ubuntu 22.04.5 LTS |
| System Python | 3.10.12 |
| Logical CPUs | 1 |
| Total memory | 5.8 GiB |
| Available memory | 5.1 GiB |
| Available root-filesystem disk | Approximately 38 GB |
| Swap | None reported |

This snapshot is not a load test or deployment approval.
The target deployment filesystem still requires confirmation.

Do not replace or modify system Python.

## 5. Local Scaffold Verification

Observed results:
- uv sync completed successfully.
- Project interpreter: Python 3.12.10.
- python-telegram-bot installed: 22.8.
- pytest installed: 8.4.2.
- Ruff installed: 0.17.6.
- Three environment tests collected and passed.
- Focused source lint passed.
- Focused source formatting check passed.
- .venv is ignored by Git.

These checks verify the local scaffold only.

No Telegram connection, database implementation, deployment,
or product acceptance test has been performed.

## 6. Isolation Requirements

Quiniela-Bot must have its own:
- Project directory.
- Python environment and lockfile.
- Bot token.
- Database.
- Runtime configuration.
- systemd service.
- Logs and backup scope.

Only one Quiniela-Bot application process is planned.

## 7. Remaining Checks

Before Telegram integration:
- Finalize commands and button layout.
- Create a separate test bot and private test group.
- Verify required Telegram permissions.

Before deployment:
- Observe existing-service resource use.
- Confirm intended deployment filesystem and capacity.
- Select service name and runtime user.
- Verify protected configuration storage.
- Establish application, database, log, and backup paths.
- Test deployment and recovery procedures.

Do not submit secrets, production databases, service credentials,
or participant records to an AI provider.

## Document Boundary

Local scaffold verification does not authorize deployment or
changes to the existing bot.