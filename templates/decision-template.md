---
id: DEC-YYYYMMDD-slug
opportunity_id: OPP-YYYYMMDD-slug
decision: null
global_score: null
opportunity_quality_index: null
decision_date: YYYY-MM-DD
decided_by: ""
status: draft
---

# Decision Record — {Title}

Standalone decision record for opportunity [{opportunity_id}](../opportunities/OPP-YYYYMMDD-slug.md).

## Decision

| Field | Value |
|-------|-------|
| **Primary Decision** | build / monitor / kill |
| **global_score** | XX |
| **opportunity_quality_index** | XX |
| **Threshold** | BUILD: global_score >= 75 AND OQI >= 70; MONITOR: 50–74; KILL: < 50 |
| **Date** | YYYY-MM-DD |
| **Decided by** | |

## OQI Breakdown

| Component | Score |
|-----------|-------|
| evidence_quality | XX |
| confidence_aggregate | XX |
| score_reliability | XX |
| risk_adjustment | XX |
| **OQI** | **XX** |

## Scenarios

| Scenario | Decision | global_score | Key Assumption |
|----------|----------|--------------|----------------|
| Optimistic | | | |
| Realistic | | | |
| Pessimistic | | | |

| Outcome | Probability |
|---------|-------------|
| build | XX% |
| monitor | XX% |
| kill | XX% |

## Evidence Summary

Key evidence supporting this decision:

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| | | verified / estimated / inferred / synthetic / unknown | | |

## Score Breakdown

| Dimension | Raw (0–10) | Weighted | Evidence |
|-----------|------------|----------|----------|
| pain_level | | | |
| urgency | | | |
| willingness_to_pay | | | |
| competition | | | |
| distribution_advantage | | | |
| technical_complexity | | | |
| maintenance_complexity | | | |
| founder_fit | | | |
| market_timing | | | |
| defensibility | | | |
| **global_score** | | **XX** | |

## Intelligence Summary

| Analysis | Score | confidence_level |
|----------|-------|------------------|
| distribution_score | XX | |
| moat_score | XX | |
| maintenance_score | XX | |
| risk_exposure_score | XX | |
| portfolio_fit_score | XX | |

## Expected Learnings

- [ ] Topic: ... — Method: ... — Applies to: monitor / kill

## Rationale

Explain why this decision was made. Reference global_score, OQI, scenarios, and validation results.

## Conditions (if MONITOR)

Conditions that must be met for promotion to BUILD:

- [ ] global_score >= 75 AND OQI >= 70
- [ ] Condition 2

**Next review date**: YYYY-MM-DD

## Dissent

| Reviewer | Position | Reasoning |
|----------|----------|-----------|
| | agree / disagree | |

## Portfolio Action

- [ ] Update [portfolio/active.md](../portfolio/active.md)
- [ ] Update [portfolio/monitoring.md](../portfolio/monitoring.md)
- [ ] Update [portfolio/archived.md](../portfolio/archived.md)
- [ ] Update opportunity Final Decision section

## Next Steps

- [ ] Step 1
- [ ] Step 2
