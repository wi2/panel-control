# Scoring Weights Configuration

Default dimension weights for calculating `global_score`. Studios may adjust weights; document changes with effective date below.

## Default Weights

| Dimension | Weight | Rubric focus |
|-----------|--------|--------------|
| pain_level | 15% | Severity and frequency of problem |
| urgency | 10% | Time pressure to solve |
| willingness_to_pay | 15% | Payment and commitment signals |
| competition | 8% | Competitive intensity (10 = weak competition) |
| distribution_advantage | 12% | Reach to target customers |
| technical_complexity | 8% | Ease of build (10 = low complexity) |
| maintenance_complexity | 7% | Ongoing burden (10 = low burden) |
| founder_fit | 10% | Domain expertise and execution capability |
| market_timing | 8% | Tailwinds and market window |
| defensibility | 7% | Long-term moat potential |

**Total: 100%**

## Formula

```text
global_score = sum(dimension_score / 10 * weight * 100)
```

Each dimension is rated **0–10**. Higher is more favorable for the opportunity.

For `technical_complexity` and `maintenance_complexity`, score **10 = low complexity/burden** (favorable), **0 = high complexity/burden** (unfavorable).

## Customization Log

| Effective date | Change | Rationale |
|----------------|--------|-----------|
| 2026-06-25 | Initial v2 weights | Decision intelligence upgrade |

When adjusting weights:

1. Update this table with effective date and rationale.
2. Re-score affected MONITOR opportunities at next review.
3. Do not retroactively change scores for archived opportunities.

## Related

- [Scoring rules](scoring-rules.md)
- [Migration v1 to v2](migration-v1-to-v2.md)
