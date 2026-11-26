# Quiniela-Bot

A Telegram bot for recreational team-assignment quinielas.

An administrator registers tournament teams and opens registration.
When all participant slots are filled, the bot automatically assigns
one random team to each participant.

The group owner or an authorized administrator records which team
advances and which team is eliminated. The bot updates the quiniela
until one team and its assigned participant remain.

## Project Status

Documentation and planning.

Application code, dependency selection, and deployment configuration
have not been implemented.

## MVP Scope

- Telegram groups.
- One active quiniela per group.
- Administrator-managed team list.
- One participant slot per team.
- One entry per Telegram user ID per quiniela.
- No participant withdrawals.
- Automatic random assignment when registration is full.
- Persistent, immutable assignments.
- Administrator-confirmed advancement and elimination.
- Status messages and winner announcement.
- Persistent state across service restarts.

The first acceptance scenario uses eight teams and eight participants.
The initial implementation does not require team rankings or a
fixed tournament bracket.

## Authority Over Results

The group owner or an authorized administrator determines which team
advances.

The bot validates the administrative action and records it.
It does not calculate aggregate scores, apply tie-breakers, generate
fixtures, or consult sports-result services.

## Language

- Documentation, code identifiers, and developer comments: English.
- User-facing Telegram messages and buttons: Mexican Spanish.

Documentation describes interface behavior in English.
Actual Telegram messages and buttons will be implemented in Mexican Spanish.

## Proposed Technical Direction

- Python.
- SQLite for initial persistent storage.
- A separate service on the existing Oracle OCI infrastructure.
- Telegram long polling for the initial deployment.

The Python version, Telegram library, and service configuration remain
pending an inventory of the existing environment.

The new bot must not modify or share runtime state with the existing bot.

## Out of Scope

- Payments, betting, or prize management.
- Prediction-based scoring.
- Automatic sports-result retrieval.
- Automatic interpretation of football rules.
- Telegram broadcast-channel support.
- Participant withdrawals or substitutions.
- Multiple active quinielas in the same group.
- AI features inside the running bot.
- A web dashboard.

## Documentation

### Foundation
- AGENTS.md — AI-assisted development instructions.
- docs/requirements.md — Product requirements and acceptance criteria.

### Planned Design Documents
- docs/architecture.md
- docs/decisions.md
- docs/user-flows.md

### Planned Delivery Documents
- docs/backlog.md
- docs/test-plan.md
- docs/risks.md

### Planned Operations Documents
- docs/runbook.md
- docs/checkpoint.md

## Development Approach

1. Agree on requirements and document unresolved decisions.
2. Implement domain rules and persistence tests.
3. Add Telegram interactions incrementally.
4. Rehearse the complete flow in a private test group.
5. Deploy independently from the existing bot.

Work in small, reviewable changes. Do not add features outside the
approved MVP without updating the requirements first.

## Security and Privacy

Never commit or submit bot tokens, credentials, live databases,
participant records, or production logs to an AI provider.

Use synthetic data during development.