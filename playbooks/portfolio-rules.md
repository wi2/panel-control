# Portfolio Rules

Governance for managing the opportunity portfolio across active, monitoring, and archived states.

## Portfolio Files

| File | Decision | Score |
|------|----------|-------|
| [`active.md`](../portfolio/active.md) | BUILD | >= 70 |
| [`monitoring.md`](../portfolio/monitoring.md) | MONITOR | 40–69 |
| [`archived.md`](../portfolio/archived.md) | KILL | < 40 |

## Capacity Limits

Default limits (adjust per studio capacity):

| Category | Max entries | Rationale |
|----------|-------------|-----------|
| Active (BUILD) | 3 | Focus resources on highest-conviction opportunities |
| Monitoring (MONITOR) | 10 | Limit overhead of periodic re-evaluation |
| Archived | Unlimited | Historical record |

When at capacity:

- **New BUILD**: requires killing or archiving an existing active opportunity, or completing one
- **New MONITOR**: requires killing lowest-scoring monitor opportunity if at limit

## Promotion Rules

### MONITOR → BUILD

Requires:

1. Re-validation with new positive evidence
2. Re-score >= 70
3. Available active capacity
4. Success Contract drafted
5. Portfolio review approval

Update: remove from `monitoring.md`, add to `active.md`.

### BUILD → MONITOR (Demotion)

When:

- Success Contract review shows missed metrics
- Re-score drops to 40–69
- Strategic reprioritization

Requires documented rationale. Update: remove from `active.md`, add to `monitoring.md`.

## Archival Rules

Move to `archived.md` when:

- Score < 40
- Any automatic kill trigger met (see [kill rules](kill-rules.md))
- Manual kill decision

Always record kill reason. Never delete archived entries.

## Review Cadence

| Category | Frequency | Actions |
|----------|-----------|---------|
| Active (BUILD) | Every 30 days | Review Success Contract metrics; check exit triggers |
| Monitoring (MONITOR) | Every 90 days | Re-run validation minimum; re-score; apply kill rules |
| Archived | None | Reference only |

Use [`templates/portfolio-review-template.md`](../templates/portfolio-review-template.md) for quarterly reviews.

## Portfolio Entry Format

Each portfolio file uses a table:

```markdown
| ID | Title | Score | Owner | Decision Date | Next Review | Link |
```

Archived adds a **Kill reason** column:

```markdown
| ID | Title | Score | Owner | Decision Date | Kill Reason | Link |
```

## State Transitions

```text
New opportunity
    → evaluating
        → BUILD (score >= 70) → active.md
        → MONITOR (score 40–69) → monitoring.md
        → KILL (score < 40) → archived.md

active.md → monitoring.md (demotion)
active.md → archived.md (kill)
monitoring.md → active.md (promotion)
monitoring.md → archived.md (kill)
```

## Resource Allocation

- BUILD opportunities receive dedicated owner and build budget
- MONITOR opportunities receive evaluation budget only (experiments, interviews)
- No resources allocated to archived opportunities

## Quarterly Portfolio Review

Every quarter:

1. Review all active and monitoring entries
2. Re-score monitoring opportunities with new evidence
3. Apply kill rules to stale monitors
4. Assess capacity and resource allocation
5. Document in portfolio review artifact

## Related

- [Kill rules](kill-rules.md)
- [Scoring rules](scoring-rules.md)
- [Evaluation process](evaluation-process.md)
