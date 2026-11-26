# Agent Instructions

## Project

Quiniela-Bot is a Python Telegram bot for recreational
team-assignment quinielas.

The authoritative product scope is in docs/requirements.md.

## Language

- Write documentation, code identifiers, and developer comments in English.
- Write user-facing Telegram messages and buttons in Mexican Spanish.

## Scope Boundaries

- The owner/admin determines which team advances and which team is eliminated.
- Do not implement score calculation, tie-breakers, fixtures,
  sports APIs, payments, or runtime AI.
- One active quiniela per group.
- One participant per Telegram user ID per quiniela.
- Participant capacity equals team count.
- No withdrawals or substitutions.
- Draw automatically when registration becomes full.
- Persist assignments; never redraw an existing quiniela.
- Elimination changes participation status, not Telegram membership.

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
- Check administrative authorization for every privileged action.
- Scope all operations to the originating Telegram group and quiniela.
- Keep secrets and personal data out of logs.

## Correctness Priorities

- Enforce participant and assignment uniqueness in storage.
- Make final registration and draw persistence atomic.
- Make repeated callbacks and confirmations safe.
- Store results before sending announcements.
- Preserve state across restarts.
- Do not silently overwrite recorded results.

## Verification

Implementation tasks must include tests for changed behavior.
Never claim a check passed unless it was actually run.

Build and test commands are not yet defined.
Document them after the project tooling is selected.

## Task Completion Summary

Report briefly:
1. Files changed.
2. Behavior or documentation added.
3. Checks performed and their outcomes.
4. Remaining blockers or decisions.