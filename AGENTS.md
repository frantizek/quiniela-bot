# Agent Instructions

## Project

Quiniela-Bot is a Python Telegram bot for recreational
team-assignment quinielas.

Product authority:
- docs/requirements.md defines required behavior.
- docs/decisions.md records accepted and unresolved decisions.

If documentation conflicts, report the conflict.
Do not silently choose a new product rule.

## Language

- Write documentation, code identifiers, and developer comments in English.
- Write actual user-facing Telegram messages and buttons in Mexican Spanish.
- Describe interface behavior in English in documentation.

## Scope Boundaries

- The owner/admin determines which team advances and which is eliminated.
- Do not implement score calculation, tie-breakers, fixtures,
  sports APIs, payments, or runtime AI.
- One non-terminal quiniela per group.
- Support 2 to 32 teams; do not require powers of two.
- One participant per Telegram user ID per quiniela.
- Participant capacity equals team count.
- No withdrawals or substitutions.
- Draw automatically when registration becomes full.
- Persist assignments; never redraw an existing quiniela.
- Elimination changes participation status, not Telegram membership.
- Cancellation is allowed only in DRAFT, OPEN, or ACTIVE.
- Preserve canceled quiniela history.
- Do not implement result editing or undo without an approved scope change.

## Authorization and Confirmation

- Current Telegram owner and all current administrators are authorized.
- There is no separate bot-managed administrator list.
- Reject administrative actions without an identifiable actor.
- Check current authorization for every privileged action.
- Recheck authorization at confirmation.
- Fail closed if authorization cannot be verified.
- Only the initiating administrator may confirm.
- Confirmations expire after 10 minutes.
- Reject consumed or stale confirmations without repeating a mutation.
- Follow the business-state version rules in D-011.

## Technical Direction

- Python.
- SQLite with explicit transactions and uniqueness constraints.
- One application process initially.
- Telegram long polling.
- Separate OCI service, token, environment, and database.
- Persist announcement intent alongside committed business changes.

Do not assume the Python version, Telegram library, OCI capacity,
or deployment supervisor. These remain open until verified.

## Working Rules

- Read only documentation and files relevant to the current task.
- Do not scan the entire repository unless necessary.
- Complete one small task at a time.
- State assumptions and unresolved decisions explicitly.
- Do not introduce dependencies without explaining the need.
- Prefer straightforward code over speculative abstractions.
- Do not implement features during documentation-only tasks.
- Do not commit, push, deploy, or modify infrastructure without approval.
- Do not modify the existing bot or its runtime resources.

## Security

- Never read .env files, tokens, private keys, live databases,
  backups, or production logs.
- Do not request real participant data.
- Use synthetic fixtures.
- Scope all operations to the originating group and quiniela.
- Keep secrets and unnecessary personal data out of logs.
- Validate callbacks against stored state.
- Never treat callback payloads as authoritative business records.

## Correctness Priorities

- Enforce participant and assignment uniqueness in storage.
- Make final registration and draw persistence atomic.
- Make repeated callbacks and confirmations safe.
- Store results and announcement intent before sending messages.
- Preserve state across restarts.
- Announcement retries must not redraw or repeat eliminations.
- Do not promise exactly-once Telegram message delivery.
- Do not silently overwrite recorded results.

## Verification

Implementation tasks must include tests for changed behavior.
Never claim a check passed unless it was actually run.

Build and test commands are not yet defined.
Document them after project tooling is selected.

## Release Boundaries

Before use with real participants:
- Approve retention and deletion rules.
- Demonstrate backup and restore.
- Verify deployment isolation.
- Pass a private-group rehearsal.
- Explicitly accept the correction limitation or implement
  an approved and tested correction workflow.

## Task Completion Summary

Report briefly:
1. Files changed.
2. Behavior or documentation added.
3. Checks performed and their outcomes.
4. Remaining blockers or decisions.