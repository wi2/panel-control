---
id: OPP-20260627-renew-desk
title: "RenewDesk — assistant de renouvellement de contrats et abonnements B2B"
eval_engine: v3-lite
portfolio_strategy: solo_micro_saas
status: decided
intake_complete: true
decision: MONITOR_MICRO
capacity_blocked: false
msfi: 51.4
speed_score: 58
economics_score: 52
reach_score: 40
time_to_first_revenue_days: 45
monthly_revenue_potential: 900
distribution_channel: seo
distribution_cost: 2
build_hours_estimate: 78
maintenance_hours_estimate: 7
wedge: "AI PDF extraction → notice-period alerts (30/60/90d) → shared renewal calendar for French SME owner + admin/accountant — without full CLM"
pipeline_stage: fit_and_decide
next_review_action: validate
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

### Experiments

| # | Experiment | Method | Success Criteria | Status |
|---|------------|--------|------------------|--------|
| 1 | TACIT feature-parity audit | Desk research: TACIT pricing, features, FR positioning, testimonials, EU hosting/RGPD claims | Document overlap with proposed wedge (AI PDF extraction, tacit-renewal alerts, notice-period focus, PME pricing); identify any gap on accountant collaboration or multi-category FR compliance | completed |
| 2 | Global renewal-tracker benchmark | Desk research: Termedora, Renewl, DocRenewal, KnowRenewals pricing and feature pages | €19–49/mo wedge is within global renewal-tracker band and ≤25% of one missed tacit-renewal cost cited by TACIT (€500+) | completed |
| 3 | Live validation sprint (planned) | SEO landing + 5 SME owner/admin interviews + 2-week concierge alert delivery | ≥4/5 confirm missed-renewal pain; ≥3/5 rate shared calendar + accountant read-only portal as "would pay €29+/mo"; waitlist ≥30 emails in 30 days | planned |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| tacit_direct_overlap | TACIT (FR PME) offers AI PDF extraction, tacit-renewal alerts, notice-period focus, unlimited users, EU hosting, Mistral AI — Starter €29/mo (25 contracts), Growth €49/mo (60 contracts) | verified | TACIT pricing page; Discovery competitor scan | 2026-06-27 |
| tacit_live_testimonials | TACIT homepage cites missed-notice cost examples (€500–50 000) and PME testimonials — product is live and marketed in target segment | verified | TACIT homepage marketing | 2026-06-27 |
| tacit_wedge_parity | RenewDesk intake wedge (AI PDF → 30/60/90d alerts → shared calendar) is near-identical to TACIT core positioning; differentiation path unproven without live SME signal | inferred | Feature-parity audit vs intake hypothesis | 2026-06-27 |
| global_price_band | Focused renewal trackers priced $0–59/mo globally (DocRenewal $19.99; Renewl $59; Termedora $49) — validates €19–49/mo band but English-first incumbents | verified | DocRenewal, Renewl, Termedora pricing pages | 2026-06-27 |
| price_compression | Proposed €29/mo sits at TACIT Starter tier (25 contracts, same price) — limited pricing headroom without clear differentiation | inferred | Pricing benchmark vs TACIT Starter €29/mo | 2026-06-27 |
| accountant_portal_unproven | Shared calendar + read-only accountant portal is a plausible differentiation vs TACIT email-only alerts, but no live SME signal confirms willingness to pay for it | synthetic | No live experiments run in this eval cycle | 2026-06-27 |
| compliance_category_gap | Multi-category FR obligations (assurance, maintenance réglementaire, SaaS) may differentiate vs generic global trackers, but TACIT already targets FR PME tacit-renewal pain | inferred | Discovery competitor scan; TACIT FR positioning | 2026-06-27 |
| category_demand_validated | 40% of companies struggle to track contract status; 25% miss renewals on time — pain is real and recurring | estimated | La Fabrique du Net — comparatif gestion contrats 2026 | 2026-01-01 |
| live_validation_pending | Zero SME interviews, concierge alert deliveries, or waitlist signups completed | synthetic | No live experiments run in this eval cycle | 2026-06-27 |

### Kill / Continue Signals

- **Continue if**: ≥4/5 SME owners/admins confirm missed tacit-renewal pain in last 12 months; ≥3/5 rate accountant read-only portal or multi-category FR compliance templates as "would pay €29+/mo"; waitlist reaches 30 emails within 30 days of SEO landing; a defensible wedge emerges (accountant collaboration, maintenance réglementaire categories) that TACIT does not cover
- **Kill if**: ≥3/5 SMEs say TACIT free/Starter tier is sufficient; zero waitlist after 4 weeks of targeted SEO ("alerte reconduction tacite PME"); AI extraction accuracy <80% on notice-period clauses in concierge pilot; TACIT or enterprise CLM adds accountant portal before differentiation is proven

```yaml
desk_only: true
confidence_level: low
```

---

## Fit and Decide

**Wedge scope**: Web app for French SMEs (5–50 FTE): upload contract PDFs → AI extraction of notice periods and tacit-renewal clauses → 30/60/90-day email alerts → shared renewal calendar with read-only accountant portal — priced €29–49/mo, solo-operable without full CLM.

### Hard Gates

| Gate | Threshold | Estimate | Result |
|------|-----------|----------|--------|
| build_hours | ≤ 100 h | 78 h | PASS |
| maintenance_hours | ≤ 10 h/mo | 7 h/mo | PASS |
| solo_operable | Yes | Yes | PASS |
| monthly_revenue_potential | ≥ 500 €/mo | 900 €/mo | PASS |
| distribution_cost | ≤ 7 | 2 (channel: seo) | PASS |
| platform / ToS | see playbook | User-upload PDFs; LLM API (Mistral/OpenAI); no scraping-only dependency | PASS |

### Platform Risk

| Field | Value |
|-------|-------|
| tos_risk | low |
| platform_dependency | medium |
| alternative_data_source | true |

### MSFI-lite

| Component | Score |
|-----------|-------|
| speed_score | 58 |
| economics_score | 52 |
| reach_score | 40 |
| **MSFI** | **51.4** |

```yaml
confidence_level: medium
```

---

## Final Decision (Micro SaaS)

| Field | Value |
|-------|-------|
| **Primary Decision** | MONITOR_MICRO |
| **MSFI** | 51.4 |
| **capacity_blocked** | false |
| **Date** | 2026-06-27 |
| **Rationale** | All hard gates pass. MSFI 51.4 sits in monitor band (50–69). Desk-only validation confirms real SME pain (missed tacit renewals, fragmented tracking) and viable MVP scope (~78 h), but TACIT (FR) already delivers AI PDF extraction, tacit-renewal alerts, and PME pricing at €29–49/mo with live testimonials — near-identical wedge compresses pricing power and reach. BUILD_MICRO blocked until live validation proves a differentiated angle (accountant read-only portal, multi-category FR compliance templates, or shared calendar retention lift) that TACIT does not satisfy. |

### Expected Learnings

- [ ] Accountant collaboration wedge — Method: 5 SME owner + expert-comptable interviews — Applies to: MONITOR_MICRO
- [ ] Shared calendar vs email-only alerts retention lift — Method: 2-week concierge pilot with 3 SMEs — Applies to: MONITOR_MICRO
- [ ] AI extraction accuracy on FR notice-period clauses — Method: concierge import of 15–25 contract PDFs — Applies to: MONITOR_MICRO

### Next Actions

- [ ] Ship SEO landing page targeting "alerte reconduction tacite PME" / "gestion échéances contrats PME" long-tail keywords
- [ ] Run 5 problem interviews with French SME owners/admins (5–50 employees, 15–40 recurring contracts)
- [ ] Deliver 2-week concierge alert + shared calendar to 3 SMEs using their contract PDFs; collect usefulness and willingness-to-pay ratings
- [ ] Document TACIT feature-gap audit on accountant portal and maintenance réglementaire categories
- [ ] Re-evaluate at 30-day review (2026-07-27); promote to BUILD_MICRO only if MSFI ≥ 70 and live validation passes with clear differentiation vs TACIT

### Portfolio Update

- [x] Added to [portfolio/micro-saas.md](../portfolio/micro-saas.md)

```yaml
confidence_level: medium
```

---

## Post-BUILD_MICRO (manual)

Complete after BUILD_MICRO decision — not orchestrated by CP — Eval.

See [docs/legacy-studio.md](../docs/legacy-studio.md) BUILD prep prompts (vision, mvp, roadmap, architecture, success_contract) or a separate product repo.
