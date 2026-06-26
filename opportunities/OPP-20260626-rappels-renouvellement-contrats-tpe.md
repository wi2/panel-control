---
id: OPP-20260626-rappels-renouvellement-contrats-tpe
title: "Rappels de renouvellement de contrats pour TPE"
status: evaluating
decision: null
global_score: null
opportunity_quality_index: null
scores: {}
decision_override: false
override_rationale: null
override_expires: null
pipeline_stage: discovery
next_review_action: null
created: 2026-06-26
updated: 2026-06-26
owner: studio-team
tags: [b2b, saas, test, automation-smoke]
prompt_versions:
  discovery: v1
  validation: v1
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

# Rappels de renouvellement de contrats pour TPE

Intake via **CP — Intake** automation smoke test (PR #4). Discovery completed 2026-06-26. This opportunity is flagged for deletion after automation validation per intake description.

---

## Discovery

### Problem Statement

French TPE (typically 5–20 employees) accumulate recurring commitments — commercial leases, professional insurance, SaaS subscriptions, maintenance contracts, telecom — without a single system of record. Renewals are tracked in spreadsheets, shared drives, or individual calendars; when the person who set the reminder leaves, deadlines are missed. The pain is episodic but costly: unwanted tacit renewals (reconduction tacite), paying for unused SaaS seats, negotiating bail extensions under time pressure, or lapsing coverage before replacement is in place. Office managers and owner-operators bear the cognitive load alongside day-to-day operations, with no dedicated legal-ops function.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| etablissements_10_19_salaries | 214 336 établissements actifs employeurs | verified | INSEE Flores — caractéristiques des établissements fin 2022 | 2022 |
| etablissements_1_9_salaries | 1 710 672 établissements | verified | INSEE Flores — caractéristiques des établissements fin 2022 | 2022 |
| microentreprises_france | ~4,8 M microentreprises (hors agricole/finance) | verified | INSEE Ésane — caractéristiques des entreprises par catégorie | 2023 |
| impact_defaut_suivi_contrats | ~9 % du résultat entreprise (citation marketing) | inferred | Oblige — blog gestion contrats TPE/PME | 2026 |
| reconduction_tacite_risque | Préavis et résiliation souvent manqués sans suivi structuré | inferred | TACIT — positionnement alertes reconduction tacite | 2026 |
| saas_sprawl_tpe | Multiplication abonnements SaaS par TPE (shadow IT) | estimated | Contexte sectoriel SaaS B2B; pas de série INSEE dédiée | 2026 |
| wtp_outil_rappels_contrats | €20–40/mo (hypothèse cible TPE) | unknown | Aucune validation studio | — |
| contrats_moyens_par_tpe | 15–40 contrats récurrents actifs | unknown | À valider en entretiens | — |

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| TACIT | CLM léger FR — upload PDF, extraction IA, alertes 90/30 j avant échéance | Focus reconduction tacite; hébergement UE; extraction auto dates/montants | Concurrent direct sur le wedge rappels; pricing non validé côté studio |
| Oblige | Gestion contrats TPE/PME FR — centralisation + rappels échéances | Positionné TPE; rappels agenda/smartphone | Moins connu que suites compta; différenciation coût annuel fournisseur non évidente |
| Angelaw | CLM FR tout-en-un (création, signature, suivi) | IA + modèles juridiques; hébergement France | Surdimensionné si besoin = rappels + inventaire; cycle de vie complet vs alertes |
| Iloh | CLM IA FR — alertes renouvellements et obligations | Workflows, assistant IA | Cible plutôt équipes juridiques / volumes élevés |
| Tomorro | CLM FR PME/ETI — création à archivage | Mature, conformité droit FR | PME+ ; onboarding lourd pour simple suivi renouvellements |
| Google Calendar / Outlook | Rappels manuels par contrat | Gratuit, familier | Pas de contexte contrat; perte si turnover; pas de rollup coûts |
| Spreadsheets (Excel/Sheets) | Tableau contrats + dates manuelles | Gratuit, flexible | Pas d'alertes fiables; saisie lourde; pas d'extraction PDF |
| Compta / ERP (Pennylane, Qonto, etc.) | Factures fournisseurs récurrentes visibles | Déjà utilisé; données paiement | Ne capture pas bail/assurance sans facture; pas préavis résiliation |
| Dossier email + Drive | Archivage ad hoc | Zéro coût | Recherche difficile; aucune alerte systématique |

### Initial Hypothesis

We believe French TPE owners and office managers (5–20 employees, no dedicated legal ops) will adopt a lightweight contract inventory with automated **90 / 30 / 7-day renewal reminders** and **annual spend rollup by vendor**, because tacit renewals and spreadsheet-based tracking create avoidable overspend and missed cancellation windows that full CLM suites feel too heavy to deploy.

### Open Questions

- [ ] Quel volume médian de contrats récurrents par TPE cible (assurance, bail, SaaS, maintenance) ?
- [ ] Les TPE paieront-elles un outil dédié alors que Calendar + Drive reste « suffisant » pour beaucoup ?
- [ ] Extraction PDF vs saisie manuelle : quel taux d'erreur acceptable avant perte de confiance ?
- [ ] Différenciation viable vs TACIT/Oblige sur le seul angle rappels + coût annuel fournisseur ?
- [ ] Acheteur économique : gérant, office manager, ou expert-comptable en recommandation ?
- [ ] Intégrations must-have : compta (Pennylane), banque (Qonto), ou standalone suffit ?
- [ ] Cette OPP est-elle un doublon portfolio une fois le smoke test terminé (suppression prévue) ?

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

<!-- Paste output from prompts/scoring.md. See playbooks/scoring-rules.md -->

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

## Final Decision

<!-- Paste output from prompts/portfolio-manager.md -->

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
