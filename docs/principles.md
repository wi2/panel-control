# Principles

Operational principles for running the evaluation pipeline and maintaining the control plane.

## Reproducibility

Every opportunity records which prompt versions were used (`prompt_versions` in frontmatter). Evaluations must be reproducible: given the same inputs and prompt versions, another reviewer should reach similar conclusions.

## Versioned Prompts

Prompts are versioned artifacts, not living documents. Material changes create a new version; deprecated versions are retained. Never delete a prompt that was used in an evaluation.

## Decision Thresholds

Scores map to decisions by fixed thresholds:

| Decision | Score |
|----------|-------|
| BUILD | >= 70 |
| MONITOR | 40–69 |
| KILL | < 40 |

Thresholds are applied consistently. Override requires documented rationale in the Final Decision section.

## Time-Boxing

- **Discovery**: 1–2 weeks maximum before validation begins
- **Validation experiments**: 2–4 weeks per experiment cycle
- **Pipeline completion**: 4–8 weeks from draft to decision for most opportunities
- **Monitoring review**: every 90 days for MONITOR opportunities
- **Active review**: every 30 days for BUILD opportunities

## Evidence Quality

Rank evidence from strongest to weakest:

1. Paid customer behavior (revenue, retention, usage)
2. Commitment signals (LOI, pilot agreement, pre-order)
3. Structured interviews with target users (5+ consistent signal)
4. Quantitative market data from credible sources
5. Expert or practitioner opinion (single source)
6. Unverified hypothesis

Scoring weights reflect this hierarchy (see [scoring rules](../playbooks/scoring-rules.md)).

## Separation of Stages

Each pipeline stage has a distinct purpose. Do not skip stages or merge outputs prematurely:

- Discovery identifies *what might be worth validating*
- Validation tests *whether the hypothesis holds*
- Scoring quantifies *how strong the opportunity is*
- Vision through Success Contract define *what to build if we build*

## Portfolio Discipline

- Capacity limits apply (see [portfolio rules](../playbooks/portfolio-rules.md))
- New BUILD decisions require available capacity
- MONITOR opportunities that fail re-validation are killed, not indefinitely deferred

## Related

- [Philosophy](philosophy.md)
- [Evaluation process](../playbooks/evaluation-process.md)
- [Conventions](../CONVENTIONS.md)
