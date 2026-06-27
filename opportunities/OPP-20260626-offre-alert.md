---
id: OPP-20260626-offre-alert
title: "OffreAlert — veille appels d'offres ultra ciblée pour PME locales"
eval_engine: v3-lite
portfolio_strategy: solo_micro_saas
status: decided
intake_complete: true
decision: MONITOR_MICRO
capacity_blocked: false
msfi: 52.7
speed_score: 60
economics_score: 52
reach_score: 42
time_to_first_revenue_days: 75
monthly_revenue_potential: 1500
distribution_channel: seo
distribution_cost: 2
build_hours_estimate: 88
maintenance_hours_estimate: 8
wedge: "Multi-source tender monitoring (CPV/NAF, geo, amount) → AI summary + relevance score → daily digest of 3–10 high-fit alerts for local SMEs without a procurement team"
pipeline_stage: fit_and_decide
next_review_action: validate
created: 2026-06-26
updated: 2026-06-27
automation_intake_at: 2026-06-26
owner: studio-team
tags: [b2b, micro-saas, ai, pme, procurement]
prompt_versions:
  discovery: v1
  validation: v2
  fit_and_decide: v1
---

# OffreAlert — veille appels d'offres ultra ciblée pour PME locales

## Discovery

### Problem Statement

Local SMEs in trades and services (construction, cleaning, maintenance, supplies, facility services) often miss relevant public tenders because monitoring is fragmented across BOAMP, PLACE, regional buyer platforms (Maximilien, Mégalis, AWS-Achat, e-Marchespublics), and individual buyer sites. Teams of 5–50 people rarely have a dedicated procurement function; the owner or office manager must scan hundreds of raw listings daily, decode CPV codes, and read lengthy consultation documents (DCE) to decide whether to respond. Missed deadlines mean lost revenue on MAPA and sub-threshold contracts that are structurally accessible to smaller firms, while false positives waste hours on irrelevant notices. The pain is recurring (daily/weekly), has direct revenue impact, and intensifies as public buyers multiply publication channels with no single national feed.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| public_procurement_volume_2024 | 223,383 contracts; €233.3B total | verified | OECP recensement 2024 (Seban Avocats summary) | 2026-03-01 |
| local_public_sector_share | 159,435 contracts; €100.7B (local public sector) | verified | OECP recensement 2024 (Seban Avocats summary) | 2026-03-01 |
| pme_contract_share | 60% of contracts won by PME; 25% of total value | verified | OECP / Nextend.ai observatory 2024–2025 | 2026-04-01 |
| pme_local_contract_share | 63% of local public contracts won by PME (by count) | verified | Nextend.ai — PME & marchés publics 2024 | 2026-04-21 |
| boamp_coverage_gap | BOAMP does not publish all MAPA below ~€90k HT; regional buyer profiles required | verified | OLRA guide — trouver appels d'offres publics 2026 | 2026-01-01 |
| source_fragmentation | No single platform covers 100% of French public tenders | verified | Remporte — comparatif plateformes AO 2026 | 2026-01-01 |
| premium_veille_pricing | Established aggregators priced €80–500/mo | estimated | Doaken / Remporte comparatives; AlertOffres alternatives page | 2026-01-01 |
| regulatory_pme_support | Decree 2024-1251 (Jan 2025): stronger PME access measures (retention, subcontracting, thresholds) | verified | CFC — favoritisme & soutien PME locales | 2025-01-01 |
| target_company_size | 5–50 employees; no dedicated procurement team | synthetic | Intake hypothesis (studio-team) | 2026-06-26 |
| alert_volume_hypothesis | 3–10 relevant alerts/week vs hundreds of raw listings | synthetic | Intake hypothesis (studio-team) | 2026-06-26 |
| wedge_price_band | €29–79/mo for ultra-targeted digest | synthetic | Intake hypothesis vs AlertOffres Pro €29.99/mo benchmark | 2026-06-26 |

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| BOAMP + PLACE free alerts | Official email alerts by keywords, CPV, geography | Free; legally authoritative; CPV filtering available | No MAPA below publication thresholds; no cross-source dedup; no DCE summarization; high noise for multi-source users |
| AlertOffres | Aggregates BOAMP, TED, PLACE, regional profiles; AI DCE summaries; Pro at €29.99/mo | Modern UX; low price vs legacy; free tier; AI summaries already marketed | Direct overlap with proposed wedge; unclear differentiation on "3–10 ultra-relevant" local-SME positioning |
| France Marchés / Marchés Online / Dématis | Legacy aggregators with deep historical data and buyer intelligence | Broad coverage; established B2B sales channels; attribution analytics on some tiers | €80–300+/mo typical; annual commitments common; heavy interfaces; weak fit for micro-SME self-serve |
| Semagora / Spigao / Klekoon / Nukema | Sector- or volume-oriented AO platforms with qualification workflows | GO/NO-GO framing; familiar to repeat bidders | Pricing and UX oriented to firms already responding at volume; not narrow "local SME digest" wedge |
| Manual multi-site monitoring | Owner checks BOAMP + 2–3 regional portals daily | No subscription cost; full control | 30–60+ min/day; missed deadlines; CPV misconfiguration; no relevance scoring |
| Commercial bid consultants | Human tender scouting and response prep | High trust; handles complex DCE | €500+/mo retainers; not scalable for 5–50 employee SMEs |
| DIY automation (n8n + open data) | Self-built scrapers on BOAMP open data + email rules | Low marginal cost for technical users | Fragile when sources change; no AI summary layer; maintenance burden on non-technical owners |

### Initial Hypothesis

We believe local SMEs (5–50 employees) in trades and facility services without a procurement team will pay €29–79/mo for a daily digest limited to 3–10 high-relevance tender alerts because multi-source monitoring and DCE triage currently consume 30–60 minutes per day and incumbent aggregators either cost €100+/mo or flood inboxes with unqualified notices.

### Open Questions

- [ ] Can relevance scoring reliably surface ≤10 alerts/week per company profile without missing deadline-critical MAPA on regional buyer platforms?
- [ ] Is €29–49/mo viable when AlertOffres Pro already offers AI summaries at €29.99/mo — what wedge (geo-local buyer graph, NAF+CPV hybrid, admin-trap detection) justifies switching?
- [ ] Do target SMEs trust AI-generated DCE summaries for go/no-go, or do they still require human review of full documents?
- [ ] Which distribution channel reaches owner-operators fastest: SEO ("veille AO [métier] [département]"), accountant/bookkeeper referrals, or chamber-of-commerce partnerships?
- [ ] What is the legal/ToS risk of aggregating and summarizing content from regional buyer platforms beyond BOAMP open data?
- [ ] Will SMEs churn after winning 1–2 contracts, or does ongoing MAPA pipeline justify retention?

```yaml
confidence_level: medium
```

---

## Validation

### Experiments

| # | Experiment | Method | Success Criteria | Status |
|---|------------|--------|------------------|--------|
| 1 | AlertOffres feature-parity audit | Desk research: AlertOffres pricing, features, source coverage, AI capabilities | Document overlap with proposed wedge (multi-source, CPV/geo filters, AI DCE summary, PME pricing); identify any gap on "3–10 curated digest" positioning | completed |
| 2 | Wedge pricing & incumbent benchmark | Desk research: AlertOffres, France Marchés, Marchés Online, BOAMP free alerts | €29–49/mo wedge is ≤50% of legacy aggregator spend (€80–300/mo) and within 2× of AlertOffres Pro €29.99/mo | completed |
| 3 | Live validation sprint (planned) | SEO landing + 5 SME owner interviews + 2-week concierge digest | ≥4/5 confirm daily multi-source monitoring pain; ≥3/5 rate curated 3–10 alert digest as "would use weekly"; waitlist ≥30 emails in 30 days | planned |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| alertoffres_direct_overlap | AlertOffres Pro at €29.99/mo HT aggregates 7 official sources (BOAMP, TED, PLACE, Maximilien, Mégalis, MarchésOnline, data.gouv.fr) with unlimited email alerts and 50 AI credits/mo | verified | AlertOffres pricing & about pages | 2026-06-27 |
| alertoffres_ai_parity | AlertOffres already markets AI DCE summaries, CPV/dept/montant filters, and PME/artisan positioning — core overlap with OffreAlert wedge | verified | AlertOffres homepage & comparatives | 2026-06-27 |
| legacy_pricing_gap | Legacy aggregators (France Marchés, Marchés Online, e-Marchespublics) start €80–150+/mo with annual commitments | verified | AlertOffres alternatives comparatif 2026 | 2026-06-27 |
| boamp_open_api | BOAMP data reusable via free DILA API under Licence Ouverte 2.0 with attribution requirements | verified | data.gouv.fr / DILA API documentation | 2026-06-27 |
| mapa_coverage_gap | MAPA below ~€90k HT may publish only on regional buyer profiles, not BOAMP — multi-source aggregation remains necessary | verified | DILA API docs; Discovery OLRA guide | 2026-06-27 |
| regional_tos_uncertainty | Regional buyer platforms (Maximilien, AWS-Achat, e-Marchespublics) lack uniform open APIs; scraping ToS varies by platform | inferred | Discovery competitor scan; no unified open-data feed found | 2026-06-27 |
| wedge_price_compression | Proposed €29–49/mo sits at or below AlertOffres Pro (€29.99) — limited pricing headroom without clear differentiation | inferred | Pricing benchmark vs intake hypothesis | 2026-06-27 |
| digest_differentiation_unproven | "3–10 ultra-relevant daily digest" vs unlimited alerts is positioning-only; no live SME signal that curation beats AlertOffres filters | synthetic | No live experiments run in this eval cycle | 2026-06-27 |
| live_validation_pending | Zero SME interviews, concierge digests, or waitlist signups completed | synthetic | No live experiments run in this eval cycle | 2026-06-27 |

### Kill / Continue Signals

- **Continue if**: ≥4/5 SME owners confirm 30+ min/day multi-source monitoring pain; ≥3/5 rate a concierge 3–10 alert digest as "would pay €29+/mo"; waitlist reaches 30 emails within 30 days of SEO landing; a defensible wedge emerges (e.g. NAF+CPV hybrid scoring, admin-trap detection, hyper-local buyer graph) that AlertOffres does not cover
- **Kill if**: ≥3/5 SMEs say AlertOffres free/Pro tier is sufficient; zero waitlist after 4 weeks of targeted SEO; regional source integration exceeds 15 h seed budget; legal review flags high ToS risk on regional scraping with no compliant alternative

```yaml
desk_only: true
confidence_level: low
```

---

## Fit and Decide

**Wedge scope**: Daily email digest of 3–10 high-relevance tender alerts for local trade/service SMEs (5–50 employees), built on multi-source aggregation (BOAMP API + regional buyer profiles), CPV/NAF/geo/amount filters, AI DCE summary, and relevance scoring — priced €29–49/mo, solo-operable without a procurement team.

### Hard Gates

| Gate | Threshold | Estimate | Result |
|------|-----------|----------|--------|
| build_hours | ≤ 100 h | 88 h | PASS |
| maintenance_hours | ≤ 10 h/mo | 8 h/mo | PASS |
| solo_operable | Yes | Yes | PASS |
| monthly_revenue_potential | ≥ 500 €/mo | 1 500 €/mo | PASS |
| distribution_cost | ≤ 7 | 2 (channel: seo) | PASS |
| platform / ToS | see playbook | BOAMP via DILA open API; regional sources hybrid; not scraping-only | PASS |

### Platform Risk

| Field | Value |
|-------|-------|
| tos_risk | medium |
| platform_dependency | medium |
| alternative_data_source | true |

### MSFI-lite

| Component | Score |
|-----------|-------|
| speed_score | 60 |
| economics_score | 52 |
| reach_score | 42 |
| **MSFI** | **52.7** |

```yaml
confidence_level: medium
```

---

## Final Decision (Micro SaaS)

| Field | Value |
|-------|-------|
| **Primary Decision** | MONITOR_MICRO |
| **MSFI** | 52.7 |
| **capacity_blocked** | false |
| **Date** | 2026-06-27 |
| **Rationale** | All hard gates pass. MSFI 52.7 sits in monitor band (50–69). Desk-only validation confirms real SME pain (fragmented sources, MAPA coverage gaps) and viable BOAMP open-data path, but AlertOffres Pro at €29.99/mo already delivers multi-source aggregation, AI DCE summaries, and PME positioning — direct overlap compresses pricing power and reach. BUILD_MICRO blocked until live validation proves a differentiated wedge (curated digest quality, NAF+CPV scoring, or hyper-local buyer graph) that incumbents do not satisfy. |

### Expected Learnings

- [ ] Curated 3–10 digest vs unlimited alerts — Method: 5 SME interviews + 2-week concierge pilot — Applies to: MONITOR_MICRO
- [ ] Defensible differentiation beyond AlertOffres filters — Method: feature-gap audit on NAF mapping, admin-trap detection, regional buyer graph — Applies to: MONITOR_MICRO
- [ ] Regional source ToS compliance path — Method: legal desk review + seed integration on 2 regional platforms — Applies to: MONITOR_MICRO

### Next Actions

- [ ] Ship SEO landing page targeting "veille AO [métier] [département]" long-tail keywords
- [ ] Run 5 problem interviews with local trade/service SME owners (5–50 employees, no procurement team)
- [ ] Deliver 2-week concierge digest (manual curation + AI summary) to 3 SMEs; collect usefulness and willingness-to-pay ratings
- [ ] Document compliant regional source integration plan (Maximilien + 1 additional buyer profile) within 15 h seed budget
- [ ] Re-evaluate at 30-day review (2026-07-27); promote to BUILD_MICRO only if MSFI ≥ 70 and live validation passes with clear differentiation

### Portfolio Update

- [x] Added to [portfolio/micro-saas.md](../portfolio/micro-saas.md)

```yaml
confidence_level: medium
```

---

## Post-BUILD_MICRO (manual)

Complete after BUILD_MICRO decision — not orchestrated by CP — Eval.

See [docs/legacy-studio.md](../docs/legacy-studio.md) BUILD prep prompts (vision, mvp, roadmap, architecture, success_contract) or a separate product repo.
