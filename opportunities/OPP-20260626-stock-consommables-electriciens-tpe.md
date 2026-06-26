---
id: OPP-20260626-stock-consommables-electriciens-tpe
title: "Suivi stock consommables et réappro pour électriciens TPE locaux"
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
tags: [b2b, saas, france, btp, electricien, micro-saas]
automation_intake_at: 2026-06-26
micro_saas:
  decision: null
  msfi: null
  build_hours_estimate: 100
  maintenance_hours_estimate: 10
  mrr_target_12m: ""
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

<!-- Paste output from prompts/validation.md -->

### Experiments

| # | Experiment | Hypothesis | Method | Success Criteria | Status |
|---|------------|------------|--------|------------------|--------|
| 1 | | | | | planned |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| | | | | |

### Kill / Continue Signals

- **Continue if**: ...
- **Kill if**: ...

**confidence_level**: high / medium / low

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

<!-- Paste output from prompts/micro-saas-evaluation.md — solo_micro_saas fast path -->

**confidence_level**: high / medium / low

---

## Final Decision (Micro SaaS)

<!-- Paste output from prompts/portfolio-manager-micro.md — primary for solo_micro_saas -->

| Field | Value |
|-------|-------|
| **Primary Decision** | BUILD_MICRO / MONITOR_MICRO / KILL_MICRO |
| **MSFI** | XX |
| **capacity_blocked** | true / false |
| **Date** | YYYY-MM-DD |
| **Rationale** | |

**confidence_level**: high / medium / low

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
