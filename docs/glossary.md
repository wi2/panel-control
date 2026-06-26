# Glossary

Terms used throughout the AI Startup Studio control plane.

## A

### Architecture Proposal

High-level system design for an opportunity: components, build-vs-buy choices, integration points, and technical risks. Documentation only—no application code. BUILD-only section; references Risk Analysis for business risks.

## B

### BUILD

**Legacy (studio, frozen):** `global_score >= 75` AND `OQI >= 70` → [portfolio/active.md](../portfolio/active.md).

**Active (v3-lite):** see **BUILD_MICRO**.

### BUILD_MICRO

Portfolio decision when hard gates PASS, MSFI-lite ≥ 70, and live validation (not desk-only). Recorded in [portfolio/micro-saas.md](../portfolio/micro-saas.md) Active table.

## C

### confidence_level

Section-level assessment of decision reliability: `high`, `medium`, or `low`. Required on Discovery, Validation, Fit and Decide, and Final Decision (Micro SaaS).

### Control Plane

This repository. The central system for evaluating, documenting, and managing startup opportunities—not the products themselves.

## D

### Decision Path

**v3-lite (active):** Discovery → Validation → Fit and Decide → portfolio/micro-saas.md.

**Legacy (frozen):** 10-stage studio path — see [legacy-studio.md](legacy-studio.md).

### Discovery

First pipeline stage. Identifies the problem, market signals, competitors, and initial hypothesis. Driven by [`prompts/discovery.md`](../prompts/discovery.md).

### Distribution Analysis

Evaluates customer acquisition feasibility. Produces `distribution_score` and `distribution_notes`. See [`playbooks/distribution-analysis.md`](../playbooks/distribution-analysis.md).

## E

### eval_engine

Version tag for evaluation rules. Active value: **`v3-lite`**. Recorded in opportunity frontmatter.

### Fit and Decide

Third pipeline stage (v3-lite). Hard gates, MSFI-lite, final BUILD_MICRO / MONITOR_MICRO / KILL_MICRO decision, portfolio sync. Driven by [fit-and-decide-v1.md](../prompts/fit-and-decide-v1.md).

### Evidence

Documented support for a claim with required evidence type. See [`playbooks/evidence-classification.md`](../playbooks/evidence-classification.md).

Allowed types: `verified`, `estimated`, `inferred`, `synthetic`, `unknown`.

### expected_learnings

Structured learning outcomes from MONITOR and KILL decisions. Required for portfolio intelligence feedback loop.

### Evaluation Pipeline

The full process including decision path and BUILD preparation stages. See [Decision Path](#decision-path).

## G

### global_score

**Legacy (frozen).** Weighted composite (0–100) from 10 scoring dimensions. See [legacy-studio.md](legacy-studio.md).

## K

### KILL_MICRO

Terminate wedge — hard gate FAIL or MSFI-lite < 50. Archived in [portfolio/micro-saas.md](../portfolio/micro-saas.md).

### KILL (legacy)

Studio decision when `global_score < 50`. Frozen — [legacy-studio.md](legacy-studio.md).

## M

### Maintenance Evaluation

Assesses ongoing operational burden. Produces `maintenance_score` (1 = low burden, 10 = high burden). See [`playbooks/maintenance-evaluation.md`](../playbooks/maintenance-evaluation.md).

### MONITOR

Portfolio decision when `global_score` is 50–74, or when score qualifies for BUILD but OQI < 70. Recorded in [`portfolio/monitoring.md`](../portfolio/monitoring.md).

### Micro SaaS Portfolio

**Primary decision engine** for `eval_engine: v3-lite`. Hard gates + MSFI-lite. Decisions: BUILD_MICRO / MONITOR_MICRO / KILL_MICRO. Registry: [portfolio/micro-saas.md](../portfolio/micro-saas.md).

### MSFI-lite

Soft score (0–100): 40% speed + 35% economics + 25% reach. Computed in [scripts/msfi_calculator.py](../scripts/msfi_calculator.py). BUILD_MICRO requires MSFI ≥ 70, gates PASS, live validation.

### micro_saas_fit_index (MSFI)

Legacy seven-component MSFI v2 — deprecated. See [ADR v3-lite](decisions/2026-06-simplification-v3-lite.md).

### portfolio_strategy

Operating lens. **Active:** `solo_micro_saas` only. **Frozen:** `startup_studio`. See [portfolio-strategy.md](portfolio-strategy.md).

### capacity_blocked

Boolean on `solo_micro_saas` opps. When true, `decision` remains MONITOR_MICRO — bandwidth saturated (maint ≥ 40 h/mo or BUILD slots full).

### MVP Definition

Minimum viable product scope. BUILD-only section. Driven by [`prompts/mvp.md`](../prompts/mvp.md).

## O

### Opportunity

A single startup idea under evaluation. One markdown file in [`opportunities/`](../opportunities/) per opportunity.

### opportunity_quality_index (OQI)

**Legacy (frozen).** Decision reliability index for studio path. See [legacy-studio.md](legacy-studio.md).

## P

### Portfolio

The set of evaluated opportunities. **Active registry:** [portfolio/micro-saas.md](../portfolio/micro-saas.md). Legacy studio files frozen.

### Portfolio Intelligence

Evaluates portfolio fit: diversification, overlap, synergies. Produces `portfolio_fit_score`. See [`playbooks/portfolio-intelligence.md`](../playbooks/portfolio-intelligence.md).

### Prompt Version

A numbered revision of a pipeline-stage prompt (e.g. `discovery-v1`, `scoring-v2`). Opportunities record which versions were used for reproducibility.

## R

### Risk Analysis

Structured risk register across market, technical, regulatory, competition, and execution risks. Produces `risk_exposure_score`. See [`playbooks/risk-analysis.md`](../playbooks/risk-analysis.md).

### Roadmap

Phased plan for delivering the opportunity. BUILD-only section. Driven by [`prompts/roadmap.md`](../prompts/roadmap.md).

## S

### Scenario Planning

Models optimistic, realistic, and pessimistic outcomes with decision probabilities. See [`playbooks/scenario-planning.md`](../playbooks/scenario-planning.md).

### Scoring

Multi-dimensional evaluation across 10 weighted sub-scores producing `global_score`. Driven by [`prompts/scoring.md`](../prompts/scoring.md) v2 and [`playbooks/scoring-rules.md`](../playbooks/scoring-rules.md).

| Decision | Criteria |
|----------|----------|
| BUILD | global_score >= 75 AND OQI >= 70 |
| MONITOR | global_score 50–74 |
| KILL | global_score < 50 |

### Success Contract

Measurable commitments, review dates, and exit triggers for a BUILD opportunity. BUILD-only section. Driven by [`prompts/success-contract.md`](../prompts/success-contract.md).

## U

### Unfair Advantage Analysis

Evaluates structural moats: audience, expertise, data, partnerships, technical/SEO/community moats. Produces `unfair_advantages` and `moat_score`. See [`playbooks/unfair-advantage-analysis.md`](../playbooks/unfair-advantage-analysis.md).

## V

### Validation

Second pipeline stage. Experiments and desk-only vs live validation flag. Driven by [validation-v2.md](../prompts/validation-v2.md).

### Validation Experiment

A time-boxed test designed to produce evidence for or against a hypothesis (e.g. customer interviews, landing page, concierge MVP).

## Related

- [ADR v3-lite](decisions/2026-06-simplification-v3-lite.md)
- [Philosophy](philosophy.md)
- [legacy-studio.md](legacy-studio.md)
- [Conventions](../CONVENTIONS.md)
