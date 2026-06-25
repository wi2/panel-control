# Scoring Rules

Default scoring framework for evaluating startup opportunities. Scores range from 0 to 100.

## Decision Thresholds

| Decision | Score |
|----------|-------|
| **BUILD** | >= 70 |
| **MONITOR** | 40–69 |
| **KILL** | < 40 |

These thresholds are fixed. Override requires documented rationale in the Final Decision section.

## Dimensions and Weights

| Dimension | Weight | Measures |
|-----------|--------|----------|
| Problem severity | 20% | Pain intensity, urgency, willingness to pay |
| Market size and timing | 15% | TAM/SAM, growth rate, trend tailwinds |
| Validation strength | 25% | Evidence quality, experiment results |
| Competitive moat | 15% | Differentiation, defensibility, switching costs |
| Execution feasibility | 15% | Team fit, technical complexity, time-to-test |
| Strategic fit | 10% | Portfolio synergy, studio thesis alignment |

**Total: 100%**

## Scoring Rubric

Rate each dimension **0–10**, then multiply by weight to get the weighted contribution.

### Problem Severity (20%)

| Score | Criteria |
|-------|----------|
| 9–10 | Acute, frequent pain; customers actively seeking and paying for solutions |
| 7–8 | Clear pain; demonstrated willingness to pay or strong commitment signals |
| 5–6 | Moderate pain; interest expressed but no payment evidence |
| 3–4 | Mild inconvenience; nice-to-have positioning |
| 0–2 | No validated pain; hypothetical problem |

### Market Size and Timing (15%)

| Score | Criteria |
|-------|----------|
| 9–10 | Large addressable market ($1B+); strong tailwinds; timing is now |
| 7–8 | Meaningful market ($100M+); favorable trends |
| 5–6 | Niche but viable ($10M+); neutral timing |
| 3–4 | Small market; uncertain growth |
| 0–2 | No credible market sizing; adverse timing |

### Validation Strength (25%)

| Score | Criteria |
|-------|----------|
| 9–10 | Paid customers or binding commitments; repeatable signal |
| 7–8 | Strong qualitative signal (5+ consistent interviews); pilot interest |
| 5–6 | Mixed signal; some positive, some negative evidence |
| 3–4 | Weak signal; mostly hypothetical or single-source |
| 0–2 | No validation attempted or all experiments failed |

### Competitive Moat (15%)

| Score | Criteria |
|-------|----------|
| 9–10 | Clear, durable differentiation; network effects or data moat |
| 7–8 | Meaningful differentiation; moderate switching costs |
| 5–6 | Some differentiation; competitive but not commoditized |
| 3–4 | Weak differentiation; easily replicated |
| 0–2 | No moat; dominated by incumbents |

### Execution Feasibility (15%)

| Score | Criteria |
|-------|----------|
| 9–10 | Team has domain expertise; MVP testable in weeks |
| 7–8 | Team capable with minor gaps; MVP testable in 1–2 months |
| 5–6 | Significant skill or resource gaps; MVP in 2–3 months |
| 3–4 | Major gaps; high technical or regulatory risk |
| 0–2 | Infeasible with current team and resources |

### Strategic Fit (10%)

| Score | Criteria |
|-------|----------|
| 9–10 | Core to studio thesis; strong portfolio synergy |
| 7–8 | Good fit; leverages existing assets or relationships |
| 5–6 | Neutral fit; no conflict but no synergy |
| 3–4 | Partial misalignment with studio focus |
| 0–2 | Conflicts with studio thesis or portfolio |

## Calculation

```text
Weighted score = sum(dimension_score / 10 * weight * 100)
```

Example:

| Dimension | Raw (0–10) | Weight | Weighted |
|-----------|------------|--------|----------|
| Problem severity | 8 | 20% | 16.0 |
| Market size and timing | 6 | 15% | 9.0 |
| Validation strength | 5 | 25% | 12.5 |
| Competitive moat | 4 | 15% | 6.0 |
| Execution feasibility | 7 | 15% | 10.5 |
| Strategic fit | 6 | 10% | 6.0 |
| **Total** | | | **60.0** |

Result: **60 → MONITOR**

## Score Table Template

Use this table in the opportunity **Scoring** section:

```markdown
| Dimension | Raw (0–10) | Weight | Weighted | Rationale |
|-----------|------------|--------|----------|-----------|
| Problem severity | | 20% | | |
| Market size and timing | | 15% | | |
| Validation strength | | 25% | | |
| Competitive moat | | 15% | | |
| Execution feasibility | | 15% | | |
| Strategic fit | | 10% | | |
| **Total** | | **100%** | **XX** | |
```

## Evidence Requirements

Every dimension score must cite evidence. See [principles](../docs/principles.md) for evidence quality hierarchy.

## Customization

Studios may adjust dimension weights if changes are documented in this file with effective date. Thresholds (70/40) should remain stable for portfolio comparability.

## Related

- [Evaluation process](evaluation-process.md)
- [Kill rules](kill-rules.md)
- [Scoring prompt](../prompts/scoring.md)
