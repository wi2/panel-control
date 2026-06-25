# Scenario Planning

Model decision outcomes under optimistic, realistic, and pessimistic assumptions. Replaces single-point decisions.

## Scenarios

| Scenario | Assumptions |
|----------|-------------|
| optimistic | Best-case validation, favorable market, advantages materialize |
| realistic | Base-case evidence and trends continue |
| pessimistic | Validation weakens, competition intensifies, execution delays |

Each scenario produces:

| Field | Description |
|-------|-------------|
| decision | build / monitor / kill for this scenario |
| global_score | Estimated score under scenario assumptions |
| assumptions | Key assumptions driving this outcome |

## Decision Probabilities

Aggregate probability estimates across scenarios:

```yaml
probabilities:
  build: 15%
  monitor: 50%
  kill: 35%
```

Probabilities must sum to 100%.

Use probabilities for resource allocation weighting, not as the sole decision driver.

## Primary Decision Rule

Portfolio Manager selects **primary decision** from the **realistic** scenario unless:

- Dual-gate BUILD fails (global_score or OQI)
- Automatic kill trigger met
- Critical sections have `confidence_level: low` without override

## Output Template

```yaml
scenarios:
  optimistic:
    decision: build
    global_score: 82
    assumptions: "Conversion doubles; incumbent delays feature launch"
  realistic:
    decision: monitor
    global_score: 68
    assumptions: "Current validation signal holds; CAC remains high"
  pessimistic:
    decision: kill
    global_score: 41
    assumptions: "No WTP confirmed; incumbent launches equivalent free tier"
probabilities:
  build: 15%
  monitor: 50%
  kill: 35%
confidence_level: medium
```

## Related

- [Scoring rules](scoring-rules.md)
- [Portfolio rules](portfolio-rules.md)
- [Scenario planning prompt](../prompts/scenario-planning.md)
- [Portfolio manager prompt](../prompts/portfolio-manager.md)
