# Portfolio Rules

Governance for managing the opportunity portfolio across active, monitoring, and archived states.

## Portfolio Files

| File | Decision | Criteria |
|------|----------|----------|
| [`active.md`](../portfolio/active.md) | BUILD | `global_score >= 75` AND `OQI >= 70` |
| [`monitoring.md`](../portfolio/monitoring.md) | MONITOR | `global_score` 50–74, OR score qualifies but OQI < 70 |
| [`archived.md`](../portfolio/archived.md) | KILL | `global_score < 50` or kill trigger |

## Dual-Gate BUILD Rule

BUILD requires **both**:

| Gate | Threshold |
|------|-----------|
| global_score | >= 75 |
| opportunity_quality_index | >= 70 |

If `global_score >= 75` but `OQI < 70`, default to **MONITOR** until evidence improves.

See [opportunity-quality-index.md](opportunity-quality-index.md).

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

Rank BUILD candidates by `global_score`, then `OQI`, then `portfolio_fit_score`.

## Promotion Rules

### MONITOR → BUILD

Requires:

1. Re-validation with new positive evidence
2. Re-score: `global_score >= 75` AND `OQI >= 70`
3. Available active capacity
4. Success Contract drafted (BUILD preparation complete)
5. Portfolio review approval
6. No `confidence_level: low` on Scoring, Distribution, or Risk without override

Update: remove from `monitoring.md`, add to `active.md`.

### BUILD → MONITOR (Demotion)

When:

- Success Contract review shows missed metrics
- Re-score drops to 50–74
- OQI drops below 70
- Strategic reprioritization

Requires documented rationale. Update: remove from `active.md`, add to `monitoring.md`.

## Archival Rules

Move to `archived.md` when:

- `global_score < 50`
- Any automatic kill trigger met (see [kill rules](kill-rules.md))
- Manual kill decision

Always record kill reason and `expected_learnings`. Never delete archived entries.

## Review Cadence

| Category | Frequency | Actions |
|----------|-----------|---------|
| Active (BUILD) | Every 30 days | Review Success Contract metrics; check exit triggers |
| Monitoring (MONITOR) | Every 90 days | Re-run validation minimum; re-score; recalculate OQI; apply kill rules |
| Archived | None | Reference for learnings |

Use [`templates/portfolio-review-template.md`](../templates/portfolio-review-template.md) for quarterly reviews.

## Portfolio Entry Format

Each portfolio file uses a table:

```markdown
| ID | Title | Global Score | OQI | Decision | Owner | Decision Date | Next Review | Link |
```

Archived adds a **Kill reason** column:

```markdown
| ID | Title | Global Score | OQI | Owner | Decision Date | Kill Reason | Link |
```

## State Transitions

```text
New opportunity
    → evaluating
        → BUILD (global_score >= 75 AND OQI >= 70) → active.md
        → MONITOR (global_score 50–74) → monitoring.md
        → KILL (global_score < 50) → archived.md

active.md → monitoring.md (demotion)
active.md → archived.md (kill)
monitoring.md → active.md (promotion)
monitoring.md → archived.md (kill)
```

## Evidence and Confidence Gates

Portfolio Manager must not BUILD when:

- Scoring, Distribution, or Risk sections have `confidence_level: low` (without documented override)
- Decision relies predominantly on `synthetic` or `unknown` evidence
- Realistic scenario decision is not BUILD

## Resource Allocation

- BUILD opportunities receive dedicated owner and build budget
- MONITOR opportunities receive evaluation budget only (experiments, interviews)
- No resources allocated to archived opportunities
- Weight allocation by scenario probabilities when multiple MONITOR opportunities compete

## Quarterly Portfolio Review

Every quarter:

1. Review all active and monitoring entries
2. Re-score monitoring opportunities with new evidence; recalculate OQI
3. Aggregate `expected_learnings` from archived opportunities
4. Apply kill rules to stale monitors
5. Assess capacity and resource allocation
6. Document in portfolio review artifact

## Related

- [Kill rules](kill-rules.md)
- [Scoring rules](scoring-rules.md)
- [Opportunity quality index](opportunity-quality-index.md)
- [Portfolio intelligence](portfolio-intelligence.md)
- [Evaluation process](evaluation-process.md)
