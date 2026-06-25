# Unfair Advantage Analysis

Evaluate structural advantages that competitors cannot easily replicate. Produces `unfair_advantages` list and `moat_score` (0–10).

## Advantage Types

| Type | Description |
|------|-------------|
| existing_audience | Built-in reach to target customers |
| existing_expertise | Deep domain knowledge or credentials |
| proprietary_data | Unique datasets or insights |
| exclusive_partnerships | Locked distribution or supply relationships |
| technical_moat | Hard-to-replicate technology or IP |
| seo_moat | Established organic search presence |
| community_moat | Engaged user community or network effects |

## Strength Levels

| Level | Criteria |
|-------|----------|
| high | Verified, durable, directly relevant to this opportunity |
| medium | Present but unproven or partially relevant |
| low | Weak, indirect, or easily replicated |
| none | Advantage type not present |

## moat_score Calculation

Rate overall moat strength 0–10:

| Score | Criteria |
|-------|----------|
| 9–10 | Multiple high-strength advantages; durable moat |
| 7–8 | One high + one medium advantage |
| 5–6 | One medium advantage; some differentiation |
| 3–4 | Low-strength advantages only |
| 0–2 | No unfair advantages identified |

## Output Template

```yaml
unfair_advantages:
  - type: existing_audience
    strength: high
    evidence: verified
    notes: "12k newsletter subscribers in target segment"
  - type: technical_moat
    strength: none
    evidence: unknown
    notes: ""
moat_score: 7
confidence_level: medium
```

## Relationship to Scoring

- Feeds `defensibility` sub-score in [scoring-rules.md](scoring-rules.md).
- Contributes to OQI via evidence types on advantage claims.

## Related

- [Scoring rules](scoring-rules.md)
- [Distribution analysis](distribution-analysis.md)
- [Unfair advantage prompt](../prompts/unfair-advantage.md)
