# Risk Analysis

Structured risk register for portfolio decisions. Produces `risks` and `risk_exposure_score` (0–100, higher = riskier).

## Mandatory Categories

| Category | Evaluates |
|----------|-----------|
| market_risk | Demand, timing, market contraction |
| technical_risk | Build feasibility, dependencies, scalability |
| regulatory_risk | Compliance, legal barriers, policy changes |
| competition_risk | Incumbent response, commoditization |
| execution_risk | Team capacity, timeline, resource gaps |

## Risk Fields

Each risk must include:

| Field | Values |
|-------|--------|
| probability | low / medium / high (or 0–10) |
| impact | low / medium / high (or 0–10) |
| mitigation | Concrete action to reduce exposure |
| evidence | Evidence type for the assessment |

## Probability and Impact Scoring

When using low/medium/high:

| Level | Numeric |
|-------|---------|
| low | 3 |
| medium | 6 |
| high | 9 |

## risk_exposure_score Calculation

For each risk:

```text
risk_value = (probability_numeric / 10) * (impact_numeric / 10) * 100
```

```text
risk_exposure_score = mean(risk_values across all 5 categories)
```

Feeds OQI: `risk_adjustment = 100 - risk_exposure_score`.

## Output Template

```yaml
risks:
  market_risk:
    probability: medium
    impact: high
    mitigation: "Run 10 additional interviews in adjacent segment before BUILD"
    evidence: inferred
  technical_risk:
    probability: low
    impact: medium
    mitigation: "Spike integration with accounting API in week 1"
    evidence: estimated
  regulatory_risk:
    probability: low
    impact: low
    mitigation: "Legal review of data handling requirements"
    evidence: verified
  competition_risk:
    probability: high
    impact: high
    mitigation: "Focus on underserved SMB segment incumbents ignore"
    evidence: verified
  execution_risk:
    probability: medium
    impact: medium
    mitigation: "Hire part-time domain advisor"
    evidence: inferred
risk_exposure_score: 65
confidence_level: medium
```

## Architecture Reference

Technical risks in **Architecture Proposal** (BUILD-only) must reference this section, not duplicate business risks.

## Related

- [Opportunity quality index](opportunity-quality-index.md)
- [Kill rules](kill-rules.md)
- [Risk analysis prompt](../prompts/risk-analysis.md)
