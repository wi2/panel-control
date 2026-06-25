# Scoring Rules

Multi-dimensional scoring framework for evaluating startup opportunities. Produces `global_score` (0–100) from 10 weighted sub-scores.

## Decision Thresholds

| Decision | Criteria |
|----------|----------|
| **BUILD** | `global_score >= 75` AND `opportunity_quality_index >= 70` |
| **MONITOR** | `global_score` 50–74, OR score qualifies but OQI < 70 |
| **KILL** | `global_score < 50` |

These thresholds are fixed. Override requires documented rationale in the Final Decision section.

See [opportunity-quality-index.md](opportunity-quality-index.md) for OQI calculation.

## Dimensions and Weights

Default weights are configured in [scoring-weights.md](scoring-weights.md).

| Dimension | Default weight | Measures |
|-----------|----------------|----------|
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

## Scoring Rubric

Rate each dimension **0–10**, then multiply by weight to get the weighted contribution. Every score must cite evidence type per [evidence-classification.md](evidence-classification.md).

### pain_level (15%)

| Score | Criteria |
|-------|----------|
| 9–10 | Acute, frequent pain; customers actively seeking solutions |
| 7–8 | Clear pain; strong qualitative signal from 5+ interviews |
| 5–6 | Moderate pain; interest expressed but inconsistent signal |
| 3–4 | Mild inconvenience; nice-to-have positioning |
| 0–2 | No validated pain; hypothetical problem |

### urgency (10%)

| Score | Criteria |
|-------|----------|
| 9–10 | Immediate need; regulatory deadline or acute cost of inaction |
| 7–8 | Strong time pressure; customers prioritizing solution now |
| 5–6 | Moderate urgency; problem worsening over months |
| 3–4 | Low urgency; deferrable problem |
| 0–2 | No time pressure; status quo acceptable |

### willingness_to_pay (15%)

| Score | Criteria |
|-------|----------|
| 9–10 | Paid customers or binding commitments; repeatable signal |
| 7–8 | Strong WTP signal from interviews; pilot or LOI interest |
| 5–6 | Mixed signal; interest but no payment evidence |
| 3–4 | Price sensitivity high; free-tier expectation |
| 0–2 | No WTP evidence; hypothetical demand |

### competition (8%)

| Score | Criteria |
|-------|----------|
| 9–10 | Fragmented market; no dominant incumbent; clear gap |
| 7–8 | Competitors exist but differentiation is credible |
| 5–6 | Moderate competition; crowded but not commoditized |
| 3–4 | Strong incumbents; difficult differentiation |
| 0–2 | Dominated by entrenched players; no viable wedge |

### distribution_advantage (12%)

| Score | Criteria |
|-------|----------|
| 9–10 | Direct access to target customers; proven channel |
| 7–8 | Accessible channels; founder has relevant audience |
| 5–6 | Standard channels available; no unique advantage |
| 3–4 | Expensive or difficult acquisition; long sales cycles |
| 0–2 | No viable distribution path identified |

Cross-reference [distribution-analysis.md](distribution-analysis.md).

### technical_complexity (8%)

| Score | Criteria |
|-------|----------|
| 9–10 | Simple build; MVP testable in weeks |
| 7–8 | Moderate complexity; MVP in 1–2 months |
| 5–6 | Significant engineering; 2–3 months to testable slice |
| 3–4 | High complexity; major technical unknowns |
| 0–2 | Infeasible with current team and resources |

### maintenance_complexity (7%)

| Score | Criteria |
|-------|----------|
| 9–10 | Almost no ongoing maintenance; self-serve product |
| 7–8 | Low operational burden; minimal support |
| 5–6 | Moderate support and integration maintenance |
| 3–4 | High support burden or costly AI/API dependencies |
| 0–2 | Heavy manual operations or regulatory overhead |

Cross-reference [maintenance-evaluation.md](maintenance-evaluation.md).

### founder_fit (10%)

| Score | Criteria |
|-------|----------|
| 9–10 | Deep domain expertise; prior success in adjacent space |
| 7–8 | Strong relevant skills; minor gaps fillable |
| 5–6 | Generalist team; learning curve required |
| 3–4 | Significant skill gaps; key capability missing |
| 0–2 | No relevant expertise; wrong team for opportunity |

### market_timing (8%)

| Score | Criteria |
|-------|----------|
| 9–10 | Strong tailwinds; window is now; category growing fast |
| 7–8 | Favorable trends; timing supports entry |
| 5–6 | Neutral timing; market stable |
| 3–4 | Uncertain timing; early or late to market |
| 0–2 | Adverse timing; market contracting or technology immature |

### defensibility (7%)

| Score | Criteria |
|-------|----------|
| 9–10 | Durable moat; network effects, data, or exclusive assets |
| 7–8 | Meaningful differentiation; moderate switching costs |
| 5–6 | Some defensibility; not easily replicated in short term |
| 3–4 | Weak moat; features copyable by incumbents |
| 0–2 | No defensibility; commodity positioning |

Cross-reference [unfair-advantage-analysis.md](unfair-advantage-analysis.md).

## Calculation

```text
global_score = sum(dimension_score / 10 * weight * 100)
```

Example:

| Dimension | Raw (0–10) | Weight | Weighted |
|-----------|------------|--------|----------|
| pain_level | 8 | 15% | 12.0 |
| urgency | 7 | 10% | 7.0 |
| willingness_to_pay | 6 | 15% | 9.0 |
| competition | 4 | 8% | 3.2 |
| distribution_advantage | 5 | 12% | 6.0 |
| technical_complexity | 7 | 8% | 5.6 |
| maintenance_complexity | 6 | 7% | 4.2 |
| founder_fit | 6 | 10% | 6.0 |
| market_timing | 7 | 8% | 5.6 |
| defensibility | 4 | 7% | 2.8 |
| **Total** | | **100%** | **61.4** |

Result: **global_score 61 → MONITOR**

## Score Table Template

Use this table in the opportunity **Scoring** section:

```markdown
| Dimension | Raw (0–10) | Weight | Weighted | Evidence | Rationale |
|-----------|------------|--------|----------|----------|-----------|
| pain_level | | 15% | | | |
| urgency | | 10% | | | |
| willingness_to_pay | | 15% | | | |
| competition | | 8% | | | |
| distribution_advantage | | 12% | | | |
| technical_complexity | | 8% | | | |
| maintenance_complexity | | 7% | | | |
| founder_fit | | 10% | | | |
| market_timing | | 8% | | | |
| defensibility | | 7% | | | |
| **Total** | | **100%** | **XX** | | |

**global_score**: XX
**confidence_level**: high / medium / low
```

## Evidence Requirements

Every dimension score must cite evidence type. See [evidence-classification.md](evidence-classification.md) and [principles](../docs/principles.md).

## Customization

Studios may adjust dimension weights in [scoring-weights.md](scoring-weights.md). Thresholds (75/50, OQI 70) should remain stable for portfolio comparability.

## Related

- [Scoring weights](scoring-weights.md)
- [Opportunity quality index](opportunity-quality-index.md)
- [Evaluation process](evaluation-process.md)
- [Scoring prompt](../prompts/scoring.md)
- [Migration v1 to v2](migration-v1-to-v2.md)
