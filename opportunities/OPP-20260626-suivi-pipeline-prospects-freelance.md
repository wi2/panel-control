---
id: OPP-20260626-suivi-pipeline-prospects-freelance
title: "Suivi pipeline prospects freelance"
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
next_review_action: null
created: 2026-06-26
updated: 2026-06-26
owner: studio-team
tags: [freelance, b2b, micro-saas, crm]
automation_intake_at: 2026-06-26
micro_saas:
  decision: MONITOR_MICRO
  msfi: 58.7
  build_hours_estimate: 80
  maintenance_hours_estimate: 5
  mrr_target_12m: "500-1200 EUR"
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

**desk-only**: true — live customer experiments (interviews, landing, concierge) are **planned** for sprint validation; one desk audit completed. BUILD_MICRO requires live validation before promotion. See [validation.md](../playbooks/validation.md).

### Experiments

| # | Experiment | Hypothesis | Method | Success Criteria | Status |
|---|------------|------------|--------|------------------|--------|
| 1 | Competitive & pain-signal audit | Solo FR/EU freelancers lose deals when pre-quote pipeline (contact→brief→devis) is fragmented across Notion/email/memory; incumbents are over-scoped or lack FR-first pipeline-only wedge with stagnation alerts + stage conversion stats | Desk research: incumbent pricing/features (SoloPipeline, Workdeck, freelanceOS, Plutio/Bonsai), portfolio overlap vs [OPP-20260626-relance-devis-freelance](../opportunities/OPP-20260626-relance-devis-freelance.md), pre-quote timing benchmarks | ≥3 verified sources confirm quote-timing / follow-up lift applies upstream of quote send; no ≤€15/mo FR-first pipeline-only incumbent without proposals/billing bundle; wedge distinct from post-quote relance-devis | completed |
| 2 | Problem interviews | Solo FR freelancers (dev/design/consulting) lose ≥1 prospect/quarter between first contact and quote send due to lack of structured pipeline | 8 entretiens (Malt, LinkedIn, CPM) | ≥5/8 confirment oubli/stagnation pré-devis + citent Notion/Excel/calendrier insuffisants | planned |
| 3 | WTP landing page | Demande €12–19/mo pour tracker pipeline minimal (étapes fixes + rappels stagnation, sans génération devis) | Landing FR + Van Westendorp ; €200 ads Meta/LinkedIn freelance | ≥25 signups ; ≥25 % acceptent ≥€12/mo | planned |
| 4 | Concierge pipeline tracker | Kanban manuel (contact→qualifié→brief→devis envoyé→gagné/perdu) + rappels email si carte stagne >5 jours réduit prospects « perdus en route » | 10 freelances, suivi Notion/Sheet + rappels manuels, 4 sem, 3+ prospects chacun | ≥7/10 NPS ≥8 ; ≥5 citent prospect oublié/avancé trop tard sans concierge | planned |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| solopipeline_pricing | $9.99–19.99/mo (Pro/Advanced) ; free tier ≤20 leads | verified | SoloPipeline pricing page | 2026 |
| workdeck_pricing | $12/mo ($120/yr) ; Kanban Lead→Won + AI proposals suite | verified | Workdeck pricing page | 2026 |
| freelanceos_pricing | Free (leads, pipeline, invoicing) ; Premium flou | verified | freelanceOS site | 2026 |
| moxie_all_in_one_floor | $10/mo annual Solo ; CRM pipeline + proposals + billing | verified | Moxie review / pricing compare 2026 | 2026 |
| plutio_bonsai_floor | €19–49/mo all-in-one freelance OS | estimated | Discovery competitor table ; comparatifs 2026 | 2026 |
| stale_deal_alerts_incumbent | WhizziQ alerte deals quiet 14+ jours ; SoloPipeline next actions + reminders ; Crmzix stale-deal detection | verified | WhizziQ ; SoloPipeline ; Crmzix product pages | 2026 |
| proposal_timing_lift | Proposals sent within 24–48 h of discovery close at significantly higher rates ; decline after 72 h | verified | Pitchsite win-rate benchmarks 2026 ; Waco3 proposal benchmarks | 2026 |
| pre_quote_qualification_lift | Pre-proposal qualification step moves win rate +10–15 pts | estimated | Waco3 — freelance proposal benchmarks | 2026 |
| followup_consistency_lift | 3-touch follow-up over 3 weeks adds +10–20 % close on fence proposals | estimated | Waco3 ; Proposify 2025 (post-quote, analogous cadence) | 2025 |
| notion_crm_substitute | 47 % freelances tech FR utilisent Notion comme CRM principal | estimated | Discovery — Plateya / Notion France 2025 | 2025 |
| pipeline_only_gap | Aucun tier FR-first ≤€15/mo « pipeline seul » sans proposals/billing/AI bundle identifié (SoloPipeline/Workdeck incluent proposals AI) | estimated | Desk audit concurrentiel ; Discovery | 2026 |
| portfolio_wedge_overlap | Pre-quote pipeline (contact→devis) chevauche partiellement post-quote relance-devis ; bundling « funnel commercial freelance » possible | inferred | PR intake ; [OPP-20260626-relance-devis-freelance](../opportunities/OPP-20260626-relance-devis-freelance.md) (MONITOR_MICRO, desk-only) | 2026 |
| pre_quote_pain_live | — | unknown | Pas d'entretiens studio (exp. 2 planned) | — |
| wtp_signal_live | — | unknown | Pas de landing / LOI (exp. 3 planned) | — |
| concierge_usefulness | — | unknown | Pas de concierge (exp. 4 planned) | — |

### Kill / Continue Signals

- **Continue if**: ≥5/8 entretiens confirment stagnation/oubli **pré-devis** (contact→brief→devis) + insuffisance Notion/calendrier ; ≥25 signups landing avec ≥25 % WTP ≥€12/mo ; concierge NPS ≥8 pour ≥7/10 ; ICP confirme 3–15 prospects actifs ; aucun incumbent ne lance tier pipeline-only ≤€15/mo FR-first avec stats conversion par étape
- **Kill if**: ≥6/8 disent Notion/Trello/calendrier ou all-in-one (Plutio/Bonsai/Moxie) suffisent ; 0 signup après €200 ads ; ≥4/8 n'ont <3 prospects actifs en parallèle ; SoloPipeline/Workdeck/freelanceOS lance tier pipeline seul ≤€12/mo FR-first avec rappels stagnation natifs ; douleur perçue = un seul problème déjà couvert par relance-devis sans valeur pré-devis distincte

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

**Wedge scope**: Kanban/liste à étapes fixes (contact → qualifié → brief → devis envoyé → gagné/perdu), rappels email/Slack si carte stagne >X jours, stats conversion par étape — pour **solo freelance FR/EU** avec 3–15 prospects actifs (~€12–19/mo). **Hors scope** : génération de devis/PDF, facturation, intégration compta, CRM multi-utilisateur agence, intégrations calendrier bidirectionnelles au MVP.

### Hard Gates

| Gate | Threshold | Estimate | Result |
|------|-----------|----------|--------|
| build_hours | ≤ 100 h | 80 h | PASS |
| maintenance_hours | ≤ 10 h/mo | 5 h/mo | PASS |
| solo_operable | Yes | Yes | PASS |
| monthly_revenue_potential | ≥ 500 €/mo | 750 €/mo (50×€15) | PASS |
| distribution_cost | ≤ 7 | 3 (channel: communities) | PASS |
| platform / ToS | see playbook | tos low ; user-owned data | PASS |

**Gate evidence**

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| build_hours_mvp | 80 h (kanban étapes fixes, moteur stagnation, rappels email/Slack, stats conversion, auth, billing Stripe, deploy) | estimated | Scope wedge Discovery ; comparable relance-devis 78 h | 2026-06-26 |
| maintenance_m6 | 5 h/mo (support solo, monitoring envoi email/Slack, bugfixes) | estimated | Pas d'intégration compta ; données user-owned ; pas de refresh données tierces | 2026-06-26 |
| mrr_ceiling_wedge | 750 €/mo = 50 clients × €15/mo | estimated | ICP 4,8 M TI Urssaf ; wedge étroit pipeline seul ; ARPU €12–19 hyp. Discovery | 2026-06-26 |
| distribution_primary | Groupes Facebook/Malt freelance FR + contenu SEO « pipeline freelance » / « CRM minimal freelance » | inferred | Validation exp. 2–3 canaux ; coût map communities=3 | 2026-06-26 |
| pipeline_only_gap | Aucun tier FR-first ≤€15/mo « pipeline seul » sans proposals/billing/AI bundle identifié | estimated | Validation desk audit #1 ; SoloPipeline/Workdeck incluent proposals AI | 2026-06-26 |

### Platform Risk

| Field | Value | Notes |
|-------|-------|-------|
| tos_risk | low | Données prospects saisies par l'utilisateur ou forward email ; pas de scrape réseaux sociaux |
| regulatory_risk | low | Suivi commercial pré-contrat ; pas de données réglementées |
| platform_dependency | low | Email (Brevo/Resend) + Slack API optionnelle ; pas de dépendance plateforme tierce pour données core |
| alternative_data_source | true | Métadonnées prospects entièrement user-owned ; export CSV |

### MSFI v2

| Component | Score | Rationale |
|-----------|-------|-----------|
| time_to_revenue_score | 50 | 75 j (landing + outreach communities freelance + 1er payant) — bande 61–120 j |
| automation_score | 86 | Rappels stagnation + stats conversion automatisés ; saisie self-serve kanban |
| maintenance_sustainability_score | 80 | 5 h/mo estimé ; pas d'intégration compta ; support solo léger |
| acquisition_score | 52 | Communities/SEO freelance faisable solo mais lent ; pas d'audience studio ; concurrence contenu CRM freelance |
| wedge_local_score | 66 | Wedge FR-first pipeline solo pré-devis ; niche métier claire mais pas hyper-local géo |
| competition_score | 52 | SoloPipeline/Workdeck $10–12, freelanceOS gratuit, Notion 47 % ICP — pression plus forte que tracker post-devis seul |
| pricing_power_score | 32 | WTP unknown ; Notion gratuit + SoloPipeline $9.99 ancrent le bas ; all-in-one €19–49 couvre pipeline natif |
| **MSFI** | **58.7** | |

MSFI calc: `0.15×50 + 0.15×86 + 0.10×80 + 0.15×52 + 0.15×66 + 0.15×52 + 0.15×32 = 58.7`

**Provisional decision**: MONITOR_MICRO — all hard gates PASS ; MSFI 58.7 in 50–69 band ; desk-only Validation (`desk-only: true`, confidence low) blocks BUILD_MICRO until live sprint (entretiens + landing + concierge). Chevauchement partiel avec [OPP-20260626-relance-devis-freelance](../opportunities/OPP-20260626-relance-devis-freelance.md) — bundling « funnel commercial freelance » à trancher en sprint.

**confidence_level**: medium

---

## Final Decision (Micro SaaS)

| Field | Value |
|-------|-------|
| **Primary Decision** | MONITOR_MICRO |
| **MSFI** | 58.7 |
| **capacity_blocked** | false |
| **Date** | 2026-06-26 |
| **Rationale** | All six hard gates PASS (build 80 h, maint 5 h/mo, solo operable, MRR 750 €/mo, distribution_cost 3, ToS low). MSFI 58.7 in MONITOR band (50–69). Desk-only Validation (`desk-only: true`, confidence low) blocks BUILD_MICRO per playbook — no live interviews, landing, or concierge yet. Pipeline-only wedge gap documented (Validation #1) but WTP unknown; Notion (47 % ICP) + SoloPipeline $9.99 + all-in-one €19–49 anchor pricing down. Partial overlap with [OPP-20260626-relance-devis-freelance](../opportunities/OPP-20260626-relance-devis-freelance.md) — bundling « funnel commercial freelance » to resolve in sprint. BUILD capacity open (0 BUILD_MICRO active) but MONITOR queue exceeds cap (6/5 after this entry) — sprint validation prioritized; not KILL because MSFI ≥50 and planned experiments address distinct pre-quote pain. |

### Expected Learnings

- [ ] Topic: pre_quote_pipeline_pain — Method: 8 entretiens freelances FR (Malt, LinkedIn, CPM) — Applies to: MONITOR_MICRO, KILL_MICRO
- [ ] Topic: willingness_to_pay — Method: Landing Van Westendorp €12–19/mo + €200 ads Meta/LinkedIn — Applies to: MONITOR_MICRO, BUILD_MICRO
- [ ] Topic: incumbent_sufficiency — Method: 8 interviews Notion/Trello/SoloPipeline vs pipeline-only tracker — Applies to: KILL_MICRO
- [ ] Topic: concierge_usefulness — Method: Concierge kanban pipeline 10 freelances 4 sem (stagnation >5 j) — Applies to: MONITOR_MICRO, BUILD_MICRO
- [ ] Topic: wedge_bundling — Method: Compare pre-quote vs post-quote pain signals vs relance-devis — Applies to: MONITOR_MICRO, KILL_MICRO

### Next Actions

- [ ] Publier landing FR « pipeline prospects freelance » + waitlist — deadline 2026-07-15
- [ ] 8 entretiens freelances dev/design/consulting (stagnation pré-devis) — deadline 2026-07-20
- [ ] Concierge pipeline tracker 10 freelances 4 semaines — deadline 2026-07-25
- [ ] Trancher bundling vs relance-devis ; re-calculer MSFI — deadline 2026-07-26

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
