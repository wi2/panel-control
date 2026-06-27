---
id: OPP-20260627-widget-tracker
title: "Test Widget Tracker (smoke)"
eval_engine: v3-lite
portfolio_strategy: solo_micro_saas
status: decided
intake_complete: true
decision: KILL_MICRO
capacity_blocked: false
msfi: 48.9
speed_score: 58
economics_score: 42
reach_score: 44
time_to_first_revenue_days: 75
monthly_revenue_potential: 480
distribution_channel: seo
distribution_cost: 2
build_hours_estimate: 72
maintenance_hours_estimate: 6
wedge: "Weekly headless crawl of indie SaaS domains → cross-project widget registry with orphan/deprecated embed alerts — priced €9–19/mo"
pipeline_stage: fit_and_decide
next_review_action: null
created: 2026-06-27
updated: 2026-06-27
automation_intake_at: 2026-06-27
owner: studio-team
tags: [smoke-test]
prompt_versions:
  discovery: v1
  validation: v2
  fit_and_decide: v1
---

# Test Widget Tracker (smoke)

## Discovery

### Problem Statement

Indie SaaS founders and solo developers who ship multiple small products accumulate third-party embed widgets over time — Stripe checkout buttons, Intercom chat, PostHog/Plausible analytics, cookie banners, affiliate pixels — without a single inventory of what is live on which domain or subdomain. When a vendor deprecates a script, changes CSP requirements, or a GDPR audit asks "list all trackers," the owner must grep repos, click through production sites, and reconcile Notion spreadsheets. The pain is episodic but sharp (compliance reviews, incident response, vendor migrations) and worsens as project count grows beyond 2–3 live apps. **Note:** this opportunity is a fictional smoke-test intake; problem framing is synthetic for pipeline verification.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| indie_saas_operator_count | ~500k–1M solo/micro SaaS operators globally (broad TAM) | estimated | Indie Hackers / MicroConf community sizing (order-of-magnitude) | 2026-06-27 |
| third_party_script_count | Typical marketing site loads 15–30 third-party scripts | estimated | HTTP Archive / web performance studies (general web) | 2026-06-27 |
| widget_sprawl_pain | Founders report losing track of embeds across 3+ projects | synthetic | Intake hypothesis (studio-team smoke test) | 2026-06-27 |
| compliance_driver | GDPR/cookie audits require tracker inventory | inferred | CNIL guidance on consent and third-party scripts | 2026-06-27 |
| smoke_test_flag | Idea exists only to verify CP — Intake automation | verified | PR #17 intake body | 2026-06-27 |

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| Manual spreadsheet / Notion | Owner maintains widget list per project | Free; flexible | Stale within weeks; no automated drift detection |
| Browser devtools + Wappalyzer | One-off scan of live pages | No subscription; immediate | No history; no cross-project dashboard; manual repeat |
| Datadog / Sentry RUM | Full observability with third-party resource tracking | Enterprise-grade | Overkill and costly for solo founders; not widget-inventory focused |
| Cookiebot / OneTrust CMP | Consent management with scanner | Compliance-first; automated detection | Priced for mid-market sites; not multi-project SaaS portfolio view |
| GitHub repo search (`grep` vendor domains) | Search codebase for script tags | Catches repo-side installs | Misses CMS/no-code embeds; no production-only widgets |
| Security scanners (Mozilla Observatory, SSL Labs) | Periodic site audits | Free baseline | Not designed for ongoing widget lifecycle tracking |

### Initial Hypothesis

We believe indie SaaS founders operating 2–5 live products will pay €9–19/mo for an automated widget registry that crawls their domains weekly and flags orphan or deprecated embeds because compliance and vendor-migration events currently require hours of manual reconciliation with no cross-project view.

### Open Questions

- [x] Is widget sprawl painful enough to pay for, or do founders only care during rare audits (episodic vs recurring value)? → Episodic; desk audit confirms low recurring willingness-to-pay at €9–19/mo
- [ ] Can headless crawling reliably detect dynamically injected widgets (GTM, segment loaders) without false negatives?
- [x] Does a €9–19/mo price band clear hard-gate economics once build and maintenance hours are estimated? → No — MRR ceiling ~€480/mo fails ≥500 €/mo gate
- [x] Is distribution feasible at distribution_cost ≤ 7 (SEO on "SaaS widget inventory" vs crowded dev-tools SEO)? → SEO viable (cost 2) but crowded; reach score low
- [x] **Smoke-test:** should this OPP proceed to `cp:eval` or be killed immediately after automation verification? → cp:eval completed; KILL_MICRO — no product build intent

```yaml
confidence_level: low
```

---

## Validation

### Experiments

| # | Experiment | Method | Success Criteria | Status |
|---|------------|--------|------------------|--------|
| 1 | CMP / script-governance competitive audit | Desk research: CookieScript, Cookiebot, Reflectiz, cside, Lokker pricing and positioning vs proposed indie multi-project registry wedge | Document overlap on automated script inventory, drift detection, and compliance scanning; identify gap on cross-project SaaS portfolio view | completed |
| 2 | Episodic-pain / pricing desk benchmark | Desk research: indie SaaS pricing sensitivity, free-alternative sufficiency (Wappalyzer, devtools, spreadsheets), €9–19/mo ARPU math | ≥3 credible signals that founders would pay recurring €9–19/mo (not only during audits); OR document free-alternative sufficiency | completed |
| 3 | Live validation sprint (not run) | SEO landing + 5 indie founder interviews + concierge weekly crawl for 2 domains | ≥4/5 confirm cross-project widget sprawl pain; ≥3/5 rate automated registry as "would pay €15+/mo"; waitlist ≥50 emails in 30 days | planned |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| cmp_inventory_overlap | CookieScript (€8–19/mo/domain), Cookiebot, Usercentrics, and Reflectiz already offer automated third-party script inventory, monthly scans, and drift detection — compliance-first positioning | verified | CookieScript pricing guide; Reflectiz CMP comparison blog | 2026-06-27 |
| enterprise_script_governance | cside and Lokker target runtime script inventory, shadow-IT detection, and governance alerts — enterprise/mid-market pricing, not indie SaaS portfolio | verified | cside blog on third-party script inventory; Lokker script governance page | 2026-06-27 |
| free_alternative_sufficient | Wappalyzer + browser devtools + manual spreadsheet covers one-off audit needs for solo founders; no recurring subscription required for episodic compliance events | inferred | Discovery competitor scan; desk pricing benchmark | 2026-06-27 |
| episodic_pain_pattern | Widget sprawl pain spikes at GDPR audits, vendor migrations, and incident response — not daily workflow; reduces recurring subscription willingness | inferred | Discovery hypothesis; desk benchmark vs CMP monthly-scan model | 2026-06-27 |
| arpu_ceiling_low | At €15/mo ARPU, ~32 paying accounts needed for €480/mo; indie multi-project segment is narrow and churn-prone on episodic use case | inferred | MRR math vs hard-gate €500/mo threshold | 2026-06-27 |
| cross_project_gap_unproven | Multi-project SaaS portfolio dashboard is a plausible differentiation vs per-domain CMPs, but no live founder signal confirms willingness to pay | synthetic | No live experiments run in this eval cycle | 2026-06-27 |
| smoke_test_complete | CP — Eval full-run executed successfully; OPP exists solely for pipeline automation verification | verified | PR #17 cp:eval trigger | 2026-06-27 |
| live_validation_pending | Zero founder interviews, concierge crawls, or waitlist signups completed | synthetic | No live experiments run in this eval cycle | 2026-06-27 |

### Kill / Continue Signals

- **Continue if**: ≥4/5 indie founders with 2+ live products confirm recurring widget-sprawl pain (not only audit-season); ≥3/5 rate cross-project registry as "would pay €15+/mo"; waitlist reaches 50 emails within 30 days; a defensible gap emerges vs per-domain CMP scanners on multi-project portfolio view
- **Kill if**: ≥3/5 founders say Wappalyzer/devtools/spreadsheet is sufficient for their audit frequency; zero waitlist after 4 weeks of targeted SEO; MRR ceiling at €15/mo ARPU stays below €500/mo for realistic solo-operable reach; smoke-test pipeline verification complete with no product build intent

```yaml
desk_only: true
confidence_level: low
```

---

## Fit and Decide

**Wedge scope**: Web app for indie SaaS founders (2–5 live products): register domains → weekly headless crawl → cross-project widget registry with orphan/deprecated embed alerts — priced €9–19/mo, solo-operable without enterprise CMP overhead.

### Hard Gates

| Gate | Threshold | Estimate | Result |
|------|-----------|----------|--------|
| build_hours | ≤ 100 h | 72 h | PASS |
| maintenance_hours | ≤ 10 h/mo | 6 h/mo | PASS |
| solo_operable | Yes | Yes | PASS |
| monthly_revenue_potential | ≥ 500 €/mo | 480 €/mo | FAIL |
| distribution_cost | ≤ 7 | 2 (channel: seo) | PASS |
| platform / ToS | see playbook | Headless crawl of user-owned domains; no scraping-only third-party dependency | PASS |

### Platform Risk

| Field | Value |
|-------|-------|
| tos_risk | low |
| platform_dependency | low |
| alternative_data_source | true |

### MSFI-lite

| Component | Score |
|-----------|-------|
| speed_score | 58 |
| economics_score | 42 |
| reach_score | 44 |
| **MSFI** | **48.9** |

```yaml
confidence_level: low
```

---

## Final Decision (Micro SaaS)

| Field | Value |
|-------|-------|
| **Primary Decision** | KILL_MICRO |
| **MSFI** | 48.9 |
| **capacity_blocked** | false |
| **Date** | 2026-06-27 |
| **Rationale** | Hard gate FAIL: monthly_revenue_potential 480 €/mo < 500 €/mo threshold at realistic €15/mo ARPU (~32 accounts) in a narrow indie multi-project segment with episodic pain and high churn risk. MSFI 48.9 (< 50) corroborates kill. Desk-only validation confirms CMP incumbents (CookieScript, Cookiebot, Reflectiz) and free tools (Wappalyzer, devtools) already cover script inventory for audit events; proposed cross-project portfolio view is unproven without live founder signal. **Smoke-test objective met:** CP — Eval full-run completed; no product build intent. |

### Expected Learnings

- [ ] Episodic vs recurring SaaS pain patterns — Method: compare audit-season vs always-on tool retention in indie founder interviews — Applies to: KILL_MICRO
- [ ] Cross-project registry differentiation vs per-domain CMP — Method: 5 founder interviews on multi-app widget sprawl — Applies to: KILL_MICRO (only if wedge re-opened)

### Next Actions

- [ ] Archive OPP; no BUILD handoff or product repo bootstrap
- [ ] Confirm CP — QA pass on PR #17; remove `cp:eval` label after review
- [ ] Use this run as regression baseline for automation-eval-v10 / orchestrator-v8 full-run contract

### Portfolio Update

- [x] Added to [portfolio/micro-saas.md](../portfolio/micro-saas.md)

```yaml
confidence_level: high
```

---

## Post-BUILD_MICRO (product repo — not panel-control)

After `BUILD_MICRO`, bootstrap a dedicated product repository:

```bash
./scripts/bootstrap_product_repo.sh OPP-20260627-widget-tracker widget-tracker ~/Projects/widget-tracker
```

See [playbooks/build-handoff.md](../playbooks/build-handoff.md). Vision, architecture, and code agents run in the product repo only.
