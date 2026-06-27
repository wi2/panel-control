---
id: OPP-20260627-renew-desk
title: "RenewDesk — assistant de renouvellement de contrats et abonnements B2B"
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
wedge: "Light contract/subscription cockpit for French SMEs (5–50 FTE): AI PDF extraction → notice-period alerts (30/60/90d) → shared renewal calendar for owner + admin/accountant — without full CLM"
pipeline_stage: discovery
next_review_action: null
created: 2026-06-27
updated: 2026-06-27
automation_intake_at: 2026-06-27
owner: studio-team
tags: [b2b, micro-saas, pme, ops, compliance]
prompt_versions:
  discovery: v1
  validation: v2
  fit_and_decide: v1
---

# RenewDesk — assistant de renouvellement de contrats et abonnements B2B

## Discovery

### Problem Statement

French SMEs with 5–50 employees and no dedicated procurement or office-manager function routinely miss critical renewal windows on recurring contracts: professional insurance, supplier agreements, SaaS subscriptions (CRM, accounting, telephony), and mandatory maintenance (fire extinguishers, elevators, certifications). Consequences range from unwanted tacit renewals and price hikes to coverage lapses, service interruptions, and supplier penalties. Today, tracking relies on personal calendars, emails buried in the CEO's inbox, or unstructured SharePoint/paper folders — with no proactive alerts and no consolidated 30/60/90-day view shared between the owner, admin assistant, and external accountant. The pain is recurring (monthly/quarterly review cycles), has direct cash and compliance impact, and intensifies as SaaS sprawl and regulatory obligations accumulate without a central contract register.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| fr_pme_non_micro_count | ~174,614 PME (non-micro) in France | verified | INSEE — L'essentiel sur les entreprises 2023 | 2026-06-27 |
| contract_tracking_difficulty | 40% of companies struggle to track contract status (active, expired, to renew) | estimated | La Fabrique du Net — comparatif gestion contrats 2026 (citing World Commerce & Contracting studies) | 2026-01-01 |
| missed_renewal_rate | 25% of contracts not renewed on time due to inadequate tracking | estimated | La Fabrique du Net — comparatif gestion contrats 2026 (citing World Commerce & Contracting studies) | 2026-01-01 |
| contract_comprehension_gap | 90% of entrepreneurs need help understanding their contracts | estimated | La Fabrique du Net — comparatif gestion contrats 2026 (citing World Commerce & Contracting studies) | 2026-01-01 |
| clm_market_growth | CLM market projected toward $5.4B by 2036 | estimated | MicroGaps — AI contract renewal tracker gap analysis | 2026-02-16 |
| tracking_confidence_low | Only 22% of businesses confident in contract tracking | estimated | MicroGaps — AI contract renewal tracker gap analysis | 2026-02-16 |
| enterprise_clm_price_band | Enterprise CLM tools often $400–700+/mo — out of reach for 10-person firms | estimated | MicroGaps; Termedora blog comparatif 2026 | 2026-06-27 |
| affordable_renewal_pricing_band | Focused renewal trackers priced $10–59/mo globally | verified | DocRenewal ($0–19.99/mo); Renewl ($0–59/mo); Termedora ($49/mo) pricing pages | 2026-06-27 |
| fr_direct_competitor_pricing | TACIT (FR PME): Free 3 contracts; Starter €29/mo (25 contracts); Growth €49/mo (60 contracts) | verified | TACIT pricing page | 2026-06-27 |
| tacit_renewal_cost_examples | Missed-notice examples cited at €500–50,000 per contract (insurance, RP, bail, telecom) | inferred | TACIT marketing testimonials and cost ranges on homepage | 2026-06-27 |
| target_company_size | 5–50 employees; no dedicated procurement/OM | synthetic | Intake hypothesis (studio-team) | 2026-06-27 |
| contracts_per_sme | 15–40 recurring contracts/subscriptions per target SME | synthetic | Intake hypothesis (studio-team) | 2026-06-27 |
| wedge_price_band | €19–49/mo for renewal cockpit vs one missed renewal cost | synthetic | Intake hypothesis vs TACIT/Renewl/DocRenewal benchmarks | 2026-06-27 |

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| TACIT (FR) | AI PDF extraction + tacit-renewal alerts for French PME; EU hosting; Mistral AI | Direct FR positioning; €29–49/mo tiers; unlimited users; notice-period focus; RGPD/SOC2 messaging | Near-identical wedge to RenewDesk intake; already live with testimonials; unclear differentiation path without live SME signal |
| Termedora | SaaS/vendor renewal tracker with email, Slack, SMS alerts | $49/mo flat; unlimited contracts/users; strong notice-period framing | English-first; US/EU positioning; less FR compliance/maintenance-obligation vocabulary |
| Renewl | Upload PDF → AI notice-deadline alerts; savings dashboard | Free tier (20 contracts); $59/mo unlimited; explicit "not a CLM" positioning | English-first; no shared calendar/accountant collaboration angle marketed |
| DocRenewal | Contract calendar + auto-renewal detection + team roles | $19.99/mo unlimited; low entry price | English-first; generic global SMB; weaker FR regulatory context |
| KnowRenewals | Subscription/contract/SaaS renewal workflow with owner accountability | 90/60/30-day operational rhythm; cross-functional framing | English-first; broader ops tool vs narrow FR PME wedge |
| Tomorro / Concord / enterprise CLM | Full contract lifecycle: drafting, negotiation, e-sign, repository | Deep legal workflows; established B2B sales | €100–400+/mo; overkill for 5–50 FTE firms needing deadline alerts only |
| Excel + Outlook/Agenda | Shared spreadsheet + personal calendar reminders | Zero subscription cost; familiar | Version drift; no notice-period logic; alerts lost when staff leaves; no document vault linkage |
| Accountant / expert-comptable manual follow-up | External advisor tracks key dates ad hoc | Trusted relationship; potential referral channel | Not scalable; inconsistent; outside core accounting scope unless upsold |
| Microsoft 365 / SharePoint add-ons (e.g. CV Renew365) | Renewal tracking inside SharePoint Online | Fits firms already on M365; centralized AMC/subscription module | Requires SharePoint adoption; IT setup; not standalone self-serve for non-M365 SMEs |
| Spendesk / Pennylane / ERP modules | Finance stack with invoice/subscription visibility | Existing spend data; accountant ecosystem | Does not parse contract PDF notice clauses; renewal alert UX not primary wedge |

### Initial Hypothesis

We believe French SME owners and admin leads (5–50 employees) managing 15–40 recurring contracts will pay €19–49/mo for a shared renewal cockpit with notice-period alerts (30/60/90 days) and light document storage, because manual Excel/calendar tracking fails silently when staff turnover occurs and a single missed tacit renewal (insurance lapse, unwanted SaaS renewal, supplier penalty) typically exceeds a year of subscription cost — while enterprise CLM remains priced out and TACIT has not yet proven category saturation in this segment.

### Open Questions

- [ ] Can RenewDesk differentiate vs TACIT on accountant collaboration (read-only portal, export for cabinet comptable), multi-category obligations (assurance, maintenance réglementaire, SaaS), or FR-specific compliance templates — or is the market already winner-take-most for AI renewal alerts?
- [ ] Do target SMEs upload PDF contracts proactively, or does onboarding require concierge import / email-forward ingestion to reach activation?
- [ ] What AI extraction accuracy threshold (notice period, tacit renewal clause, montant) is acceptable before owners trust alerts without manual re-read?
- [ ] Is €29/mo viable at 15–25 contracts when TACIT Starter offers 25 contracts at the same price and DocRenewal/Renewl free tiers cover early experimentation?
- [ ] Which distribution channel converts fastest: SEO ("alerte reconduction tacite PME"), expert-comptable referral partnerships, or insurance broker co-marketing?
- [ ] Does a shared calendar view (owner + admin + external accountant) materially improve retention vs email-only alerts?
- [ ] What is the maintenance burden of keeping FR contract-type templates and regulatory reminder categories current (extincteurs, ascenseurs, certifications)?

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
