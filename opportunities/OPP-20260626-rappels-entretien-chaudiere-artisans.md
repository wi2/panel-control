---
id: OPP-20260626-rappels-entretien-chaudiere-artisans
title: "Rappels entretien chaudière pour chauffagistes indépendants"
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
pipeline_stage: validation
next_review_action: null
created: 2026-06-26
updated: 2026-06-26
owner: studio-team
tags: [b2b, saas, france, btp, chauffage, micro-saas]
automation_intake_at: 2026-06-26
micro_saas:
  decision: null
  msfi: null
  build_hours_estimate: null
  maintenance_hours_estimate: null
  mrr_target_12m: ""
  wedge: "Rappels contrats entretien chaudière — 1 dept, TPE sans ERP"
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

# Rappels entretien chaudière pour chauffagistes indépendants

Intake completed 2026-06-26. Desk discovery only — no live validation yet. Wedge: lightweight client + contract tracking with automatic email/SMS reminders 30/7 days before mandatory annual boiler maintenance, for solo/TPE heating contractors without heavy ERP.

---

## Discovery

### Problem Statement

French **plombiers-chauffagistes** and **chauffagistes TPE** (1–5 employees, often owner-operators) must schedule **mandatory annual maintenance visits** for client boilers and heat pumps (4–400 kW) under maintenance contracts. Each missed appointment means **lost recurring revenue** (typical visit €80–150) and weakens client retention, while the artisan remains exposed if clients lack valid maintenance attestations (décret 2009-649).

Today most track due dates in **paper agendas**, **Google Calendar**, or **post-its** — with no centralized client list, no automated client reminders, and no team visibility when the owner is on site. Without a dedicated secretary, follow-up falls through during peak season (October–February). Pain is **recurrent** (every contract, every year), **moderately urgent** (revenue + relationship risk), and **operationally frequent** for artisans holding 50–200 active maintenance contracts.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| entretien_annuel_obligatoire | Chaudières 4–400 kW, chaque année civile | verified | Décret n° 2009-649 ; [ecologie.gouv.fr](https://www.ecologie.gouv.fr/politiques-publiques/entretien-inspection-systemes-chauffage-climatisation) | 2009 |
| attestation_conservation | Attestation sous 15 j ; conservation ≥ 2 ans | verified | Code de l'environnement R.224-41-7 | 2009 |
| etablissements_plomberie_chauffage | ~73 000 établissements | verified | Observatoire métiers BTP — NAF 43.22A/B | 2021 |
| part_tpe_secteur | ~94 % < 10 salariés ; ~60 % micro sans salarié | verified | [Le Bâtiment Performant](https://lebatimentperformant.fr/actualites/le-poids-des-tpe-dans-la-plomberie-et-le-chauffage/1/6303) | 2021 |
| croissance_chauffagistes | +22 % établissements chauffage 2017–2021 | verified | Observatoire métiers BTP | 2021 |
| contrat_entretien_non_obligatoire | Visite annuelle obligatoire ; contrat formel optionnel | verified | [Garanka — guide entretien](https://www.garanka.fr/assurance-entretien-chaudiere/) | 2025 |
| tarif_visite_entretien | €80–150 / visite | inferred | Intake PR + études marché chauffagiste | 2026 |
| contrats_actifs_icp | 50–200 contrats entretien | inferred | Intake PR (ICP cible) | 2026 |
| wtp_outil_leger | €9–19/mo hypothèse studio | unknown | Pas d'entretiens ; à valider | — |
| transition_pac | Entretien PAC compense baisse chaudières fioul/gaz | estimated | [Cerfrance — chiffres clés 2024-2025](https://www.cerfrance.fr/actualites/les-chiffres-cles-de-la-plomberie-du-chauffage-en-2024-2025) | 2025 |

> **Evidence** (verified): Décret 2009-649 creates recurring annual demand for qualified heating professionals — every maintained installation generates at least one billable visit per civil year.

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| Google Calendar / iPhone Reminders | Rappels manuels par client | Gratuit, familier | Pas de liste clients centralisée ; pas de relance client auto ; oublis en saison |
| Excel / cahier papier | Suivi artisanal des échéances | Gratuit, offline | Pas d'alertes SMS/email ; pas de partage équipe ; saisie répétitive |
| Batappli | ERP artisan devis/factures + module contrats | Rappels contrats d'entretien ; SMS client ([blog Batappli](https://www.batappli.fr/blog-du-logiciel-batiment/plombiers-chauffagistes-comment-suivre-ses-contrats-d-entretien)) | €39–119 HT/mo ; surdimensionné si seul besoin = rappels entretien |
| Obat / Tolteck / HERO | ERP BTP généraliste | Suite métier intégrée | €50–150/mo ; courbe d'apprentissage ; pas wedge rappels seuls |
| ChaudièrePro | Logiciel spécialisé CVC + attestations réglementaires | Attestations décret 2009-649 ; relances J-60/30/7 ; CERFA 15497 | Prix plus élevé ; orienté conformité doc, pas micro-TPE minimaliste |
| Mediabat / Mobil outils | Modules entretien optionnels | Intégré écosystème métier | Module payant ; complexité ERP |
| Secrétaire / conjoint | Relance téléphonique manuelle | Relationnel | Coût implicite ; non scalable pour ICP solo |

### Initial Hypothesis

We believe **chauffagistes indépendants et TPE** (1–5 salariés, 50–200 contrats entretien actifs) in **one French département** will pay **€9–19/month** for **centralized client + contract tracking** with **automatic email/SMS reminders** to both artisan and end-client at 30/7 days before annual maintenance due dates, because **mandatory annual visits create predictable recurring revenue**, **generic calendars lack client-level contract history**, and **full ERP tools (Batappli, Obat) are overpriced** for a single scheduling pain point.

### Open Questions

- [ ] Les chauffagistes TPE paient-ils un outil dédié alors que Calendar gratuit existe ?
- [ ] Quel % oublie ou reporte des entretiens contractuels par an (perte revenu mesurable) ?
- [ ] Rappels **client** (SMS/email) vs rappels **artisan** seul — quel levier convertit le plus ?
- [ ] SEO local (« rappel entretien chaudière artisan ») suffit-il sans audience fondateur ?
- [ ] ARPU €9–19/mo viable vs Batappli Devis à partir de €39 HT/mo ?
- [ ] Extension PAC/climatisation change-t-elle la douleur ou le WTP vs chaudières gaz/fioul ?

**confidence_level**: medium

---

## Validation

Desk evaluation only. **desk-only**: true — CP — Eval automation run; live artisan experiments below are **planned**, not executed. One completed internal desk audit satisfies the desk-only fast path per [validation.md](../playbooks/validation.md).

### Experiments

| # | Experiment | Hypothesis | Method | Success Criteria | Status |
|---|------------|------------|--------|------------------|--------|
| 0 | Competitive pricing & feature-gap desk audit | Full ERPs (Batappli, ChaudièrePro) are overpriced or over-scoped vs a €9–19/mo rappels-only wedge | Desk research: public pricing pages, ChaudièrePro 2026 comparatif, Batappli blog contrats entretien | ≥2 incumbents priced ≥€39/mo for entretien+rappels ; no standalone €9–19 rappels-only SKU found | **completed** |
| 1 | Problem interviews | Chauffagistes TPE oublient ≥5 % entretiens contractuels/saison | 8 entretiens via CMA/chambre métiers (1 dept cible) | ≥5/8 confirment oublis récurrents + citent revenu perdu | planned |
| 2 | WTP landing | Demande à €9–19/mo pour rappels client+artisan | Landing FR + Van Westendorp ; €150 ads Meta artisans chauffage | ≥20 signups ; ≥25 % acceptent ≥€9/mo | planned |
| 3 | Concierge rappels | Rappels SMS/email J-30/J-7 réduisent oublis vs Calendar seul | 10 artisans, suivi manuel 4 semaines (peak season) | ≥7/10 NPS ≥8 ; ≥3 citent RDV sauvé sans relance manuelle | planned |
| 4 | Calendar sufficiency | Calendar/iPhone suffit sans outil dédié | 8 interviews usage actuel | ≤3/8 disent Calendar suffit pour 50+ contrats | planned |

### Results

**Experiment 0 (completed)** — Competitive desk audit (2026-06-26):

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| batappli_artisan_prix | 79 € HT/mo (contrats entretien + SMS relance) | verified | [Batappli tarifs](https://www.batappli.fr/tarifs) ; [blog contrats entretien](https://www.batappli.fr/blog-du-logiciel-batiment/plombiers-chauffagistes-comment-suivre-ses-contrats-d-entretien) | 2026-06 |
| chaudierepro_standard_prix | Freemium 0 € (15 clients) ; Standard 39 €/mo (29 €/mo annuel) ; relances J-60/30/7 | verified | [ChaudièrePro comparatif 2026](https://chaudierepro.com/meilleur-logiciel-chauffagiste) | 2026-06 |
| standalone_rappels_sku | Aucun concurrent identifié à €9–19/mo rappels-only sans ERP | inferred | Audit 9 solutions comparatif ChaudièrePro ; BatUp/ArtisanPro dès ~15–29 €/mo avec devis+factures | 2026-06 |
| entretien_obligatoire_demande | Entretien annuel obligatoire chaudières 4–400 kW | verified | Décret 2009-649 ; [ecologie.gouv.fr](https://www.ecologie.gouv.fr/politiques-publiques/entretien-inspection-systemes-chauffage-climatisation) | 2009 |
| contrats_rentabilite_solo | 80–150 visites entretien/an ; CA récurrent 12–22 k€/an | estimated | [Artisan Rentable — chauffagiste](https://artisanrentable.fr/metier/chauffagiste-independant) | 2026 |
| seuil_outil_numerique | À partir de ~20 contrats, logiciel recommandé pour éviter oublis | inferred | [Adler Technologies — contrat entretien](https://www.adlertechnologies.eu/blog-contrat-entretien-chauffagiste) | 2026 |
| pain_confirmation | — | unknown | Pas d'entretiens studio | — |
| wtp_signal | — | unknown | Pas de landing / LOI | — |
| concierge_usefulness | — | unknown | Pas de concierge | — |
| calendar_sufficiency | — | unknown | Pas d'interviews usage | — |

**Desk audit conclusion**: Regulatory demand is verified and recurring. Incumbent solutions bundle rappels into ERP/CVC suites at **€39–79+/mo** (ChaudièrePro Standard 39 €, Batappli Artisan 79 € HT). A **narrow wedge** (client list + contract dates + email/SMS rappels only) at **€9–19/mo** is **not disproven** by desk research — but **WTP and Calendar sufficiency remain unvalidated** without live experiments. ChaudièrePro Freemium (15 clients) is a **direct substitute risk** for micro-TPE before paid conversion.

### Kill / Continue Signals

- **Continue if**: ≥5/8 entretiens confirment oublis saisonniers ; ≥3 pré-commandes ou LOI à €9+/mo ; concierge NPS ≥8 pour ≥7/10 ; ≤3/8 disent Calendar suffit à 50+ contrats
- **Kill if**: ≥5/8 disent Calendar + ChaudièrePro gratuit suffisent ; 0 signup après €150 ads ; ARPU viable <€7/mo ; ≥6/8 refusent payer pour rappels seuls

**confidence_level**: low

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
