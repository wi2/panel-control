---
id: REVIEW-YYYY-QN
title: "Portfolio Review Q{N} YYYY"
review_date: YYYY-MM-DD
reviewer: ""
status: draft
---

# Portfolio Review — Q{N} YYYY

## Summary

Brief overview of portfolio health and key changes this quarter.

## Active (BUILD) Review

| ID | Title | Global Score | OQI | Owner | Success Contract Status | Action |
|----|-------|--------------|-----|-------|-------------------------|--------|
| | | | | | on track / at risk / failing | continue / demote / kill |

### Active Changes

- Promotions: none
- Demotions: none
- Kills: none

## Monitoring (MONITOR) Review

| ID | Title | Global Score | OQI | Owner | Last Review | Re-score | Scenario (realistic) | Action |
|----|-------|--------------|-----|-------|-------------|----------|----------------------|--------|
| | | | | | YYYY-MM-DD | XX | build / monitor / kill | promote / continue / kill |

### Monitoring Changes

- Promotions to BUILD: none
- Kills: none
- Stale (approaching timeout): none

## Archived This Quarter

| ID | Title | Global Score | OQI | Kill Reason | Date | Key Learning |
|----|-------|--------------|-----|-------------|------|--------------|
| | | | | | | |

## Learnings Aggregation

Cross-opportunity learnings from `expected_learnings` and archived entries:

| Topic | Opportunities | Method | Portfolio implication |
|-------|---------------|--------|----------------------|
| pricing_sensitivity | | | |
| acquisition_channel_efficiency | | | |
| customer_willingness_to_pay | | | |
| onboarding_friction | | | |

## Capacity Assessment

| Category | Current | Max | Available |
|----------|---------|-----|-----------|
| Active (BUILD) | | 3 | |
| Monitoring (MONITOR) | | 10 | |

## Resource Allocation

| Opportunity | Owner | Budget / Allocation | Scenario probabilities | Notes |
|-------------|-------|---------------------|------------------------|-------|
| | | | build X% / monitor Y% / kill Z% | |

## Kill Recommendations

Opportunities recommended for kill with rationale:

1. **{ID}**: {reason}

## New Opportunities Evaluated

| ID | Title | Global Score | OQI | Decision |
|----|-------|--------------|-----|----------|
| | | | | |

## Action Items

- [ ] Action 1 — owner — due date
- [ ] Action 2 — owner — due date

## Next Review

Scheduled: YYYY-MM-DD

---

## Micro SaaS (solo_micro_saas)

Use these sections when reviewing [portfolio/micro-saas.md](../portfolio/micro-saas.md). Skip studio sections above for micro-only runs.

## Active (BUILD_MICRO) Review

| ID | Wedge | MSFI | Owner | Success Contract Status | Maint h/mo | Action |
|----|-------|------|-------|-------------------------|------------|--------|
| | | | | on track / at risk / failing | | continue / demote / kill |

### BUILD_MICRO Changes

- Promotions from MONITOR_MICRO: none
- Demotions to MONITOR_MICRO: none
- Kills: none

## Monitoring (MONITOR_MICRO) Review

| ID | Wedge | MSFI | Owner | Last Review | Re-score MSFI | Desk-only | Action |
|----|-------|------|-------|-------------|---------------|-----------|--------|
| | | | | YYYY-MM-DD | XX | yes / no | BUILD_MICRO / continue / kill |

### MONITOR_MICRO Changes

- Promotions to BUILD_MICRO: none
- Kills: none
- Stale (2× 30-day cycles without BUILD qualification): none
- capacity_blocked: none

## Archived This Quarter (KILL_MICRO)

| ID | Wedge | MSFI | Kill Reason | Date | Key Learning |
|----|-------|------|-------------|------|--------------|
| | | | hard-gate-fail / monitor-timeout / … | | |

## Micro SaaS Capacity Assessment

| Category | Current | Max | Available |
|----------|---------|-----|-----------|
| Active (BUILD_MICRO) | | 3 | |
| Monitoring (MONITOR_MICRO) | | 5 | |
| Total maint h/mo (Active BUILD) | | 40 | |
