---
id: OPP-20260626-coachbrief
title: "CoachBrief — digest hebdo pour coachs endurance solo"
eval_engine: v3-lite
portfolio_strategy: solo_micro_saas
status: evaluating
intake_complete: true
decision: null
capacity_blocked: false
msfi: null
speed_score: null
economics_score: null
reach_score: null
time_to_first_revenue_days: null
monthly_revenue_potential: null
distribution_channel: seo
distribution_cost: null
build_hours_estimate: null
maintenance_hours_estimate: null
wedge: "CSV/text import → structured weekly digest (athletes at risk, missed sessions, short recommendations) for solo endurance coaches"
pipeline_stage: discovery
next_review_action: null
created: 2026-06-26
updated: 2026-06-26
automation_intake_at: 2026-06-26
owner: studio-team
tags: [sports, b2b, micro-saas, ai, coaching]
prompt_versions:
  discovery: v1
  validation: v2
  fit_and_decide: v1
---

# CoachBrief — digest hebdo pour coachs endurance solo

## Discovery

### Problem Statement

Independent endurance coaches (running, trail, triathlon) managing roughly 15–40 athletes spend significant time each week reviewing fragmented data across TrainingPeaks, Strava, WhatsApp, and spreadsheets before they can prepare the coming week’s sessions. The recurring work is not plan authoring alone — it is synthesizing who missed key workouts, who shows fatigue or compliance drift, and who needs a volume or intensity correction. TrainingPeaks and peer platforms optimize calendar, analytics, and per-athlete views, but they do not produce a coach-level weekly roster digest ready to paste into client emails or notes. For solo coaches without admin support, this review loop is a recurring time sink and a burnout risk as roster size grows past ~10 athletes.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| us_sports_coaching_market | $15.5B (US, 2026) | verified | IBISWorld Sports Coaching industry | 2026-06-26 |
| us_sports_coaching_businesses | ~196k businesses (US) | verified | IBISWorld Sports Coaching industry | 2026-06-26 |
| triathlon_coaching_market | $0.4B global (2025) | estimated | MarketIntelo triathlon coaching report | 2025-01-01 |
| triathlon_coaching_cagr | 6.2% CAGR to 2034 | estimated | MarketIntelo triathlon coaching report | 2025-01-01 |
| running_coach_individual_segment | ~31.7% of running coaching market | estimated | DataIntelo running coaching report | 2025-01-01 |
| coach_scale_pain_threshold | Productivity systems needed beyond ~10 athletes | verified | TrainingPeaks coach blog (productivity tips) | 2026-06-26 |
| tp_coach_market_position | Industry standard for endurance coaches; Coach Home compliance overview | verified | TrainingPeaks coach blog / Coachbox comparison | 2026-06-26 |
| weekly_review_time | 2–4 h/week on TP + Strava + WhatsApp review | synthetic | Intake hypothesis (studio-team) | 2026-06-26 |
| target_roster_size | 15–40 athletes per solo coach | synthetic | Intake hypothesis (studio-team) | 2026-06-26 |
| monetization_band | €29–49/mo; €800–2,000/mo ceiling at 20–50 coaches | synthetic | Intake hypothesis (studio-team) | 2026-06-26 |

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| TrainingPeaks Coach Edition | Full training platform: calendars, PMC, compliance dots, athlete messaging | Industry standard; large device ecosystem; Coach Home roster compliance view | No structured multi-athlete weekly digest export; per-athlete pricing adds up; still requires manual synthesis across athletes |
| Coachbox | All-in-one endurance coaching: plans, health sync, comms, business tools | Replaces spreadsheets + WhatsApp patchwork; smart calendar and load insights | Platform switch cost; broad product, not a narrow digest wedge; pricing oriented to full-stack adoption |
| KULG for coaches | Running-focused coach dashboard with weekly planner and activity history | Weekly planning; immediate athlete feedback loop | Runner-app centric; no dedicated “weekly roster digest for email” export positioning |
| Final Surge / spreadsheet workflows | Training platform or manual CSV/Sheets tracking | Flexible; familiar to many coaches | Time-intensive; error-prone; no AI synthesis layer |
| lope / RunPulse (B2C AI) | AI weekly summaries and plans for self-coached athletes via Strava | Strong athlete-facing weekly summaries | Athlete-facing, not coach-roster B2B; does not replace coach’s multi-client review workflow |
| Manual weekly review routine | Daily/weekly TP file checks + scheduled athlete calls | Personal relationship; no new tool spend | Does not scale linearly; documented burnout risk for self-employed coaches |

### Initial Hypothesis

We believe solo endurance coaches managing 15–40 athletes will subscribe at €29–49/mo for a reliable weekly digest if it saves 1–2 h/week on client review, because incumbent platforms expose per-athlete analytics but not a copy-paste-ready roster synthesis across missed sessions, fatigue signals, and short coaching actions.

### Open Questions

- [ ] Do coaches trust digest quality from CSV paste / weekly export without live Strava or TrainingPeaks API integrations?
- [ ] What minimum accuracy rate (e.g., false “at risk” flags) is acceptable over a 4-week pilot?
- [ ] Is €29/mo sufficient at 20+ subscribers, or does €49/mo reduce conversion below viable SEO/community funnel volume?
- [ ] Will FR/EU French-speaking coaches adopt an English-first SEO wedge before localized copy?
- [ ] Does the digest wedge expand retention, or do coaches churn once they internalize the review pattern?

```yaml
confidence_level: medium
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
