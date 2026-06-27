---
id: OPP-20260627-widget-tracker
title: "Test Widget Tracker (smoke)"
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
distribution_channel: null
distribution_cost: null
build_hours_estimate: null
maintenance_hours_estimate: null
wedge: "Central registry of third-party embed widgets (analytics, chat, payments) across indie SaaS projects — detect stale/orphan scripts before they break checkout or compliance"
pipeline_stage: discovery
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

- [ ] Is widget sprawl painful enough to pay for, or do founders only care during rare audits (episodic vs recurring value)?
- [ ] Can headless crawling reliably detect dynamically injected widgets (GTM, segment loaders) without false negatives?
- [ ] Does a €9–19/mo price band clear hard-gate economics once build and maintenance hours are estimated?
- [ ] Is distribution feasible at distribution_cost ≤ 7 (SEO on "SaaS widget inventory" vs crowded dev-tools SEO)?
- [ ] **Smoke-test:** should this OPP proceed to `cp:eval` or be killed immediately after automation verification?

```yaml
confidence_level: low
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

## Post-BUILD_MICRO (product repo — not panel-control)

After `BUILD_MICRO`, bootstrap a dedicated product repository:

```bash
./scripts/bootstrap_product_repo.sh OPP-20260627-widget-tracker widget-tracker ~/Projects/widget-tracker
```

See [playbooks/build-handoff.md](../playbooks/build-handoff.md). Vision, architecture, and code agents run in the product repo only.
