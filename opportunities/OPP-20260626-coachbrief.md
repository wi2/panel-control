---
id: OPP-20260626-coachbrief
title: "CoachBrief — digest hebdo pour coachs endurance solo"
eval_engine: v3-lite
portfolio_strategy: solo_micro_saas
status: decided
intake_complete: true
decision: MONITOR_MICRO
capacity_blocked: false
msfi: 63.5
speed_score: 70
economics_score: 62
reach_score: 55
time_to_first_revenue_days: 75
monthly_revenue_potential: 980
distribution_channel: seo
distribution_cost: 2
build_hours_estimate: 68
maintenance_hours_estimate: 5
wedge: "CSV/text import → structured weekly digest (athletes at risk, missed sessions, short recommendations) for solo endurance coaches"
pipeline_stage: fit_and_decide
next_review_action: validate
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

Independent endurance coaches (running, trail, triathlon) managing roughly 15–40 athletes spend significant time each week reviewing fragmented data across TrainingPeaks, Strava, WhatsApp, and spreadsheets before they can prepare the coming week's sessions. The recurring work is not plan authoring alone — it is synthesizing who missed key workouts, who shows fatigue or compliance drift, and who needs a volume or intensity correction. TrainingPeaks and peer platforms optimize calendar, analytics, and per-athlete views, but they do not produce a coach-level weekly roster digest ready to paste into client emails or notes. For solo coaches without admin support, this review loop is a recurring time sink and a burnout risk as roster size grows past ~10 athletes.

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
| KULG for coaches | Running-focused coach dashboard with weekly planner and activity history | Weekly planning; immediate athlete feedback loop | Runner-app centric; no dedicated "weekly roster digest for email" export positioning |
| Final Surge / spreadsheet workflows | Training platform or manual CSV/Sheets tracking | Flexible; familiar to many coaches | Time-intensive; error-prone; no AI synthesis layer |
| lope / RunPulse (B2C AI) | AI weekly summaries and plans for self-coached athletes via Strava | Strong athlete-facing weekly summaries | Athlete-facing, not coach-roster B2B; does not replace coach's multi-client review workflow |
| Manual weekly review routine | Daily/weekly TP file checks + scheduled athlete calls | Personal relationship; no new tool spend | Does not scale linearly; documented burnout risk for self-employed coaches |

### Initial Hypothesis

We believe solo endurance coaches managing 15–40 athletes will subscribe at €29–49/mo for a reliable weekly digest if it saves 1–2 h/week on client review, because incumbent platforms expose per-athlete analytics but not a copy-paste-ready roster synthesis across missed sessions, fatigue signals, and short coaching actions.

### Open Questions

- [ ] Do coaches trust digest quality from CSV paste / weekly export without live Strava or TrainingPeaks API integrations?
- [ ] What minimum accuracy rate (e.g., false "at risk" flags) is acceptable over a 4-week pilot?
- [ ] Is €29/mo sufficient at 20+ subscribers, or does €49/mo reduce conversion below viable SEO/community funnel volume?
- [ ] Will FR/EU French-speaking coaches adopt an English-first SEO wedge before localized copy?
- [ ] Does the digest wedge expand retention, or do coaches churn once they internalize the review pattern?

```yaml
confidence_level: medium
```

---

## Validation

### Experiments

| # | Experiment | Method | Success Criteria | Status |
|---|------------|--------|------------------|--------|
| 1 | Incumbent feature-gap audit | Desk research: TrainingPeaks Help Center, coach blog, third-party export tooling | Confirm no native multi-athlete weekly digest export; document CSV export path per athlete | completed |
| 2 | Wedge pricing & stack benchmark | Desk research: TrainingPeaks, Coachbox, Good Coach App, EndoGusto pricing pages | €29–49/mo add-on is ≤25% of typical coach platform spend at 15–40 athletes | completed |
| 3 | Live validation sprint (planned) | Landing + 5 coach interviews + concierge digest delivery | ≥4/5 confirm weekly review pain; ≥3/5 would pay €29+ after seeing sample digest | planned |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| tp_no_roster_digest | TrainingPeaks Coach Home shows per-athlete compliance dots but no multi-athlete weekly digest export | verified | TrainingPeaks coach blog (Coach Home feature) | 2026-06-26 |
| tp_csv_per_athlete | CSV workout summary export requires navigating each athlete account settings individually | verified | TrainingPeaks Help Center — Data Export | 2026-06-26 |
| tp_export_tos_risk | Third-party bulk exporters exist but violate TP ToS for non-personal use | verified | tp-exporter GitHub README | 2026-06-26 |
| coach_platform_spend | $22–80/mo typical for 15–40 athlete rosters on incumbent platforms | verified | TrainingPeaks pricing blog; Good Coach vs TP comparison | 2026-06-26 |
| wedge_price_ratio | €29/mo add-on ≈ 15–35% of incumbent platform spend at target roster size | inferred | Pricing benchmark vs intake €29–49/mo hypothesis | 2026-06-26 |
| b2c_ai_gap | Athlete-facing AI summaries (Strava apps) do not address coach-roster B2B workflow | verified | Discovery competitor scan (lope, RunPulse) | 2026-06-26 |
| csv_wedge_feasible | Manual CSV paste + LLM synthesis is technically viable without API dependency for MVP | inferred | Export path audit + wedge scope definition | 2026-06-26 |
| live_validation_pending | Zero coach interviews or concierge deliveries completed | synthetic | No live experiments run in this eval cycle | 2026-06-26 |

### Kill / Continue Signals

- **Continue if**: ≥4/5 coaches in interviews confirm 1–2 h/week review pain; ≥3/5 rate a sample concierge digest as "would use weekly"; waitlist reaches 30 emails within 30 days of SEO landing launch
- **Kill if**: ≥3/5 coaches say Coach Home + spreadsheets are sufficient; digest false-positive rate >30% in concierge pilot; zero waitlist signups after 4 weeks of targeted community outreach

```yaml
desk_only: true
confidence_level: low
```

---

## Fit and Decide

**Wedge scope**: Web app accepting pasted CSV/text workout exports (no live API in MVP) → LLM-generated weekly roster digest with at-risk athletes, missed sessions, and short coaching recommendations — exportable as email-ready text for solo endurance coaches managing 15–40 athletes.

### Hard Gates

| Gate | Threshold | Estimate | Result |
|------|-----------|----------|--------|
| build_hours | ≤ 100 h | 68 h | PASS |
| maintenance_hours | ≤ 10 h/mo | 5 h/mo | PASS |
| solo_operable | Yes | Yes | PASS |
| monthly_revenue_potential | ≥ 500 €/mo | 980 €/mo | PASS |
| distribution_cost | ≤ 7 | 2 (channel: seo) | PASS |
| platform / ToS | see playbook | CSV paste MVP; no scraping-only dependency | PASS |

### Platform Risk

| Field | Value |
|-------|-------|
| tos_risk | low |
| platform_dependency | low |
| alternative_data_source | true |

### MSFI-lite

| Component | Score |
|-----------|-------|
| speed_score | 70 |
| economics_score | 62 |
| reach_score | 55 |
| **MSFI** | **63.5** |

```yaml
confidence_level: medium
```

---

## Final Decision (Micro SaaS)

| Field | Value |
|-------|-------|
| **Primary Decision** | MONITOR_MICRO |
| **MSFI** | 63.5 |
| **capacity_blocked** | false |
| **Date** | 2026-06-26 |
| **Rationale** | All hard gates pass. MSFI 63.5 sits in monitor band (50–69). Desk-only validation — competitive audit confirms wedge gap (no TP roster digest, per-athlete CSV export only) and pricing headroom (€29 add-on ≈15–35% of platform spend), but zero live coach signal. BUILD_MICRO blocked until interview + concierge sprint completes. |

### Expected Learnings

- [ ] Coach trust in CSV-paste digest quality — Method: 5 interviews + 2-week concierge pilot — Applies to: MONITOR_MICRO
- [ ] SEO/community acquisition for niche coach wedge — Method: landing + waitlist in r/triathlon and coach Facebook groups — Applies to: MONITOR_MICRO
- [ ] False-positive tolerance for "at risk" flags — Method: concierge digest with usefulness rating — Applies to: MONITOR_MICRO

### Next Actions

- [ ] Ship SEO landing page targeting "TrainingPeaks weekly review" / "coach roster digest" keywords
- [ ] Run 5 problem interviews with solo endurance coaches (15–40 athletes)
- [ ] Deliver 2-week concierge digest to 3 coaches using their CSV exports; collect usefulness ratings
- [ ] Re-evaluate at 30-day review (2026-07-26); promote to BUILD_MICRO if MSFI ≥70 and live validation passes

### Portfolio Update

- [x] Added to [portfolio/micro-saas.md](../portfolio/micro-saas.md)

```yaml
confidence_level: medium
```

---

## Post-BUILD_MICRO (product repo — not panel-control)

After `BUILD_MICRO`, bootstrap a dedicated product repository:

```bash
./scripts/bootstrap_product_repo.sh OPP-YYYYMMDD-slug slug ~/Projects/slug
```

See [playbooks/build-handoff.md](../playbooks/build-handoff.md). Vision, architecture, and code agents run in the product repo only.
