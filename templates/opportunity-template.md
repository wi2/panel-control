---
id: OPP-YYYYMMDD-slug
title: ""
eval_engine: v3-lite
portfolio_strategy: solo_micro_saas
status: draft
intake_complete: false
decision: null
capacity_blocked: false
msfi: null
speed_score: null
economics_score: null
reach_score: null
time_to_first_revenue_days: null
monthly_revenue_potential: null
distribution_channel: null
distribution_cost: null
build_hours_estimate: null
maintenance_hours_estimate: null
wedge: ""
pipeline_stage: null
next_review_action: null
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: ""
tags: []
prompt_versions:
  discovery: v1
  validation: v2
  fit_and_decide: v1
---

# {Title}

## Discovery

<!-- Paste output from prompts/discovery-v1.md -->

### Problem Statement

Who has the problem? How painful is it?

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| | | verified / estimated / inferred / synthetic / unknown | | |

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| | | | |

### Initial Hypothesis

We believe [target user] will [behavior] because [reason].

### Open Questions

- [ ] Question 1

```yaml
confidence_level: high / medium / low
```

---

## Validation

<!-- Paste output from prompts/validation-v2.md -->

### Experiments

| # | Experiment | Method | Success Criteria | Status |
|---|------------|--------|------------------|--------|

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|

### Kill / Continue Signals

- **Continue if**:
- **Kill if**:

```yaml
desk_only: true
confidence_level: high / medium / low
```

---

## Fit and Decide

<!-- Paste output from prompts/fit-and-decide-v1.md -->

**Wedge scope**:

### Hard Gates

| Gate | Threshold | Estimate | Result |
|------|-----------|----------|--------|
| build_hours | ≤ 100 h | | |
| maintenance_hours | ≤ 10 h/mo | | |
| solo_operable | Yes | | |
| monthly_revenue_potential | ≥ 500 €/mo | | |
| distribution_cost | ≤ 7 | | |
| platform / ToS | see playbook | | |

### Platform Risk

| Field | Value |
|-------|-------|
| tos_risk | |
| platform_dependency | |
| alternative_data_source | |

### MSFI-lite

| Component | Score |
|-----------|-------|
| speed_score | |
| economics_score | |
| reach_score | |
| **MSFI** | |

```yaml
confidence_level: high / medium / low
```

---

## Final Decision (Micro SaaS)

| Field | Value |
|-------|-------|
| **Primary Decision** | BUILD_MICRO / MONITOR_MICRO / KILL_MICRO |
| **MSFI** | |
| **capacity_blocked** | true / false |
| **Date** | YYYY-MM-DD |
| **Rationale** | |

### Expected Learnings

- [ ] Topic — Method — Applies to: MONITOR_MICRO / KILL_MICRO

### Next Actions

- [ ] Action 1

### Portfolio Update

- [ ] Added to [portfolio/micro-saas.md](../portfolio/micro-saas.md)

```yaml
confidence_level: high / medium / low
```

---

## Post-BUILD_MICRO (manual)

Complete after BUILD_MICRO decision — not orchestrated by CP — Eval.

See [docs/legacy-studio.md](../docs/legacy-studio.md) BUILD prep prompts (vision, mvp, roadmap, architecture, success_contract) or a separate product repo.
