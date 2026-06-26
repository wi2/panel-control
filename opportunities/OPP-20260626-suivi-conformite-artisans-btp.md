---
id: OPP-20260626-suivi-conformite-artisans-btp
title: "Suivi échéances conformité pour artisans BTP locaux"
portfolio_strategy: solo_micro_saas
status: evaluating
intake_complete: true
decision: null
capacity_blocked: false
global_score: null
opportunity_quality_index: null
time_to_first_revenue_days: null
monthly_revenue_potential: null
distribution_channel: null
distribution_cost: null
scores: {}
decision_override: false
override_rationale: null
override_expires: null
pipeline_stage: discovery
next_review_action: null
created: 2026-06-26
updated: 2026-06-26
owner: studio-team
tags: [b2b, saas, france, btp, conformite, micro-saas]
automation_intake_at: 2026-06-26
micro_saas:
  decision: null
  msfi: null
  build_hours_estimate: null
  maintenance_hours_estimate: null
  mrr_target_12m: ""
  wedge: ""
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

<!-- Paste output from prompts/validation.md -->

---

## Micro SaaS Evaluation

<!-- Paste output from prompts/micro-saas-evaluation.md -->

**confidence_level**: high / medium / low

---

## Final Decision (Micro SaaS)

<!-- Paste output from prompts/portfolio-manager-micro.md -->

**confidence_level**: high / medium / low

---

## Scoring

<!-- studio path skipped for solo_micro_saas -->

---

## Final Decision (Studio — startup_studio only)

<!-- skipped for solo_micro_saas -->
