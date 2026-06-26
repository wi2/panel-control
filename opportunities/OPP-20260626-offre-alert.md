---
id: OPP-20260626-offre-alert
title: "OffreAlert — veille appels d'offres ultra ciblée pour PME locales"
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
wedge: "Multi-source tender monitoring (CPV/NAF, geo, amount) → AI summary + relevance score → daily digest of 3–10 high-fit alerts for local SMEs without a procurement team"
pipeline_stage: discovery
next_review_action: null
created: 2026-06-26
updated: 2026-06-26
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
