# Principles

Operational principles for running the evaluation pipeline and maintaining the control plane.

## Reproducibility

Every opportunity records which prompt versions were used (`prompt_versions` in frontmatter). Evaluations must be reproducible: given the same inputs and prompt versions, another reviewer should reach similar conclusions.

## Versioned Prompts

Prompts are versioned artifacts, not living documents. Material changes create a new version; deprecated versions are retained. Never delete a prompt that was used in an evaluation.

## Decision Thresholds

Decisions map to criteria by fixed thresholds:

| Decision | Criteria |
|----------|----------|
| BUILD | `global_score >= 75` AND `opportunity_quality_index >= 70` |
| MONITOR | `global_score` 50–74, OR score qualifies but OQI < 70 |
| KILL | `global_score < 50` |

Thresholds are applied consistently. Override requires documented rationale in the Final Decision section.

## Evidence Quality

Rank evidence from strongest to weakest:

1. Paid customer behavior (revenue, retention, usage)
2. Commitment signals (LOI, pilot agreement, pre-order)
3. Structured interviews with target users (5+ consistent signal)
4. Quantitative market data from credible sources
5. Expert or practitioner opinion (single source)
6. Unverified hypothesis

Map to evidence types per [evidence-classification.md](../playbooks/evidence-classification.md):

| Tiers 1–4 | `verified` or `estimated` |
| Tier 5 | `inferred` |
| Tier 6 | `unknown` or `synthetic` |

Every claim influencing scoring or decisions must include an evidence type. OQI penalizes decisions built on weak evidence.

## Confidence Levels

Every decision-path section must declare `confidence_level`. Portfolio Manager must not BUILD when critical sections (Scoring, Distribution, Risk) are `low` without documented override.

## Separation of Stages

Each pipeline stage has a distinct purpose:

- Discovery identifies *what might be worth validating*
- Validation tests *whether the hypothesis holds*
- Scoring and intelligence analyses quantify *how strong and reliable the opportunity is*
- Scenario Planning models *decision outcomes under uncertainty*
- Portfolio Management decides *build, monitor, or kill*
- Vision through Success Contract define *what to build if we build* (BUILD-only)

## Portfolio Discipline

- Capacity limits apply (see [portfolio rules](../playbooks/portfolio-rules.md))
- BUILD requires dual-gate: global_score AND OQI
- MONITOR opportunities that fail re-validation are killed, not indefinitely deferred
- Every KILL and MONITOR must record `expected_learnings`

## Related

- [Philosophy](philosophy.md)
- [Evaluation process](../playbooks/evaluation-process.md)
- [Opportunity quality index](../playbooks/opportunity-quality-index.md)
- [Conventions](../CONVENTIONS.md)
