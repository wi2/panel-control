---
id: OPP-20260626-suivi-conformite-artisans-btp
title: "Suivi échéances conformité pour artisans BTP locaux"
portfolio_strategy: solo_micro_saas
status: decided
intake_complete: true
decision: MONITOR_MICRO
capacity_blocked: false
global_score: null
opportunity_quality_index: null
time_to_first_revenue_days: 90
monthly_revenue_potential: 800
distribution_channel: seo
distribution_cost: 2
scores: {}
decision_override: false
override_rationale: null
override_expires: null
pipeline_stage: portfolio_manager_micro
next_review_action: validate
created: 2026-06-26
updated: 2026-06-26
owner: studio-team
tags: [b2b, saas, france, btp, conformite, micro-saas]
automation_intake_at: 2026-06-26
micro_saas:
  decision: MONITOR_MICRO
  msfi: 65
  build_hours_estimate: 48
  maintenance_hours_estimate: 4
  mrr_target_12m: "500-1000 EUR"
  wedge: "Rappels multi-doc conformité BTP — 1 dept"
prompt_versions:
  discovery: v1
  validation: v1
  micro_saas_evaluation: v2
  portfolio_manager_micro: v1
  scoring: v2
  distribution_analysis: v1
  unfair_advantage: v1
  maintenance_evaluation: v1
  risk_analysis: v1
  portfolio_intelligence: v1
  scenario_planning: v1
  portfolio_manager: v2
  vision: v1
  mvp: v1
  roadmap: v1
  architecture: v1
  success_contract: v1
---

# Suivi échéances conformité pour artisans BTP locaux

Desk evaluation completed 2026-06-26. No live validation experiments yet. Primary decision **MONITOR_MICRO** (MSFI 65) — 30-day validation sprint before BUILD_MICRO or KILL_MICRO.

**Proposition** : rappels automatiques multi-documents (assurance décennale, RC Pro, Qualibat, attestation URSSAF) pour artisans du bâtiment TPE qui gèrent encore leurs échéances sur calendrier papier ou Excel.

---

## Discovery

### Problem Statement

French **artisans du bâtiment** (TPE 1–10 salariés — plombiers, électriciens, menuisiers, peintres) must maintain valid compliance documents to sign new chantiers: **assurance décennale**, **RC Pro**, labels **Qualibat/RGE** where required, and periodic **attestations URSSAF**. Missing an expiration blocks quotes, subcontracts, or public/private tenders. Dirigeants track deadlines manually (Google Calendar, Excel, paper folders) or rely on their **assureur/courtier** for décennale only — leaving gaps on RC Pro renewals, Qualibat, and URSSAF.

Pain is **recurrent and costly**: a lapsed décennale can halt all new work for days; fines and rejected dossiers are common. Frequency is quarterly-to-annual per document type. Urgency spikes 30–60 days before expiration when clients or maîtres d'ouvrage request fresh attestations.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| entreprises_batiment_fr | ~430 000 | verified | INSEE — secteur F construction | 2024 |
| artisans_tpe_part | ~85 % TPE/PME dans le BTP | estimated | FFB / INSEE agrégats | 2024 |
| assurance_decennale_obligatoire | Obligatoire pour travaux structure | verified | Code des assurances / jurisprudence | 2024 |
| qualibat_rge_marches | Requis pour aides rénovation / MAPA énergie | verified | Qualibat, ADEME | 2025 |
| outils_existants_generiques | Notion/Trello/Calendar sans métier BTP | inferred | Pratique terrain | 2026 |
| wtp_studio_hypothese | €9–19/mo | unknown | Pas d'entretiens studio | — |
| douleur_manquement | Blocage chantier + stress dirigeant | inferred | Retours CCI / forums artisans | 2026 |

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| Google Calendar / iPhone Reminders | Rappels manuels par doc | Gratuit, familier | Pas multi-doc centralisé ; oublis fréquents |
| Excel / cahier papier | Suivi artisanal | Gratuit | Pas d'alertes push ; pas partage équipe |
| Assureur / courtier décennale | Rappel décennale seulement | Gratuit, fiable pour 1 doc | Ne couvre pas RC Pro, Qualibat, URSSAF |
| Obat / Tolteck / Batappli | ERP artisan complet | Suite métier intégrée | €50–150/mo ; surdimensionné pour seul suivi conformité |
| LegalPlace / Captain Contrat | Conformité juridique générique | Marque connue | Pas spécialisé échéances assurance BTP |
| Comptable / expert-comptable | Relance URSSAF/Kbis | Relation existante | Pas temps réel ; pas tous les docs chantier |

### Initial Hypothesis

We believe **artisans BTP TPE** (1–5 salariés, 2–8 chantiers/mo) in **one French département** will pay **€9–19/month** for **centralized compliance deadline tracking** with SMS/email alerts 30/7/1 days before expiry, because **assureur reminders cover décennale only**, **generic calendars lack BTP document templates**, and **ERP tools are too expensive** for a single pain point.

### Open Questions

- [ ] Les artisans paient-ils un outil dédié alors que Calendar gratuit existe ?
- [ ] Quel % oublie au moins une échéance RC Pro ou Qualibat par an ?
- [ ] Distribution viable via CMA/FFB locales sans audience fondateur ?
- [ ] ARPU €9–19/mo suffisant vs Obat entry tiers ?

**confidence_level**: medium

---

## Validation

Desk evaluation only. **desk-only**: true — live experiments below are **planned**, not executed. See [validation.md](../playbooks/validation.md).

### Experiments

| # | Experiment | Hypothesis | Method | Success Criteria | Status |
|---|------------|------------|--------|------------------|--------|
| 1 | Problem interviews | Artisans confirment oublis RC Pro/Qualibat ≥1×/an | 8 entretiens via CMA dept 69 | ≥5/8 confirment pain + citent blocage chantier | planned |
| 2 | WTP landing | Demande à €9+/mo existe | Landing FR + Van Westendorp ; €200 ads Facebook artisans | ≥25 signups ; ≥20 % acceptent ≥€9/mo | planned |
| 3 | Concierge rappels | Rappels manuels SMS 30/7/1 jours réduisent stress | 10 artisans, suivi Excel + SMS, 4 semaines | ≥7/10 NPS ≥8 ; ≥3 citent doc oublié sans concierge | planned |
| 4 | Competitive sufficiency | Calendar/assureur insuffisants | 8 interviews usage actuel | ≥4/8 disent solution actuelle incomplète | planned |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| pain_confirmation | — | unknown | Pas d'entretiens studio | — |
| wtp_signal | — | unknown | Pas de landing / LOI | — |
| concierge_usefulness | — | unknown | Pas de concierge | — |
| competitive_sufficiency | — | unknown | Pas d'interviews | — |

### Kill / Continue Signals

- **Continue if**: ≥3 pré-commandes €9+/mo ; ≥5/8 entretiens confirment oublis multi-doc ; concierge NPS ≥8 pour ≥7/10
- **Kill if**: ≥5/8 disent Calendar + assureur suffisent ; 0 signup après €200 ads ; ARPU viable <€7/mo

**confidence_level**: low

---

## Micro SaaS Evaluation

**Wedge scope**: Suivi centralisé échéances conformité BTP (décennale, RC Pro, Qualibat, URSSAF) avec alertes email/SMS — **1 département**, artisans TPE 1–5 salariés. **Hors scope** : ERP chantier, devis, compta, multi-dept self-serve.

### Hard Gates

| Gate | Threshold | Estimate | Result |
|------|-----------|----------|--------|
| build_hours | ≤ 100 h | 48 h | PASS |
| maintenance_hours | ≤ 10 h/mo | 4 h/mo | PASS |
| solo_operable | Yes | Yes | PASS |
| monthly_revenue_potential | ≥ 500 €/mo | 800 €/mo (40×€19) | PASS |
| distribution_cost | ≤ 7 | 2 (channel: seo) | PASS |
| platform / ToS | see playbook | tos low, no scrape | PASS |

### Platform Risk

| Field | Value | Notes |
|-------|-------|-------|
| tos_risk | low | User-uploaded docs ; no platform API dependency |
| regulatory_risk | low | Reminders only ; disclaimer non-conseil juridique |
| platform_dependency | low | Email/SMS providers only |
| alternative_data_source | true | User enters own expiry dates |

### MSFI v2

| Component | Score |
|-----------|-------|
| time_to_revenue_score | 50 |
| automation_score | 85 |
| maintenance_sustainability_score | 90 |
| acquisition_score | 62 |
| wedge_local_score | 70 |
| competition_score | 58 |
| pricing_power_score | 52 |
| **MSFI** | **65** |

MSFI calc: `0.15×50 + 0.15×85 + 0.10×90 + 0.15×62 + 0.15×70 + 0.15×58 + 0.15×52 = 65.35 → 65`

**Provisional decision**: MONITOR_MICRO

**confidence_level**: medium

---

## Final Decision (Micro SaaS)

| Field | Value |
|-------|-------|
| **Primary Decision** | MONITOR_MICRO |
| **MSFI** | 65 |
| **capacity_blocked** | false |
| **Date** | 2026-06-26 |
| **Rationale** | All hard gates PASS. MSFI 65 in MONITOR band (50–69). Pain structurel vérifié (obligations décennale/RC Pro) mais WTP et différenciation vs Calendar/assureur non validés. Desk-only Validation — BUILD_MICRO blocked until live sprint. |

### Expected Learnings

- [ ] Topic: multi_doc_pain — Method: 8 entretiens CMA artisans dept 69 — Applies to: MONITOR_MICRO, KILL_MICRO
- [ ] Topic: willingness_to_pay — Method: Landing Van Westendorp €9–19/mo — Applies to: MONITOR_MICRO, BUILD_MICRO
- [ ] Topic: competitive_sufficiency — Method: 8 interviews Calendar vs outil dédié — Applies to: KILL_MICRO

### Next Actions

- [ ] Publier landing SEO "rappel assurance décennale artisan" + waitlist — deadline 2026-07-15
- [ ] 8 entretiens artisans via CMA Rhône — deadline 2026-07-20
- [ ] Concierge SMS 10 artisans 4 semaines — deadline 2026-07-25
- [ ] Re-calculer MSFI ; promouvoir BUILD_MICRO si MSFI ≥70 + live validation — deadline 2026-07-26

### Portfolio Update

- [x] Added to [portfolio/micro-saas.md](../portfolio/micro-saas.md) (Monitoring)

**confidence_level**: medium

---
