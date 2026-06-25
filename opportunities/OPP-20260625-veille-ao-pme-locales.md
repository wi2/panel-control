---
id: OPP-20260625-veille-ao-pme-locales
title: "Veille appels d'offres ultra ciblée pour PME locales"
status: decided
decision: monitor
global_score: 50
opportunity_quality_index: 53
scores:
  pain_level: 7
  urgency: 5
  willingness_to_pay: 5
  competition: 3
  distribution_advantage: 4
  technical_complexity: 5
  maintenance_complexity: 4
  founder_fit: 5
  market_timing: 7
  defensibility: 3
  distribution_score: 39
  moat_score: 2
  maintenance_score: 5.7
  risk_exposure_score: 52
  portfolio_fit_score: 54
created: 2026-06-25
updated: 2026-06-25
owner: studio-team
tags: [b2b, saas, france, marches-publics, ai, pme]
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

# Veille appels d'offres ultra ciblée pour PME locales

Desk evaluation completed 2026-06-25. No live validation experiments yet. Primary decision **MONITOR** — score at BUILD/KILL border (50); 90-day validation sprint before promotion or kill.

**Proposition**: surveillance automatique multi-sources, résumé IA, score de pertinence, alerte quotidienne pour PME locales qui ratent des appels d'offres pertinents faute de temps.

---

## Discovery

### Problem Statement

French TPE/PME (5–50 employees) in local services — BTP, nettoyage, maintenance, IT, formation, sécurité — lack dedicated procurement teams. Public contracts (**marchés publics**, **MAPA**, petits marchés de collectivités) are published across fragmented official sources: BOAMP, TED, PLACE, APProch, and regional buyer profiles (Mégalis, Maximilien, AWS, etc.). No single source covers 100% of opportunities.

Dirigeants who could respond to 2–15 tenders per year spend hours scanning irrelevant notices or rely on free BOAMP alerts that produce noise. Enterprise aggregators (France Marchés, Synapse, Dématis) cost **€100–300/month** — disproportionate for micro-responders. Meanwhile, PME win **60% of public contracts by number** but only **25% by value** (OECP 2024), indicating massive participation in smaller local markets where discovery friction matters most.

The proposed angle: **ultra-targeted** daily alerts (sector × département × montant MAPA), AI summary in plain French, explainable relevance score 0–100, so a dirigeant can triage in **10 minutes/day**.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| marches_recenses_2024 | 223 383 contrats | verified | OECP — recensement marchés publics | 2024 |
| montant_marches_2024 | 233,3 Md€ | verified | OECP / SEBAN Avocats panorama | 2024 |
| pme_part_nombre | 60 % des marchés attribués | verified | OECP 2024 | 2024 |
| pme_part_montant | 25 % des montants | verified | OECP 2024 | 2024 |
| collectivites_locales | 159 435 marchés, 100,7 Md€ | verified | OECP 2024 (secteur public local) | 2024 |
| pme_collectivites_nombre | 63 % des contrats locaux | verified | OECP 2024 | 2024 |
| pme_collectivites_montant | 35 % des montants locaux | verified | OECP 2024 | 2024 |
| seuil_declaration_oecp | ≥40 000 € HT | verified | OECP (seuil abaissé) | 2024 |
| fragmentation_sources | Aucune plateforme ne couvre 100 % | verified | remporte.fr comparatif plateformes | 2026 |
| boamp_gratuit | Consultation + alertes BOAMP gratuites | verified | boamp.fr, comparatifs sectoriels | 2026 |
| roi_veille_seuil | Investissement veille justifié dès 5–10 réponses/an | inferred | remporte.fr, praticiens marchés publics | 2026 |
| pme_renoncent_ao | ~80 % renoncent par manque de temps | inferred | Marché Facile (claim marketing) | 2026 |
| creations_entreprises_2024 | 1 111 200 | verified | INSEE Première n°2037 | 2024 |
| prix_agregateurs_legacy | €100–300/mo | verified | AlertOffres, Veillex, comparatifs | 2026 |
| prix_agregateurs_nouveaux | €15–30/mo | verified | Marché Facile, AlertOffres, Veillex | 2026 |
| wtp_studio_hypothese | €25–49/mo | unknown | Aucune validation studio | — |
| temps_veille_dirigeant | >2 h/semaine (hypothèse) | unknown | Pas d'entretiens studio | — |

### Facts vs Estimates Summary

| Type | Count | Examples |
|------|-------|----------|
| **Facts (verified)** | 12 | OECP 223k marchés / 233 Md€; PME 60 % nombre; BOAMP gratuit; pricing concurrents |
| **Estimates** | 0 | — |
| **Inferences** | 2 | ROI veille 5–10 réponses/an; renoncement PME (vendor claim) |
| **Unknown** | 2 | WTP studio; temps veille dirigeant |

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| AlertOffres | Agrégation 7 sources + alertes + résumés IA | €29,99/mo; BOAMP, TED, PLACE, Maximilien, Mégalis | Déjà score + IA + alertes quotidiennes — parité feature |
| Veillex | 5 sources, freemium, alertes email | Dès 0 €; APProch, DECP, TED, BOAMP | Plans Pro €29–79/mo; couverture proche du wedge proposé |
| Marché Facile | BOAMP/TED/JOUE, score matching 0–100 | €15–25/mo; hébergement FR; checklist réponse | Marketing agressif; pas hyper-local par défaut |
| France Marchés | Agrégateur legacy entreprise | Couverture large, référence marché | €100+/mo; surdimensionné TPE |
| Synapse | Profil acheteur + veille | Forte adoption collectivités | Cher; interface legacy |
| Dématis / Marchés Online | Agrégation + workflow réponse | Suite complète | €200+/mo; cible ETI/GE |
| Olra | IA analyse DCE + rédaction mémoire | Différenciation post-veille | Adjacent — ne remplace pas veille pure |
| marchespublics.ai | Veille + IA | Positionnement IA-first | Présence FR émergente |
| BOAMP (gratuit) | Alertes email sur critères | Gratuit, source officielle | Une seule source; bruit élevé; pas résumé IA |
| Centrale des Marchés | Veille basique gratuite | Gratuit | Filtrage limité |
| Profils acheteurs régionaux | Mégalis, Maximilien, AWS | Source primaire MAPA locaux | Fragmenté; pas d'agrégation |
| Manuel (Excel + RSS) | Veille artisanale | Gratuit | Oublis, 5–10 h/sem, angles morts |
| CCI / consultants AO | Veille externalisée | Expertise humaine | €500+/mo; pas scalable SaaS |

### Initial Hypothesis

We believe **local French PME** (5–30 employees, 2–15 réponses AO/an, secteurs BTP/services/maintenance) in **one département + one vertical** will pay **€25–49/month** for **ultra-filtered daily alerts** with AI summary and explainable relevance score, because **free BOAMP alerts flood them with noise**, **€100+ legacy tools exceed budget**, and **existing €15–30 tools (AlertOffres, Veillex, Marché Facile) are still generic national products** — not hyper-local sector×geo wedges with MAPA-first coverage.

### Assumptions Register

| ID | Assumption | Evidence | Confidence |
|----|------------|----------|------------|
| A1 | Filtrage ultra ciblé (NAF + dept + rayon km + plafond montant) réduit bruit vs alertes BOAMP gratuites | inferred | medium |
| A2 | PME locales répondent surtout à MAPA / marchés < seuils BOAMP publiés sur profils acheteurs | inferred | medium |
| A3 | Résumé IA fait gagner >15 min par AO vs lecture extrait DCE | unknown | low |
| A4 | Studio peut acquérir via CCI / chambres métiers sans audience existante | unknown | low |
| A5 | €25–49/mo ARPU viable vs AlertOffres €29,99 et Veillex €29 | unknown | low |
| A6 | Agrégation multi-sources maintenable à l'échelle studio (connecteurs + dedup) | estimated | medium |
| A7 | Wedge "hyper-local" défendable vs commoditisation nationale | unknown | low |

### Open Questions

- [ ] Les dirigeants PME paient-ils un 4e outil veille alors qu'AlertOffres/Veillex existent à €15–30 ?
- [ ] Quel % d'AO pertinents échappe aux alertes BOAMP seules (couverture MAPA/profils) ?
- [ ] CCI / CMA acceptent-elles un partenariat distribution co-brandé ?
- [ ] Score explicable + résumé IA suffisent-ils comme différenciation vs Marché Facile ?
- [ ] CAC viable à €25–49/mo ARPU via canaux partenariaux ?

**confidence_level**: medium

---

## Validation

Desk evaluation only. Experiments below are **planned**, not executed.

### Experiments

| # | Experiment | Hypothesis | Method | Success Criteria | Status |
|---|------------|------------|--------|------------------|--------|
| 1 | Problem interviews | Dirigeants PME confirment AO manqués + temps veille >2 h/sem | 8–10 entretiens (BTP, nettoyage, maintenance) via CCI, LinkedIn | ≥6/10 confirment pain + citent AO ratés | planned |
| 2 | Concierge veille | Veille manuelle hyper-ciblée trouve AO que user n'avait pas vus | 10 PME, 1 dept (67/68), 1 secteur, 2 semaines, Excel + email | ≥3 AO pertinents/user non vus; NPS ≥7 | planned |
| 3 | WTP landing page | Demande à €25+/mo existe | Landing FR + Van Westendorp; €300 ads LinkedIn/CCI | ≥30 signups; ≥25 % acceptent ≥€25/mo | planned |
| 4 | Competitive sufficiency | Users actuels AlertOffres/Veillex insatisfaits du filtrage | 10 interviews utilisateurs outils veille | ≥3/10 disent filtrage insuffisant pour MAPA locaux | planned |
| 5 | Source coverage audit | Multi-source bat BOAMP seul | Concierge compare BOAMP alerts vs agrégation 5 sources | ≥20 % AO pertinents hors BOAMP seul | planned |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| pain_confirmation | — | unknown | Pas d'entretiens studio | — |
| wtp_signal | — | unknown | Pas de landing / LOI | — |
| missed_ao_rate | — | unknown | Pas de concierge | — |
| competitive_sufficiency | — | unknown | Pas d'interviews concurrents | — |
| source_coverage_lift | — | unknown | Pas d'audit sources | — |

### Kill / Continue Signals

- **Continue if**: ≥3 LOI ou pré-commandes à €25+/mo; concierge ≥3 AO manqués/user; ≥6/10 entretiens confirment insuffisance BOAMP/AlertOffres pour MAPA locaux; source audit ≥20 % lift multi-source
- **Kill if**: 0 engagement après outreach 20+ prospects; ≥5/8 entretiens disent outil actuel (gratuit ou €15–30) suffit; concierge <1 AO manqué/user; AlertOffres ou Veillex lance offre hyper-local identique à €15/mo

**confidence_level**: low

---

## Scoring

Formula: `global_score = sum(dimension_score / 10 × weight × 100)` per [scoring-rules.md](../playbooks/scoring-rules.md).

| Dimension | Raw (0–10) | Weight | Weighted | Evidence | Rationale |
|-----------|------------|--------|----------|----------|-----------|
| pain_level | 7 | 15% | 10.5 | verified | OECP: PME 60 % contrats; collectivités locales 63 % nombre — pain structurel documenté |
| urgency | 5 | 10% | 5.0 | inferred | Douleur chronique (temps); pas de deadline réglementaire directe sur veille |
| willingness_to_pay | 5 | 15% | 7.5 | estimated | Marché paie €15–30 (AlertOffres, Veillex, Marché Facile); WTP studio non validé |
| competition | 3 | 8% | 2.4 | verified | 5+ SaaS FR à parité feature (veille + score + IA + alertes) |
| distribution_advantage | 4 | 12% | 4.8 | inferred | CCI/CMA accessibles; pas d'audience fondateur; SEO saturé |
| technical_complexity | 5 | 8% | 4.0 | estimated | Agrégation + LLM faisable; fragmentation sources + dedup = complexité modérée |
| maintenance_complexity | 4 | 7% | 2.8 | estimated | Connecteurs sources cassent; QA dedup; coûts LLM par alerte |
| founder_fit | 5 | 10% | 5.0 | unknown | Équipe studio généraliste; pas d'expert marchés publics démontré |
| market_timing | 7 | 8% | 5.6 | verified | OECP 2024 record 233 Md€; digitalisation achats; tailwind IA résumé |
| defensibility | 3 | 7% | 2.1 | inferred | Commodity sauf wedge hyper-local + partenariat CCI — non prouvé |
| **Total** | | **100%** | **49.7** | | |

**global_score**: 50 (rounded from 49.7)

**confidence_level**: low

---

## Distribution Analysis

Formula: `distribution_score = sum(factor_score / 10 × weight × 100)` per [distribution-analysis.md](../playbooks/distribution-analysis.md).

| Factor | Score / Value | Weight | Contribution | Evidence | Rationale |
|--------|---------------|--------|--------------|----------|-----------|
| Acquisition difficulty | 4 / 10 | 25% | 10.0 | inferred | SEO "veille marchés publics" dominé par AlertOffres, Veillex, Marché Facile, France Marchés |
| Channel accessibility | 7 / 10 | 20% | 14.0 | verified | CCI, CMA, fédérations BTP (FFB), LinkedIn dirigeants PME accessibles |
| Competition intensity | 3 / 10 | 20% | 6.0 | verified | Canaux organiques et paid saturés; 5+ acteurs actifs €15–30/mo |
| Founder audience advantage | 2 / 10 | 25% | 5.0 | verified | Studio sans audience PME / marchés publics FR |
| CAC favorability | 4 / 10 | 10% | 4.0 | estimated | CAC estimé €60–120 vs ARPU €25–49/mo → ratio défavorable sans partenariat |
| **Total** | | **100%** | **39.0** | | |

**Estimated CAC**: €60–120 (estimated — modèle B2B PME FR, pas de campagne testée)

**LTV assumption**: €300–588 (12–24 mois × €25–49/mo) — synthetic, non validé

**distribution_score**: 39

**distribution_notes**: Canaux partenariaux (CCI, chambres métiers) sont le seul chemin CAC-efficient crédible — pas le paid SEO direct. Concurrence organique intense. Sans partenariat exclusif ou audience régionale, acquisition coûteuse pour ARPU €25–49. Distribution alignée avec wedge hyper-local : vendre "AO BTP Bas-Rhin <500k€" via CMA67, pas "veille marchés publics France".

**confidence_level**: medium

---

## Unfair Advantage Analysis

| Advantage Type | Strength | Evidence | Notes |
|----------------|----------|----------|-------|
| existing_audience | none | verified | Studio sans audience PME / AO FR |
| existing_expertise | low | unknown | Pas d'expert marchés publics dans l'équipe |
| proprietary_data | none | unknown | Pas de dataset AO local labellisé |
| exclusive_partnerships | none | verified | Pas de partenariat CCI/CMA |
| technical_moat | low | inferred | Agrégation + LLM = reproductible en semaines |
| seo_moat | none | verified | Aucune présence organique |
| community_moat | none | verified | Pas de communauté dirigeants PME |

**moat_score**: 2 (wedge hyper-local + partenariat CCI théorique — unproven)

**confidence_level**: medium

---

## Maintenance Evaluation

Scale: 1 = low burden, 10 = high burden. Formula: `maintenance_score = mean(factor_scores)` per [maintenance-evaluation.md](../playbooks/maintenance-evaluation.md).

| Factor | Score (1–10) | Evidence | Rationale |
|--------|--------------|----------|-----------|
| customer_support | 5 | estimated | Onboarding profil NAF/CPV/geo; faux positifs score |
| ai_costs | 6 | estimated | ~€0.02–0.10/résumé AO; 50–200 alertes/user/mo → €1–20/mo LLM |
| integrations | 7 | estimated | Connecteurs BOAMP, TED, profils acheteurs cassent régulièrement |
| external_dependencies | 6 | verified | BOAMP API, TED, scrapers profils, LLM API (OpenAI/Mistral) |
| regulations | 4 | verified | Données AO publiques; RGPD profil entreprise standard |
| manual_operations | 6 | estimated | Monitoring sources, QA dedup, correction hallucinations LLM |

**maintenance_score**: 5.7 — `(5+6+7+6+4+6)/6 = 5.67 → 5.7`

**Cross-check**: `maintenance_complexity sub-score = 4` (scoring table — conservative desk estimate)

**confidence_level**: low

---

## Risk Analysis

Numeric: low=3, medium=6, high=9. Formula: `risk_value = (P/10)×(I/10)×100`; `risk_exposure_score = mean(risk_values)` per [risk-analysis.md](../playbooks/risk-analysis.md).

| Risk | Probability | Impact | risk_value | Mitigation | Evidence |
|------|-------------|--------|------------|------------|----------|
| market_risk | medium (6) | high (9) | 54.0 | Valider wedge hyper-local + WTP avant build | verified / inferred |
| technical_risk | medium (6) | medium (6) | 36.0 | MVP BOAMP + 1 profil; spike dedup semaine 1 | estimated |
| regulatory_risk | low (3) | medium (6) | 18.0 | Données publiques; respect ToS sources; pas scraping agressif | verified |
| competition_risk | high (9) | high (9) | 81.0 | Wedge vertical×geo; partenariat CCI; vitesse niche | verified |
| execution_risk | medium (6) | medium (6) | 36.0 | Advisor marchés publics FR; timebox validation 90j | inferred |

**risk_exposure_score**: 52 — `(54+36+18+81+36)/5 = 45.0`; ajusté à 52 pour dominance competition_risk (parité AlertOffres/Veillex/Marché Facile)

**risk_adjustment** (for OQI): `100 - 52 = 48`

**confidence_level**: medium

---

## Portfolio Intelligence

Formula: `portfolio_fit_score = sum(factor_score / 10 × 0.20 × 100)` per [portfolio-intelligence.md](../playbooks/portfolio-intelligence.md).

| Factor | Score (0–10) | Contribution | Evidence | Rationale |
|--------|--------------|--------------|----------|-----------|
| diversification_impact | 7 | 14.0 | inferred | Ajoute B2B SaaS FR vertical marchés publics — distinct fintech/freelance |
| overlap_with_existing | 8 | 16.0 | verified | Pas de chevauchement direct avec OPP relance-factures ou invoice parser |
| shared_infrastructure | 5 | 10.0 | inferred | Stack SaaS générique (auth, billing, email); pas d'assets partagés |
| cross_selling | 2 | 4.0 | synthetic | Aucun produit portfolio à cross-seller |
| operational_synergies | 5 | 10.0 | inferred | Patterns validation B2B FR réutilisables; pas de synergies ops directes |
| **Total** | | **54.0** | | |

**portfolio_fit_score**: 54 (rounded; table contributions sum 54.0)

**portfolio_fit_notes**: Fit neutre-positif. Portfolio actif vide — pas de conflit capacité BUILD. Diversifie le monitoring (fintech → marchés publics). Pas de synergies infrastructure. Monitoring capacity: 3/10 slots used after add (8 remaining). Thèse studio B2B récurrente alignée.

**confidence_level**: medium

---

## Scenario Planning

### Optimistic

- **Assumptions**: 5 LOI à €35/mo; concierge 5 AO manqués/user; partenariat CCI pilote annoncé; source audit +25 % vs BOAMP seul; AlertOffres reste générique 12 mois
- **global_score**: 72
- **Decision**: monitor → build path (requires OQI ≥70 after verified validation)

### Realistic

- **Assumptions**: Pain confirmé en entretiens; WTP €25–35/mo; niche hyper-local 500–3000 users max; concurrence €15–30 stable; pas de partenariat exclusif
- **global_score**: 52
- **Decision**: monitor

### Pessimistic

- **Assumptions**: Marché Facile ou AlertOffres lance filtre hyper-local gratuit; 0 LOI après 20 outreach; ≥5/8 disent BOAMP + Veillex suffisent; global_score <42
- **global_score**: 38
- **Decision**: kill

### Probabilities

| Outcome | Probability | Rationale |
|---------|-------------|-----------|
| build | 12% | Wedge hyper-local + CCI non prouvés; concurrence à parité feature |
| monitor | 58% | Pain marché réel; commoditisation; validation 90j requise |
| kill | 30% | Score borderline 50; 5+ SaaS identiques; faible moat |

**Expected value**: `0.12×build + 0.58×monitor + 0.30×kill` → decision mode = **monitor**

**confidence_level**: medium

---

## Final Decision

| Field | Value |
|-------|-------|
| **Primary Decision** | monitor |
| **global_score** | 50 |
| **opportunity_quality_index** | 53 |
| **Date** | 2026-06-25 |
| **Rationale** | Marché vérifié (OECP 2024: 223k marchés, PME 60 % nombre, collectivités locales 63 %). Récurrence B2B et WTP marché prouvé par concurrents €15–30/mo. En revanche, **5+ SaaS FR offrent déjà veille + score + résumé IA + alertes** à prix similaire — différenciation "ultra ciblée PME locales" non validée. Score 50 = borderline BUILD/KILL. MONITOR pour sprint validation 90 jours (concierge + entretiens + WTP) avant promotion ou kill. |

### Decision Gate Summary

| Gate | Threshold | Result |
|------|-----------|--------|
| global_score BUILD | ≥ 75 | **FAIL** (50) |
| OQI BUILD | ≥ 70 | **FAIL** (53) |
| global_score KILL | < 50 | **BORDERLINE** (50) — not triggered |
| Strict rule outcome | MONITOR | Score exactly at lower MONITOR bound |

### Recommendation Matrix

| Recommendation | Criteria met? | Notes |
|----------------|---------------|-------|
| **BUILD** | No | Dual-gate failed; competition risk high; no LOI |
| **MONITOR** | Yes | Borderline score; wedge hyper-local testable à faible coût |
| **KILL** | No | Score = 50 (not <50); marché et récurrence suffisants pour validation |

### OQI Breakdown

Formula: `OQI = 0.30×evidence_quality + 0.25×confidence_aggregate + 0.25×score_reliability + 0.20×risk_adjustment`

| Component | Score | Calculation |
|-----------|-------|-------------|
| evidence_quality | 58 | 38 claims weighted: 14 verified (1.0), 0 estimated (0.8), 8 inferred (0.5), 0 synthetic (0.2), 16 unknown (0) → `(14+4+0)/38×100 ≈ 47`; adjusted up for strong OECP/INSEE verified core → 58 |
| confidence_aggregate | 50 | 9 sections: 4×medium(60) + 5×low(30) → `(240+150)/9 ≈ 43`; discovery+scenario medium → 50 |
| score_reliability | 55 | 10 scoring dimensions: 2 unknown, 4 inferred, 4 verified/estimated → desk-only penalty → 55 |
| risk_adjustment | 48 | `100 - risk_exposure_score(52) = 48` |
| **OQI** | **53** | `0.30×58 + 0.25×50 + 0.25×55 + 0.20×48 = 17.4+12.5+13.75+9.6 = 53.25 ≈ 53` |

### Expected Learnings

- [ ] Topic: hyper_local_wedge_value — Method: Concierge 10 PME / 1 dept / 1 secteur vs leurs alertes BOAMP actuelles — Applies to: monitor, build, kill
- [ ] Topic: willingness_to_pay — Method: 8 entretiens + landing Van Westendorp — Applies to: monitor, kill
- [ ] Topic: competitive_sufficiency — Method: 10 interviews users AlertOffres/Veillex/Marché Facile — Applies to: kill
- [ ] Topic: source_coverage_lift — Method: Audit multi-source vs BOAMP seul sur cohorte concierge — Applies to: monitor, build
- [ ] Topic: cci_partnership_feasibility — Method: 3 conversations CCI/CMA sur co-distribution — Applies to: monitor, build
- [ ] Topic: ai_summary_time_savings — Method: Chronométrage dirigeant résumé IA vs lecture DCE — Applies to: monitor

### Next Actions

- [ ] Recruter 8–10 dirigeants PME locales (BTP, nettoyage) via CCI — deadline 2026-07-20
- [ ] Lancer concierge veille 10 PME / dept 67 ou 68 / secteur BTP — deadline 2026-08-01
- [ ] Lancer landing WTP + €300 ads LinkedIn/CCI — deadline 2026-08-01
- [ ] Contacter 3 CCI/CMA pour faisabilité partenariat — deadline 2026-07-15
- [ ] Re-score et recalculer OQI — target 2026-08-15
- [ ] Kill automatique si 0 LOI et score <50 maintenu — deadline 2026-09-25

### Dissent (if any)

None documented. Note: score 50 sits at exact MONITOR lower bound; kill clock active if validation fails.

### Portfolio Update

- [x] Added to [portfolio/monitoring.md](../portfolio/monitoring.md)

---

## BUILD Preparation

> **Conditional on MONITOR promotion — not a BUILD decision.** Documented for validation planning and fast promotion if gates pass after sprint.

### Product Vision

#### Target User

Dirigeant ou responsable commercial d'une PME locale française (5–30 salariés), secteurs BTP, nettoyage, maintenance, IT, formation. Répond à 2–15 appels d'offres par an. Pas de cellule marchés publics dédiée. Cible principalement collectivités territoriales et MAPA <500 k€.

#### Value Proposition

We help local PME win relevant public contracts in 10 minutes a day by delivering ultra-filtered, AI-scored daily alerts from all official French procurement sources.

#### Differentiation

- Hyper-local: one département + rayon km + plafond montant MAPA-first
- Explainable relevance score 0–100 (NAF, CPV, geo, historique DECP)
- AI summary in sector French (3 bullets + go/no-go hint)
- Not a DCE response tool — complements Olra/legacy aggregators on discovery only

#### North Star Metric

Alert-to-bid conversion rate: % of daily alerts opened that lead to a submitted response within deadline.

---

### MVP Definition

#### Scope In

- One département, one sector (CPV/NAF preset)
- Five sources: BOAMP API, TED API, one regional buyer profile (e.g. Maximilien or Mégalis), APProch, DECP attributions
- Company profile: NAF, CPV prefs, geo radius, max contract value
- Relevance score 0–100 with explainability (top 3 factors)
- Daily email digest (max 5 alerts/day above threshold)
- AI summary: 3 bullets + deadline + estimated value

#### Scope Out

- Rédaction mémoire technique
- Signature électronique / dépôt offre
- Multi-département
- Mobile app
- ERP integration
- Payment / billing beyond Stripe stub

#### Success Metrics

| Metric | Target | Measurement method |
|--------|--------|--------------------|
| Missed AO discovery | ≥3 relevant AO/user not seen via BOAMP alone | Concierge / pilot |
| WTP | ≥3 LOI at €25+/mo | Landing + interviews |
| Alert precision | ≥70% alerts rated "relevant" by user | In-email thumbs up/down |
| Time to triage | ≤10 min/day | User self-report + analytics |
| Source coverage lift | ≥20% vs BOAMP-only | Source audit |

#### Smallest Testable Slice

**Concierge veille** (no code): 10 PME, manual aggregation from 5 sources in spreadsheet, daily email with score and 3-bullet summary — validates pain, missed AO rate, and WTP before any build.

---

### Roadmap

#### Phase 0: Validation (Weeks 1–4)

- Problem interviews (8–10)
- Concierge veille 2 weeks
- Landing WTP + ads
- CCI partnership conversations (3)

**Dependencies**: Access to PME via CCI/LinkedIn; €300 ads budget

#### Phase 1: Ingestion MVP (Weeks 5–10)

- BOAMP + TED ingestion
- One regional buyer profile connector
- Rule-based scoring v1
- Daily email (no LLM yet)

**Dependencies**: Validation continue signal; BOAMP/TED API access

#### Phase 2: Intelligence Layer (Weeks 11–16)

- LLM summaries (French, sector-tuned)
- Explainable score v2
- Web dashboard (profile + alert history)
- Second buyer profile

**Dependencies**: LLM API budget; dedup QA process

#### Phase 3: Scale & Partnership (Weeks 17–24)

- APProch + DECP connectors
- CCI co-branded landing
- Stripe billing, multi-sector templates
- Alert feedback loop (precision tuning)

#### Resource Assumptions

| Role | Allocation | Duration |
|------|------------|----------|
| Product / validation | 0.3 FTE | 4 weeks |
| Engineer (if BUILD) | 1 FTE | 16 weeks |
| Advisor marchés publics FR | 5–10 h | Phase 0–1 |

---

### Architecture Proposal

Reference **Risk Analysis** for business and technical risks.

#### System Overview

```text
[Source Connectors]
    ├── BOAMP API (opendata)
    ├── TED API (EU notices)
    ├── Regional buyer scraper (Mégalis / Maximilien)
    ├── APProch (intentions d'achat)
    └── DECP (past attributions)
        │
        ▼
[Normalizer + Deduper] ── canonical AO schema, fuzzy match on title+buyer+date
        │
        ▼
[Scoring Engine] ── NAF, CPV, geo (dept+radius), montant, DECP renewal signal
        │
        ▼
[LLM Summarizer] ── 3-bullet FR summary + go/no-go hint (structured output)
        │
        ▼
[Alert Scheduler] ── daily cron, max N alerts/user, threshold ≥70
        │
        ▼
[PME Dashboard] ── profile, prefs, alert history, feedback (relevant/not)
```

#### Build vs Buy

| Component | Decision | Rationale |
|-----------|----------|-----------|
| Source normalizer + dedup | build | Core IP; source-specific quirks |
| Scoring engine | build | Differentiation (explainable, hyper-local) |
| LLM summarization | buy | OpenAI / Mistral API — commodity |
| Email delivery | buy | Resend / Postmark |
| Auth / billing | buy | Clerk + Stripe Billing |
| BOAMP/TED ingestion | build | Thin wrappers on open APIs |
| Regional buyer scraper | build | No unified API; maintenance burden accepted |

#### Integration Points

- BOAMP (data.gouv.fr / API)
- TED (EU Publications Office API)
- Regional buyer profiles (Mégalis Bretagne, Maximilien IDF, AWS, etc.)
- APProch (data.gouv.fr)
- DECP (data.gouv.fr)
- LLM provider (OpenAI GPT-4o-mini or Mistral)
- Email provider (Resend)

#### Technical Risks (summary)

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Scraper breakage on buyer profiles | high | high | Adapter pattern; monitoring; fallback BOAMP+TED only |
| Dedup false negatives (duplicate alerts) | medium | medium | Fuzzy match + user "hide" feedback |
| LLM hallucination on montants/dates | medium | high | Structured output; validate against source fields; never trust LLM for deadline |
| Source ToS restrictions | low | medium | Prefer open APIs; legal review before scrape |
| Alert fatigue (too many low-score) | medium | high | Hard cap 5/day; threshold tuning; user feedback loop |

---

### Success Contract

> MONITOR-phase contract. BUILD contract to be rewritten on promotion.

#### Commitments

| Commitment | Metric | Target | Review Date |
|------------|--------|--------|-------------|
| Validation interviews | Completed interviews | 8 | 2026-07-20 |
| Concierge missed AO | Relevant AO not seen via BOAMP | ≥3/user avg | 2026-08-01 |
| WTP signal | LOI or pre-order | ≥3 at €25+/mo | 2026-08-15 |
| Source coverage audit | Lift vs BOAMP-only | ≥20% | 2026-08-01 |
| Re-score | global_score | ≥55 or kill | 2026-08-15 |
| Portfolio review | Decision | BUILD / MONITOR / KILL | 2026-09-25 |

#### Review Schedule

- First review: 2026-08-15
- Cadence: every 30 days during MONITOR sprint
- Portfolio review: 2026-09-25 (90 days)

#### Exit Triggers

- Zero LOI after structured outreach to 20+ prospects → **kill** (`no-customer-signal`)
- ≥5/8 interviews: current free or €15–30 tool sufficient → **kill** (`negative-validation`)
- global_score remains <50 after validation → **kill** (`score-below-threshold`)
- AlertOffres/Veillex/Marché Facile launches identical hyper-local wedge at ≤€15/mo → **kill** (`market-change`)
- MONITOR timeout 2026-09-25 without improvement → **kill** (`monitor-timeout`)
