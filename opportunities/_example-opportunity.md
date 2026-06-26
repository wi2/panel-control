---
id: OPP-20260615-waitlist-wedge-demo
title: "Waitlist Wedge Demo — fictional v3-lite example"
eval_engine: v3-lite
portfolio_strategy: solo_micro_saas
status: decided
intake_complete: true
decision: MONITOR_MICRO
capacity_blocked: false
msfi: 58.5
speed_score: 65
economics_score: 55
reach_score: 52
time_to_first_revenue_days: 90
monthly_revenue_potential: 800
distribution_channel: seo
distribution_cost: 2
build_hours_estimate: 72
maintenance_hours_estimate: 6
wedge: "SEO landing + email waitlist for SMB invoice OCR wedge"
pipeline_stage: fit_and_decide
created: 2026-06-15
updated: 2026-06-26
owner: "studio-team"
tags: [demo, micro-saas]
prompt_versions:
  discovery: v1
  validation: v2
  fit_and_decide: v1
---

# Waitlist Wedge Demo — fictional v3-lite example

> **Note**: Fictional example for v3-lite. **Not a live portfolio entry.**

## Discovery

### Problem Statement

SMB accountants spend hours on manual invoice entry. A narrow wedge: self-serve upload + structured export for firms with 5–20 staff.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| pain_prevalence | 62% cite manual entry as top-3 pain | verified | AICPA survey | 2026-03 |

### Competitors and Alternatives

| Competitor | Approach | Strengths | Weaknesses |
|------------|----------|-----------|------------|
| Dext | OCR + rules | Established | Expensive, rigid |

### Initial Hypothesis

We believe SMB accountants will join a waitlist for AI-assisted invoice parsing if setup takes under 10 minutes.

### Open Questions

- [ ] Will firms pay €29/mo for export-only wedge?

```yaml
confidence_level: medium
```

---

## Validation

### Experiments

| # | Experiment | Method | Success Criteria | Status |
|---|------------|--------|------------------|--------|
| 1 | Landing + waitlist | Desk research + 5 interviews | 50 emails or kill | Planned |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| interview_pain | 4/5 confirm pain | inferred | Founder calls | 2026-06-20 |

### Kill / Continue Signals

- **Continue if**: waitlist hits 50 in 2 weeks after launch
- **Kill if**: zero signups after SEO push

```yaml
desk_only: true
confidence_level: low
```

---

## Fit and Decide

**Wedge scope**: Landing page + waitlist + manual concierge export — no full OCR build yet.

### Hard Gates

| Gate | Threshold | Estimate | Result |
|------|-----------|----------|--------|
| build_hours | ≤ 100 h | 72 h | PASS |
| maintenance_hours | ≤ 10 h/mo | 6 h/mo | PASS |
| solo_operable | Yes | Yes | PASS |
| monthly_revenue_potential | ≥ 500 €/mo | 800 €/mo | PASS |
| distribution_cost | ≤ 7 | 2 (seo) | PASS |
| platform / ToS | see playbook | low dependency | PASS |

### Platform Risk

| Field | Value |
|-------|-------|
| tos_risk | low |
| platform_dependency | low |
| alternative_data_source | true |

### MSFI-lite

| Component | Score |
|-----------|-------|
| speed_score | 65 |
| economics_score | 55 |
| reach_score | 52 |
| **MSFI** | **58.5** |

```yaml
confidence_level: medium
```

---

## Final Decision (Micro SaaS)

| Field | Value |
|-------|-------|
| **Primary Decision** | MONITOR_MICRO |
| **MSFI** | 58.5 |
| **capacity_blocked** | false |
| **Date** | 2026-06-26 |
| **Rationale** | Gates pass; MSFI in monitor band; desk-only validation — run waitlist sprint |

### Expected Learnings

- [ ] Waitlist conversion from SEO — Method: 2-week landing test — Applies to: MONITOR_MICRO

### Next Actions

- [ ] Ship landing + waitlist
- [ ] Re-eval after 30 days

### Portfolio Update

- [ ] Not in live portfolio (example only)

```yaml
confidence_level: medium
```
