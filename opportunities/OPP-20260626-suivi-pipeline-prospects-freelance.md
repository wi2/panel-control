---
id: OPP-20260626-suivi-pipeline-prospects-freelance
title: "Suivi pipeline prospects freelance"
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
tags: [freelance, b2b, micro-saas, crm]
automation_intake_at: 2026-06-26
micro_saas:
  decision: null
  msfi: null
  build_hours_estimate: null
  maintenance_hours_estimate: null
  mrr_target_12m: "144-228 EUR"
  wedge: "Kanban/liste à étapes fixes (contact → qualifié → brief → devis envoyé → gagné/perdu), rappels email/Slack si carte stagne >X jours, stats conversion par étape — solo freelance FR/EU 3–15 prospects actifs ; pas CRM lourd, pas compta au MVP"
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

# Suivi pipeline prospects freelance

**Wedge** : outil minimal type kanban/liste — étapes fixes (contact → qualifié → brief → devis envoyé → gagné / perdu), rappels automatiques email ou Slack quand une carte stagne plus de X jours, stats basiques (délai moyen par étape, taux de conversion) — pour **solo freelance FR/EU** avec 3–15 prospects actifs en parallèle (~€12–19/mo, saisie manuelle ou forward email au MVP, pas d'intégration compta).

---

## Discovery

### Problem Statement

French and EU **solo freelancers** (developers, designers, consultants, writers) juggling **3–15 active prospects** lose deals when **pre-quote commercial follow-up** is fragmented across **email, Notion, and memory**. After first contact or a discovery call, many fail to advance leads through **qualification, brief receipt, and timely quote send** — opportunities cool off, quotes go out late, and there is no simple view of **conversion by stage** or **average time stuck per step**. Pain is **recurring** during active prospecting cycles; cost is **lower win rate**, **delayed revenue**, and **mental load** from reconstructing status before each touchpoint. Urgency peaks **3–10 days after last contact** when competitors respond faster or the prospect deprioritizes the project.

This is distinct from **post-quote follow-up** ([OPP-20260626-relance-devis-freelance](../opportunities/OPP-20260626-relance-devis-freelance.md)): here the problem spans **first contact through quote send**, not nudging an already-sent proposal.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| travailleurs_independants_urssaf | 4,8 M comptes TI fin 2024 | verified | Urssaf Stat'Ur 409 | 2024 |
| independants_emploi_principal | 13,3 % personnes en emploi (emploi principal) | verified | INSEE — Statuts d'emploi | 2024 |
| icp_prospects_actifs | 3–15 prospects actifs en parallèle | inferred | PR intake | 2026 |
| notion_crm_freelance_adoption | 47 % freelances tech utilisent Notion comme CRM principal (FR) | estimated | Plateya blog citant étude Notion France 2025 | 2025 |
| notion_icp_volume | CRM Notion adapté à <50–100 leads actifs | inferred | Guide Productivité ; Creativ Conflans | 2026 |
| freelance_crm_pricing_band | €7–19/mo (Customermates, Workdeck) ; $9.99–19.99/mo (SoloPipeline) | verified | Sites produits | 2026 |
| all_in_one_freelance_pricing | €19–49/mo (Plutio, Bonsai, HoneyBook) | estimated | Comparatifs freelance CRM | 2026 |
| proposify_pipeline_velocity | +10 % taux de clôture avec rappels automatisés sur propositions | verified | Proposify research 2025 (~1 M propositions) | 2025 |
| wtp_hypothese | €12–19/mo outil pipeline dédié | unknown | PR intake ; pas d'entretiens studio | — |
| pain_vs_notion_gratuit | Douleur = suivi entre contact et devis, pas seulement relance post-envoi | inferred | PR intake hypothèse | 2026 |

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| Notion / Excel / Sheets | Pipeline DIY (base Opportunités + vue Board) | Gratuit si Notion déjà utilisé ; flexible | Pas de rappels natifs fiables ; setup manuel ; stats conversion à construire ; adoption faible |
| Trello / Asana | Kanban générique | Gratuit ou low-cost ; visuel | Pas de métriques conversion ; pas de rappels stagnation métier ; pas orienté freelance |
| Google Calendar / Outlook | Rappels ponctuels par prospect | Gratuit | Pas de pipeline ; pas d'agrégats ; oubli si non configuré |
| SoloPipeline | CRM pipeline freelance + AI proposals | $9.99–19.99/mo ; étapes + next actions ; focus solo | US-centric ; proposals AI inclus (scope plus large) ; jeune produit |
| Workdeck | Dashboard freelance + Kanban Lead→Won | $12/mo ; pipeline visuel ; AI proposals | Suite élargie (time, expenses) ; pas FR-first |
| freelanceOS | CRM freelance gratuit | Pipeline leads + projets + facturation ; flat free | Monétisation Premium floue ; pas wedge stagnation dédié |
| LancerWise | CRM freelance freemium | Kanban pipeline ; free tier 2 clients | Free limité ; suite all-in-one |
| Customermates | CRM open-source self-hostable | €7/mo ; Kanban pipeline ; n8n | Setup technique ; pas micro-app ultra-minimal |
| Plutio / Bonsai / HoneyBook | All-in-one freelance OS | Proposals + pipeline + billing intégrés | €19–49+/mo ; remplace stack entier, pas tracker étroit |
| HubSpot Free / Pipedrive | CRM sales généraliste | Enrichissement contacts ; pipelines natifs | Surdimensionné solo ; limites free HubSpot ; $14+/user Pipedrive |
| Streak / folk | CRM dans Gmail | Zero context switch email | US-centric ; pas stats étapes freelance FR |
| Make / Zapier + Notion | Automatisation relances stagnation | Personnalisable | Setup technique ; maintenance ; pas produit self-serve |
| [OPP-20260626-relance-devis-freelance](../opportunities/OPP-20260626-relance-devis-freelance.md) | Tracker post-envoi devis | Wedge étroit relance devis | Ne couvre pas contact→brief→devis ; chevauchement portfolio |

### Initial Hypothesis

We believe **solo FR/EU freelancers** (dev, design, conseil, rédaction) with **3–15 active prospects** will pay **€12–19/month** for a **minimal fixed-stage pipeline** (contact → qualifié → brief → devis envoyé → gagné/perdu) with **email or Slack stagnation reminders** and **basic stage conversion stats**, because **Notion/Excel/memory tracking fails between first contact and quote send**, **deals cool without structured nudges**, and **all-in-one freelance suites ($19–49/mo) or generic kanban tools lack purpose-built stagnation alerts and conversion metrics** — while post-quote tools like [relance devis](../opportunities/OPP-20260626-relance-devis-freelance.md) address a later funnel step only.

### Open Questions

- [ ] La douleur est-elle réellement **pré-devis** (contact→brief→devis) vs. post-devis déjà couverte par relance-devis — ou les freelances perçoivent-ils un seul problème « suivi commercial » ?
- [ ] Willingness to pay €12–19/mo vs. Notion gratuit + Make vs. SoloPipeline/Workdeck à $10–12/mo ?
- [ ] Quelle part de l'ICP utilise déjà un all-in-one (Plutio/Bonsai) avec pipeline natif — et refuserait un second outil ?
- [ ] Email seul vs. Slack : valeur marginale des rappels Slack pour solo freelance FR ?
- [ ] Saisie manuelle vs. forward email : quel taux d'adoption sans intégration calendrier bidirectionnelle ?
- [ ] Bundling avec [OPP-20260626-relance-devis-freelance](../opportunities/OPP-20260626-relance-devis-freelance.md) en produit unique « funnel commercial freelance » ou deux wedges distincts ?
- [ ] SoloPipeline / freelanceOS / incumbents lancent-ils un tier « pipeline seul » ≤€15/mo sans proposals/billing ?

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
