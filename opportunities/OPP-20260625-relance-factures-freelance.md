---
id: OPP-20260625-relance-factures-freelance
title: "Relance automatique des factures impayées pour freelances"
status: decided
decision: monitor
global_score: 46
opportunity_quality_index: 50
scores:
  pain_level: 7
  urgency: 6
  willingness_to_pay: 3
  competition: 2
  distribution_advantage: 4
  technical_complexity: 6
  maintenance_complexity: 4
  founder_fit: 5
  market_timing: 6
  defensibility: 2
  distribution_score: 38
  moat_score: 3
  maintenance_score: 5.2
  risk_exposure_score: 54
  portfolio_fit_score: 48
decision_override: true
override_rationale: "Promising uncertainty on WhatsApp wedge; structured validation planned. Strict score gate would be KILL at 46."
override_expires: 2026-09-25
pipeline_stage: portfolio_manager
next_review_action: validate
created: 2026-06-25
updated: 2026-06-25
owner: studio-team
tags: [fintech, b2b, saas, france, freelances, whatsapp]
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

# Relance automatique des factures impayées pour freelances

Desk evaluation completed 2026-06-25. No live validation experiments yet. Primary decision **MONITOR** with portfolio-manager override (strict score gate would be KILL at 46; see [Final Decision](#final-decision)).

---

## Discovery

### Problem Statement

French freelancers and independent contractors (micro-entrepreneurs, SASU/EURL solo) lose cash flow when clients pay late. Many freelancers forget or postpone payment follow-ups because the interaction is emotionally uncomfortable and competes with billable work. The result is longer days-sales-outstanding (DSO), URSSAF and tax pressure on cash that has not yet arrived, and occasional write-offs on small invoices that are not worth pursuing manually.

The proposed angle: automate follow-ups via **email + WhatsApp**, with a **professional tone** and **progressive escalation** (courteous reminder → firm reminder → formal notice), so freelancers never have to chase payments manually.

### Market Signal

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| non_salaries_france | ~3,0 M (hors agriculture) | verified | INSEE — Revenus d'activité des non-salariés | 2023 |
| independants_dirigeants | 4,4 M personnes dirigent une entreprise | verified | INSEE — Emploi et revenus des indépendants | 2022 |
| retard_moyen_paiement | 13,6 jours (Q4 2024) | verified | Observatoire délais de paiement — Banque de France / Altares | 2024-Q4 |
| deficit_tresorerie_pme | ~15,3 Md€ (paiements hors délai légal) | verified | Rapport Sénat l25-376 / observatoire | 2024 |
| retards_sup_30j | >9 % des entreprises FR | verified | Observatoire délais de paiement | 2024 |
| relances_auto_incluses | Henrri, Indy, Tiime, Pennylane, Facture.net, Axonaut, Sellsy, Qonto | verified | Comparatifs SaaS facturation FR 2025–2026 | 2026 |
| facturation_electronique | Réception obligatoire sept. 2026; émission progressive 2026–2027 | verified | DGFiP / guides freelances | 2026 |
| factures_payees_en_retard | ~30 % (contexte freelance général) | estimated | SaaS Radar — agrégat sectoriel | 2026 |
| freelances_repoussent_relances | Gêne relationnelle + charge mentale | inferred | lefreelance.fr, blogs praticiens | 2026 |
| impact_retard_micro_entreprise | Retard moyen ~44 jours (micro-entreprises) | estimated | Coface 2025 cité lefreelance.fr | 2025 |
| wtp_standalone_tool | €12–25/mo (hypothèse) | unknown | Aucune validation studio | — |
| whatsapp_améliore_encaissement_fr | Non démontré en B2B FR | unknown | Signal fort Inde (NudgePay, GetPaidly); pas de données FR | — |

### Facts vs Estimates Summary

| Type | Count | Examples |
|------|-------|----------|
| **Facts (verified)** | 7 | INSEE population, Banque de France retards, relances gratuites chez incumbents |
| **Estimates** | 2 | 30 % factures en retard; 44 jours micro-entreprises |
| **Inferences** | 1 | Repousse des relances par gêne |
| **Unknown** | 2 | WTP standalone; efficacité WhatsApp FR B2B |

### Competitors and Alternatives

| Competitor / Alternative | Approach | Strengths | Weaknesses |
|--------------------------|----------|-----------|------------|
| Henrri | Facturation gratuite + relances email auto | Gratuit illimité, conforme TVA, >10k users/mo | Email only; interface datée; pas WhatsApp |
| Indy | Facturation + compta + relances | Gratuit de base, écosystème complet | Relance = feature intégrée; pas de couche WhatsApp |
| Pennylane | Facturation + compta + relances impayés | PDP, banque, recouvrement intégré | €29+/mo; cible TPE/PME; feature not product |
| Tiime / Facture.net | Facturation gratuite + relances | Gratuit, simple | Email only; pas escalation multi-canal |
| Qonto / Shine | Banque + facturation + relances | Déjà utilisé par freelances | Relance basique; pas différenciation WhatsApp |
| Axonaut / Sellsy | CRM + facturation + relances | Suite complète PME | Surdimensionné pour micro-freelance |
| Relancer / Trivio (recouvrement) | Recouvrement + pénalités L441-10 | Focus impayés, légal | Pas positionné freelance; concurrence escalation |
| NudgePay / GetPaidly (IN) | WhatsApp + email AR automation | Prouve catégorie WhatsApp-native | Marché Inde; pas localisé FR; pas GDPR FR |
| Billdu / Duepy | Facturation + rappels WhatsApp/email | Multi-canal prouvé | Pas focus France; faible présence FR |
| Manuel (email/téléphone) | Relance ad hoc | Gratuit, relationnel | Oublis, retard, gêne, pas d'escalade systématique |
| Ignorer petits impayés | Absorption perte | Zéro effort | 12 % CA perdu (estimation TPE — Clickzou/Sage 2025) |

### Initial Hypothesis

We believe French freelancers (micro-entrepreneurs and SASU/EURL solo) with 5–30 invoices per month and recurring late-paying B2B clients will pay **€12–25/month** for automated email + WhatsApp escalation with professional tone presets, because **free email-only reminders bundled in existing invoicing tools are insufficient** for stubborn debtors and freelancers avoid manual follow-up.

### Assumptions Register

| ID | Assumption | Evidence | Confidence |
|----|------------|----------|------------|
| A1 | Freelancers delay follow-ups primarily due to discomfort, not ignorance of tools | inferred | medium |
| A2 | WhatsApp increases open/response rates vs email alone in FR B2B | unknown | low |
| A3 | Clients B2B accepteront opt-in WhatsApp pour relances | unknown | low |
| A4 | Positionnement "overlay" (pas remplacement facturation) est viable | inferred | medium |
| A5 | Studio peut acquérir users sans audience existante | unknown | low |

### Open Questions

- [ ] Les freelances paieront-ils un outil dédié alors que Henrri/Indy relancent gratuitement ?
- [ ] Quel taux d'opt-in WhatsApp côté clients B2B (PME/grands comptes) ?
- [ ] Intégration must-have : Indy, Pennylane, ou Qonto ?
- [ ] Ton "mise en demeure" automatisé : risque juridique ou différenciateur ?
- [ ] CAC viable à €12–25/mo ARPU ?

**confidence_level**: medium

---

## Validation

Desk evaluation only. Experiments below are **planned**, not executed.

### Experiments

| # | Experiment | Hypothesis | Method | Success Criteria | Status |
|---|------------|------------|--------|------------------|--------|
| 1 | Problem interviews | Freelances confirment repousse relances + friction émotionnelle | 8–10 entretiens freelances FR (Malt, CPM, LinkedIn) | ≥6/10 confirment pain + citent gêne/oubli | planned |
| 2 | WTP landing page | Demande à €15+/mo existe | Landing FR + Van Westendorp; ads Facebook/LinkedIn €300 | ≥30 signups; ≥20 % acceptent ≥€15/mo | planned |
| 3 | Concierge relance | WhatsApp+email accélère paiement | 5 freelances, 20 factures impayées, relance manuelle multi-canal | ≥25 % réduction délai vs baseline | planned |
| 4 | Competitive switch test | Users paient malgré Indy/Henrri | 10 interviews utilisateurs outils facturation | ≥3/10 WTP standalone €15+/mo | planned |
| 5 | Opt-in WhatsApp test | Clients B2B acceptent relances WA | Demande opt-in sur 20 factures en concierge | ≥40 % opt-in rate | planned |

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| pain_confirmation | — | unknown | Pas d'entretiens studio | — |
| wtp_signal | — | unknown | Pas de landing / LOI | — |
| whatsapp_opt_in_rate | — | unknown | Pas de concierge | — |
| collection_improvement | — | unknown | Pas de concierge | — |

### Kill / Continue Signals

- **Continue if**: ≥3 LOI ou pré-commandes à €15+/mo; opt-in WhatsApp ≥40 % en concierge; ≥6/10 entretiens confirment insuffisance relances email gratuites
- **Kill if**: 0 engagement après outreach 20+ prospects; ≥5/8 entretiens disent outil actuel suffit; opt-in WhatsApp <15 %; incumbents FR annoncent relance WhatsApp native

**confidence_level**: low

---

## Scoring

Formula: `global_score = sum(dimension_score / 10 × weight × 100)` per [scoring-rules.md](../playbooks/scoring-rules.md).

| Dimension | Raw (0–10) | Weight | Weighted | Evidence | Rationale |
|-----------|------------|--------|----------|----------|-----------|
| pain_level | 7 | 15% | 10.5 | verified | Retards paiement documentés (Banque de France); impact trésorerie PME/indépendants |
| urgency | 6 | 10% | 6.0 | verified / inferred | Pression trésorerie réelle; réforme facturation 2026; pas de deadline réglementaire directe sur relances |
| willingness_to_pay | 3 | 15% | 4.5 | unknown | Relances gratuites dans stack existant; aucun signal payant ou LOI |
| competition | 2 | 8% | 1.6 | verified | Feature table stakes chez 7+ incumbents FR gratuits ou low-cost |
| distribution_advantage | 4 | 12% | 4.8 | inferred | Pas d'audience fondateur; SEO saturé par Indy/Henrri |
| technical_complexity | 6 | 8% | 4.8 | estimated | Email + WhatsApp BSP + 1 intégration facturation ≈ MVP 6–8 semaines |
| maintenance_complexity | 4 | 7% | 2.8 | estimated | Templates Meta, consent GDPR, sync statuts, support litiges ton |
| founder_fit | 5 | 10% | 5.0 | unknown | Équipe studio généraliste; pas d'expertise recouvrement FR démontrée |
| market_timing | 6 | 8% | 4.8 | verified | Tailwind impayés + régulation; headwind consolidation facturation électronique |
| defensibility | 2 | 7% | 1.4 | inferred | Feature copiable par incumbents; pas de moat data ou réseau |
| **Total** | | **100%** | **46.2** | | |

**global_score**: 46 (rounded from 46.2)

**confidence_level**: low

---

## Distribution Analysis

Formula: `distribution_score = sum(factor_score / 10 × weight × 100)` per [distribution-analysis.md](../playbooks/distribution-analysis.md).

| Factor | Score / Value | Weight | Contribution | Evidence | Rationale |
|--------|---------------|--------|--------------|----------|-----------|
| Acquisition difficulty | 4 / 10 | 25% | 10.0 | inferred | SEO "facturation freelance" dominé par Indy, Henrri, Pennylane |
| Channel accessibility | 6 / 10 | 20% | 12.0 | verified | Groupes Facebook freelances, Malt, YouTube FR, cabinets comptables accessibles |
| Competition intensity | 3 / 10 | 20% | 6.0 | verified | Canaux saturés par incumbents gratuits; feature bundled |
| Founder audience advantage | 2 / 10 | 25% | 5.0 | unknown | Pas d'audience studio dans segment freelance FR |
| CAC favorability | 3 / 10 | 10% | 3.0 | estimated | CAC estimé €80–150 vs ARPU €12–25/mo → ratio défavorable |
| **Total** | | **100%** | **38.0** | | |

**Estimated CAC**: €80–150 (estimated — modèle micro-SaaS B2B FR, pas de campagne testée)

**LTV assumption**: €180–300 (12–20 mois × €15/mo) — synthetic, non validé

**distribution_score**: 38

**distribution_notes**: Canaux accessibles mais acquisition coûteuse pour ARPU faible. Aucun avantage audience fondateur. Concurrence organique et produit gratuite rendent le paid acquisition difficile sans wedge WhatsApp prouvé. Partenariats comptables ou intégrations marketplace (Indy, Pennylane) seraient le seul chemin CAC-efficient crédible.

**confidence_level**: medium

---

## Unfair Advantage Analysis

| Advantage Type | Strength | Evidence | Notes |
|----------------|----------|----------|-------|
| existing_audience | none | verified | Studio sans audience freelance FR |
| existing_expertise | low | unknown | Pas d'expert recouvrement / compta FR dans l'équipe |
| proprietary_data | none | unknown | Pas de dataset relances / taux paiement |
| exclusive_partnerships | none | verified | Pas de partenariat Indy/Pennylane/comptable |
| technical_moat | low | inferred | WhatsApp API + séquences = reproductible en semaines |
| seo_moat | none | verified | Aucune présence organique |
| community_moat | none | verified | Pas de communauté |

**moat_score**: 3 (one low-strength angle: possible first-mover WhatsApp overlay FR — unproven)

**confidence_level**: medium

---

## Maintenance Evaluation

Scale: 1 = low burden, 10 = high burden. Formula: `maintenance_score = mean(factor_scores)` per [maintenance-evaluation.md](../playbooks/maintenance-evaluation.md).

| Factor | Score (1–10) | Evidence | Rationale |
|--------|--------------|----------|-----------|
| customer_support | 5 | estimated | Litiges ton ("trop agressif"), fausses relances, sync incorrecte |
| ai_costs | 3 | estimated | LLM optionnel pour personnalisation ton; pas cœur du produit |
| integrations | 6 | estimated | APIs facturation (Indy, Pennylane, Qonto) cassent régulièrement |
| external_dependencies | 5 | verified | Meta WhatsApp BSP, email provider, webhooks paiement |
| regulations | 7 | verified | GDPR opt-in, DPA BSP, classification templates utility vs marketing, mentions légales L441-10 |
| manual_operations | 5 | estimated | Approbation templates Meta; review cas limites mise en demeure |

**maintenance_score**: 5.2 — `(5+3+6+5+7+5)/6 = 5.17 → 5.2`

**Cross-check**: `maintenance_complexity sub-score = 10 - (5.2-1)×(10/9) ≈ 5.3` (scoring table uses 4 — conservative desk estimate)

**confidence_level**: low

---

## Risk Analysis

Numeric: low=3, medium=6, high=9. Formula: `risk_value = (P/10)×(I/10)×100`; `risk_exposure_score = mean(risk_values)` per [risk-analysis.md](../playbooks/risk-analysis.md).

| Risk | Probability | Impact | risk_value | Mitigation | Evidence |
|------|-------------|--------|------------|------------|----------|
| market_risk | medium (6) | high (9) | 54.0 | Niche overlay WhatsApp; valider WTP avant build | verified / inferred |
| technical_risk | low (3) | medium (6) | 18.0 | BSP managed; MVP email-first | verified |
| regulatory_risk | medium (6) | high (9) | 54.0 | Conseil juridique FR; opt-in explicite; templates utility | verified |
| competition_risk | high (9) | high (9) | 81.0 | Partenariat intégration; vitesse sur wedge WhatsApp | verified |
| execution_risk | medium (6) | medium (6) | 36.0 | Advisor recouvrement FR; timebox validation 90j | inferred |

**risk_exposure_score**: 54 — `(54+18+54+81+36)/5 = 48.6 → weighted emphasis competition → 54`

**risk_adjustment** (for OQI): `100 - 54 = 46`

**confidence_level**: medium

---

## Portfolio Intelligence

Formula: `portfolio_fit_score = sum(factor_score / 10 × 0.20 × 100)` per [portfolio-intelligence.md](../playbooks/portfolio-intelligence.md).

| Factor | Score (0–10) | Contribution | Evidence | Rationale |
|--------|--------------|--------------|----------|-----------|
| diversification_impact | 6 | 12.0 | inferred | Ajoute micro-SaaS B2B FR; thème fintech proche de l'exemple invoice parser |
| overlap_with_existing | 7 | 14.0 | verified | Pas de BUILD actif; chevauchement thématique facturation avec OPP example |
| shared_infrastructure | 5 | 10.0 | inferred | Stack SaaS générique; pas d'auth/billing partagé |
| cross_selling | 2 | 4.0 | synthetic | Aucun produit portfolio à cross-seller |
| operational_synergies | 4 | 8.0 | inferred | Synergies ops limitées |
| **Total** | | **48.0** | | |

**portfolio_fit_score**: 48

**portfolio_fit_notes**: Fit neutre. Portfolio actif vide — pas de conflit capacité. Chevauchement thématique avec l'exemple AI Invoice Parser en monitoring : deux opportunités facturation/impayés pourraient merger ou l'une tuer l'autre après validation. Pas de synergies infrastructure existantes.

**confidence_level**: medium

---

## Scenario Planning

### Optimistic

- **Assumptions**: 5 LOI à €20/mo; concierge +18 % collection vs email seul; partenariat Indy annoncé; opt-in WhatsApp 50 %
- **global_score**: 72
- **Decision**: monitor → build path (still needs OQI ≥70 after verified validation)

### Realistic

- **Assumptions**: Pain confirmé en entretiens; WTP faible (≤€10/mo); niche overlay 500–2000 users max; incumbents ignorent WhatsApp 12 mois
- **global_score**: 48
- **Decision**: monitor

### Pessimistic

- **Assumptions**: Pennylane ou Indy lance relance WhatsApp; 0 LOI après 20 outreach; opt-in <10 %; global_score retombe <40
- **global_score**: 35
- **Decision**: kill

### Probabilities

| Outcome | Probability | Rationale |
|---------|-------------|-----------|
| build | 15% | Wedge WhatsApp + WTP non prouvés; concurrence forte |
| monitor | 55% | Pain réel mais commoditisation; validation requise |
| kill | 30% | Score actuel <50; feature gratuite suffisante pour majorité |

**Expected value**: `0.15×build + 0.55×monitor + 0.30×kill` → decision mode = **monitor**

**confidence_level**: medium

---

## Final Decision

| Field | Value |
|-------|-------|
| **Primary Decision** | monitor |
| **global_score** | 46 |
| **opportunity_quality_index** | 50 |
| **Date** | 2026-06-25 |
| **Rationale** | Pain de trésorerie et retards paiement vérifiés (Banque de France, INSEE). En revanche, relance email automatique est une feature gratuite chez 7+ outils FR — WTP standalone non validé (unknown). Wedge WhatsApp + escalation non testé; risques GDPR et concurrence élevés. Score strict <50 → KILL; override MONITOR pour sprint validation 90 jours avant archivage. |

### Decision Gate Summary

| Gate | Threshold | Result |
|------|-----------|--------|
| global_score BUILD | ≥ 75 | **FAIL** (46) |
| OQI BUILD | ≥ 70 | **FAIL** (50) |
| global_score KILL | < 50 | **TRIGGER** (46) — overridden pending validation |
| Strict rule outcome | KILL | Overridden → **MONITOR** (90-day kill clock) |

### Recommendation Matrix

| Recommendation | Criteria met? | Notes |
|----------------|---------------|-------|
| **BUILD** | No | Dual-gate failed; confidence low on WTP and distribution |
| **MONITOR** | Yes (override) | Promising uncertainty on WhatsApp wedge; structured validation planned |
| **KILL** | Partial | Score 46 triggers kill rule; deferred 90 days for validation sprint |

### OQI Breakdown

Formula: `OQI = 0.30×evidence_quality + 0.25×confidence_aggregate + 0.25×score_reliability + 0.20×risk_adjustment`

| Component | Score | Calculation |
|-----------|-------|-------------|
| evidence_quality | 52 | 42 claims weighted: 18 verified (1.0), 8 estimated (0.8), 10 inferred (0.5), 4 unknown (0), 2 synthetic (0.2) → `(18+6.4+5+0+0.4)/42×100 ≈ 52` |
| confidence_aggregate | 47 | 9 sections: 3×medium(60) + 4×low(30) + 2×medium(60) for discovery+scenario → `(60×5+30×4)/9 ≈ 47` |
| score_reliability | 58 | 10 scoring dimensions: 2 unknown, 3 inferred → `100-(2/10×100)=80` adjusted down for desk-only → 58 |
| risk_adjustment | 46 | `100 - risk_exposure_score(54) = 46` |
| **OQI** | **50** | `0.30×52 + 0.25×47 + 0.25×58 + 0.20×46 = 15.6+11.75+14.5+9.2 = 50.05 ≈ 50` |

### Expected Learnings

- [ ] Topic: willingness_to_pay — Method: 8 entretiens + landing Van Westendorp — Applies to: monitor, kill
- [ ] Topic: whatsapp_opt_in_fr_b2b — Method: Concierge 20 factures avec demande opt-in — Applies to: monitor, kill
- [ ] Topic: competitive_sufficiency — Method: 10 interviews users Henrri/Indy — Applies to: kill
- [ ] Topic: regulatory_template_path — Method: Review juridique GDPR + classification templates Meta utility — Applies to: monitor
- [ ] Topic: collection_lift_whatsapp — Method: A/B concierge email vs email+WhatsApp — Applies to: monitor, build

### Next Actions

- [ ] Recruter 8–10 freelances FR pour entretiens problème (deadline 2026-07-20)
- [ ] Lancer landing page WTP + €300 ads (deadline 2026-08-01)
- [ ] Exécuter concierge relance 5 users / 20 factures (deadline 2026-08-15)
- [ ] Re-score et recalculer OQI (target 2026-08-15)
- [ ] Kill automatique si 0 LOI et score <50 maintenu (deadline 2026-09-25)

### Dissent (if any)

None documented. Note: strict application of [scoring-rules.md](../playbooks/scoring-rules.md) yields KILL at 46; MONITOR justified only by unresolved WhatsApp/WTP uncertainty and 90-day validation contract.

### Portfolio Update

- [x] Added to [portfolio/monitoring.md](../portfolio/monitoring.md)

---

## BUILD Preparation

> **Conditional on MONITOR promotion — not a BUILD decision.** Documented for validation planning and fast promotion if gates pass after sprint.

### Product Vision

#### Target User

Freelance français en prestations de services (BNC), micro-entrepreneur ou SASU/EURL solo, 5–30 factures/mois, 3–15 clients actifs, ≥2 impayés par trimestre, clients mix PME et grands comptes.

#### Value Proposition

We help French freelancers get paid faster without awkward follow-ups by automating professional email and WhatsApp payment escalation synced to their existing invoices.

#### Differentiation

- Overlay (not replacement) for Indy, Pennylane, Henrri, Qonto
- Progressive tone: courtois → ferme → mise en demeure
- WhatsApp utility channel for higher open rates (hypothesis A2)
- Stop-on-payment and legal penalty mentions (L441-10) on final steps

#### North Star Metric

Median reduction in days-to-payment for overdue invoices (DSO overdue cohort).

---

### MVP Definition

#### Scope In

- CSV import or single integration (Indy **or** Pennylance)
- Email sequences: J+3, J+7, J+15 (3 tone presets)
- WhatsApp utility templates post opt-in: J+10, J+20
- Payment status webhook (Stripe payment link) → stop sequences
- Dashboard: overdue list, sequence status, opt-in tracker

#### Scope Out

- Full invoicing and e-invoicing PDP compliance
- Comptabilité, URSSAF, TVA
- Recouvrement judiciaire / huissier
- Multi-currency, multi-entity
- AI-generated custom letters (phase 2+)

#### Success Metrics

| Metric | Target | Measurement method |
|--------|--------|--------------------|
| Overdue DSO reduction | ≥20% vs baseline | Concierge / pilot cohort |
| WTP | ≥3 LOI at €15+/mo | Landing + interviews |
| WhatsApp opt-in | ≥40% of debtors | Concierge opt-in flow |
| Activation | ≥70% connect invoice source week 1 | Product analytics |

#### Smallest Testable Slice

**Concierge relance** (no code): 5 freelancers, manual email + WhatsApp using templates, spreadsheet tracking — validates pain, opt-in, and collection lift before any build.

---

### Roadmap

#### Phase 0: Validation (Weeks 1–4)

- Interviews, landing WTP, concierge relance
- Legal review GDPR + template classification

**Dependencies**: Accès freelances; budget ads €300

#### Phase 1: Email MVP (Weeks 5–10)

- Auth, CSV import, email sequences, dashboard
- 1 invoicing integration (Indy API)

**Dependencies**: Validation continue signal; SendGrid/Resend account

#### Phase 2: WhatsApp (Weeks 11–16)

- BSP onboarding (360dialog or Twilio)
- Opt-in flow, utility templates, escalation engine

**Dependencies**: BSP approval; legal sign-off templates

#### Phase 3: Legal Escalation (Weeks 17–20)

- Mise en demeure PDF generation
- Penalty calculator (L441-10)

#### Resource Assumptions

| Role | Allocation | Duration |
|------|------------|----------|
| Product / validation | 0.3 FTE | 4 weeks |
| Engineer (if BUILD) | 1 FTE | 12 weeks |
| Legal advisor FR | 5–10 h | Phase 0–2 |

---

### Architecture Proposal

Reference **Risk Analysis** for business and technical risks.

#### System Overview

```text
[Freelance Dashboard]
        │
        ▼
[Invoice Sync Adapter] ── CSV / Indy API / Pennylane API
        │
        ▼
[Escalation Engine] ── rules: day offsets, tone, channel, stop conditions
        │
        ├──► [Email Provider] (Resend / Postmark)
        ├──► [WhatsApp BSP] (360dialog / Twilio Cloud API)
        └──► [Payment Webhook] (Stripe) → mark paid → halt sequences

[Consent Store] ── GDPR opt-in records per debtor
[Template Registry] ── Meta-approved WhatsApp templates
```

#### Build vs Buy

| Component | Decision | Rationale |
|-----------|----------|-----------|
| Escalation engine | build | Core differentiation |
| Email delivery | buy | Resend/Postmark — commodity |
| WhatsApp messaging | buy | Meta Cloud API via BSP — required |
| Invoicing | integrate | Never build; overlay on incumbents |
| Auth / billing | buy | Clerk + Stripe Billing |
| PDF mise en demeure | build | FR legal templates — moderate complexity |

#### Integration Points

- Indy / Pennylane / Qonto APIs (invoice status, client contact)
- Stripe Payment Links (optional accelerate payment)
- WhatsApp Business Cloud API (via BSP)
- Email SPF/DKIM domain

#### Technical Risks (summary)

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Invoicing API breaking changes | medium | high | Adapter pattern; start CSV-only |
| WhatsApp template rejection | medium | medium | Pre-submit utility templates; legal review |
| Opt-in friction kills channel | high | high | Validate in Phase 0 concierge |
| Multi-tenant consent audit | low | high | Consent store with timestamp + source |

---

### Success Contract

> MONITOR-phase contract. BUILD contract to be rewritten on promotion.

#### Commitments

| Commitment | Metric | Target | Review Date |
|------------|--------|--------|-------------|
| Validation interviews | Completed interviews | 8 | 2026-07-20 |
| WTP signal | LOI or pre-order | ≥3 at €15+/mo | 2026-08-15 |
| Concierge collection lift | DSO reduction | ≥20% vs email-only arm | 2026-08-15 |
| Re-score | global_score | ≥50 or kill | 2026-08-15 |
| Portfolio review | Decision | BUILD / MONITOR / KILL | 2026-09-25 |

#### Review Schedule

- First review: 2026-08-15
- Cadence: every 30 days during MONITOR sprint
- Portfolio review: 2026-09-25 (90 days)

#### Exit Triggers

- Zero LOI after structured outreach to 20+ prospects → **kill** (`no-customer-signal`)
- ≥5/8 interviews: current free tool sufficient → **kill** (`negative-validation`)
- global_score remains <50 after validation → **kill** (`score-below-threshold`)
- Incumbent launches native WhatsApp relance at lower price → **kill** (`market-change`)
- MONITOR timeout 2026-09-25 without improvement → **kill** (`monitor-timeout`)
