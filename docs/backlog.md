# Delivery Backlog

Status: Initial implementation backlog.

Authority:
- docs/requirements.md
- docs/decisions.md

## 1. Working Rules

- Complete one task at a time.
- Split tasks estimated above three hours before implementation.
- Use synthetic data.
- Review changes and run relevant tests before committing.
- Do not deploy during foundation or domain implementation.
- Do not expand scope to resolve an unrelated issue.

Estimates include implementation, AI assistance, review, and tests.
They exclude waiting for approvals or infrastructure access.

## 2. Definition of Ready

A task is ready when:
- Its expected behavior is clear.
- Dependencies are satisfied.
- Relevant decisions are approved.
- Acceptance checks are defined.
- Required context contains no secrets or live participant data.

## 3. Definition of Done

A task is done when:
- Its acceptance checks pass.
- Relevant automated tests pass.
- The diff has been reviewed.
- Documentation reflects changed behavior.
- No secrets or runtime data are staged.
- The checkpoint and backlog are updated.
- A focused commit records the work.

Never claim checks passed unless they were run.

## 4. Milestone 1 — Foundation

| ID | Task | Hours | Depends on | Acceptance |
|---|---|---:|---|---|
| F-01 | Inventory environment safely | 1–2 | None | Record Python, existing library, deployment method, and available OCI capacity without copying secrets |
| F-02 | Select tooling and library | 1–2 | F-01 | Record supported versions, dependency strategy, and local check commands |
| F-03 | Create application scaffold | 1–2 | F-02 | Isolated environment; configuration validation; empty test suite runs |
| F-04 | Implement schema and initial migration | 2–3 | F-03 | Required tables and constraints exist; migration test passes |
| F-05 | Add lifecycle and validation primitives | 2–3 | F-04 | Team counts, names, allowed transitions, and group isolation are tested |

Exit gate:
- A reproducible local setup exists.
- Schema and domain validation tests pass.
- No Telegram credentials are required for these tests.

## 5. Milestone 2 — Registration and Draw

| ID | Task | Hours | Depends on | Acceptance |
|---|---|---:|---|---|
| R-01 | Create and edit draft quinielas | 2–3 | F-05 | One non-terminal quiniela per group; draft edits increment version |
| R-02 | Implement pending confirmations | 2–3 | R-01 | Ownership, 10-minute expiry, version, and consumed-state checks |
| R-03 | Open registration | 1–2 | R-02 | Valid team list locks; transition commits once |
| R-04 | Implement registration transaction | 2–3 | R-03 | Unique users; capacity enforced under concurrent requests |
| R-05 | Implement atomic final-slot draw | 2–3 | R-04 | Final participant and unique assignments commit together |
| R-06 | Add audit and pending announcements | 2–3 | R-05 | State and announcement intent commit together; retries never redraw |

Exit gate:
- Eight synthetic users receive eight unique assignments.
- Concurrent final-slot claims do not exceed capacity.
- Restart and repeated actions preserve the original draw.

## 6. Milestone 3 — Outcomes and Telegram Integration

Each item must be split into small implementation tasks before work begins.

- Implement confirmed outcomes and automatic completion.
- Implement cancellation in DRAFT, OPEN, and ACTIVE.
- Add current Telegram-role authorization.
- Add Spanish commands, buttons, and confirmation messages.
- Add registration and status rendering.
- Add announcement delivery and startup recovery.
- Test callbacks belonging to old, canceled, or completed quinielas.

Exit gate:
- A private test group completes the eight-team scenario.
- Unauthorized, stale, expired, and repeated actions do not mutate state.
- No score calculation or tournament-rule logic exists.

## 7. Milestone 4 — Operational Readiness

- Confirm deployment isolation and OCI capacity.
- Implement and test backup and restore procedures.
- Document migrations and rollback.
- Validate secret handling and log redaction.
- Decide retention and deletion rules.
- Resolve the correction release gate.
- Rehearse deployment and restart in a test environment.
- Approve a real-participant pilot explicitly.

Exit gate:
- Restore has been demonstrated.
- Existing bot remains unaffected.
- Operational and privacy decisions are documented.
- Correction limitation is accepted or correction is implemented and tested.

## 8. Planning Envelope

Foundation and registration tasks: approximately 21–34 hours.

Later milestones require refinement after the Telegram library and
environment are selected.

Initial whole-project planning envelope:
- 45–70 working hours before contingency.
- Approximately 56–88 hours with 25% contingency.

These are estimates, not delivery commitments.
A deadline requires confirmed weekly availability.

## 9. AI Usage Strategy

- Use Plan mode for one bounded analysis task.
- Use Build mode only after approving the task.
- Provide relevant files, acceptance checks, and short error excerpts.
- Avoid repository-wide scans and parallel agent fan-out.
- Prefer short implementation summaries over repeated full plans.
- Save progress before changing models or reaching usage limits.
- When unavailable, continue local tests, review, or documentation.
- Verify provider-specific retention before sending project context.