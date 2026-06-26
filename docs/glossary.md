# Glossary

Terms used throughout the AI Startup Studio control plane.

## A

### Architecture Proposal

High-level system design for an opportunity: components, build-vs-buy choices, integration points, and technical risks. Documentation only—no application code. BUILD-only section; references Risk Analysis for business risks.

## B

### BUILD

Portfolio decision when `global_score >= 75` AND `opportunity_quality_index >= 70`. Indicates sufficient evidence and fit to allocate build resources. Recorded in [`portfolio/active.md`](../portfolio/active.md).

## C

### confidence_level

Section-level assessment of decision reliability: `high`, `medium`, or `low`. Required on every decision-path section. Portfolio Manager must not BUILD when Scoring, Distribution, or Risk are `low` without override.

### Control Plane

This repository. The central system for evaluating, documenting, and managing startup opportunities—not the products themselves.

## D

### Decision Path

The evaluation sequence for all opportunities: Discovery → Validation → Scoring → Distribution Analysis → Unfair Advantage → Maintenance Evaluation → Risk Analysis → Portfolio Intelligence → Scenario Planning → Portfolio Management.

### Discovery

First pipeline stage. Identifies the problem, market signals, competitors, and initial hypothesis. Driven by [`prompts/discovery.md`](../prompts/discovery.md).

### Distribution Analysis

Evaluates customer acquisition feasibility. Produces `distribution_score` and `distribution_notes`. See [`playbooks/distribution-analysis.md`](../playbooks/distribution-analysis.md).

## E

### Evidence

Documented support for a claim with required evidence type. See [`playbooks/evidence-classification.md`](../playbooks/evidence-classification.md).

Allowed types: `verified`, `estimated`, `inferred`, `synthetic`, `unknown`.

### expected_learnings

Structured learning outcomes from MONITOR and KILL decisions. Required for portfolio intelligence feedback loop.

### Evaluation Pipeline

The full process including decision path and BUILD preparation stages. See [Decision Path](#decision-path).

## G

### global_score

Weighted composite (0–100) from 10 scoring dimensions. Replaces legacy single `score`. See [`playbooks/scoring-rules.md`](../playbooks/scoring-rules.md).

## K

### KILL

Portfolio decision when `global_score < 50`, or when automatic kill triggers are met. Terminates further investment. Recorded in [`portfolio/archived.md`](../portfolio/archived.md).

## M

### Maintenance Evaluation

Assesses ongoing operational burden. Produces `maintenance_score` (1 = low burden, 10 = high burden). See [`playbooks/maintenance-evaluation.md`](../playbooks/maintenance-evaluation.md).

### MONITOR

Portfolio decision when `global_score` is 50–74, or when score qualifies for BUILD but OQI < 70. Recorded in [`portfolio/monitoring.md`](../portfolio/monitoring.md).

### Micro SaaS Portfolio

**Primary decision engine** when `portfolio_strategy: solo_micro_saas`. Asset allocator for solo AI micro-apps (6 hard gates + MSFI v2). Decisions: BUILD_MICRO / MONITOR_MICRO / KILL_MICRO. Canonical registry: [`portfolio/micro-saas.md`](../portfolio/micro-saas.md).

### micro_saas_fit_index (MSFI)

Soft score (0–100) after hard gates pass. MSFI v2: time to revenue, automation, maintenance, acquisition, wedge local, competition, pricing power. BUILD_MICRO requires MSFI ≥ 70, all hard gates PASS, and live validation.

### portfolio_strategy

Operating lens: `solo_micro_saas` (default), `startup_studio`, `vc_moonshot`, `cashflow_business`. See [`docs/portfolio-strategy.md`](portfolio-strategy.md).

### capacity_blocked

Boolean on `solo_micro_saas` opps. When true, `decision` remains MONITOR_MICRO — bandwidth saturated (maint ≥ 40 h/mo or BUILD slots full).

### MVP Definition

Minimum viable product scope. BUILD-only section. Driven by [`prompts/mvp.md`](../prompts/mvp.md).

## O

### Opportunity

A single startup idea under evaluation. One markdown file in [`opportunities/`](../opportunities/) per opportunity.

### opportunity_quality_index (OQI)

Decision reliability index (0–100) combining evidence quality, confidence levels, score reliability, and risk profile. BUILD requires OQI >= 70. See [`playbooks/opportunity-quality-index.md`](../playbooks/opportunity-quality-index.md).

## P

### Portfolio

The set of all evaluated opportunities, split by decision: active (BUILD), monitoring (MONITOR), archived (KILL).

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

Second pipeline stage. Designs and records experiments to test the discovery hypothesis. Driven by [`prompts/validation.md`](../prompts/validation.md).

### Validation Experiment

A time-boxed test designed to produce evidence for or against a hypothesis (e.g. customer interviews, landing page, concierge MVP).

## Related

- [Philosophy](philosophy.md)
- [Principles](principles.md)
- [Conventions](../CONVENTIONS.md)
- [Migration v1 to v2](../playbooks/migration-v1-to-v2.md)
