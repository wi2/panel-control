---
id: OPP-20260626-relance-devis-freelance
title: "Relance devis freelance"
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
next_review_action: "2026-07-26 — re-run validation sprint (interviews + landing + concierge); promote BUILD_MICRO if MSFI ≥70 + live signal"
created: 2026-06-26
updated: 2026-06-26
owner: studio-team
tags: [freelance, b2b, micro-saas]
automation_intake_at: 2026-06-26
micro_saas:
  decision: MONITOR_MICRO
  msfi: 60.9
  build_hours_estimate: 78
  maintenance_hours_estimate: 5
  mrr_target_12m: "500-1200 EUR"
  wedge: "Minimal quote tracker — register quote metadata (amount, client, send/expiry dates), email/Slack reminders (J+3/J+7/J+14 + pre-expiry), status pipeline (pending, nudged, won, lost, expired), conversion stats — solo FR/EU freelancer; no quote generation, invoicing, or CRM"
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

**desk-only**: true — live customer experiments (interviews, landing, concierge) are **planned** for sprint validation; one desk audit completed. BUILD_MICRO requires live validation before promotion. See [validation.md](../playbooks/validation.md).

### Experiments

| # | Experiment | Hypothesis | Method | Success Criteria | Status |
|---|------------|------------|--------|------------------|--------|
| 1 | Competitive & pain-signal audit | Solo freelancers lose deals from absent quote follow-up; incumbents are over-scoped/expensive for tracker-only wedge | Desk research: FR/US benchmarks, incumbent pricing, portfolio overlap vs [OPP-20260625-relance-factures-freelance](../opportunities/OPP-20260625-relance-factures-freelance.md) | ≥3 verified sources confirm follow-up lift; no ≤€15/mo FR-first tracker-only incumbent; wedge distinct from invoice relance | completed |
| 2 | Problem interviews | Solo FR freelancers (dev/design/consulting) forget quote follow-up ≥1×/month | 8 entretiens (Malt, LinkedIn, CPM) | ≥5/8 confirment oubli/retard relance + citent Notion/Excel/calendrier | planned |
| 3 | WTP landing page | Demande €9–19/mo pour tracker devis minimal (sans génération devis) | Landing FR + Van Westendorp ; €200 ads Meta/LinkedIn freelance | ≥25 signups ; ≥25 % acceptent ≥€9/mo | planned |
| 4 | Concierge quote tracker | Rappels J+3/J+7/J+14 + alerte expiration réduisent devis expirés sans signature | 10 freelances, suivi manuel 4 sem, 3+ devis chacun | ≥7/10 NPS ≥8 ; ≥5 citent devis oublié/expiré sans concierge | planned |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| devis_signed_after_followup | 44 % des devis signés après ≥1 relance | verified | lefreelance.fr — article relance freelance 2026 | 2026 |
| followup_required_b2b | 80 % des ventes B2B nécessitent ≥5 points de contact ; 48 % des reps abandonnent avant 2e relance | verified | Propal.io citant étude Uptoo | 2026 |
| structured_followup_lift | +15–30 pts taux transformation avec séquence structurée | estimated | DevisTrack blog ; PromptConsulting cadence 7-14-30 | 2026 |
| cadence_7_14_30_lift | 22 % → 34 % signature (médiane PME) avec cadence automatisée | estimated | PromptConsulting — déploiements 18 mois | 2025 |
| automated_reminders_lift | +10 % close rate avec rappels automatisés | verified | Proposify State of Proposals 2025 (~1 M propositions) | 2025 |
| auto_reminder_adoption | 7 % seulement des vendeurs activent rappels auto | verified | Proposify 2025 report | 2025 |
| btp_systematic_followup_lift | +5–8 pts conversion si relances systématiques | estimated | Payflo benchmark BTP 2026 (15 000+ devis) | 2026 |
| incumbent_all_in_one_floor | €19–49/mo (Bonsai Starter ~$19 ; HoneyBook Essentials ~$39–49 pour automation) | verified | HoneyBook / Bonsai pricing pages ; Plutio compare 2026 | 2026 |
| free_incumbent_relance | Henrri/Indy/Tiime incluent relances email devis/facture gratuites ou low-cost | inferred | Discovery competitor table ; pas d'entretiens ICP | 2026 |
| calendar_sufficient_subset | Partie ICP peut utiliser rappels Google/Outlook sans payer outil dédié | inferred | PR hypothèse Discovery ; à tester exp. 2 | 2026 |
| portfolio_wedge_distinct | Devis pre-win ≠ relance facture post-win ; OPP factures archivée KILL_MICRO (mrr-below-minimum) | verified | [OPP-20260625-relance-factures-freelance](../opportunities/OPP-20260625-relance-factures-freelance.md) | 2026 |
| tracker_only_incumbent_gap | Aucun tier FR-first ≤€15/mo « tracker seul » identifié (DevisTrack/Relance+ = devis complet ou enterprise) | estimated | Discovery + audit concurrentiel desk | 2026 |
| pain_confirmation_live | — | unknown | Pas d'entretiens studio (exp. 2 planned) | — |
| wtp_signal_live | — | unknown | Pas de landing / LOI (exp. 3 planned) | — |
| concierge_usefulness | — | unknown | Pas de concierge (exp. 4 planned) | — |

### Kill / Continue Signals

- **Continue if**: ≥5/8 entretiens confirment oubli relance devis + insuffisance Notion/calendrier ; ≥25 signups landing avec ≥25 % WTP ≥€9/mo ; concierge NPS ≥8 pour ≥7/10 ; aucun incumbent ne lance tier tracker ≤€15/mo FR-first
- **Kill if**: ≥6/8 disent Henrri/Indy/calendrier suffisent ; 0 signup après €200 ads ; ≥4/8 n'envoient <3 devis/mo ; DevisTrack ou facturation FR lance tracker seul ≤€12/mo avec stats conversion ; chevauchement bundling rend wedge indifférencié vs suite existante

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

**Wedge scope**: Enregistrer un devis (montant, client, date d'envoi, date d'expiration), rappels email/Slack (J+3/J+7/J+14 + alerte pré-expiration), statuts (en attente, relancé, gagné, perdu, expiré), stats simples (taux de conversion, délai moyen de réponse) — pour **solo freelance FR/EU** (~€9–19/mo). **Hors scope** : génération de devis/PDF, facturation, intégration compta, CRM/pipeline commercial complet, multi-utilisateur agence.

### Hard Gates

| Gate | Threshold | Estimate | Result |
|------|-----------|----------|--------|
| build_hours | ≤ 100 h | 78 h | PASS |
| maintenance_hours | ≤ 10 h/mo | 5 h/mo | PASS |
| solo_operable | Yes | Yes | PASS |
| monthly_revenue_potential | ≥ 500 €/mo | 750 €/mo (50×€15) | PASS |
| distribution_cost | ≤ 7 | 3 (channel: communities) | PASS |
| platform / ToS | see playbook | tos low ; user-owned data | PASS |

**Gate evidence**

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| build_hours_mvp | 78 h (CRUD devis, moteur rappels email/Slack, pipeline statuts, stats conversion, auth, billing Stripe, deploy) | estimated | Scope wedge Discovery ; stack SaaS standard comparable wedges MONITOR | 2026-06-26 |
| maintenance_m6 | 5 h/mo (support solo, monitoring envoi email, bugfixes) | estimated | Pas d'intégration compta ; données user-owned ; comparable suivi-conformite 4 h/mo | 2026-06-26 |
| mrr_ceiling_wedge | 750 €/mo = 50 clients × €15/mo | estimated | ICP 4,8 M TI Urssaf ; wedge étroit tracker seul ; ARPU €9–19 hyp. Discovery | 2026-06-26 |
| distribution_primary | Groupes Facebook/Malt freelance FR + contenu SEO « relance devis freelance » | inferred | Validation exp. 2–3 canaux ; coût map communities=3 | 2026-06-26 |
| tracker_only_gap | Aucun tier FR-first ≤€15/mo tracker seul identifié | estimated | Validation desk audit #1 ; DevisTrack/Relance+ = devis complet ou enterprise | 2026-06-26 |

### Platform Risk

| Field | Value | Notes |
|-------|-------|-------|
| tos_risk | low | Données devis saisies par l'utilisateur ; pas de scrape réseaux sociaux |
| regulatory_risk | low | Suivi commercial pré-contrat ; pas de données réglementées |
| platform_dependency | low | Email (Brevo/Resend) + Slack API optionnelle ; pas de dépendance plateforme tierce pour données core |
| alternative_data_source | true | Métadonnées devis entièrement user-owned ; export CSV |

### MSFI v2

| Component | Score | Rationale |
|-----------|-------|-----------|
| time_to_revenue_score | 50 | 75 j (landing + outreach communities freelance + 1er payant) — bande 61–120 j |
| automation_score | 88 | Rappels J+3/J+7/J+14 + alerte expiration automatisés ; saisie self-serve |
| maintenance_sustainability_score | 82 | 5 h/mo estimé ; pas d'intégration compta ; support solo léger |
| acquisition_score | 52 | Communities/SEO freelance faisable solo mais lent ; pas d'audience studio ; concurrence contenu relance |
| wedge_local_score | 68 | Wedge FR-first tracker devis solo ; pas hyper-local géo mais niche métier claire |
| competition_score | 58 | Gap tracker seul documenté (Validation #1) ; pression Henrri/Indy gratuits et suites all-in-one |
| pricing_power_score | 35 | WTP unknown ; Henrri/Indy relances gratuites + rappels calendrier ancrent le bas |
| **MSFI** | **60.9** | |

MSFI calc: `0.15×50 + 0.15×88 + 0.10×82 + 0.15×52 + 0.15×68 + 0.15×58 + 0.15×35 = 60.9`

**Provisional decision**: MONITOR_MICRO — all hard gates PASS ; MSFI 60.9 in 50–69 band ; desk-only Validation (`desk-only: true`, confidence low) blocks BUILD_MICRO until live sprint (entretiens + landing + concierge).

**confidence_level**: medium

---

## Final Decision (Micro SaaS)

| Field | Value |
|-------|-------|
| **Primary Decision** | MONITOR_MICRO |
| **MSFI** | 60.9 |
| **capacity_blocked** | false |
| **Date** | 2026-06-26 |
| **Rationale** | All six hard gates PASS (build 78 h, maint 5 h/mo, solo operable, MRR 750 €/mo, distribution_cost 3, ToS low). MSFI 60.9 in MONITOR band (50–69). Desk-only Validation (`desk-only: true`, confidence low) blocks BUILD_MICRO per playbook — no live interviews, landing, or concierge yet. Tracker-only wedge gap documented (Validation #1) but WTP unknown and free incumbent relances (Henrri/Indy) + calendar reminders anchor pricing down. Portfolio capacity open (0 BUILD_MICRO active) but MONITOR queue at 5/5 after this entry — sprint validation prioritized before promotion. |

### Expected Learnings

- [ ] Topic: quote_followup_pain — Method: 8 entretiens freelances FR (Malt, LinkedIn, CPM) — Applies to: MONITOR_MICRO, KILL_MICRO
- [ ] Topic: willingness_to_pay — Method: Landing Van Westendorp €9–19/mo + €200 ads Meta/LinkedIn — Applies to: MONITOR_MICRO, BUILD_MICRO
- [ ] Topic: incumbent_sufficiency — Method: 8 interviews Henrri/Indy/calendar vs tracker dédié — Applies to: KILL_MICRO
- [ ] Topic: concierge_usefulness — Method: Concierge quote tracker 10 freelances 4 sem (J+3/J+7/J+14) — Applies to: MONITOR_MICRO, BUILD_MICRO

### Next Actions

- [ ] Publier landing FR « relance devis freelance » + waitlist — deadline 2026-07-15
- [ ] 8 entretiens freelances dev/design/consulting — deadline 2026-07-20
- [ ] Concierge quote tracker 10 freelances 4 semaines — deadline 2026-07-25
- [ ] Re-calculer MSFI ; promouvoir BUILD_MICRO si MSFI ≥70 + live validation — deadline 2026-07-26

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
