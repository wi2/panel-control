# Migration: Scoring v1 to v2

Guide for converting opportunities evaluated under the legacy 6-dimension framework to the v2 decision intelligence model.

## What Changed

| v1 | v2 |
|----|-----|
| Single `score` (0–100) | `global_score` from 10 sub-scores |
| 6 dimensions | 10 dimensions (see [scoring-weights.md](scoring-weights.md)) |
| BUILD >= 70 | BUILD: global_score >= 75 AND OQI >= 70 |
| MONITOR 40–69 | MONITOR: global_score 50–74 |
| KILL < 40 | KILL: global_score < 50 |
| Blockquote evidence only | Evidence type required on every claim |
| Single decision | Scenario planning + primary decision |
| All 9 stages before decision | 10 decision stages; product stages BUILD-only |

## Dimension Mapping

| v1 dimension | v2 mapping |
|--------------|------------|
| Problem severity | pain_level + urgency + willingness_to_pay |
| Market size and timing | market_timing (+ market claims in Discovery) |
| Validation strength | Feeds evidence_quality in OQI (not a sub-score) |
| Competitive moat | competition + defensibility + unfair_advantage analysis |
| Execution feasibility | technical_complexity + founder_fit |
| Strategic fit | portfolio_fit_score (Portfolio Intelligence section) |

## Migration Steps

1. Add migration banner to opportunity file (see example below).
2. Re-run decision path with v2 prompts; do not map old scores directly.
3. Tag all existing claims with evidence types.
4. Add new sections: Distribution, Unfair Advantage, Maintenance, Risk, Portfolio Intelligence, Scenario Planning.
5. Calculate OQI and update frontmatter: `global_score`, `opportunity_quality_index`.
6. Update portfolio registry row with Global Score and OQI columns.
7. Record `prompt_versions` for all v2 stages used.

## Migration Banner

Add at top of body for in-flight v1 opportunities:

```markdown
> **Migration note**: This opportunity was evaluated under scoring v1. Re-run the [evaluation process](evaluation-process.md) with v2 prompts before the next portfolio review.
```

## Prompt Version Updates

```yaml
prompt_versions:
  discovery: v1
  validation: v1
  scoring: v2
  distribution_analysis: v1
  unfair_advantage: v1
  maintenance_evaluation: v1
  risk_analysis: v1
  portfolio_intelligence: v1
  scenario_planning: v1
  portfolio_manager: v2
  # BUILD-only (if applicable):
  vision: v1
  mvp: v1
  roadmap: v1
  architecture: v1
  success_contract: v1
```

## Related

- [Evaluation process](evaluation-process.md)
- [Scoring rules](scoring-rules.md)
- [Scoring weights](scoring-weights.md)
