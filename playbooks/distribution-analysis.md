# Distribution Analysis

Evaluate how the opportunity reaches target customers. Produces `distribution_score` (0–100) and `distribution_notes`.

## Factors

| Factor | Scale | Measures |
|--------|-------|----------|
| Acquisition difficulty | 0–10 | Cost and effort to acquire one customer (10 = easy) |
| Channel accessibility | 0–10 | Availability of viable acquisition channels (10 = many accessible) |
| Estimated CAC | value + evidence | Customer acquisition cost estimate |
| Competition intensity | 0–10 | How crowded paid/organic channels are (10 = low intensity) |
| Founder audience advantage | 0–10 | Existing reach to target segment (10 = strong advantage) |

## distribution_score Calculation

Default weights (adjust in studio config if needed):

| Factor | Weight |
|--------|--------|
| Acquisition difficulty | 25% |
| Channel accessibility | 20% |
| Competition intensity | 20% |
| Founder audience advantage | 25% |
| CAC favorability | 10% |

```text
distribution_score = sum(factor_score / 10 * weight * 100)
```

For CAC favorability: score 10 if CAC < 20% of LTV (verified/estimated), scale down for higher ratios or unknown LTV.

## Evidence Requirements

Every factor must include evidence type per [evidence-classification.md](evidence-classification.md).

## Output Template

```yaml
distribution_score: 62
distribution_notes: "Primary channel is outbound sales; founder has 2k LinkedIn followers in segment but no proven conversion."
confidence_level: medium
```

## Relationship to Scoring

- `distribution_advantage` sub-score in [scoring-rules.md](scoring-rules.md) should align with `distribution_score`.
- Portfolio Manager uses distribution analysis for BUILD resource allocation.

## Related

- [Scoring rules](scoring-rules.md)
- [Distribution analysis prompt](../prompts/distribution-analysis.md)
- [Unfair advantage analysis](unfair-advantage-analysis.md)
