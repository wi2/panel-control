# Portfolio Intelligence

Evaluate how an opportunity fits the existing portfolio. Produces `portfolio_fit_score` (0–100) and `portfolio_fit_notes`.

Replaces the legacy "Strategic fit" scoring dimension.

## Inputs

- Current [active](../portfolio/active.md) and [monitoring](../portfolio/monitoring.md) portfolios
- Opportunity tags and studio thesis ([philosophy](../docs/philosophy.md))
- Unfair advantage and distribution analyses

## Factors

| Factor | Scale | Measures |
|--------|-------|----------|
| diversification_impact | 0–10 | Reduces portfolio concentration risk (10 = strong diversification) |
| overlap_with_existing | 0–10 | Low overlap is favorable (10 = no overlap; score inverted from overlap %) |
| shared_infrastructure | 0–10 | Reuse of auth, billing, data pipeline, etc. |
| cross_selling | 0–10 | Upsell/cross-sell potential with existing products |
| operational_synergies | 0–10 | Shared support, marketing, or ops |

## portfolio_fit_score Calculation

Default equal weights (20% each):

```text
portfolio_fit_score = sum(factor_score / 10 * 0.20 * 100)
```

## Output Template

```yaml
portfolio_fit_score: 74
portfolio_fit_notes: "Complements active B2B SaaS entries; shares auth infrastructure; no direct overlap with monitoring opportunities."
confidence_level: medium
```

## Portfolio Manager Usage

- Rank BUILD candidates when capacity is limited
- Flag high-overlap opportunities for kill or merge consideration
- Identify cross-sell and infrastructure reuse at BUILD allocation

## Related

- [Portfolio rules](portfolio-rules.md)
- [Scoring rules](scoring-rules.md)
- [Portfolio intelligence prompt](../prompts/portfolio-intelligence.md)
