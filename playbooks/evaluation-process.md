# Evaluation Process

Step-by-step workflow for evaluating a startup opportunity from discovery to portfolio decision.

## Overview

```text
Decision path (all opportunities):
  Discovery → Validation → Scoring → Distribution → Unfair Advantage
  → Maintenance → Risk → Portfolio Intelligence → Scenario Planning
  → Portfolio Manager → Update portfolio

BUILD preparation (BUILD only):
  Product Vision → MVP → Roadmap → Architecture → Success Contract
```

Target timeline: **4–8 weeks** from draft to decision for `startup_studio` opportunities.

## Strategy router

Read `portfolio_strategy` from frontmatter. Default for new opportunities: `solo_micro_saas` ([portfolio strategy](../docs/portfolio-strategy.md)).

### solo_micro_saas (fast path — default)

```text
Discovery → Validation → Micro SaaS Evaluation → Portfolio Manager Micro → portfolio/micro-saas.md
```

| Order | Prompt | Section |
|-------|--------|---------|
| 1 | Discovery | Discovery |
| 2 | Validation | Validation |
| 3 | [Micro SaaS Evaluation](../prompts/micro-saas-evaluation.md) | Micro SaaS Evaluation |
| 4 | [Portfolio Manager Micro](../prompts/portfolio-manager-micro.md) | Final Decision (Micro SaaS) |

Skipped: Scoring through studio Portfolio Manager. `global_score`/OQI optional diagnostics only.

### startup_studio (legacy)

```text
Discovery → Validation → Scoring → … → Portfolio Manager → active/monitoring/archived
```

## Step 1: Create Opportunity

1. Copy [`templates/opportunity-template.md`](../templates/opportunity-template.md) to [`opportunities/`](../opportunities/).
2. Name the file: `OPP-YYYYMMDD-{slug}.md`.
3. Fill frontmatter: `id`, `title`, `owner`, `created`.
4. Set `status: draft`.

## Step 2: Run Decision Path

Set `status: evaluating`. Execute prompts in order. Paste each output into the matching opportunity section.

| Order | Prompt | Section | Time-box |
|-------|--------|---------|----------|
| 1 | [Discovery](../prompts/discovery.md) | Discovery | 1–2 weeks |
| 2 | [Validation](../prompts/validation.md) | Validation | 2–4 weeks |
| 3 | [Scoring](../prompts/scoring.md) | Scoring | 1–3 days |
| 4 | [Distribution Analysis](../prompts/distribution-analysis.md) | Distribution Analysis | 1–2 days |
| 5 | [Unfair Advantage](../prompts/unfair-advantage.md) | Unfair Advantage Analysis | 1–2 days |
| 6 | [Maintenance Evaluation](../prompts/maintenance-evaluation.md) | Maintenance Evaluation | 1 day |
| 7 | [Risk Analysis](../prompts/risk-analysis.md) | Risk Analysis | 1–2 days |
| 8 | [Portfolio Intelligence](../prompts/portfolio-intelligence.md) | Portfolio Intelligence | 1 day |
| 9 | [Scenario Planning](../prompts/scenario-planning.md) | Scenario Planning | 1 day |
| 10 | [Portfolio Manager](../prompts/portfolio-manager.md) | Final Decision | 1 day |

Record `prompt_versions` in frontmatter after completing the decision path.

### Stage Gates

Do not advance without minimum output:

- **Discovery → Validation**: problem statement, hypothesis, market claims with evidence types (see [discovery.md](discovery.md))
- **Validation → Scoring**: at least one experiment completed with evidence-typed results, **or** documented desk-only fast path (see [validation.md](validation.md))
- **Scoring → Distribution**: `global_score` calculated with 10-dimension breakdown
- **Distribution → Unfair Advantage**: `distribution_score` and notes documented
- **Unfair Advantage → Maintenance**: `unfair_advantages` and `moat_score` documented
- **Maintenance → Risk**: `maintenance_score` and factor breakdown documented
- **Risk → Portfolio Intelligence**: all five risk categories with mitigation
- **Portfolio Intelligence → Scenario Planning**: `portfolio_fit_score` documented
- **Scenario Planning → Portfolio Manager**: three scenarios and probabilities (sum to 100%)
- **Portfolio Manager → Portfolio update**: primary decision, OQI, expected_learnings recorded

## Step 3: Score and Calculate OQI

Apply [`scoring-rules.md`](scoring-rules.md) and [`opportunity-quality-index.md`](opportunity-quality-index.md):

1. Rate each of 10 dimensions 0–10 with evidence types.
2. Apply weights from [`scoring-weights.md`](scoring-weights.md) to compute `global_score`.
3. Calculate OQI from evidence quality, confidence levels, score reliability, and risk adjustment.
4. Update frontmatter: `global_score`, `opportunity_quality_index`.

## Step 4: Decide

Map to decision using dual-gate rules:

| Decision | Criteria |
|----------|----------|
| BUILD | `global_score >= 75` AND `OQI >= 70` |
| MONITOR | `global_score` 50–74, OR score qualifies but OQI < 70 |
| KILL | `global_score < 50` |

Also check [`kill-rules.md`](kill-rules.md) for automatic kill triggers regardless of score.

Record in **Final Decision**: primary decision, OQI breakdown, scenarios, expected_learnings, rationale, next actions.

Update frontmatter: `decision`, `status: decided`, `updated`.

## Step 5: BUILD Preparation (BUILD only)

If primary decision is BUILD, complete BUILD-only sections **manually** (not orchestrated by CP — Eval):

| Order | Prompt | Section |
|-------|--------|---------|
| 11 | [Vision](../prompts/vision.md) | Product Vision |
| 12 | [MVP](../prompts/mvp.md) | MVP Definition |
| 13 | [Roadmap](../prompts/roadmap.md) | Roadmap |
| 14 | [Architecture](../prompts/architecture.md) | Architecture Proposal |
| 15 | [Success Contract](../prompts/success-contract.md) | Success Contract |

MONITOR and KILL opportunities skip BUILD preparation.

## Step 6: Update Portfolio

Add or move the opportunity in the appropriate portfolio file:

- BUILD → [`portfolio/active.md`](../portfolio/active.md)
- MONITOR → [`portfolio/monitoring.md`](../portfolio/monitoring.md)
- KILL → [`portfolio/archived.md`](../portfolio/archived.md)

Follow [`portfolio-rules.md`](portfolio-rules.md) for capacity and review scheduling.

## Step 7: Schedule Review

| Decision | Review cadence |
|----------|----------------|
| BUILD | Every 30 days |
| MONITOR | Every 90 days |
| KILL | None (archived) |

Set `Next Review` date in the portfolio entry.

## Learning Feedback Loop

Every MONITOR and KILL decision must record `expected_learnings` in Final Decision. Quarterly portfolio reviews aggregate learnings to improve scoring calibration and playbook updates.

Failed projects are learning assets. See [`kill-rules.md`](kill-rules.md).

## Re-Evaluation

MONITOR opportunities re-enter the pipeline at **Validation** (minimum) on each review cycle. Re-run intelligence sections and recalculate OQI. If re-validation fails or `global_score` drops below 50, apply KILL.

BUILD opportunities are reviewed against their Success Contract. Failure to meet commitments triggers re-evaluation or kill per [`kill-rules.md`](kill-rules.md).

## Migration from v1

Opportunities evaluated under scoring v1 must be re-evaluated. See [`migration-v1-to-v2.md`](migration-v1-to-v2.md).

## Related

- [Scoring rules](scoring-rules.md)
- [Opportunity quality index](opportunity-quality-index.md)
- [Evidence classification](evidence-classification.md)
- [Kill rules](kill-rules.md)
- [Portfolio rules](portfolio-rules.md)
- [Contributing](../CONTRIBUTING.md)
