# Opportunity Quality Index (OQI)

The Opportunity Quality Index measures decision reliability, not opportunity attractiveness alone. Scale: **0–100**.

A high `global_score` with low OQI means the opportunity looks good but the evidence base is weak. BUILD requires both.

## Formula

```text
OQI = 0.30 * evidence_quality
    + 0.25 * confidence_aggregate
    + 0.25 * score_reliability
    + 0.20 * risk_adjustment
```

## Components

### evidence_quality (0–100)

Percentage of decision-relevant claims weighted by evidence type. See [evidence-classification.md](evidence-classification.md) for type weights.

```text
evidence_quality = (sum of claim weights) / (number of claims) * 100
```

Count claims from: Discovery, Validation, Scoring rationales, Distribution Analysis, Unfair Advantage, Maintenance, Risk Analysis, Portfolio Intelligence.

### confidence_aggregate (0–100)

Mean of section `confidence_level` values across all decision-path sections:

| Level | Score |
|-------|-------|
| high | 100 |
| medium | 60 |
| low | 30 |

Sections: Discovery, Validation, Scoring, Distribution Analysis, Unfair Advantage, Maintenance Evaluation, Risk Analysis, Portfolio Intelligence, Scenario Planning.

### score_reliability (0–100)

Penalizes `global_score` when scoring inputs rely on weak evidence.

```text
score_reliability = 100 - (synthetic_or_unknown_claims_in_scoring / total_scoring_claims * 100)
```

If no scoring claims are tagged, default to 50 (medium reliability).

### risk_adjustment (0–100)

```text
risk_adjustment = 100 - risk_exposure_score
```

Where `risk_exposure_score` comes from [Risk Analysis](risk-analysis.md). Higher risk exposure lowers OQI.

## Dual-Gate BUILD Rule

| Gate | Threshold |
|------|-----------|
| global_score | >= 75 |
| opportunity_quality_index | >= 70 |

Both must pass for BUILD. If `global_score >= 75` but `OQI < 70`, default decision is **MONITOR** until evidence improves.

## Recording OQI

In opportunity frontmatter:

```yaml
opportunity_quality_index: 68
```

In **Final Decision** section, include breakdown:

```markdown
| Component | Score |
|-----------|-------|
| evidence_quality | 72 |
| confidence_aggregate | 60 |
| score_reliability | 65 |
| risk_adjustment | 75 |
| **OQI** | **68** |
```

## Related

- [Scoring rules](scoring-rules.md)
- [Evidence classification](evidence-classification.md)
- [Portfolio rules](portfolio-rules.md)
- [Risk analysis](risk-analysis.md)
