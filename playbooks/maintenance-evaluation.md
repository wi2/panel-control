# Maintenance Evaluation

Assess ongoing operational burden after launch. Produces `maintenance_score` (1–10).

## Scale

| Score | Meaning |
|-------|---------|
| 1 | Almost no maintenance; fully self-serve |
| 5 | Moderate ongoing effort |
| 10 | High operational burden; constant manual intervention |

## Factors

| Factor | Evaluates |
|--------|-----------|
| customer_support | Ticket volume, complexity, SLA requirements |
| ai_costs | LLM/API inference costs at scale |
| integrations | Third-party API maintenance, breakage risk |
| external_dependencies | Reliance on vendors, platforms, data providers |
| regulations | Compliance overhead, audits, reporting |
| manual_operations | Human-in-the-loop processes that cannot be automated |

Each factor: score 1–10 (higher = more burden) with evidence type.

## maintenance_score Calculation

```text
maintenance_score = mean(factor_scores)
```

Round to one decimal.

## Cross-Validation with Scoring

`maintenance_complexity` sub-score in [scoring-rules.md](scoring-rules.md) is **inverted**:

```text
maintenance_complexity sub-score = 10 - (maintenance_score - 1) * (10 / 9)
```

Example: maintenance_score 8 → maintenance_complexity sub-score ≈ 2.2

## Output Template

```yaml
maintenance_score: 6
maintenance_factors:
  customer_support: { score: 5, evidence: estimated }
  ai_costs: { score: 7, evidence: inferred }
  integrations: { score: 6, evidence: estimated }
  external_dependencies: { score: 4, evidence: verified }
  regulations: { score: 3, evidence: verified }
  manual_operations: { score: 8, evidence: inferred }
confidence_level: low
```

## Related

- [Scoring rules](scoring-rules.md)
- [Maintenance evaluation prompt](../prompts/maintenance-evaluation.md)
- [Risk analysis](risk-analysis.md)
