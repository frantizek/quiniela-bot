# Quiniela-Bot

A Telegram bot for recreational team-assignment quinielas.

An administrator registers tournament teams and opens registration.
When all participant slots are filled, the bot automatically assigns
one random team to each participant.

The group owner or a current group administrator records which team
advances and which team is eliminated. The bot updates the quiniela
until one team and its assigned participant remain.

## Project Status

Documentation and planning.

Application code, dependency selection, and deployment configuration
have not been implemented.

## MVP Scope

- Telegram groups.
- One non-terminal quiniela per group.
- Administrator-managed team list.
- Support for 2 to 32 teams, including non-powers of two.
- One participant slot per team.
- One entry per Telegram user ID per quiniela.
- No participant withdrawals or substitutions.
- Automatic random assignment when registration is full.
- Persistent, immutable assignments.
- Administrator-confirmed advancement and elimination.
- Administrator-confirmed cancellation before completion.
- Status messages and winner announcement.
- Persistent state across service restarts.
- Recoverable announcements without repeating business actions.

The primary acceptance scenario uses eight teams and eight participants.
The implementation does not require team rankings or a fixed bracket.

## Authority Over Results

The group owner or a current group administrator determines which team
advances and which team is eliminated.

The bot validates the administrative action and records it.
It does not calculate aggregate scores, apply tie-breakers, generate
fixtures, or consult sports-result services.

## Administrator Authorization

The current Telegram group owner and all current group administrators
are authorized to manage the quiniela.

There is no separate bot-managed administrator list.

Privileged actions require an identifiable acting user.
Authorization is checked again before confirming a sensitive action.
If authorization cannot be verified, no state is changed.

## Administrative Confirmations

Opening registration, recording outcomes, and cancellation require
confirmation.

- Only the initiating administrator may confirm.
- Confirmations expire after 10 minutes.
- Consumed confirmations cannot repeat an action.
- A change to the quiniela's business-state version invalidates
  an outstanding confirmation.

## Cancellation and Correction

Administrators may cancel a quiniela in DRAFT, OPEN, or ACTIVE.
Cancellation preserves history and closes the entire quiniela.

Cancellation is not a withdrawal, correction, or redraw.
A later quiniela is a separate record.

The first implementation does not support result correction.
An incorrect confirmed outcome cannot be repaired in this version.

Before use with real participants, explicitly accept this limitation
or implement a separately designed and tested correction workflow.

## Language

- Documentation, code identifiers, and developer comments: English.
- User-facing Telegram messages and buttons: Mexican Spanish.

Documentation describes interface behavior in English.
Actual Telegram messages and buttons will be implemented in Mexican Spanish.

## Accepted Technical Direction

- Python.
- SQLite for initial persistent storage.
- One application process initially.
- Telegram long polling.
- A separate service on the existing Oracle OCI infrastructure.
- Stored announcement intent for delivery recovery.

The Python version, Telegram library, OCI capacity, and service
configuration remain pending an inventory of the existing environment.

The new bot must not modify or share runtime state with the existing bot.

## Out of Scope

- Payments, betting, or prize management.
- Prediction-based scoring.
- Automatic sports-result retrieval.
- Automatic interpretation of football rules.
- Automatic bracket generation.
- Telegram broadcast-channel support.
- Participant withdrawals or substitutions.
- Multiple non-terminal quinielas in the same group.
- AI features inside the running bot.
- A web dashboard.
- Result correction in the first implementation, subject to an
  explicit decision before real-participant release.

## Documentation

### Foundation
- AGENTS.md — AI-assisted development instructions.
- docs/requirements.md — Product requirements and acceptance criteria.

### Design
- docs/architecture.md — Components, lifecycle, and persistence.
- docs/decisions.md — Accepted and unresolved decisions.
- docs/user-flows.md — Telegram interaction behavior.

### Delivery and Validation
- docs/backlog.md — Implementation tasks and milestone gates.
- docs/test-plan.md — Verification scenarios and release checks.
- docs/risks.md — Risks, mitigations, and accepted trade-offs.

### Planned Operations Documents
- docs/runbook.md — Deployment, backup, restore, and recovery.
- docs/checkpoint.md — Current progress and session handoff.

## Development Approach

1. Confirm unresolved environment details.
2. Implement domain rules and persistence tests.
3. Add Telegram interactions incrementally.
4. Rehearse the complete flow in a private test group.
5. Complete operational and privacy release gates.
6. Deploy independently from the existing bot.

Work in small, reviewable changes.
Do not add features outside the approved MVP without updating
the requirements and decision log.

## Security and Privacy

Never commit or submit bot tokens, credentials, live databases,
participant records, or production logs to an AI provider.

Use synthetic data during development.
Approve retention and deletion rules before a real-participant pilot.