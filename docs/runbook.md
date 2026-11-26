# Operations Runbook

Status: Operational planning baseline.
Local development checks passed; deployment procedures remain unverified.

Do not use this document as an executable deployment guide yet.

## 1. Purpose

Operate Quiniela-Bot independently from the existing OCI bot.

Recovery must preserve assignments and committed outcomes.
Announcement retries must not repeat business actions.

No outcome correction exists in the first implementation.

## 2. Environment Summary

Operator-reported OCI details:
- Ubuntu 22.04.5 LTS.
- Existing bot uses Python 3.12, uv, systemd, and polling.
- One logical CPU.
- Approximately 5.1 GiB available memory at the reported snapshot.
- Approximately 38 GB available root-filesystem space.

Locally verified:
- Python 3.12.10.
- uv-based environment and dependency lock.
- Three smoke tests passed.
- Lint and formatting passed.

This is not deployment or capacity approval.

## 3. Unresolved Operational Configuration

| Item | Status |
|---|---|
| Target filesystem and capacity under load | Unverified |
| Application directory | Unselected |
| Service name | Unselected |
| Runtime user | Unselected |
| Database path | Unselected |
| Protected secret storage | Unselected |
| Log path and rotation | Unselected |
| Backup method, schedule, and retention | Unselected |
| Deployment commands | Unverified |
| Restore and rollback commands | Unverified |

Do not record credentials or unnecessary host identifiers.

## 4. Isolation Requirements

Use separate:
- Token and protected configuration.
- Project directory and Python environment.
- Database.
- systemd service.
- Logs and backup scope.

Do not alter the existing bot's dependencies, environment, data, or service.
Run one Quiniela-Bot process initially.
Do not change OCI system Python.

## 5. Deployment Gate

Before deployment:
- Product tests and private rehearsal pass.
- OCI capacity and isolation are verified.
- Secret handling and logs are reviewed.
- Migrations are tested.
- Backup and restore are demonstrated.
- Deployment and rollback procedures are documented.

Before real-participant use:
- Approve retention and deletion.
- Accept the correction limitation explicitly or implement approved correction.

## 6. Planned Deployment Sequence

Exact commands remain pending.

1. Identify the release commit.
2. Review changes and migrations.
3. Confirm isolation from the existing bot.
4. Create and verify a recoverable backup when data exists.
5. Stop only Quiniela-Bot if the procedure requires it.
6. Apply the release and reviewed migrations.
7. Start exactly one process.
8. Run smoke checks.
9. Record release and results.

Validate manually before automating deployment.

## 7. Operational Smoke Checks

Verify:
- Startup without secret exposure.
- Response in the designated test group.
- Current-role authorization.
- Rejection of unauthorized mutations.
- Existing state loads correctly.
- No redraw of stored assignments.
- Announcement recovery does not repeat outcomes.
- Existing bot remains operational.

Avoid destructive checks against real quinielas.

## 8. Restart

Exact commands remain pending.

1. Identify the correct service.
2. Restart only Quiniela-Bot.
3. Verify one process.
4. Verify state and announcement recovery.
5. Record unexpected behavior.

Never delete the database to fix startup.
Never redraw during recovery.

## 9. Backup

Method, commands, frequency, and retention remain pending.

The verified procedure must:
- Capture a consistent database backup.
- Protect participant information.
- Record required recovery metadata.
- Verify integrity.
- Account for pending announcements.

Do not assume copying a live database is sufficient.
Use a tested method appropriate to the configuration.

Never commit backups or submit them to AI providers.

## 10. Restore

Exact commands remain pending.

1. Stop only Quiniela-Bot.
2. Preserve current data for investigation.
3. Choose a verified backup and compatible application release.
4. Restore using the tested procedure.
5. Validate schema and business state.
6. Identify actions potentially lost since the backup.
7. Review announcement replay and duplicate-delivery risks.
8. Start one process and run checks.
9. Document reconciliation and inform administrators when required.

Do not silently present older restored state as current.

## 11. Rollback

Exact commands remain pending.

Before rollback:
- Check previous application compatibility with the current schema.
- Preserve data and diagnostics.
- Identify actions committed after deployment.

Application rollback does not automatically reverse migrations.
An older backup may lose committed actions.

Use a rehearsed recovery path.

## 12. Incident Handling

### Startup Failure
Preserve data.
Inspect sanitized diagnostics locally.
Check configuration, dependencies, and migrations.

### Delivery Failure
Retain business state.
Retry stored announcement intent.
Do not redraw or repeat outcomes.

### Authorization Failure
Reject privileged mutations until verification is restored.

### Incorrect Confirmed Outcome
Do not manually edit database records.
Explain the unsupported correction limitation.
Pause further outcome entry if needed.
Cancellation closes the quiniela but does not repair the result.

### Suspected Credential Exposure
Treat the credential as compromised.
Replace it through the provider's verified management process.
Update protected configuration and investigate exposure.

### Existing Bot Disruption
Stop Quiniela-Bot if needed to protect the existing service.
Resolve isolation or resource problems before restarting.

## 13. Operational Records

Record:
- Date and responsible person.
- Release commit.
- Action and verification results.
- Data-loss or reconciliation concerns.
- Follow-up work.

Exclude secrets and unnecessary personal information.

## Document Boundary

Deployment, backup, restore, and rollback commands remain unverified.
This document does not authorize infrastructure changes.