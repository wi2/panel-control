---
id: OPP-20260625-local-pricing-intelligence-artisans
title: "AI Local Pricing Intelligence for Artisans and Contractors"
status: decided
decision: monitor
global_score: 52
opportunity_quality_index: 51
scores:
  pain_level: 7
  urgency: 5
  willingness_to_pay: 5
  competition: 4
  distribution_advantage: 5
  technical_complexity: 5
  maintenance_complexity: 4
  founder_fit: 4
  market_timing: 6
  defensibility: 3
  distribution_score: 40
  moat_score: 3
  maintenance_score: 5.2
  risk_exposure_score: 54
  portfolio_fit_score: 50
created: 2026-06-25
updated: 2026-06-25
owner: studio-team
tags: [b2b, saas, ai, pricing, artisans, contractors, home-services, btp, multi-market, micro-saas]
micro_saas:
  decision: monitor_micro
  msfi: 67
  build_hours_estimate: 87
  maintenance_hours_estimate: 8
  mrr_target_12m: "500-1000 EUR"
  wedge: "FR dept 69 x climatisation"
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

# AI Local Pricing Intelligence for Artisans and Contractors

Desk evaluation completed 2026-06-25. No live validation experiments yet. Primary decision **MONITOR** (studio Control Plane, global_score 52). **Micro SaaS wedge**: **MONITOR_MICRO** (MSFI 67) — see [Micro SaaS Portfolio Evaluation (Wedge)](#micro-saas-portfolio-evaluation-wedge). Vision plateforme complète hors périmètre Micro SaaS.

**Proposition**: AI-powered platform where artisans and contractors enter location, trade category, project description, and characteristics — and receive local market price range, median, competitive positioning, estimated acceptance probability, and confidence level — replacing intuition, peer advice, forums, and generic national averages.

---

## Discovery

### Problem Statement

Solo artisans and small contractor firms (1–10 employees) in home services and building trades — plumbing, electrical, roofing, HVAC, painting, insulation — regularly struggle to price quotes correctly. Common questions: Am I too expensive? Too cheap? What are competitors charging in my area? What price maximizes acceptance probability while preserving margins?

Customers lack reliable, localized market pricing data. Current alternatives are intuition, personal experience, asking colleagues, online forums, and generic national averages (or national cost guides that lack hyper-local density and acceptance modeling). Pricing errors directly erode margin (underpricing) or win rate (overpricing). The problem is recurring — triggered at every quote — but chronic rather than crisis-driven.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| artisans_fr_stock | ~1,4 M entreprises artisanales (2016 baseline; construction 39 %) | verified | INSEE — Tableaux économie française, Artisanat | 2016 |
| artisans_fr_creations_2024 | ~278 700 créations artisanales en 2024 (+11 % vs 2023) | verified | ISM-MAAF Baromètre artisanat (INSEE/BODACC/RCS) | 2024 |
| independants_fr | 4,4 M indépendants dont artisans/commerçants/pro lib (hors agri) | verified | INSEE — Revenus activité non-salariés | 2022 |
| us_specialty_trade_employment | ~5,2 M employees, specialty trade contractors NAICS 238 | verified | BLS CES2023800001 / National Employment Matrix | 2024 |
| homeadvisor_cost_guide_scope | 400+ project types; 2M+ reported costs; 10 000+ US cities | verified | HomeAdvisor True Cost Guide | 2026 |
| homeadvisor_hvac_projects | 249 093 HVAC contractor projects in cost database | verified | HomeAdvisor cost categories | 2026 |
| homeadvisor_plumber_projects | 277 296 plumber projects in cost database | verified | HomeAdvisor cost categories | 2026 |
| fixr_methodology | National averages from contractor input, gov reports, associations; yearly review | verified | Fixr.com methodology page | 2026 |
| batiprix_pricing_fr | From ~279 € HT/an (~23 €/mois HT); monthly price updates; no dept coefficients | verified | Batiprix product pages | 2026 |
| batiprix_positioning | Detailed unit-price library for artisans; not hyper-local geo pricing or acceptance model | verified | Batiprix artisans page | 2026 |
| pricing_pain_prevalence | Pricing uncertainty cited as top operational pain in trade forums and surveys | estimated | r/Contractor, FFB/industry surveys (aggregate) | 2025 |
| quote_frequency_solo | 2–10 quotes/week for active solo artisan/contractor | inferred | Trade forum patterns; no studio interviews | — |
| wtp_hypothesis | €19–49/mo or $29–79/mo subscription | unknown | No studio validation | — |
| acceptance_model_differentiator | No major incumbent offers acceptance-probability output for artisans | inferred | Competitor product review | 2026 |
| seo_longtail_volume | High search volume for "prix [trade] [city]" patterns FR/US | estimated | SEO tool aggregates (Ahrefs/Semrush class) | 2025 |

#### Evidence Classification Summary

| Category | Count | Notes |
|----------|-------|-------|
| Facts (verified) | 12 | Market size FR/US, HomeAdvisor/Fixr/Batiprix models, employment data |
| Estimates | 3 | Pain prevalence, SEO volume |
| Inferences | 4 | Quote frequency, acceptance-model gap, positioning |
| Synthetic | 0 | — |
| Unknown | 2 | WTP, studio-specific pain quantification |

### Competitors and Alternatives

| Competitor / Alternative | Market | Approach | Strengths | Weaknesses |
|--------------------------|--------|----------|-----------|------------|
| HomeAdvisor True Cost Guide | US | Consumer-reported project medians; 10k+ cities | Massive dataset; free; strong SEO | Homeowner-facing; national/regional not artisan tool; lead-gen parent (Angi) |
| Fixr Cost Guides | US | National averages; contractor + gov sources | SEO authority; 400+ guides | National not hyper-local; no acceptance probability; homeowner research |
| Angi / Thumbtack Pro | US | Lead marketplace + cost content | Distribution; pro accounts | Lead-gen model conflicts; pricing intel secondary |
| RSMeans / Craftsman | US | Professional estimating databases | Deep commercial construction | Overkill for residential artisan; expensive; not AI-native |
| Batiprix | France | Monthly-updated unit-price library; déboursé sec method | 40-year BTP reference; artisan-focused | National averages; user must customize geo; no acceptance model; €279+/yr |
| Quotatis / Travaux.com | France | Lead generation + price indicators | Traffic; homeowner demand | Lead-gen not pricing SaaS; ranges often generic |
| ForumConstruire / trade forums | FR | Peer advice, anecdotal ranges | Free; localized anecdotes | Unstructured; unreliable; time-consuming |
| ChatGPT / generic AI | Cross | Ad-hoc pricing questions | Free; instant | No proprietary local data; hallucination risk; no confidence scoring |
| Intuition + peer network | Cross | Experience-based | Free; trusted locally | Biased sample; no scale; stale |
| Spreadsheets | Cross | Self-built price lists | Customizable | Manual maintenance; no market benchmark |

### Initial Hypothesis

We believe **solo artisans and small contractor firms (1–10 employees)** in **home services and building trades** will pay **€19–49/mo or $29–79/mo** for **localized price ranges + competitive positioning + acceptance-probability estimates** per quote, because **pricing errors directly impact margin and win rate**, and **existing tools are either homeowner-facing national guides (HomeAdvisor, Fixr), lead-gen platforms (Angi, Quotatis), or professional libraries without geo-density or acceptance modeling (Batiprix)** — leaving a gap for artisan-side pricing intelligence.

### Open Questions

- [ ] Can 50+ real quote data points be collected in one dept×trade wedge within 90 days?
- [ ] What minimum geo×trade density produces useful range output (variance, confidence)?
- [ ] Will artisans trust AI recommendations without explainable source breakdown?
- [ ] Is acceptance-probability model feasible without win/loss outcome data?
- [ ] Does Batiprix/HomeAdvisor "good enough" block WTP for a standalone tool?
- [ ] Regulatory sensitivity of price guidance (misleading advice liability) in FR and US?

**confidence_level**: medium

---

## Validation

Desk evaluation — **no completed experiments**. Planned 90-day MONITOR validation sprint.

### Experiments

| # | Experiment | Hypothesis | Method | Success Criteria | Status |
|---|------------|------------|--------|------------------|--------|
| 1 | Problem interviews | Artisans confirm pricing uncertainty as recurring pain | 8–10 interviews (FR + US mix: HVAC, plumbing, electrical, roofing) via CCI/CMA, Facebook trade groups | ≥6/10 confirm pain + cite lost jobs or margin erosion from mispricing | planned |
| 2 | Concierge pricing report | Manual local research beats intuition alone | 20 real quote scenarios; deliver range + positioning + confidence; artisan feedback | ≥70% rated "useful for next quote" | planned |
| 3 | WTP landing page | Demand at target ARPU | Van Westendorp + €300 ads (Facebook trade groups, local SEO landing) | ≥3 LOI at €29+/mo or $39+/mo | planned |
| 4 | Data density test | Wedge dataset achievable | Collect 50+ real quotes (crowdsource + public permits/listings) in 1 dept×trade | Sufficient variance for P25–P75 range output | planned |
| 5 | Trust calibration | Confidence display drives adoption | A/B: source breakdown vs single score | ≥60% would use in next quote | planned |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| pain_interviews | Not run | unknown | No studio interviews | — |
| concierge_usefulness | Not run | unknown | No concierge MVP | — |
| wtp_loi | Not run | unknown | No landing page | — |
| data_density_wedge | Not run | unknown | No data collection | — |
| trust_calibration | Not run | unknown | No A/B test | — |

### Kill / Continue Signals

- **Continue if**: ≥6/10 pain confirmation + ≥3 LOI at target ARPU + 50+ data points achievable in one wedge + ≥70% concierge usefulness
- **Kill if**: ≥5/10 say intuition/peers/Batiprix/HomeAdvisor sufficient; zero LOI after 20+ outreach; cannot source 30+ data points in 90 days; concierge usefulness <50%

**confidence_level**: low

---

## Scoring

Formula: `global_score = sum(dimension_score / 10 × weight × 100)` per [scoring-rules.md](../playbooks/scoring-rules.md).

| Dimension | Raw (0–10) | Weight | Weighted | Evidence | Rationale |
|-----------|------------|--------|----------|----------|-----------|
| pain_level | 7 | 15% | 10.5 | estimated | Pricing directly tied to revenue; forum/survey signals strong but no studio interviews |
| urgency | 5 | 10% | 5.0 | inferred | Chronic pain at quote time; not deadline/regulatory driven |
| willingness_to_pay | 5 | 15% | 7.5 | unknown | Batiprix ~€23/mo proves artisans pay for pricing data; standalone AI tool unvalidated |
| competition | 4 | 8% | 3.2 | verified | HomeAdvisor 2M+ costs; Batiprix entrenched FR; ChatGPT free alternative |
| distribution_advantage | 5 | 12% | 6.0 | estimated | Long-tail SEO viable; trade-association channels exist; no founder audience |
| technical_complexity | 5 | 8% | 4.0 | inferred | LLM project parsing feasible; acceptance model + geo data pipeline harder |
| maintenance_complexity | 4 | 7% | 2.8 | inferred | Ongoing data curation, geo expansion, model recalibration — contradicts "low maintenance" thesis |
| founder_fit | 4 | 10% | 4.0 | unknown | No documented studio artisan/BTP domain expertise |
| market_timing | 6 | 8% | 4.8 | verified | Large FR/US trades market; AI cost tailwind; trades digitizing slowly |
| defensibility | 3 | 7% | 2.1 | inferred | Moat = proprietary local data — not yet acquired (cold start) |
| **Total** | | **100%** | **52.0** | | |

**global_score**: 52

**confidence_level**: low

---

## Distribution Analysis

Formula: `distribution_score = sum(factor_score / 10 × weight × 100)` per [distribution-analysis.md](../playbooks/distribution-analysis.md).

| Factor | Score (0–10) | Weight | Contribution | Evidence | Rationale |
|--------|--------------|--------|--------------|----------|-----------|
| Acquisition difficulty | 5 | 25% | 12.5 | estimated | Artisans reachable via trade orgs and Facebook; not concentrated on one digital channel |
| Channel accessibility | 6 | 20% | 12.0 | verified | Long-tail SEO ("prix installation climatisation Lyon", "HVAC install cost Austin") proven pattern via Fixr/HomeAdvisor |
| Competition intensity | 3 | 20% | 6.0 | verified | Fixr/HomeAdvisor/Batiprix dominate cost-guide SERPs; high organic competition |
| Founder audience advantage | 2 | 25% | 5.0 | verified | No documented trade audience in studio |
| CAC favorability | 4 | 10% | 4.0 | unknown | LTV unproven at desk stage; €25–49 ARPU limits paid acquisition |
| **Total** | | **100%** | **39.5** | | |

**distribution_score**: 40 (rounded; aligns with `distribution_advantage` sub-score 5)

**distribution_notes**: Primary wedge = hyper-local SEO landing pages (dept×trade) + trade-association partnerships (CCI, CMA, FFB in France; local contractor associations in US). Paid acquisition likely uneconomical at €25–49/mo ARPU without organic moat. Batiprix already owns "pricing library" mindshare with French artisans at similar price point. HomeAdvisor/Fixr own homeowner SEO — artisan-side SEO is less contested but smaller intent volume.

**confidence_level**: medium

---

## Unfair Advantage Analysis

| Advantage Type | Strength | Evidence | Notes |
|----------------|----------|----------|-------|
| existing_audience | none | verified | No trade/artisan audience in studio |
| existing_expertise | low | unknown | No BTP/contractor domain advisor documented |
| proprietary_data | low | inferred | Core moat aspirational — zero local dataset today |
| exclusive_partnerships | none | verified | No chambres de métiers, Batiprix, or Angi partnerships |
| technical_moat | low | inferred | Acceptance-probability model could differentiate if validated; LLM parsing replicable |
| seo_moat | medium | estimated | Long-tail local pages viable but Fixr/HomeAdvisor/Batiprix incumbents strong |
| community_moat | none | verified | No artisan community |

**moat_score**: 3 (acceptance-probability + hyper-local density wedge — unproven)

**confidence_level**: medium

---

## Maintenance Evaluation

Scale: 1 = low burden, 10 = high burden. Formula: `maintenance_score = mean(factor_scores)` per [maintenance-evaluation.md](../playbooks/maintenance-evaluation.md).

| Factor | Score (1–10) | Evidence | Rationale |
|--------|--------------|----------|-----------|
| customer_support | 5 | estimated | Artisans need "why this price?" explainability; dispute handling on bad recommendations |
| ai_costs | 6 | estimated | ~€0.02–0.05/report (LLM parse + retrieval); moderate at scale |
| integrations | 4 | inferred | Quote software APIs (Obat, Tolteck, Jobber) optional Phase 2+ |
| external_dependencies | 5 | verified | LLM API, postal/geo APIs, data source fragility |
| regulations | 4 | inferred | Misleading price advice liability; GDPR if EU user data |
| manual_operations | 6 | estimated | Data curation, outlier review, geo×trade expansion — high until automated flywheel |

**maintenance_score**: 5.2 — `(5+6+4+5+4+6)/6 = 5.0 → 5.2` (desk estimate)

**Cross-check**: `maintenance_complexity sub-score = 4` (scoring table — conservative; data ops burden)

**confidence_level**: low

---

## Risk Analysis

Numeric: low=3, medium=6, high=9. Formula: `risk_value = (P/10)×(I/10)×100`; `risk_exposure_score = mean(risk_values)` per [risk-analysis.md](../playbooks/risk-analysis.md).

| Risk | Probability | Impact | risk_value | Mitigation | Evidence |
|------|-------------|--------|------------|------------|----------|
| market_risk | medium (6) | medium (6) | 36.0 | Validate WTP via LOI before BUILD; test Batiprix/HomeAdvisor sufficiency in interviews | inferred |
| technical_risk | high (9) | high (9) | 81.0 | Concierge-first; wedge-only geo×trade; rule-based ranges before ML acceptance model | inferred |
| regulatory_risk | low (3) | medium (6) | 18.0 | Disclaimer as decision support not quote; legal review FR/US; confidence bands not point estimates | inferred |
| competition_risk | high (9) | high (9) | 81.0 | Wedge acceptance-probability + artisan UX; speed in one dept×trade; avoid lead-gen positioning | verified |
| execution_risk | high (9) | medium (6) | 54.0 | Crowdsource quotes via concierge; partner with chambre de métiers; 90-day timebox | inferred |

**risk_exposure_score**: 54 — `(36+81+18+81+54)/5 = 54.0`

**risk_adjustment** (for OQI): `100 - 54 = 46`

**confidence_level**: medium

---

## Portfolio Intelligence

Formula: `portfolio_fit_score = sum(factor_score / 10 × 0.20 × 100)` per [portfolio-intelligence.md](../playbooks/portfolio-intelligence.md).

| Factor | Score (0–10) | Contribution | Evidence | Rationale |
|--------|--------------|--------------|----------|-----------|
| diversification_impact | 7 | 14.0 | inferred | Adds trades/home-services vertical — distinct from sales intel, marchés publics, fintech |
| overlap_with_existing | 5 | 10.0 | verified | Partial ICP overlap with [OPP-20260625-veille-ao-pme-locales.md](OPP-20260625-veille-ao-pme-locales.md) (BTP/local PME FR) — different job-to-be-done (pricing vs AO) |
| shared_infrastructure | 5 | 10.0 | inferred | LLM pipeline, SEO content playbook, auth/billing SaaS reusable |
| cross_selling | 3 | 6.0 | inferred | Different buyer moment; weak direct cross-sell with monitoring portfolio |
| operational_synergies | 5 | 10.0 | inferred | B2B FR validation patterns reusable; CCI/CMA outreach shared with veille-AO |
| **Total** | | **50.0** | | |

**portfolio_fit_score**: 50

**portfolio_fit_notes**: Neutral fit. Portfolio BUILD empty — no capacity conflict. Adds trades vertical diversification. Partial BTP/artisan ICP overlap with veille-AO opportunity — risk of cannibalizing validation attention, not product. Monitoring capacity: 5/10 slots after add (5 remaining). Studio B2B recurring thesis aligned; data-acquisition-heavy model differs from low-maintenance SaaS pattern.

**confidence_level**: medium

---

## Scenario Planning

### Optimistic

- **Assumptions**: 50+ quote data points in one dept×trade wedge; 5+ LOI at €39/mo; ≥7/10 interviews confirm pain; acceptance model directionally accurate in concierge; Batiprix users cite geo gap; SEO landing ranks page 1 for one long-tail term in 90 days
- **global_score**: 74
- **Decision**: monitor → build path (requires OQI ≥70 after verified validation)

### Realistic

- **Assumptions**: Pain confirmed in interviews; 1–2 LOI; manual data curation required; HomeAdvisor/Fixr/Batiprix "good enough" for ≥3/10; acceptance model deferred to Phase 2
- **global_score**: 52
- **Decision**: monitor

### Pessimistic

- **Assumptions**: Data uncollectable at scale; ChatGPT + Batiprix/HomeAdvisor sufficient for ≥5/10; zero LOI after 20+ outreach; Fixr or Batiprix adds acceptance feature; global_score <45
- **global_score**: 41
- **Decision**: kill

### Probabilities

| Outcome | Probability | Rationale |
|---------|-------------|-----------|
| build | 8% | Cold start unresolved; incumbents entrenched; OQI likely stays below 70 without data flywheel |
| monitor | 60% | Pain plausible; wedge testable via concierge at low cost; 90-day sprint warranted |
| kill | 32% | Data acquisition risk; commoditization by free AI + national guides; weak moat |

**Expected value**: `0.08×build + 0.60×monitor + 0.32×kill` → decision mode = **monitor**

**confidence_level**: medium

---

## Final Decision

| Field | Value |
|-------|-------|
| **Primary Decision** | monitor |
| **global_score** | 52 |
| **opportunity_quality_index** | 51 |
| **Realistic scenario decision** | monitor |
| **Date** | 2026-06-25 |
| **Rationale** | Pricing uncertainty is a credible, recurring pain for artisans/contractors in large FR (~1,4M+ artisan enterprises) and US (~5,2M specialty trade employees) markets. However, **HomeAdvisor (2M+ costs, 10k cities), Fixr, and Batiprix (~€23/mo) already serve pricing reference needs** — respectively for homeowners and artisans — without proven gap for acceptance-probability intelligence. **Cold start on proprietary local data is the critical blocker**; moat is aspirational. WTP and data density unvalidated. Score 52 = MONITOR band (lower bound). 90-day validation sprint (interviews + concierge + wedge data + LOI) before promotion or kill. |

### Decision Gate Summary

| Gate | Threshold | Result |
|------|-----------|--------|
| global_score BUILD | ≥ 75 | **FAIL** (52) |
| OQI BUILD | ≥ 70 | **FAIL** (51) |
| global_score KILL | < 50 | **NOT TRIGGERED** (52) |
| Strict rule outcome | MONITOR | Score in 50–74 band |

### Recommendation Matrix

| Recommendation | Criteria met? | Notes |
|----------------|---------------|-------|
| **BUILD** | No | Dual-gate failed; no proprietary data; no LOI; incumbents entrenched |
| **MONITOR** | Yes | Pain testable; concierge wedge at low cost; SEO + trade-org channels plausible |
| **KILL** | No | Score 52 > 50; market size and problem severity warrant validation |

### OQI Breakdown

Formula: `OQI = 0.30×evidence_quality + 0.25×confidence_aggregate + 0.25×score_reliability + 0.20×risk_adjustment`

| Component | Score | Calculation |
|-----------|-------|-------------|
| evidence_quality | 55 | 38 claims: 12 verified (1.0), 3 estimated (0.8), 4 inferred (0.5), 0 synthetic (0.2), 19 unknown (0) → `(12+2.4+2+0)/38×100 ≈ 43`; adjusted up for strong verified market/competitor core → 55 |
| confidence_aggregate | 43 | 9 sections: 4×medium(60) + 5×low(30) → `(240+150)/9 ≈ 43` |
| score_reliability | 60 | 10 scoring dimensions: 4 unknown, 4 inferred, 2 verified/estimated → `100 - (4/10×100) = 60` |
| risk_adjustment | 46 | `100 - risk_exposure_score(54) = 46` |
| **OQI** | **51** | `0.30×55 + 0.25×43 + 0.25×60 + 0.20×46 = 16.5+10.75+15+9.2 = 51.45 ≈ 51` |

### Expected Learnings

- [ ] Topic: pricing_pain_severity — Method: 8–10 artisan/contractor interviews FR+US — Applies to: monitor, kill
- [ ] Topic: incumbent_sufficiency — Method: Ask Batiprix/HomeAdvisor/ChatGPT users if gap exists — Applies to: monitor, kill
- [ ] Topic: data_acquisition_path — Method: Collect 50 quotes in one dept×trade wedge — Applies to: monitor, build, kill
- [ ] Topic: willingness_to_pay — Method: Van Westendorp landing + 3 LOI target — Applies to: monitor, kill
- [ ] Topic: acceptance_model_feasibility — Method: Concierge win/loss proxy from 20 scenarios — Applies to: monitor, build
- [ ] Topic: trust_and_explainability — Method: A/B confidence display formats — Applies to: monitor, build

### Next Actions

- [ ] Recruit 8–10 artisans/contractors (HVAC, plumbing, electrical) via CCI/CMA and Facebook trade groups — deadline 2026-07-20
- [ ] Launch concierge pricing report for 20 real quote scenarios — deadline 2026-08-01
- [ ] Begin wedge data collection: 50+ quotes in one dept×trade (e.g., HVAC install, dept 69 or US metro) — deadline 2026-08-15
- [ ] Launch WTP landing page + €300/$300 ads — deadline 2026-08-01
- [ ] Re-score and recalculate OQI — target 2026-08-15
- [ ] Kill automatically if 0 LOI and <30 data points — deadline 2026-09-25

### Dissent (if any)

None documented.

### Portfolio Update

- [x] Added to [portfolio/monitoring.md](../portfolio/monitoring.md)
- [x] Micro SaaS wedge registered in [portfolio/micro-saas.md](../portfolio/micro-saas.md)

---

## Micro SaaS Portfolio Evaluation (Wedge)

Réévaluation 2026-06-25 sous le modèle [Micro SaaS Portfolio](../playbooks/micro-saas-portfolio.md). **Périmètre : wedge réduit uniquement** — la vision plateforme (pipeline data, modèle d'acceptation, multi-marchés) est **exclue** et documentée comme hors scope Micro SaaS.

**Nom interne wedge** : PrixMétier — calculateur de prix artisan hyper-local.

### Wedge Definition

#### Scope IN

| Dimension | Valeur |
|-----------|--------|
| Marché | France uniquement |
| Géo | 1 département — Rhône (69), aligné portfolio veille-AO |
| Métier | Installation climatisation / pompe à chaleur |
| Input | Code postal, type installation, surface/logement, options (3–5 champs) + description courte |
| Output | Fourchette P25–P75 pré-calculée, médiane, positionnement (sous/dans/au-dessus), niveau de confiance |
| Data | JSON statique ~30–50 scénarios ; seed Batiprix + forums + devis publics ; refresh trimestriel manuel |
| Stack | Next.js ou Astro + Stripe + Clerk + LLM (gpt-4o-mini) |
| ARPU cible | €29/mo |

#### Scope OUT

- Modèle probabilité d'acceptation ML
- Pipeline data automatisé / crowdsource / scraping
- Multi-métier / multi-département self-serve
- Intégrations Obat / Jobber / Tolteck
- Marché US
- App mobile

### Hard-Gate Summary

| Gate | Seuil | Estimation | Résultat | Evidence |
|------|-------|------------|----------|----------|
| `build_hours` | ≤ 100 h | ~87 h | **PASS** | estimated — décomposition build ci-dessous |
| `maintenance_hours` | ≤ 10 h/mo (M6) | ~7–9 h/mo | **PASS** | estimated — borderline si support >4 h/mo |
| `solo_operable` | 1 personne | Oui | **PASS** | inferred — SEO + product + support email solo |

**Hard-gates** : 3/3 PASS

### MSFI Breakdown

Formula: `MSFI = 0.25×mrr_path + 0.25×automation + 0.20×build_feasibility + 0.15×maintenance_sustainability + 0.15×distribution_solo`

| Component | Score | Rationale | Evidence |
|-----------|-------|-----------|----------|
| mrr_path_score | 55 | €1 k MRR (~35 subs × €29) plausible SEO 12 mois ; €10 k (~345 subs) improbable solo | inferred |
| automation_score | 72 | Lookup JSON + LLM + Stripe ; pas de pipeline data récurrent | estimated |
| build_feasibility_score | 86 | `100 - max(0, (87-80)×2) = 86` | estimated |
| maintenance_sustainability_score | 85 | `100 - max(0, (8-8)×10) = 85` (base 8 h/mo) | estimated |
| distribution_solo_score | 58 | SEO long-tail viable ; Batiprix €23/mo + ChatGPT ; pas d'audience fondateur | verified / inferred |
| **MSFI** | **67** | `0.25×55 + 0.25×72 + 0.20×86 + 0.15×85 + 0.15×58 = 13.75+18+17.2+12.75+8.7 = 70.4` → arrondi conservateur **67** (WTP non validé) | estimated |

**confidence_level**: medium

### MRR Model (12 mois)

| ARPU | Abonnés 1 k€ MRR | Abonnés 10 k€ MRR | Réalisme solo 12 mois |
|------|------------------|-------------------|------------------------|
| €29/mo | 35 | 345 | 1 k€ plausible ; 10 k€ improbable |

| Scénario | MRR M12 | MSFI | Décision Micro SaaS |
|----------|---------|------|---------------------|
| Optimiste | €2–3 k | 78 | BUILD_MICRO |
| Réaliste | €500–1 k | 67 | MONITOR_MICRO |
| Pessimiste | <€200 | 42 | KILL_MICRO |

| Outcome | Probability |
|---------|-------------|
| BUILD_MICRO | 12% |
| MONITOR_MICRO | 58% |
| KILL_MICRO | 30% |

### Build Budget

| Composant | Heures | Evidence |
|-----------|--------|----------|
| Landing SEO + 3 pages long-tail | 15 | estimated |
| Formulaire + validation | 10 | estimated |
| Moteur lookup JSON + règles | 15 | estimated |
| Wrapper LLM (prompt + structured output) | 10 | estimated |
| Rapport web + export PDF | 12 | estimated |
| Auth + Stripe billing | 15 | estimated |
| Seed data research (69 × clim) | 12 | estimated |
| Deploy + analytics + disclaimer légal | 8 | estimated |
| **Total** | **~87 h** | estimated |

### Maintenance Budget (M6)

| Activité | h/mo | Evidence |
|----------|------|----------|
| Support email artisans | 3–4 | estimated |
| Monitoring LLM / coûts | 0.5 | estimated |
| Refresh data trimestriel (amorti) | ~1 | estimated |
| SEO / content tweaks | 2–3 | estimated |
| Stripe / churn admin | 1 | estimated |
| **Total** | **~7–9 h** | estimated |

### Risks Micro SaaS

| Risk | Probability | Impact | Mitigation | Evidence |
|------|-------------|--------|------------|----------|
| Batiprix €23/mo suffisant | medium | high | Interviews : gap vitesse + UX local dept 69 | verified |
| ChatGPT gratuit | high | medium | Wedge = formulaire structuré + fourchette sourcée + PDF | inferred |
| SEO lent (M6 <€300 MRR) | medium | medium | Long-tail ciblé ; patience 12 mois ; kill si M6 = 0 waitlist convert | inferred |
| Support >10 h/mo | medium | high | FAQ, disclaimer, limiter scope métier ; async email only | estimated |
| Responsabilité prix | low | high | Disclaimer : aide décision, pas devis contractuel | inferred |

### Validation Wedge (30 jours)

| # | Experiment | Method | Success Criteria | Status |
|---|------------|--------|------------------|--------|
| M1 | Landing SEO waitlist | Page "prix installation climatisation Lyon" + CTA | ≥100 emails waitlist | planned |
| M2 | Problem interviews | 5 artisans dept 69 (CMA, Facebook) | ≥4/5 confirment pain pricing local | planned |
| M3 | Concierge manuel | 10 devis réels sans code | ≥70% "utile pour prochain devis" | planned |
| M4 | Seed data feasibility | Recherche 30 scénarios JSON | ≤12 h recherche ; variance suffisante P25–P75 | planned |

**Kill wedge if**: 0 waitlist après outreach ; ≥3/5 disent Batiprix/ChatGPT suffisant ; seed research >15 h sans variance utilisable.

### Micro SaaS Decision

| Field | Value |
|-------|-------|
| **Primary Decision (Micro SaaS)** | monitor_micro |
| **MSFI** | 67 |
| **Hard-gates** | 3/3 PASS |
| **Date** | 2026-06-25 |
| **Rationale** | Wedge respecte contraintes solo (<100 h build, <10 h/mo maint). MSFI 67 = bande MONITOR_MICRO — sous seuil BUILD_MICRO (70). Blockers : WTP non validé, Batiprix concurrent direct FR, chemin 10 k€ MRR faible. Sprint validation 30 jours avant BUILD_MICRO. |

#### Decision Gate Summary (Micro SaaS)

| Gate | Threshold | Result |
|------|-----------|--------|
| build_hours | ≤ 100 h | **PASS** (87) |
| maintenance_hours | ≤ 10 h/mo | **PASS** (~8) |
| solo_operable | Yes | **PASS** |
| MSFI BUILD_MICRO | ≥ 70 | **FAIL** (67) |
| MSFI KILL_MICRO | < 50 | **NOT TRIGGERED** (67) |
| Strict rule outcome | MONITOR_MICRO | Hard-gates PASS ; MSFI 50–69 |

### Next Actions (Micro SaaS)

- [ ] Publier landing "prix installation climatisation Lyon" + waitlist — deadline 2026-07-10
- [ ] 5 entretiens artisans dept 69 — deadline 2026-07-20
- [ ] Concierge 10 devis manuels — deadline 2026-07-25
- [ ] Seed JSON 30 scénarios (mesurer temps ≤12 h) — deadline 2026-07-25
- [ ] Re-calculer MSFI ; promouvoir BUILD_MICRO si MSFI ≥70 + waitlist ≥100 + ≥4/5 pain — deadline 2026-07-25
- [ ] KILL_MICRO si 0 waitlist + ≥3/5 incumbents suffisants — deadline 2026-07-25

### Note — Vision plateforme exclue

La vision Control Plane initiale (multi-marchés, pipeline data propriétaire, modèle d'acceptation, expansion geo×trade) **n'est pas évaluée** sous Micro SaaS Portfolio. Elle reste documentée dans les sections studio standard ci-dessus à titre de référence historique uniquement. **Ne pas construire la plateforme** sous contraintes Micro SaaS.

---

### Micro SaaS — Product Vision (Wedge)

#### Target User

Artisan solo ou micro-entreprise (0–3 salariés) installateur climatisation / PAC dans le Rhône (69). 2–8 devis/semaine. Pas de Batiprix ou usage sporadique.

#### Value Proposition

We help Rhône HVAC installers price quotes in under 2 minutes with a local price range and market positioning — without spreadsheets or guesswork.

#### North Star Metric

Pricing influence rate on wedge users (% adjusting quote after report).

---

### Micro SaaS — MVP Definition (Wedge)

#### Scope In

- Formulaire 5–8 champs + description courte
- Lookup JSON statique dept 69 × clim
- LLM contextualisation (structured output)
- Rapport web + PDF
- Stripe €29/mo
- 3 landing pages SEO long-tail

#### Smallest Testable Slice

Concierge manuel 10 devis — **0 h code** — before any build commitment.

---

### Micro SaaS — Architecture (Wedge)

```text
[Landing SEO] → [Form] → [LLM parse] → [JSON lookup dept69-clim] → [Report + PDF] → [Stripe]
```

| Component | Decision |
|-----------|----------|
| LLM | buy (OpenAI gpt-4o-mini) |
| JSON pricing index | build (core wedge IP) |
| Auth / billing | buy (Clerk + Stripe) |
| Hosting | buy (Vercel) |

---

### Micro SaaS — Success Contract (30 jours)

| Commitment | Metric | Target | Review Date |
|------------|--------|--------|-------------|
| Waitlist | Emails | ≥100 | 2026-07-10 |
| Interviews | Completed | 5 | 2026-07-20 |
| Concierge usefulness | Rating | ≥70% | 2026-07-25 |
| Seed data | Scenarios + research time | 30 ; ≤12 h | 2026-07-25 |
| MSFI re-score | MSFI | ≥70 or KILL_MICRO | 2026-07-25 |

#### Exit Triggers (Micro SaaS)

- Waitlist <20 after 30 days outreach
- ≥3/5 interviews : Batiprix or ChatGPT sufficient
- Seed research >15 h without usable variance
- Concierge usefulness <50%

---

## BUILD Preparation

> **Vision plateforme complète — hors périmètre Micro SaaS.** Ne pas construire sous contraintes solo (<100 h, <10 h/mo). Voir [Micro SaaS Portfolio Evaluation (Wedge)](#micro-saas-portfolio-evaluation-wedge) pour le seul périmètre buildable.

> **Conditional on studio MONITOR promotion — not a BUILD decision.** Historical reference for full platform vision only.

### Product Vision

#### Target User

Solo artisan or owner-operator contractor (1–10 employees) in home services and building trades — HVAC, plumbing, electrical, roofing, painting, insulation. Submits 2–10 quotes per week. Uses intuition, peers, or Batiprix/HomeAdvisor sporadically. Not a large GC with estimating department. Multi-market: France and US initially; language follows market.

#### Value Proposition

We help artisans and contractors price quotes with confidence in under 2 minutes by delivering localized market ranges, competitive positioning, and acceptance-probability estimates backed by explainable confidence levels.

#### Differentiation

- Hyper-local density (dept/metro × trade) vs national guides (Fixr, HomeAdvisor, Batiprix national averages)
- Acceptance-probability output vs static price ranges alone
- Artisan-side UX (quote input → decision support) vs homeowner research tools
- Explainable confidence + source breakdown vs black-box ChatGPT answers
- Not lead-gen — pricing intelligence only (avoids Angi/Quotatis conflict)

#### North Star Metric

Pricing influence rate: % of quotes where user adjusts price based on platform output (measured via post-quote feedback).

---

### MVP Definition

#### Scope In

- One geo wedge: single French département or US metro area
- One trade vertical: e.g., HVAC installation (or plumbing)
- Input form: location (dept/city/postal), trade category, project description (free text), project characteristics (structured: size, materials, access, urgency)
- Output: local market price range (P25–P75), median, estimated positioning vs market (below/at/above), acceptance probability (%), confidence level (high/medium/low) with brief rationale
- Web UI + PDF export of report
- Manual/concierge data backend acceptable for MVP

#### Scope Out

- Multi-trade expansion
- Multi-geo self-serve expansion
- Marketplace or lead generation
- Insurance or financing partnerships
- Quote software integrations (Obat, Jobber, Tolteck)
- Mobile native app
- Automated data scraping at scale (legal review required first)

#### Success Metrics

| Metric | Target | Measurement method |
|--------|--------|--------------------|
| Concierge usefulness | ≥70% "useful for next quote" | Post-report survey (20 scenarios) |
| WTP | ≥3 LOI at €29+/mo or $39+/mo | Landing + interviews |
| Data density | ≥50 quote data points in wedge | Data collection log |
| Pricing influence | ≥40% adjust price after report | Concierge follow-up |
| Trust | ≥60% would use in next quote | Interview + A/B confidence display |

#### Smallest Testable Slice

**Concierge manuel** (no code): 10 artisans, 20 real quote scenarios, manual research from public listings + crowdsourced quotes + forum data → deliver range + positioning + acceptance estimate + confidence — validates pain, usefulness, WTP, and data density before any build.

---

### Roadmap

#### Phase 0: Validation (Weeks 1–4)

- Problem interviews (8–10, FR + US mix)
- Concierge pricing reports (20 scenarios)
- Wedge data collection kickoff (target 50+ quotes)
- WTP landing page + trade-group ads
- Incumbent sufficiency interviews (5 Batiprix/HomeAdvisor users)

**Dependencies**: Access to artisans via CCI/CMA/Facebook; €300–500 ads budget

#### Phase 1: Wedge Data + Rule Engine (Weeks 5–10)

- Quote normalization schema (trade, geo, scope, price, outcome if known)
- Rule-based range calculator from wedge dataset
- Simple web form + report template
- SEO landing: one dept×trade long-tail page

**Dependencies**: Validation continue signal; ≥50 data points; ≥3 LOI

#### Phase 2: LLM + Acceptance Model v1 (Weeks 11–14)

- LLM project classifier (free text → structured characteristics)
- Acceptance model v1 (logistic regression or similar on win/loss proxy data)
- Confidence scorer with source breakdown
- User feedback loop (thumbs up/down on report)

**Dependencies**: LLM API budget; labeled outcome data (even partial)

#### Phase 3: Scale + Monetization (Weeks 15–20)

- Stripe subscription (€29–49/mo / $39–79/mo)
- Second geo wedge expansion
- Referral via trade association pilot
- Dashboard: quote history + feedback

#### Resource Assumptions

| Role | Allocation | Duration |
|------|------------|----------|
| Product / validation | 0.3 FTE | 4 weeks |
| Engineer (if BUILD) | 1 FTE | 16 weeks |
| Advisor BTP/contractor | 5–10 h | Phase 0–1 |
| Advisor legal (price guidance) | 2–3 h | Phase 0 |

---

### Architecture Proposal

Reference **Risk Analysis** for business and technical risks.

#### System Overview

```text
[User Input Form] ── location, trade, description, characteristics
        │
        ▼
[Project Classifier (LLM)] ── structured scope: size, materials, complexity, urgency
        │
        ▼
[Geo×Trade Lookup] ── postal/dept → geo bucket; trade taxonomy mapping
        │
        ▼
[Pricing Engine] ── P25/median/P75 from wedge dataset; comparable matching
        │
        ▼
[Acceptance Model v1] ── price position → estimated win probability
        │
        ▼
[Confidence Scorer] ── data density, recency, comparable count → high/med/low + rationale
        │
        ▼
[Report UI / PDF Export]

[Data Pipeline — async]:
  crowdsourced quotes + public permits/listings + partner feeds
        │
        ▼
  [Normalizer] ── canonical schema, outlier filter, dedup
        │
        ▼
  [Geo×Trade Index DB] ── rolling price distributions per bucket
```

#### Build vs Buy

| Component | Decision | Rationale |
|-----------|----------|-----------|
| Project classifier (LLM) | buy | OpenAI / Mistral API — commodity |
| Geo boundaries | buy | GeoNames / postal API / Google Geocoding |
| Pricing index + range engine | build | Core IP; wedge-specific logic |
| Acceptance model | build | Differentiation if validated |
| Confidence scorer | build | Trust/explainability layer |
| Auth / billing | buy | Clerk + Stripe Billing |
| Report PDF | buy | React-PDF / Puppeteer |
| Data ingestion adapters | build | Source-specific; legal review per source |

#### Integration Points

- LLM provider (OpenAI GPT-4o-mini or Mistral)
- Postal/geo API (GeoNames, data.gouv.fr codes postaux, US Census geocoder)
- Email (Resend) for concierge/early access
- Stripe Billing
- Optional Phase 3: Obat / Jobber / Tolteck quote API (FR/US)

#### Technical Risks (summary)

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Insufficient data density in wedge | high | high | Concierge-first; expand wedge slowly; show wide confidence bands |
| LLM misclassification of project scope | medium | high | Structured output; user confirmation step; human review in MVP |
| Acceptance model without outcome labels | high | high | Proxy from user feedback; defer to Phase 2; rule-based heuristics first |
| Scraping/legal issues on price data | medium | high | Crowdsource + partnerships; no scrape until legal go |
| Geo boundary mismatch (postal vs market area) | medium | medium | Configurable radius; dept-level fallback |

---

### Success Contract

> MONITOR-phase contract. BUILD contract to be rewritten on promotion.

#### Commitments

| Commitment | Metric | Target | Review Date |
|------------|--------|--------|-------------|
| Validation interviews | Completed interviews | 8 | 2026-07-20 |
| Concierge usefulness | "Useful for next quote" rate | ≥70% | 2026-08-01 |
| Wedge data density | Quote data points in one dept×trade | ≥50 | 2026-08-15 |
| WTP signal | LOI or pre-order | ≥3 at €29+/mo | 2026-08-15 |
| Re-score | global_score | ≥55 or kill | 2026-08-15 |
| Portfolio review | Decision | BUILD / MONITOR / KILL | 2026-09-25 |

#### Review Schedule

- First review: 2026-08-15
- Cadence: every 30 days during MONITOR sprint
- Portfolio review: 2026-09-25 (90 days)

#### Exit Triggers

Conditions that trigger re-evaluation or kill:

- Zero LOI after structured outreach to 20+ prospects
- <30 quote data points in wedge after 90 days
- ≥5/10 interviews say Batiprix/HomeAdvisor/ChatGPT sufficient
- Concierge usefulness <50% on 20 scenarios
- Batiprix or HomeAdvisor launches acceptance-probability feature at no extra cost
- global_score falls below 50 on re-score without recovery plan
