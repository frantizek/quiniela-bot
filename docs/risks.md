# Risk Register

Status: Initial assessment.

Likelihood and impact are planning judgments.
Review at each milestone and before real-participant use.

Default owner: project owner/developer.

## 1. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| RK-01 | Free-model limits interrupt work | High | Medium | Small tasks, saved checkpoints, manual checks while capped |
| RK-02 | Provider retains submitted data | Medium | High | Verify policy; never submit secrets or live records |
| RK-03 | Concurrent requests corrupt registration or draw | Medium | High | Transactions, constraints, concurrency tests |
| RK-04 | Repeated callbacks repeat mutations | Medium | High | Consumed actions, unique IDs, transactional validation |
| RK-05 | Incorrect confirmed outcome cannot be repaired | Medium | High | Clear confirmation and explicit correction release gate |
| RK-06 | Unauthorized action changes state | Medium | High | Current-role checks; fail closed |
| RK-07 | Valid admin intent becomes stale | Medium | Low | Explain rejection and allow re-initiation |
| RK-08 | Announcement delivery is uncertain | Medium | Medium | Stored intent; retry without repeating business state |
| RK-09 | Registration never fills | Medium | Medium | Visible capacity and whole-quiniela cancellation |
| RK-10 | Participants dispute draw fairness | Low | Medium | OS-backed randomness, immutable assignments, published result; avoid unsupported verifiability claims |
| RK-11 | New service disrupts existing OCI bot | Medium | High | Capacity inventory and separate runtime resources |
| RK-12 | Data loss or migration failure | Low | High | Backups, restore rehearsal, migration checks, rollback plan |
| RK-13 | Retention expectations are unclear | Medium | High | Approve retention and deletion before real-user pilot |
| RK-14 | Sports features expand scope | High | Medium | Require explicit requirements change |
| RK-15 | Cancel-and-recreate is used to seek another draw | Low | Medium | Preserve history and visibly distinguish new quinielas |
| RK-16 | Documentation is copied into the wrong file or truncated | Medium | Medium | Verify file titles and endings; review staged diffs |

## 2. Escalation Rules

Stop implementation or deployment when:
- AI work requires secrets or production records.
- Authorization cannot be implemented safely.
- Tests expose partial assignments or duplicate eliminations.
- Deployment threatens the existing bot.
- A migration lacks a tested backup and recovery path.
- Authoritative documentation is missing or contradictory.

Stop real-participant release when:
- Retention and deletion are unresolved.
- Correction limitation has not been explicitly accepted.
- Private rehearsal or restore checks fail.

## 3. Accepted Trade-offs

The following are supported by accepted decisions:

- All current Telegram administrators have quiniela authority: D-007.
- No withdrawals or substitutions: D-003.
- No correction in the first implementation, with a release gate: D-013.
- Conservative version checks may reject pending confirmations: D-011.
- Recovery may produce duplicate announcements, not duplicate state: D-009.

These trade-offs still require testing and monitoring.

## 4. Draw Fairness Communication

The approved scope requires random, immutable assignments.
It does not approve a public verification protocol.

Do not describe the draw as independently verifiable unless a separate
mechanism has been designed, approved, implemented, and tested.

Participant concerns should be reviewed without silently expanding scope.

## 5. Review Record

No completed risk-review sessions are recorded.

For each review, record:
- Date.
- Milestone.
- Changed risks.
- Mitigations.
- Decisions and responsible person.

## Document Boundary

This register identifies risks and existing trade-offs.
It does not approve new product behavior.