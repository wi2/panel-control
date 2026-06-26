---
id: OPP-20260626-relance-devis-freelance
title: "Relance devis freelance"
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
tags: [freelance, b2b, micro-saas]
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

# Relance devis freelance

**Wedge** : outil minimal — enregistrer un devis (montant, client, date d'envoi, date d'expiration), rappels email/Slack pour relancer, statuts (en attente, relancé, gagné, perdu, expiré), stats simples (taux de conversion, délai moyen de réponse) — pour **solo freelance FR/EU** sans suite CRM/compta lourde (~€9–19/mo, pas d'intégration compta au MVP).

---

## Discovery

### Problem Statement

French and EU **solo freelancers and very small agencies** (consultants, designers, developers, creative services) lose billable revenue when **sent quotes go cold** because follow-up is inconsistent. After sending a proposal, many track status in **Notion, Excel, or memory** — or forget entirely. There is no systematic **reminder before quote expiry**, no lightweight **conversion analytics** (win rate, average response delay), and follow-up competes with delivery work. Pain is **recurring** for anyone sending multiple quotes per month; cost is **lost margin on won-but-forgotten deals** and **lower win rate** from late or absent nudges. Urgency spikes **3–14 days after send** when prospects compare vendors or the validity window closes.

This is distinct from **invoice payment follow-up** (post-win cash collection): here the problem is **pre-contract commercial follow-up on quotes/proposals** still in decision.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| travailleurs_independants_urssaf | 4,8 M comptes TI fin 2024 | verified | Urssaf Stat Ur 409 | 2024 |
| independants_emploi_principal | 13,3 % personnes en emploi (emploi principal) | verified | INSEE — Statuts d'emploi | 2024 |
| independants_dirigeants | 4,4 M personnes dirigent une entreprise | verified | INSEE — Emploi et revenus des indépendants | 2022 |
| taux_conversion_devis_tpe_pme | 25–35 % (ordre de grandeur FR) | estimated | DevisTrack blog ; comparatifs sectoriels | 2026 |
| taux_conversion_devis_btp | 22–28 % moyenne ; +5–8 pts si relances systématiques | estimated | Payflo benchmark BTP | 2026 |
| pros_sans_relance | ~45–50 % ne relancent pas après envoi | estimated | relance-devis.fr (GrowthList relayé) ; blogs prospection | 2026 |
| devis_acceptes_apres_relance | ~60 % acceptés après relance (praticien web) | inferred | na-web.fr — retour freelance 400 devis | 2026 |
| relances_auto_lift_close | +10 % taux de clôture avec rappels automatisés | verified | Proposify — recherche 2025 (~1 M propositions) | 2025 |
| propositions_viewed_24h_win_rate | 43 % win rate si ouverture <24 h | verified | Proposify 2025 research cité Plutio | 2025 |
| software_proposals_close_rate | 36 % vs ~20 % moyenne industrie | verified | Proposify 2025 research cité Plutio | 2025 |
| wtp_hypothese | €9–19/mo outil dédié suivi devis | unknown | PR intake ; pas d'entretiens studio | — |
| calendar_free_alternative | Rappels Google/Outlook gratuits suffisants pour une partie de l'ICP | inferred | PR hypothèse à valider | 2026 |

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| Notion / Excel / Sheets | Suivi manuel statuts + dates | Gratuit, flexible | Pas de rappels natifs ; pas de stats conversion ; adoption faible |
| Google Calendar / Outlook reminders | Rappel ponctuel par devis | Gratuit, déjà utilisé | Pas de pipeline ; pas d'agrégats ; oubli si non configuré |
| Henrri / Indy / Tiime | Devis + facturation + relances email intégrées | Gratuit ou low-cost ; conforme FR | Relance = feature secondaire ; pas wedge stats/expiration dédié |
| Axonaut / Sellsy / Pennylane | CRM + devis + relances + pipeline | Suite complète, stats commerciales | Surdimensionné et €29+/mo ; pas micro-app solo |
| DevisTrack | Devis interactifs + CRM + notif ouverture + signature | Focus FR artisans/PME ; multi-canal | Produit devis complet, pas tracker minimal post-PDF |
| Relance+ | IA relance PDF devis existants | Spécialisé relance ; promesse +20 % signés | Devis restent hors outil ; pricing enterprise opaque |
| Proposify / PandaDoc / Better Proposals | Proposals web + analytics + auto-reminders | Tracking ouverture, relances, benchmarks | $19–49+/mo ; US-centric ; overkill si devis déjà faits ailleurs |
| SendQuote / Proposar | AI proposal + auto follow-up 3/7 j | Anti-ghosting, expiry countdown | Génération proposal incluse ; $29+/mo ; pas FR-first |
| Plutio / Bonsai / HoneyBook | All-in-one freelance OS | Proposals + PM + billing | €19–49+/mo ; remplace stack entier, pas wedge tracker |
| Make / Zapier DIY | Automatisation relance depuis facturation | Personnalisable | Setup technique ; pas produit self-serve ; maintenance |

### Initial Hypothesis

We believe **solo FR/EU freelancers** (consultants, devs, designers) sending **5–20 quotes per month** via email/PDF or lightweight invoicing tools will pay **€9–19/month** for a **minimal quote tracker** (register quote metadata, expiry, email/Slack reminders, status pipeline, conversion stats), because **manual Notion/Excel tracking and calendar hacks fail systematically**, **late follow-up loses deals before signature**, and **full proposal/CRM suites are priced and scoped for entire business management** — not a narrow pre-win follow-up wedge.

### Open Questions

- [ ] Fréquence réelle d'oubli de relance chez freelances dev/design vs. artisans BTP (devis déjà outillés via DevisTrack) ?
- [ ] Willingness to pay €9–19/mo vs. relances gratuites Henrri/Indy vs. rappels calendrier gratuits ?
- [ ] Part de l'ICP qui envoie des PDF depuis Word/Canva (besoin tracker pur) vs. devis natifs dans un logiciel existant ?
- [ ] Slack vs. email seul : valeur marginale pour solo freelance FR ?
- [ ] Chevauchement portfolio avec [OPP-20260625-relance-factures-freelance](../opportunities/OPP-20260625-relance-factures-freelance.md) — bundling « devis → facture » ou cannibalisation ?
- [ ] DevisTrack / Relance+ / incumbents facturation lancent-ils un tier « tracker seul » à ≤€15/mo ?

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
