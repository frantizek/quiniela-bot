# Operations Runbook

Status: Planning baseline. Not yet an executable deployment guide.

Do not deploy using this document until environment details,
commands, and recovery procedures have been verified.

## 1. Purpose

Document safe operation of Quiniela-Bot on the existing Oracle OCI
infrastructure without disrupting the existing bot.

Product behavior:
- Administrators determine advancement and elimination.
- Assignments are immutable.
- Committed outcomes have no correction workflow in the first version.
- Announcement retries must not repeat business actions.

## 2. Environment Record

Complete this table using sanitized information.

| Item | Current value |
|---|---|
| Host operating system | Unconfirmed |
| Python version | Unconfirmed |
| Telegram library and version | Unconfirmed |
| Existing deployment supervisor | Unconfirmed |
| Available CPU, memory, and disk | Unconfirmed |
| Application directory | Unconfirmed |
| Service name | Unconfirmed |
| Runtime user | Unconfirmed |
| Database location | Unconfirmed |
| Secret storage method | Unconfirmed |
| Backup location and access controls | Unconfirmed |
| Log location and rotation policy | Unconfirmed |
| Deployment and rollback commands | Unconfirmed |

Do not record tokens, private keys, passwords, public access credentials,
or unnecessary host identifiers in this repository.

## 3. Isolation Requirements

Quiniela-Bot must have its own:
- Telegram bot token.
- Runtime configuration.
- Python environment.
- Database.
- Service definition.
- Logs and backup scope.

Do not alter the existing bot's environment, database, configuration,
or service.

Verify available capacity before deployment.
Run only one Quiniela-Bot application process initially.

## 4. Pre-Deployment Gate

Deployment is blocked until:

- Python and Telegram library versions are selected.
- Local setup and test commands are documented.
- Critical automated tests pass.
- Private-group rehearsal passes.
- OCI capacity and service isolation are verified.
- Secret handling and log behavior are reviewed.
- Database migration procedures are verified.
- Backup and restore have been demonstrated.
- Deployment and rollback commands are documented.

Real-participant use additionally requires:
- Approved retention and deletion rules.
- Explicit acceptance of the correction limitation, or an approved
  and tested correction workflow.

## 5. Deployment Procedure

Exact commands: Pending environment verification.

Approved sequence:

1. Identify the release commit.
2. Review changes and applicable migration notes.
3. Confirm the existing bot will not be affected.
4. Create and verify a recoverable backup if persistent data exists.
5. Stop only Quiniela-Bot when required by the release procedure.
6. Apply the reviewed release and migrations.
7. Start exactly one Quiniela-Bot process.
8. Perform smoke checks.
9. Record the deployed commit and verification results.

Do not automate deployment before this sequence is verified manually.

## 6. Smoke Checks

Verify:
- The process starts without exposing secrets.
- The bot responds in the designated test group.
- Current administrator authorization works.
- Unauthorized actions do not mutate state.
- Stored quiniela state loads correctly.
- No new assignments appear for an existing draw.
- Pending announcements can recover without repeating outcomes.
- The existing bot remains operational.

Use non-destructive checks for any existing real quiniela.

## 7. Restart Procedure

Exact commands: Pending supervisor selection.

1. Identify the Quiniela-Bot service.
2. Confirm the restart does not target the existing bot.
3. Restart only Quiniela-Bot.
4. Verify there is exactly one application process.
5. Check state recovery and pending announcements.
6. Record unexpected behavior.

Never delete the database to resolve a startup problem.
Never manually redraw teams during recovery.

## 8. Backup Procedure

Backup commands, frequency, and retention: Pending approval.

The verified procedure must:
- Capture a consistent database backup.
- Protect participant information.
- Include required recovery metadata.
- Keep secrets out of repository backups.
- Verify backup integrity.
- Document how pending announcements are handled after restoration.

Do not assume copying a live database file is a sufficient procedure.
Use a tested backup method appropriate to the selected configuration.

Backups must not be committed or submitted to an AI provider.

## 9. Restore Procedure

Exact commands: Pending implementation and rehearsal.

1. Stop only Quiniela-Bot.
2. Preserve the current database for investigation.
3. Select a verified backup and compatible application release.
4. Restore using the tested procedure.
5. Validate schema and committed business state.
6. Review potential loss of actions recorded after the backup.
7. Review pending announcements and possible duplicate publication.
8. Start one process and perform smoke checks.
9. Record the recovery and any reconciliation required.

Do not silently treat restored older state as current.
Recovery may require an administrator-facing explanation.

## 10. Rollback Procedure

Exact commands: Pending release design.

Before rollback:
- Determine whether the previous application supports the current schema.
- Preserve current data and diagnostic information.
- Identify any actions committed after deployment.

Do not assume application rollback also reverses a migration.
Do not restore an old backup without reviewing resulting data loss.

Use only a documented and rehearsed rollback path.

## 11. Incident Handling

### Startup Failure
- Preserve the database.
- Inspect sanitized diagnostics locally.
- Verify configuration, migration state, and dependency compatibility.
- Do not expose secrets to an AI provider.

### Telegram Delivery Failure
- Preserve committed business state.
- Retry stored announcement intent when delivery is available.
- Do not redraw or repeat an outcome.

### Authorization Verification Failure
- Reject privileged mutations.
- Restore verification before accepting administrative actions.

### Incorrect Confirmed Outcome
- Do not edit database records manually.
- No supported correction exists in the first implementation.
- Explain the limitation and stop further outcome entry if necessary.
- Cancellation closes the quiniela; it does not repair the result.

### Suspected Token Exposure
- Treat the credential as compromised.
- Replace it through the provider's verified credential-management process.
- Update protected runtime configuration.
- Investigate exposure without copying the credential into documentation.

### Impact on Existing Bot
- Stop Quiniela-Bot if needed to protect the existing service.
- Investigate resource use and isolation before restarting.

## 12. Operational Records

For deployments and incidents, record:
- Date and responsible person.
- Release commit.
- Action performed.
- Checks and outcomes.
- Data-loss or reconciliation concerns.
- Follow-up tasks.

Keep operational records free of secrets and unnecessary personal data.

## Document Boundary

Commands and procedures remain unverified until explicitly recorded
and rehearsed. This document does not authorize deployment.