 # Project Checkpoint

## Current Stage

Documentation foundation complete through Batch 3.
Batch 4 operational documents are being prepared.

Application implementation has not started.
No deployment or infrastructure changes have been performed as part
of this documented workflow.

## Completed Documentation

- README.md
- AGENTS.md
- docs/requirements.md
- docs/architecture.md
- docs/decisions.md
- docs/user-flows.md
- docs/backlog.md
- docs/test-plan.md
- docs/risks.md

Batch 3 documentation review reported no remaining contradictions
or critical omissions.

## Current Batch

Batch 4:
- docs/runbook.md
- docs/checkpoint.md

Status: Created; review and commit pending.

## Accepted Scope

- Telegram groups first.
- English repository and documentation.
- Mexican Spanish bot interface.
- Python on existing Oracle OCI infrastructure.
- Independent runtime from the existing bot.
- SQLite and one application process.
- One non-terminal quiniela per group.
- 2 to 32 teams; powers of two not required.
- One participant per Telegram user ID per quiniela.
- No withdrawals or substitutions.
- Automatic immutable draw when capacity is reached.
- Administrator-controlled advancement and elimination.
- Current Telegram owner and all current administrators are authorized.
- Initiator-only confirmation with 10-minute expiry.
- Business-state version checks and duplicate protection.
- Cancellation only in DRAFT, OPEN, and ACTIVE.
- Stored announcement intent and safe delivery retries.
- No result correction in the first implementation.

See docs/decisions.md for the authoritative decision details.

## Not Implemented

- Application scaffold.
- Dependencies and test commands.
- Database schema or migrations.
- Domain services.
- Telegram handlers.
- Deployment configuration.
- Backup and restore tooling.

## Verification Record

- Documentation review: Batch 3 passed.
- Application tests: Not run; application does not exist yet.
- Deployment checks: Not performed.
- Backup restore: Not performed.
- Private-group rehearsal: Not performed.

Do not interpret documentation approval as implementation verification.

## Open Decisions

- Python version and Telegram library.
- OCI capacity and deployment supervisor.
- Final commands and button layout.
- Retention and deletion policy.
- Real-participant acceptance of the correction limitation.
- Deadline and weekly development availability.

## Next Task

Review and commit Batch 4.

After approval:
Start F-01 from docs/backlog.md: sanitized environment inventory.

Gather only:
- Operating system.
- Python version.
- Existing Telegram library and version.
- Existing deployment method.
- Available runtime capacity.

Do not read or submit secrets, production databases, or chat records.
Do not modify the existing bot.

## Last Confirmed Commit

Not recorded here.

The operator should record the relevant commit after verifying it locally.
Do not invent a commit identifier.

## Session Handoff Rules

Update this file with:
- Last completed task.
- Current task and blocker.
- Actual checks performed.
- Next bounded action.

Keep it concise.
Do not paste full logs, secrets, participant records, or repeated plans.

## Document Boundary

This file summarizes progress.
Requirements and decisions remain authoritative in their own documents.