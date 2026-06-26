---
id: OPP-20260626-stock-consommables-electriciens-tpe
title: "Suivi stock consommables et réappro pour électriciens TPE locaux"
portfolio_strategy: solo_micro_saas
status: decided
intake_complete: true
decision: MONITOR_MICRO
capacity_blocked: false
global_score: null
opportunity_quality_index: null
time_to_first_revenue_days: 75
monthly_revenue_potential: 750
distribution_channel: communities
distribution_cost: 3
scores: {}
decision_override: false
override_rationale: null
override_expires: null
pipeline_stage: portfolio_manager_micro
next_review_action: "Sprint validation: 8 entretiens CMA + landing WTP + concierge SMS — deadline 2026-07-26"
created: 2026-06-26
updated: 2026-06-26
owner: studio-team
tags: [b2b, saas, france, btp, electricien, micro-saas]
automation_intake_at: 2026-06-26
micro_saas:
  decision: MONITOR_MICRO
  msfi: 64.3
  build_hours_estimate: 92
  maintenance_hours_estimate: 8
  mrr_target_12m: "500-900 EUR"
  wedge: "Catalogue consommables + seuils + alertes réappro — 1 département, TPE sans magasinier"
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

# Suivi stock consommables et réappro pour électriciens TPE locaux

**Wedge** : app minimaliste — catalogue perso de consommables (dominos, goulottes, câbles courants), seuils mini/maxi, alertes email/SMS réappro, historique consommation par chantier — pour **un département**, artisans **solo/TPE sans magasinier** (1–5 salariés, 3–8 chantiers/semaine, pas d'ERP).

---

## Discovery

### Problem Statement

French **electrician micro-businesses** (solo or TPE with 1–5 employees, no dedicated storekeeper) lose billable time and risk job delays when **consumable stock** (wire nuts, cable trays, common cable gauges, fixings) is poorly tracked across **van stock** and a small depot. Typical failure modes: **stock-out on site** mid-intervention, **emergency runs to the wholesaler (négoce)**, and **overstock tied up in vans** because nobody reconciles usage per job. Today most use **Excel, paper notebooks, or memory**; full **ERP suites** (Obat, Tolteck, Esabora, Vertuoza) bundle stock with quoting, invoicing, and HR at **€25–150+/month** — overkill when the pain is narrowly **"do I have enough dominos on the truck for today's three jobs?"**

Pain is **frequent and operational**: consumables are used on nearly every job; a missing SKU costs 30–90 minutes plus fuel; repeated emergency purchases erode margin. Urgency is **same-day** when a tech discovers a gap on site. Frequency is **weekly** for active TPEs running multiple concurrent chantiers.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| entreprises_installation_electrique_4321A | ~118 000–133 000 entreprises FR | verified | INSEE secteur 432 / Propulse by CA étude marché | 2020–2024 |
| tpe_moins_20_salaries_part | ~98 % entreprises <20 sal. dans secteur 432 | verified | INSEE fiche secteur 432 | 2024 |
| icp_tpe_1_5_salaries | Sous-ensemble TPE 1–5 sal. sans magasinier | inferred | PR intake + structure secteur | 2026 |
| erp_pricing_band | €25–150/mo (Obat, Tolteck, suites installateurs) | estimated | Tool-advisor comparatif électriciens ; comparatif Obat/Tolteck | 2026 |
| stock_pain_frequency | Ruptures / courses urgentes hebdo pour TPE actifs | inferred | PR intake ; retours forums métier | 2026 |
| wtp_hypothese | €9–19/mo pour outil stock seul | unknown | Pas d'entretiens studio | — |
| distribution_seo_local | Requêtes « stock consommables électricien » + CMA/Facebook métier | inferred | PR intake canal | 2026 |
| build_maint_constraint | Build ≤100 h ; maint ≤10 h/mo | synthetic | Contrainte studio intake | 2026 |

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| Excel / cahier papier | Suivi manuel camion + dépôt | Gratuit, familier | Pas d'alertes ; pas d'historique par chantier ; oublis fréquents |
| Mémoire / chef de chantier | Réappro ad hoc | Zéro coût | Non scalable dès 2–3 équipes ; ruptures récurrentes |
| Obat / Tolteck | ERP BTP complet (devis, factures, parfois stock) | Suite intégrée, mobile, référencé électriciens | €25–150+/mo ; stock secondaire vs devis ; surdimensionné pour seul pain stock |
| Esabora Business / Vertuoza / Kalitics | ERP installateurs avec module stock | Stock + marge chantier natif | Prix et complexité élevés ; onboarding lourd pour TPE sans ERP |
| Primadis / Yoyolo (BTP) | Gestion stock + factures fournisseurs | Suivi consommables et marges | Moins connu ; toujours suite large, pas wedge minimal |
| Nocodia (no-code sur mesure) | App métier custom Airtable/Softr | Alertes seuil par camion/technicien | Sur-mesure cher ; pas produit self-serve scalable |
| Négoce (Rexel, Sonepar, etc.) | Commande réactive | Livraison rapide, crédit pro | Ne prévient pas la rupture ; coût course + temps perdu |
| Notion / Google Sheets template | DIY inventaire | Flexible, peu cher | Pas SMS/seuils métier ; adoption faible sur le terrain |

### Initial Hypothesis

We believe **electrician TPE owners** (1–5 employees, 3–8 jobs/week, no ERP, one French département) will pay **€9–19/month** for a **minimal consumables catalogue with min/max thresholds, email/SMS reorder alerts, and per-job consumption history**, because **Excel and memory fail on van stock**, **emergency wholesaler runs cost margin and schedule**, and **full ERP tools are priced and scoped for entire business management**, not a single operational wedge.

### Open Questions

- [ ] Quelle fréquence réelle de rupture consommables (dominos, goulottes, câble 1,5²/2,5²) par semaine pour TPE 2–4 salariés ?
- [ ] Les électriciens paient-ils un outil dédié stock ou préfèrent-ils rester sur Excel gratuit ?
- [ ] ARPU €9–19/mo suffisant vs module stock inclus dans Tolteck (~€25/mo) ?
- [ ] Saisie manuelle / import CSV : taux d'abandon après 30 jours sur le terrain ?
- [ ] SEO local « stock consommables électricien » : volume et intent achat suffisants dans un département pilote ?
- [ ] Chevauchement avec [OPP-20260626-suivi-conformite-artisans-btp](../opportunities/OPP-20260626-suivi-conformite-artisans-btp.md) sur ICP BTP TPE — bundling ou cannibalisation ?

**confidence_level**: medium

---

## Validation

Desk evaluation only. **desk-only**: true — live customer experiments below are **planned**, not executed; one **completed** desk scan satisfies the orchestrator gate for MONITOR_MICRO path only (BUILD_MICRO requires live validation). See [validation.md](../playbooks/validation.md).

### Experiments

| # | Experiment | Hypothesis | Method | Success Criteria | Status |
|---|------------|------------|--------|------------------|--------|
| 1 | Problem interviews | TPE électriciens confirment ruptures consommables ≥1×/semaine | 8 entretiens via CMA / groupe Facebook métier dept pilote | ≥5/8 confirment pain + citent course négoce urgente | planned |
| 2 | WTP landing | Demande à €9–19/mo pour stock seul | Landing FR + Van Westendorp ; €200 ads Facebook artisans locaux | ≥25 signups ; ≥20 % acceptent ≥€9/mo | planned |
| 3 | Concierge stock | Suivi manuel seuils + alertes SMS réduit ruptures | 8 TPE, catalogue 30 SKU, alertes SMS 4 semaines | ≥6/8 rapportent ≥1 rupture évitée ; ≥3 pré-commandent après pilote | planned |
| 4 | Competitive landscape desk scan | Tolteck/Obat/Excel ne couvrent pas le wedge alertes camion | Revue éditeurs BTP, comparatifs, StockEleec/Nocodia, templates Excel BTP | Gap documenté sur ≥2 critères wedge (seuils camion, alertes SMS, historique/chantier) | **completed** |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| pain_confirmation | — | unknown | Pas d'entretiens studio | — |
| wtp_signal | — | unknown | Pas de landing / LOI | — |
| concierge_usefulness | — | unknown | Pas de concierge | — |
| erp_entry_floor | €19–25/mo HT (Tolteck annuel 19 € ; mensuel 25 € ; Obat Pro dès 25 € annuel) | verified | tool-advisor Tolteck ; compafacturation Obat vs Tolteck ; independant.io | 2026 |
| tolteck_obat_stock_module | Devis/factures + ouvrages ; pas de module stock consommables camion documenté | verified | Comparatifs Obat/Tolteck ; organilog comparatif électriciens | 2026 |
| organilog_stock_bundled | Module stock présent mais suite CRM/planning €24–40/mo/utilisateur | verified | Yolah CRM électricien ; Organilog comparatif | 2026 |
| free_alternative_dominance | Excel/Sheets + modèles BTP gratuits restent l'alternative #1 | verified | sheetcontrole ; cours-genie-civil modèles chantier ; archipelia comparatif stock | 2026 |
| stockeleec_positioning | App stock électricien gratuite (Google Sheets) — cible pédagogique Bac Pro/CAP, pas TPE pro | verified | MyEleec StockEleec | 2026 |
| nocodia_custom_stock | Stock camion + alertes existe en sur-mesure no-code (coût projet, pas SaaS self-serve) | verified | nocodia.fr application métier électricien | 2026 |
| wedge_gap_score | 4/4 critères wedge absents ou secondaires chez incumbents entry-tier | inferred | Desk scan #4 vs wedge scope Discovery | 2026-06-26 |
| excel_pain_pattern | Ateliers/BTP : sorties consommables non tracées → ruptures au mauvais moment | inferred | sheetcontrole cas atelier consommables ; PR intake | 2026 |

**Experiment #4 summary**: Entry-tier ERPs (Tolteck, Obat) compete on devis/factures/chantier, not van consumable min/max alerts. Organilog bundles stock at higher per-user pricing. Free paths (Excel, StockEleec pédagogique) confirm demand for stock tracking but lack SMS/seuils métier TPE and field adoption discipline. **Wedge gap is plausible** but **WTP vs €19 Tolteck bundle and vs Excel gratuit remains unvalidated**.

### Kill / Continue Signals

- **Continue if**: ≥5/8 entretiens confirment ruptures hebdo ; ≥3 pré-commandes ou LOI €9+/mo ; concierge ≥6/8 cite rupture évitée ; ARPU viable ≥€9/mo après Van Westendorp
- **Kill if**: ≥5/8 disent Excel/Tolteck suffisent ; 0 signup après €200 ads ; ≥4/8 refusent tout outil payant stock seul ; Tolteck/Obat lance module stock camion natif à ≤€15/mo

**confidence_level**: low

---

## Scoring

> **N/A for `portfolio_strategy: solo_micro_saas`** — fast path skips this section. Leave empty; QA must not fail on unfilled rows.

<!-- Paste output from prompts/scoring.md. startup_studio only. See playbooks/scoring-rules.md -->

| Dimension | Raw (0–10) | Weight | Weighted | Evidence | Rationale |
|-----------|------------|--------|----------|----------|-----------|
| pain_level | | 15% | | | |
| urgency | | 10% | | | |
| willingness_to_pay | | 15% | | | |
| competition | | 8% | | | |
| distribution_advantage | | 12% | | | |
| technical_complexity | | 8% | | | |
| maintenance_complexity | | 7% | | | |
| founder_fit | | 10% | | | |
| market_timing | | 8% | | | |
| defensibility | | 7% | | | |
| **Total** | | **100%** | **XX** | | |

**global_score**: XX

**confidence_level**: high / medium / low

---

## Distribution Analysis

<!-- Paste output from prompts/distribution-analysis.md -->

| Factor | Score / Value | Evidence | Rationale |
|--------|---------------|----------|-----------|
| Acquisition difficulty | 0–10 | | |
| Channel accessibility | 0–10 | | |
| Estimated CAC | | | |
| Competition intensity | 0–10 | | |
| Founder audience advantage | 0–10 | | |

**distribution_score**: XX

**distribution_notes**:

**confidence_level**: high / medium / low

---

## Unfair Advantage Analysis

<!-- Paste output from prompts/unfair-advantage.md -->

| Advantage Type | Strength | Evidence | Notes |
|----------------|----------|----------|-------|
| existing_audience | high/medium/low/none | | |
| existing_expertise | | | |
| proprietary_data | | | |
| exclusive_partnerships | | | |
| technical_moat | | | |
| seo_moat | | | |
| community_moat | | | |

**moat_score**: XX

**confidence_level**: high / medium / low

---

## Maintenance Evaluation

<!-- Paste output from prompts/maintenance-evaluation.md -->

| Factor | Score (1–10) | Evidence | Rationale |
|--------|--------------|----------|-----------|
| customer_support | | | |
| ai_costs | | | |
| integrations | | | |
| external_dependencies | | | |
| regulations | | | |
| manual_operations | | | |

**maintenance_score**: XX

**confidence_level**: high / medium / low

---

## Risk Analysis

<!-- Paste output from prompts/risk-analysis.md -->

| Risk | Probability | Impact | Mitigation | Evidence |
|------|-------------|--------|------------|----------|
| market_risk | low/medium/high | | | |
| technical_risk | | | | |
| regulatory_risk | | | | |
| competition_risk | | | | |
| execution_risk | | | | |

**risk_exposure_score**: XX

**confidence_level**: high / medium / low

---

## Portfolio Intelligence

<!-- Paste output from prompts/portfolio-intelligence.md -->

| Factor | Score (0–10) | Evidence | Rationale |
|--------|--------------|----------|-----------|
| diversification_impact | | | |
| overlap_with_existing | | | |
| shared_infrastructure | | | |
| cross_selling | | | |
| operational_synergies | | | |

**portfolio_fit_score**: XX

**portfolio_fit_notes**:

**confidence_level**: high / medium / low

---

## Scenario Planning

<!-- Paste output from prompts/scenario-planning.md -->

### Optimistic

- **Assumptions**:
- **global_score**: XX
- **Decision**: build / monitor / kill

### Realistic

- **Assumptions**:
- **global_score**: XX
- **Decision**: build / monitor / kill

### Pessimistic

- **Assumptions**:
- **global_score**: XX
- **Decision**: build / monitor / kill

### Probabilities

| Outcome | Probability |
|---------|-------------|
| build | XX% |
| monitor | XX% |
| kill | XX% |

**confidence_level**: high / medium / low

---

## Micro SaaS Evaluation

**Wedge scope**: Catalogue perso de consommables électricien (dominos, goulottes, câbles courants), seuils mini/maxi par SKU, alertes email/SMS réappro, historique consommation par chantier — **1 département**, TPE **1–5 salariés sans magasinier**. **Hors scope** : ERP/devis/factures, multi-dépôt enterprise, intégration négoce temps réel, multi-département self-serve.

### Hard Gates

| Gate | Threshold | Estimate | Result |
|------|-----------|----------|--------|
| build_hours | ≤ 100 h | 92 h | PASS |
| maintenance_hours | ≤ 10 h/mo | 8 h/mo | PASS |
| solo_operable | Yes | Yes | PASS |
| monthly_revenue_potential | ≥ 500 €/mo | 750 €/mo (50×€15) | PASS |
| distribution_cost | ≤ 7 | 3 (channel: communities) | PASS |
| platform / ToS | see playbook | tos low ; user data | PASS |

**Gate evidence**

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| build_hours_mvp | 92 h (catalogue CRUD, seuils, alertes SMS/email, log/chantier, auth, billing, deploy) | estimated | Scope wedge Discovery + stack SaaS standard | 2026-06-26 |
| maintenance_m6 | 8 h/mo (support TPE, SMS monitoring, bugfixes) | estimated | Comparable MONITOR wedges ; pas d'intégration négoce | 2026-06-26 |
| mrr_ceiling_dept | 750 €/mo = 50 clients × €15/mo | estimated | ICP ~1k TPE/dept × 5% conv. ; ARPU €9–19 hyp. Discovery | 2026-06-26 |
| distribution_primary | CMA + groupes Facebook métier locaux | inferred | Discovery canal ; coût map communities=3 | 2026-06-26 |

### Platform Risk

| Field | Value | Notes |
|-------|-------|-------|
| tos_risk | low | Données inventaire saisies par l'utilisateur ; pas de scrape |
| regulatory_risk | low | Suivi stock consommables ; pas de données réglementées |
| platform_dependency | low | Email/SMS via API (Twilio/Brevo) ; pas de dépendance réseau social |
| alternative_data_source | true | Catalogue et seuils entièrement user-owned |

### MSFI v2

| Component | Score | Rationale |
|-----------|-------|-----------|
| time_to_revenue_score | 50 | 75 j (landing + CMA outreach + 1er payant) — bande 61–120 j |
| automation_score | 85 | Alertes seuil + SMS/email automatisés ; saisie self-serve |
| maintenance_sustainability_score | 75 | 8 h/mo estimé ; support TPE terrain modéré |
| acquisition_score | 58 | CMA/Facebook locaux faisable solo mais lent ; pas d'audience studio |
| wedge_local_score | 82 | Wedge hyper-local dept + catalogue perso consommables |
| competition_score | 62 | Gap wedge documenté (Validation #4) ; Excel/Tolteck pression entry-tier |
| pricing_power_score | 42 | WTP unknown ; Tolteck ~€19/mo et Excel gratuit ancrent le bas |
| **MSFI** | **64.3** | |

MSFI calc: `0.15×50 + 0.15×85 + 0.10×75 + 0.15×58 + 0.15×82 + 0.15×62 + 0.15×42 = 64.3`

**Provisional decision**: MONITOR_MICRO — all hard gates PASS ; MSFI 64.3 in 50–69 band ; desk-only Validation blocks BUILD_MICRO until live sprint (entretiens + landing + concierge).

**confidence_level**: medium

---

## Final Decision (Micro SaaS)

| Field | Value |
|-------|-------|
| **Primary Decision** | MONITOR_MICRO |
| **MSFI** | 64.3 |
| **capacity_blocked** | false |
| **Date** | 2026-06-26 |
| **Rationale** | All six hard gates PASS (build 92 h, maint 8 h/mo, solo-operable, MRR 750 €/mo, distribution_cost 3, ToS low). MSFI 64.3 in MONITOR band (50–69). Desk-only Validation (`desk-only: true`, confidence low) blocks BUILD_MICRO — no live interviews, landing, or concierge completed. WTP unknown vs Tolteck ~€19/mo and Excel gratuit. Wedge gap plausible (Validation #4 desk scan) but requires live sprint before BUILD promotion. Portfolio capacity available (0 BUILD active, 3/5 MONITOR slots) — not capacity-blocked. |

### Expected Learnings

- [ ] Topic: pain_frequency — Method: 8 entretiens TPE électriciens via CMA / Facebook métier dept pilote — Applies to: MONITOR_MICRO, KILL_MICRO
- [ ] Topic: willingness_to_pay — Method: Landing FR + Van Westendorp €9–19/mo + €200 ads Facebook artisans — Applies to: MONITOR_MICRO, BUILD_MICRO
- [ ] Topic: concierge_value — Method: Concierge SMS seuils 8 TPE × 4 semaines — Applies to: MONITOR_MICRO, BUILD_MICRO
- [ ] Topic: incumbent_sufficiency — Method: ≥5/8 disent Excel/Tolteck suffisent ? — Applies to: KILL_MICRO

### Next Actions

- [ ] 8 entretiens CMA / groupe Facebook électriciens dept pilote — deadline 2026-07-15
- [ ] Publier landing « stock consommables électricien » + waitlist Van Westendorp — deadline 2026-07-15
- [ ] Concierge manuel alertes SMS 8 TPE × 4 semaines — deadline 2026-07-20
- [ ] Re-calculer MSFI ; promouvoir BUILD_MICRO si MSFI ≥70 + live validation pass — deadline 2026-07-26

### Portfolio Update

- [x] Added to [portfolio/micro-saas.md](../portfolio/micro-saas.md) (Monitoring)

**confidence_level**: medium

---

## Final Decision (Studio — startup_studio only)

<!-- Paste output from prompts/portfolio-manager.md — skip for solo_micro_saas -->

| Field | Value |
|-------|-------|
| **Primary Decision** | build / monitor / kill |
| **global_score** | XX |
| **opportunity_quality_index** | XX |
| **Date** | YYYY-MM-DD |
| **Rationale** | |

### OQI Breakdown

| Component | Score |
|-----------|-------|
| evidence_quality | XX |
| confidence_aggregate | XX |
| score_reliability | XX |
| risk_adjustment | XX |
| **OQI** | **XX** |

### Expected Learnings

- [ ] Topic: ... — Method: ... — Applies to: monitor / kill

### Next Actions

- [ ] Action 1
- [ ] Action 2

### Dissent (if any)

Record any disagreement and reasoning.

### Portfolio Update

- [ ] Added to [portfolio/active.md](../portfolio/active.md) / [monitoring.md](../portfolio/monitoring.md) / [archived.md](../portfolio/archived.md)

---

## BUILD Preparation

<!-- Complete only if Primary Decision is BUILD -->

### Product Vision

<!-- Paste output from prompts/vision.md -->

#### Target User

Who is the primary user? Be specific (role, company size, context).

#### Value Proposition

One sentence: We help [user] do [outcome] by [approach].

#### Differentiation

What makes this different from alternatives?

#### North Star Metric

The single metric that best captures value delivered.

---

### MVP Definition

<!-- Paste output from prompts/mvp.md -->

#### Scope In

- Item 1

#### Scope Out

- Item 1

#### Success Metrics

| Metric | Target | Measurement method |
|--------|--------|--------------------|
| | | |

#### Smallest Testable Slice

The minimum build or experiment to validate core value.

---

### Roadmap

<!-- Paste output from prompts/roadmap.md -->

#### Phase 1: {Name} (Weeks X–Y)

- Milestone 1

**Dependencies**: ...

#### Resource Assumptions

| Role | Allocation | Duration |
|------|------------|----------|
| | | |

---

### Architecture Proposal

<!-- Paste output from prompts/architecture.md. Documentation only — no code -->

Reference **Risk Analysis** for business and technical risks.

#### System Overview

High-level description of components and data flow.

#### Build vs Buy

| Component | Decision | Rationale |
|-----------|----------|-----------|
| | build / buy | |

#### Integration Points

External systems, APIs, or data sources required.

#### Technical Risks (summary)

See [Risk Analysis](#risk-analysis) for full register. Key technical items:

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| | | | |

---

### Success Contract

<!-- Paste output from prompts/success-contract.md -->

#### Commitments

| Commitment | Metric | Target | Review Date |
|------------|--------|--------|-------------|
| | | | |

#### Review Schedule

- First review: YYYY-MM-DD
- Cadence: every 30 days

#### Exit Triggers

Conditions that trigger re-evaluation or kill:

- Trigger 1: ...
