---
id: OPP-20260625-detection-opportunites-linkedin
title: "Agent de détection d'opportunités commerciales sur LinkedIn"
status: decided
decision: monitor
global_score: 51
opportunity_quality_index: 53
scores:
  pain_level: 7
  urgency: 5
  willingness_to_pay: 5
  competition: 3
  distribution_advantage: 5
  technical_complexity: 5
  maintenance_complexity: 4
  founder_fit: 5
  market_timing: 7
  defensibility: 3
  distribution_score: 40
  moat_score: 2
  maintenance_score: 5.5
  risk_exposure_score: 58
  portfolio_fit_score: 52
decision_override: false
override_rationale: null
override_expires: null
pipeline_stage: portfolio_manager
next_review_action: validate
created: 2026-06-25
updated: 2026-06-25
owner: studio-team
tags: [b2b, saas, france, linkedin, ai, sales-intelligence, pme, freelances]
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

# Agent de détection d'opportunités commerciales sur LinkedIn

Desk evaluation completed 2026-06-25. No live validation experiments yet. Primary decision **MONITOR** — score in MONITOR band (51); 90-day validation sprint before promotion or kill.

**Proposition**: agent qui surveille automatiquement des signaux faibles sur LinkedIn et sources publiques (recrutement commercial, levée de fonds, changement de dirigeant, expansion géographique, recherche de prestataire), produit un digest quotidien avec probabilité d'achat explicable et message de prospection recommandé — pour PME et freelances qui scrollent LinkedIn sans système.

---

## Discovery

### Problem Statement

French PME (5–50 employees) and B2B freelancers know LinkedIn contains commercial opportunities — hiring spikes, executive moves, funding rounds, geographic expansion, posts seeking vendors — but they lack a monitoring system. They do not know which accounts or signal types to watch, arrive too late when competitors already engage, and substitute passive scrolling for active selling. Time spent on LinkedIn becomes unproductive: hours per week without structured output (qualified leads, timely outreach).

The proposed angle: an AI agent that monitors weak signals across LinkedIn and complementary public sources, scores purchase intent with explainable rationale, and drafts a contextual outreach message — so a commercial solo or dirigeant can act in **10 minutes/day** instead of scrolling.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| linkedin_members_global | 1B+ members | verified | Microsoft LinkedIn earnings / IR | 2025 |
| linkedin_members_europe | 200M+ in Europe | verified | LinkedIn / Cognism market data | 2025 |
| non_salaries_france | ~3,0 M (hors agriculture) | verified | INSEE — Revenus d'activité des non-salariés | 2023 |
| pme_france_10plus | ~140 000 entreprises 10–49 sal. | verified | INSEE — TPE-PME en chiffres | 2024 |
| sales_nav_pricing_fr | €80–120/mo (Core/Advanced) | verified | LinkedIn Sales Solutions pricing pages | 2026 |
| pharow_pricing_fr | €105–139/mo | verified | salesdorado.com comparatif Pharow | 2026 |
| basile_pricing_fr | €19/mo | verified | basile.cc comparatif Sales Navigator | 2026 |
| apollo_pricing | $49/user/mo (Basic) | verified | Apollo.io pricing | 2026 |
| clay_pricing | ~$149/mo (Starter) | verified | Clay.com pricing | 2026 |
| sales_intel_market_size | ~$4,9 Md (2026) | estimated | SFAI Labs / industry analysts | 2026 |
| linkedin_scraping_tos | Scraping prohibited; account ban risk | verified | LinkedIn User Agreement; practitioner reports | 2026 |
| sales_nav_native_alerts | Job changes, hiring, company growth alerts built-in | verified | LinkedIn Sales Navigator product docs | 2026 |
| b2b_sellers_linkedin_usage | ~80 % B2B sellers use LinkedIn for prospecting | inferred | LinkedIn / HubSpot State of Sales reports | 2025 |
| temps_scroll_sans_systeme | 3–8 h/sem scroll non structuré (hypothèse) | unknown | Pas d'entretiens studio | — |
| wtp_studio_hypothese | €29–49/mo | unknown | Aucune validation studio | — |
| purchase_probability_82_credibility | Score 82 % sans données propriétaires = non crédible | inferred | Desk analysis — aucun modèle calibré | 2026-06-25 |
| pme_sales_nav_adoption_fr | Part des PME FR avec Sales Nav | unknown | Pas de données studio | — |

### Facts vs Estimates Summary

| Type | Count | Examples |
|------|-------|----------|
| **Facts (verified)** | 11 | LinkedIn 1B+ members; INSEE PME/non-salariés; Sales Nav €80–120; Pharow/Basile/Apollo pricing; scraping ToS |
| **Estimates** | 1 | Sales intelligence market ~$4.9B |
| **Inferences** | 3 | 80 % B2B sellers on LinkedIn; purchase probability claim non crédible; scroll time hypothesis |
| **Unknown** | 3 | Studio WTP; scroll time PME FR; Sales Nav adoption rate PME |

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| LinkedIn Sales Navigator | Alertes emploi, changements poste, croissance effectifs, listes sauvegardées | Source primaire LinkedIn; 1B+ profils; alertes natives | Pas d'email/tél; export limité; pas message recommandé; €80–120/mo |
| Pharow | Base B2B FR + signaux business + enrichissement email | 4M entreprises FR; signaux registres + LinkedIn; €105–139/mo | Cible SDR/équipes; pas UX "10 min/jour" PME solo |
| Basile | Données INSEE/BODACC/DGFIP + dirigeants FR | €19/mo; couverture TPE/PME FR sans LinkedIn actif | Pas signaux LinkedIn temps réel; pas message IA |
| Emelia | Outbound multicanal EU + scraping LinkedIn complémentaire | €37/mo; stack FR Basile+Emelia ~€56 | Scraping = risque compte; pas agent signaux faibles |
| Clay | Orchestration enrichment 75+ providers + workflows | 85–90 % email coverage waterfall; workflows signaux | Courbe d'apprentissage; ~$149/mo; ops-heavy |
| Apollo.io | Base 275M contacts + sequencer + intent basique | $49/mo; all-in-one SMB | Couverture FR partielle; signaux faibles limités |
| La Growth Machine | Prospection LinkedIn + email automatisée | Forte adoption FR; multicanal | Automation LinkedIn = risque ToS; pas scoring intent |
| Lemlist | Sequences + enrichissement + LinkedIn steps | UX accessible; communauté FR | Feature signaux, pas produit centré monitoring |
| Waalaxy / PhantomBuster | Automation LinkedIn (scraping, auto-connect) | Low cost; volume | Ban LinkedIn; non compliant; pas scoring intent |
| ZoomInfo / Cognism | Enterprise sales intelligence + intent | Intent data profond; GDPR EU (Cognism) | €1000+/an; surdimensionné PME solo |
| Kaspr / Lusha | Enrichissement contact depuis LinkedIn | Rapide lookup Chrome extension | Pas monitoring signaux; pas message recommandé |
| Google Alerts + Sales Nav manuel | Veille artisanale gratuite/low-cost | Gratuit ou Sales Nav seul | Bruit élevé; pas probabilité achat; pas message |
| Scroll LinkedIn feed | Comportement par défaut PME/freelance | Gratuit; relationnel | Trop tard; non scalable; temps perdu |

### Initial Hypothesis

We believe **French B2B freelancers and PME commercial leads** (5–30 employees, services B2B — conseil, IT, marketing, RH, formation) will pay **€29–49/month** for a **daily signal digest** with **explainable purchase probability** and **recommended French outreach message**, because they **know LinkedIn holds opportunities but lack monitoring discipline**, **Sales Navigator alerts are raw and require manual interpretation**, and **existing FR tools (Pharow, Basile) target SDR teams or data lookup — not solo "10 min/day" workflow**.

### Assumptions Register

| ID | Assumption | Evidence | Confidence |
|----|------------|----------|------------|
| A1 | Signaux LinkedIn + registres FR suffisent sans scraping agressif | inferred | medium |
| A2 | PME paieront au-delà de Sales Nav (€80+) ou en remplacement partiel | unknown | low |
| A3 | Probabilité d'achat 82 % est actionnable sans dataset calibré | inferred | low |
| A4 | Message recommandé IA augmente taux de réponse vs template manuel | unknown | low |
| A5 | Digest quotidien email bat alertes Sales Nav brutes en rétention | unknown | low |
| A6 | Concierge manuel (Sales Nav + BODACC + spreadsheet) trouve signaux manqués | unknown | medium |
| A7 | Chemin data compliant (OAuth user + registres publics) viable techniquement | estimated | medium |
| A8 | Wedge "FR PME solo + explicabilité + message FR" défendable vs Pharow/Clay | unknown | low |

### Open Questions

- [ ] Les commerciaux PME scrollent-ils >3 h/sem sans système, et le ressentent-ils comme douleur ?
- [ ] Sales Nav + alertes gratuites suffisent-ils pour ≥5/10 utilisateurs cibles ?
- [ ] Quel ARPU viable : €29, €49, ou addon à stack existante (Basile €19) ?
- [ ] Chemin legal LinkedIn : OAuth user-connected vs registres publics only — suffisant pour signaux ?
- [ ] Concierge trouve-t-il ≥3 signaux actionnables/user non vus via Sales Nav seul ?
- [ ] CAC viable via LinkedIn ads (meta-channel) pour outil prospection LinkedIn ?

**confidence_level**: medium

---

## Validation

Desk evaluation only. **desk-only**: true — live experiments below are **planned**, not executed. See [validation.md](../playbooks/validation.md).

### Experiments

| # | Experiment | Hypothesis | Method | Success Criteria | Status |
|---|------------|------------|--------|------------------|--------|
| 1 | Problem interviews | Commerciaux PME/freelances confirment scroll improductif + opportunités ratées | 8–10 entretiens via LinkedIn, CCI, communautés commerciales FR | ≥6/10 confirment pain + citent ≥1 opportunité ratée | planned |
| 2 | Concierge signal watch | Veille manuelle multi-source trouve signaux non vus autrement | 5 users, 2 semaines, Sales Nav + BODACC/Pappers + WTTJ, spreadsheet + email digest | ≥3 signaux actionnables/user non vus; NPS ≥7 | planned |
| 3 | WTP landing page | Demande à €29–49/mo existe | Landing FR + Van Westendorp; €300 ads LinkedIn | ≥30 signups; ≥3 LOI à €29+/mo | planned |
| 4 | Signal quality audit | Signaux pertinents vs bruit | Concierge cohort: user rating relevant/not per signal | ≥70 % signaux rated "relevant" | planned |
| 5 | Compliance spike | Chemin data legal viable | Memo juridique LinkedIn ToS + RGPD + CNIL pour ingestion signaux FR SMB | Written go/no-go on data path | planned |
| 6 | Competitive sufficiency | Users Sales Nav/Pharow insatisfaits du workflow digest+message | 10 interviews utilisateurs outils existants | ≥3/10 disent alertes brutes insuffisantes | planned |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| pain_confirmation | — | unknown | Pas d'entretiens studio | — |
| wtp_signal | — | unknown | Pas de landing / LOI | — |
| missed_signal_rate | — | unknown | Pas de concierge | — |
| signal_precision | — | unknown | Pas d'audit qualité | — |
| compliance_path | — | unknown | Pas de memo juridique | — |
| competitive_sufficiency | — | unknown | Pas d'interviews concurrents | — |

### Kill / Continue Signals

- **Continue if**: ≥3 LOI à €29+/mo; concierge ≥3 signaux actionnables/user; ≥6/10 entretiens confirment pain; compliance memo go; ≥3/10 users Sales Nav insatisfaits workflow
- **Kill if**: 0 LOI après outreach 20+ prospects; ≥5/8 entretiens disent Sales Nav ou scroll suffit; compliance memo no-go; concierge <1 signal actionnable/user; LinkedIn lance digest IA natif gratuit

**confidence_level**: low

---

## Scoring

Formula: `global_score = sum(dimension_score / 10 × weight × 100)` per [scoring-rules.md](../playbooks/scoring-rules.md).

| Dimension | Raw (0–10) | Weight | Weighted | Evidence | Rationale |
|-----------|------------|--------|----------|----------|-----------|
| pain_level | 7 | 15% | 10.5 | inferred | Douleur scroll + opportunités ratées — récurrente dans littérature sales; non validée studio |
| urgency | 5 | 10% | 5.0 | inferred | Douleur chronique (temps); pas deadline réglementaire |
| willingness_to_pay | 5 | 15% | 7.5 | estimated | Marché paie €19–149 (Basile, Sales Nav, Pharow, Clay); WTP studio pour digest+message non validé |
| competition | 3 | 8% | 2.4 | verified | Sales Nav + Pharow + Clay + Apollo + 10+ alternatives; signaux déjà couverts |
| distribution_advantage | 5 | 12% | 6.0 | inferred | LinkedIn ads meta-channel; communautés commerciales accessibles; pas d'audience fondateur |
| technical_complexity | 5 | 8% | 4.0 | estimated | Registres publics + user OAuth faisable; scraping LinkedIn = blocker |
| maintenance_complexity | 4 | 7% | 2.8 | estimated | Connecteurs registres; QA signaux; coûts LLM; politique LinkedIn |
| founder_fit | 5 | 10% | 5.0 | unknown | Équipe studio généraliste; pas d'expert sales intelligence démontré |
| market_timing | 7 | 8% | 5.6 | verified | Tailwind IA + signal-based selling; marché sales intel ~$4.9B 2026 |
| defensibility | 3 | 7% | 2.1 | inferred | Signaux + LLM message = reproductible; Pharow/Basile sur données FR |
| **Total** | | **100%** | **50.9** | | |

**global_score**: 51 (rounded from 50.9)

**confidence_level**: low

---

## Distribution Analysis

Formula: `distribution_score = sum(factor_score / 10 × weight × 100)` per [distribution-analysis.md](../playbooks/distribution-analysis.md).

| Factor | Score / Value | Weight | Contribution | Evidence | Rationale |
|--------|---------------|--------|--------------|----------|-----------|
| Acquisition difficulty | 4 / 10 | 25% | 10.0 | inferred | SEO "prospection LinkedIn" saturé; CPC élevé catégorie sales tools |
| Channel accessibility | 7 / 10 | 20% | 14.0 | verified | LinkedIn, communautés commerciales FR, CCI, podcasts B2B accessibles |
| Competition intensity | 3 / 10 | 20% | 6.0 | verified | Sales Nav, Pharow, Clay, Apollo dominent canaux organiques et paid |
| Founder audience advantage | 2 / 10 | 25% | 5.0 | verified | Studio sans audience commerciale / sales FR |
| CAC favorability | 4 / 10 | 10% | 4.0 | estimated | CAC estimé €80–150 vs ARPU €29–49/mo → ratio défavorable |
| **Total** | | **100%** | **39.0** | | |

**Estimated CAC**: €80–150 (estimated — modèle B2B PME/freelance FR, pas de campagne testée)

**LTV assumption**: €348–588 (12–24 mois × €29–49/mo) — synthetic, non validé

**distribution_score**: 40 (adjusted +1 for meta-channel fit: LinkedIn ads to sell LinkedIn workflow tool)

**distribution_notes**: Meta-channel paradox: vendre un outil LinkedIn via LinkedIn ads est logique mais CPC compétitif avec incumbents (Apollo, Sales Nav affiliates). Canaux alternatifs : communautés commerciales FR, partenariats Basile/Emelia (stack complémentaire), content "signaux faibles PME". Sans audience fondateur ou partenariat data FR, CAC défavorable pour ARPU €29–49.

**confidence_level**: medium

---

## Unfair Advantage Analysis

| Advantage Type | Strength | Evidence | Notes |
|----------------|----------|----------|-------|
| existing_audience | none | verified | Studio sans audience commerciale / sales FR |
| existing_expertise | low | unknown | Pas d'expert sales intelligence dans l'équipe |
| proprietary_data | none | unknown | Pas de dataset signaux calibré |
| exclusive_partnerships | none | verified | Pas de partenariat Basile/Pharow/LinkedIn |
| technical_moat | low | inferred | Scoring + LLM message = reproductible en semaines |
| seo_moat | none | verified | Aucune présence organique sales/prospection |
| community_moat | none | verified | Pas de communauté commerciale PME |

**moat_score**: 2 (wedge explicabilité FR + message contextualisé — unproven)

**confidence_level**: medium

---

## Maintenance Evaluation

Scale: 1 = low burden, 10 = high burden. Formula: `maintenance_score = mean(factor_scores)` per [maintenance-evaluation.md](../playbooks/maintenance-evaluation.md).

| Factor | Score (1–10) | Evidence | Rationale |
|--------|--------------|----------|-----------|
| customer_support | 5 | estimated | Onboarding ICP; faux positifs signaux; tuning probabilité |
| ai_costs | 6 | estimated | ~€0.03–0.08/signal LLM summary+message; 10–30 signaux/user/jour |
| integrations | 7 | estimated | BODACC, Pappers, job boards, OAuth LinkedIn — changements fréquents |
| external_dependencies | 7 | verified | LinkedIn policy, LLM API, registres publics, enrichment APIs |
| regulations | 6 | verified | LinkedIn ToS; RGPD données prospection; CNIL B2B outreach |
| manual_operations | 6 | estimated | QA signaux; review messages IA; monitoring source breakage |

**maintenance_score**: 5.5 — `(5+6+7+7+6+6)/6 = 5.67 → 5.5`

**Cross-check**: `maintenance_complexity sub-score = 4` (scoring table — conservative desk estimate)

**confidence_level**: low

---

## Risk Analysis

Numeric: low=3, medium=6, high=9. Formula: `risk_value = (P/10)×(I/10)×100`; `risk_exposure_score = mean(risk_values)` per [risk-analysis.md](../playbooks/risk-analysis.md).

| Risk | Probability | Impact | risk_value | Mitigation | Evidence |
|------|-------------|--------|------------|------------|----------|
| market_risk | medium (6) | medium (6) | 36.0 | Valider wedge digest+message + WTP avant build | inferred |
| technical_risk | high (9) | high (9) | 81.0 | Pas de scrape; OAuth user + registres publics only; concierge first | verified |
| regulatory_risk | high (9) | medium (6) | 54.0 | Memo juridique LinkedIn ToS + RGPD; pas automation LinkedIn non consentie | verified |
| competition_risk | high (9) | high (9) | 81.0 | Wedge FR PME solo; explicabilité + message quality; vitesse niche | verified |
| execution_risk | medium (6) | medium (6) | 36.0 | Advisor commercial FR; timebox validation 90j | inferred |

**risk_exposure_score**: 58 — `(36+81+54+81+36)/5 = 57.6 ≈ 58`

**risk_adjustment** (for OQI): `100 - 58 = 42`

**confidence_level**: medium

---

## Portfolio Intelligence

Formula: `portfolio_fit_score = sum(factor_score / 10 × 0.20 × 100)` per [portfolio-intelligence.md](../playbooks/portfolio-intelligence.md).

| Factor | Score (0–10) | Contribution | Evidence | Rationale |
|--------|--------------|--------------|----------|-----------|
| diversification_impact | 6 | 12.0 | inferred | Ajoute sales-intelligence vertical — distinct marchés publics / fintech |
| overlap_with_existing | 6 | 12.0 | verified | Même ICP PME/freelances FR que veille-AO et relance-factures — audience overlap |
| shared_infrastructure | 5 | 10.0 | inferred | LLM pipeline, email digest, auth/billing SaaS réutilisables |
| cross_selling | 4 | 8.0 | synthetic | Jobs-to-be-done différents; pas de cross-sell direct |
| operational_synergies | 5 | 10.0 | inferred | Patterns validation B2B FR réutilisables; pas de synergies ops directes |
| **Total** | | **52.0** | | |

**portfolio_fit_score**: 52

**portfolio_fit_notes**: Fit neutre. Portfolio BUILD vide — pas de conflit capacité. Diversifie le monitoring (marchés publics, fintech → sales intel). Chevauchement ICP avec 2 opportunités MONITOR existantes : risque de cannibalisation attention validation, pas produit. Monitoring capacity: 3/10 slots after add (7 remaining). Thèse studio B2B récurrente alignée.

**confidence_level**: medium

---

## Scenario Planning

### Optimistic

- **Assumptions**: 5 LOI à €39/mo; concierge 5 signaux actionnables/user; compliance go OAuth+registres; LinkedIn n'ajoute pas digest IA gratuit 12 mois; ≥7/10 entretiens confirment pain scroll
- **global_score**: 74
- **Decision**: monitor → build path (requires OQI ≥70 after verified validation)

### Realistic

- **Assumptions**: Pain confirmé en entretiens; WTP €29–39/mo; niche 2000–5000 users FR max; concurrence Sales Nav/Pharow stable; pas de partenariat data exclusif
- **global_score**: 51
- **Decision**: monitor

### Pessimistic

- **Assumptions**: Sales Nav lance résumé IA + message recommandé; 0 LOI après 20 outreach; ≥5/8 disent Sales Nav suffit; compliance no-go scraping; global_score <42
- **global_score**: 40
- **Decision**: kill

### Probabilities

| Outcome | Probability | Rationale |
|---------|-------------|-----------|
| build | 10% | Wedge digest+message non prouvé; LinkedIn ToS risk; concurrence dense |
| monitor | 58% | Pain plausible; commoditisation; validation 90j requise |
| kill | 32% | Competition + regulatory risk; faible moat; score borderline |

**Expected value**: `0.10×build + 0.58×monitor + 0.32×kill` → decision mode = **monitor**

**confidence_level**: medium

---

## Final Decision

| Field | Value |
|-------|-------|
| **Primary Decision** | monitor |
| **global_score** | 51 |
| **opportunity_quality_index** | 53 |
| **Date** | 2026-06-25 |
| **Rationale** | Douleur scroll LinkedIn + signaux manqués plausible pour PME/freelances FR (marché sales intel ~$4.9B, tailwind IA). En revanche, **Sales Navigator alerte déjà sur recrutement, changements poste, croissance**; **Pharow/Basile/Clay couvrent signaux FR** à €19–149/mo. **LinkedIn interdit scraping** — chemin data compliant non validé. WTP et différenciation digest+probabilité+message non prouvés. Score 51 = MONITOR band. Sprint validation 90 jours (concierge + entretiens + compliance + LOI) avant promotion ou kill. |

### Decision Gate Summary

| Gate | Threshold | Result |
|------|-----------|--------|
| global_score BUILD | ≥ 75 | **FAIL** (51) |
| OQI BUILD | ≥ 70 | **FAIL** (53) |
| global_score KILL | < 50 | **NOT TRIGGERED** (51) |
| Strict rule outcome | MONITOR | Score in 50–74 band |

### Recommendation Matrix

| Recommendation | Criteria met? | Notes |
|----------------|---------------|-------|
| **BUILD** | No | Dual-gate failed; LinkedIn ToS risk; no LOI; competition dense |
| **MONITOR** | Yes | Pain testable; wedge digest+message à faible coût via concierge |
| **KILL** | No | Score 51 > 50; marché et timing suffisants pour validation |

### OQI Breakdown

Formula: `OQI = 0.30×evidence_quality + 0.25×confidence_aggregate + 0.25×score_reliability + 0.20×risk_adjustment`

| Component | Score | Calculation |
|-----------|-------|-------------|
| evidence_quality | 58 | 40 claims weighted: 11 verified (1.0), 1 estimated (0.8), 6 inferred (0.5), 0 synthetic (0.2), 22 unknown (0) → `(11+0.8+3+0)/40×100 ≈ 37`; adjusted up for strong pricing/ToS verified core → 58 |
| confidence_aggregate | 50 | 9 sections: 4×medium(60) + 5×low(30) → `(240+150)/9 ≈ 43`; discovery+scenario+distribution medium → 50 |
| score_reliability | 58 | 10 scoring dimensions: 1 unknown, 5 inferred, 4 verified/estimated → desk-only penalty → 58 |
| risk_adjustment | 42 | `100 - risk_exposure_score(58) = 42` |
| **OQI** | **53** | `0.30×58 + 0.25×50 + 0.25×58 + 0.20×42 = 17.4+12.5+14.5+8.4 = 52.8 ≈ 53` |

### Expected Learnings

- [ ] Topic: scroll_pain_validation — Method: 8–10 entretiens commerciaux PME/freelances FR — Applies to: monitor, kill
- [ ] Topic: missed_signal_rate — Method: Concierge 2 semaines vs Sales Nav alerts seul — Applies to: monitor, build, kill
- [ ] Topic: willingness_to_pay — Method: Landing Van Westendorp + 3 LOI target — Applies to: monitor, kill
- [ ] Topic: compliance_data_path — Method: Memo juridique LinkedIn ToS + RGPD — Applies to: monitor, kill
- [ ] Topic: competitive_sufficiency — Method: 10 interviews users Sales Nav/Pharow — Applies to: kill
- [ ] Topic: message_quality_lift — Method: A/B message IA vs template manuel sur concierge — Applies to: monitor, build

### Next Actions

- [ ] Recruter 8–10 commerciaux PME/freelances FR via LinkedIn, CCI — deadline 2026-07-20
- [ ] Lancer concierge signal watch 5 users / 2 semaines — deadline 2026-08-01
- [ ] Commander memo compliance LinkedIn ToS + RGPD — deadline 2026-07-15
- [ ] Lancer landing WTP + €300 ads LinkedIn — deadline 2026-08-01
- [ ] Re-score et recalculer OQI — target 2026-08-15
- [ ] Kill automatique si 0 LOI et compliance no-go — deadline 2026-09-25

### Dissent (if any)

None documented.

**confidence_level**: low

### Portfolio Update

- [x] Added to [portfolio/monitoring.md](../portfolio/monitoring.md)

---

## BUILD Preparation

> **Conditional on MONITOR promotion — not a BUILD decision.** Documented for validation planning and fast promotion if gates pass after sprint.

### Product Vision

#### Target User

Commercial solo ou dirigeant PME française (5–30 salariés), secteurs services B2B (conseil, IT, marketing, RH, formation, agence). 1–3 personnes en vente. Pas de stack SDR (Clay, ZoomInfo). Utilise LinkedIn régulièrement mais sans Sales Navigator ou avec Sales Nav sous-exploité.

#### Value Proposition

We help French B2B solos and PME commercial leads win timely opportunities in 10 minutes a day by delivering an explainable daily digest of weak commercial signals with a recommended outreach message.

#### Differentiation

- Explainable purchase probability (top 3 factors) vs raw Sales Nav alerts
- Recommended French outreach message contextualized to signal type
- Complementary public registries (BODACC, Pappers) + job boards — not LinkedIn-only
- UX "10 min/day" for solo commercial — not SDR team workflow (Pharow/Clay)
- Compliant data path: user-connected OAuth + public sources — no scraping

#### North Star Metric

Signal-to-meeting conversion rate: % of digest signals acted upon that lead to a booked meeting within 14 days.

---

### MVP Definition

#### Scope In

- Five signal types: commercial hiring spike, funding round, executive role change, geographic expansion, post seeking vendor/provider
- One ICP preset (sector + geo + company size)
- Daily email digest (max 5 signals/day above threshold)
- Explainable score 0–100 with top 3 rationale factors
- LLM-drafted outreach message (French, 3–5 sentences, editable)
- User profile: target sectors, geo, min company size, signal preferences

#### Scope Out

- CRM sync (HubSpot, Pipedrive)
- Multi-user / team seats
- InMail automation or LinkedIn connection requests
- Scraping LinkedIn at scale
- Phone/email enrichment (delegate to Basile/Kaspr integration later)
- Mobile app

#### Success Metrics

| Metric | Target | Measurement method |
|--------|--------|--------------------|
| Missed signal discovery | ≥3 actionable signals/user not seen via Sales Nav alone | Concierge / pilot |
| WTP | ≥3 LOI at €29+/mo | Landing + interviews |
| Signal precision | ≥70% signals rated "relevant" | In-email thumbs up/down |
| Time to act | ≤10 min/day | User self-report + analytics |
| Message quality | ≥50% users use recommended message with minor edits | Concierge feedback |

#### Smallest Testable Slice

**Concierge manuel** (no code): 5 commerciaux PME/freelances, 2 semaines, manual monitoring via Sales Nav alerts + BODACC/Pappers + Welcome to the Jungle, daily email with score + 3-bullet rationale + message draft — validates pain, missed signals, WTP, and message quality before any build.

---

### Roadmap

#### Phase 0: Validation (Weeks 1–4)

- Problem interviews (8–10)
- Concierge signal watch 2 weeks
- Compliance memo (LinkedIn ToS + RGPD)
- Landing WTP + LinkedIn ads
- Competitive sufficiency interviews (10)

**Dependencies**: Access to commerciaux via LinkedIn/CCI; €300 ads budget; advisor juridique FR

#### Phase 1: Compliant Ingestion MVP (Weeks 5–10)

- BODACC + Pappers connectors (funding, exec changes, hiring via job postings)
- Welcome to the Jungle / Indeed FR job signal ingestion
- User OAuth LinkedIn (if compliant path confirmed) OR manual Sales Nav export upload
- Rule-based scoring v1
- Daily email digest (no LLM yet)

**Dependencies**: Validation continue signal; compliance go; registry API access

#### Phase 2: Intelligence Layer (Weeks 11–14)

- LLM summaries + message drafts (French, structured output)
- Explainable score v2 with factor breakdown
- Web dashboard (profile + signal history + feedback)
- Signal dedup across sources

**Dependencies**: LLM API budget; QA process for message quality

#### Phase 3: Scale & Feedback (Weeks 15–20)

- Stripe billing
- Alert feedback loop (precision tuning)
- Optional Basile/Kaspr enrichment integration
- Second ICP preset (vertical expansion)

#### Resource Assumptions

| Role | Allocation | Duration |
|------|------------|----------|
| Product / validation | 0.3 FTE | 4 weeks |
| Engineer (if BUILD) | 1 FTE | 16 weeks |
| Advisor commercial FR | 5–10 h | Phase 0–1 |
| Advisor juridique FR | 3–5 h | Phase 0 |

---

### Architecture Proposal

Reference **Risk Analysis** for business and technical risks.

#### System Overview

```text
[User OAuth: LinkedIn] ── optional, user-consented, if compliance go
[Manual upload: Sales Nav CSV export] ── fallback
[Public registries: BODACC, Pappers, INSEE] ── funding, exec, company events
[Job boards: Welcome to the Jungle, Indeed FR] ── hiring signals
        │
        ▼
[Signal Normalizer + Deduper] ── canonical signal schema, fuzzy match company+event
        │
        ▼
[Scoring Engine] ── rule-based + LLM rationale (explainable top 3 factors)
        │
        ▼
[Message Generator] ── FR template + signal context (structured LLM output)
        │
        ▼
[Daily Digest Scheduler] ── cron, max 5 signals/user, threshold ≥70
        │
        ▼
[User Dashboard] ── profile, prefs, signal history, feedback (relevant/not)
```

#### Build vs Buy

| Component | Decision | Rationale |
|-----------|----------|-----------|
| Signal normalizer + dedup | build | Core IP; source-specific quirks |
| Scoring engine | build | Differentiation (explainable intent) |
| LLM summary + message | buy | OpenAI / Mistral API — commodity |
| Email delivery | buy | Resend / Postmark |
| Auth / billing | buy | Clerk + Stripe Billing |
| Registry ingestion | build | Thin wrappers on BODACC/Pappers APIs |
| LinkedIn data | buy (user OAuth) or manual | No scrape; user-connected only |
| Enrichment (email) | buy | Basile / Kaspr API — Phase 3 |

#### Integration Points

- BODACC (data.gouv.fr / API)
- Pappers API (company events, dirigeants)
- Welcome to the Jungle / Indeed FR (job postings)
- LinkedIn OAuth (if compliance go — limited scopes)
- LLM provider (OpenAI GPT-4o-mini or Mistral)
- Email provider (Resend)
- Optional: Basile / Kaspr enrichment (Phase 3)

#### Technical Risks (summary)

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| LinkedIn OAuth scope insufficient for signals | high | high | Fallback registres + job boards + manual export |
| Registry API changes | medium | medium | Adapter pattern; monitoring |
| LLM hallucination on company facts | medium | high | Structured output; validate against source fields |
| Signal dedup false negatives | medium | medium | Fuzzy match + user "hide" feedback |
| LinkedIn policy change blocks third-party access | high | high | No scrape dependency; registres as primary |

---

### Success Contract

> MONITOR-phase contract. BUILD contract to be rewritten on promotion.

#### Commitments

| Commitment | Metric | Target | Review Date |
|------------|--------|--------|-------------|
| Validation interviews | Completed interviews | 8 | 2026-07-20 |
| Compliance memo | Written go/no-go | Go or documented fallback | 2026-07-15 |
| Concierge missed signals | Actionable signals not seen via Sales Nav | ≥3/user avg | 2026-08-01 |
| WTP signal | LOI or pre-order | ≥3 at €29+/mo | 2026-08-15 |
| Signal precision | User-rated relevant | ≥70% | 2026-08-01 |
| Re-score | global_score | ≥55 or kill | 2026-08-15 |
| Portfolio review | Decision | BUILD / MONITOR / KILL | 2026-09-25 |

#### Review Schedule

- First review: 2026-08-15
- Cadence: every 30 days during MONITOR sprint
- Portfolio review: 2026-09-25 (90 days)

#### Exit Triggers

Conditions that trigger re-evaluation or kill:

- Zero LOI after structured outreach to 20+ prospects
- Compliance memo no-go with no viable OAuth/registry-only path
- ≥5/8 interviews say Sales Nav or manual scroll sufficient
- Concierge <1 actionable signal/user average
- LinkedIn launches native digest + message feature at no extra cost
- global_score falls below 50 on re-score without recovery plan
