# Principles

Operational principles for running the evaluation pipeline and maintaining the control plane.

> **Active path:** `eval_engine: v3-lite`, `portfolio_strategy: solo_micro_saas` only. Decision thresholds below use **MSFI-lite** and **hard gates** — see [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md). Studio thresholds (`global_score`, OQI) in the legacy section are frozen — [legacy-studio.md](legacy-studio.md).

## Reproducibility

Every opportunity records which prompt versions were used (`prompt_versions` in frontmatter). Evaluations must be reproducible: given the same inputs and prompt versions, another reviewer should reach similar conclusions.

## Versioned Prompts

Prompts are versioned artifacts, not living documents. Material changes create a new version; deprecated versions are retained. Never delete a prompt that was used in an evaluation.

## Decision Thresholds (v3-lite — active)

Decisions map to criteria by fixed thresholds for `solo_micro_saas`:

| Decision | Criteria |
|----------|----------|
| BUILD_MICRO | All hard gates PASS + MSFI-lite ≥ 70 + **live** validation (not desk-only) + capacity available |
| MONITOR_MICRO | Gates PASS + MSFI 50–69, OR one borderline gate (10%), OR `capacity_blocked: true` |
| KILL_MICRO | Any hard gate FAIL OR MSFI-lite < 50 |

`decision_override` is **not allowed** on the solo path. Thresholds are applied consistently via [scripts/msfi_calculator.py](../scripts/msfi_calculator.py) and CI.

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

Every claim influencing scoring or decisions must include an evidence type.

## Confidence Levels

Every decision-path section must declare `confidence_level: high | medium | low`.

For BUILD_MICRO: do not proceed to product development when Validation or Fit and Decide are `low` without documented mitigation in Final Decision.

## Separation of Stages (v3-lite)

Each pipeline stage has a distinct purpose:

- **Discovery** identifies *what might be worth validating*
- **Validation** tests *whether the hypothesis holds*
- **Fit and Decide** applies hard gates, MSFI-lite, and records the final decision
- **Post-BUILD prep** (manual) defines *what to build* — vision through success contract in the product repo

## Portfolio Discipline (v3-lite)

- Capacity limits apply — see [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md)
- BUILD_MICRO requires live validation signal (not desk-only)
- MONITOR_MICRO opportunities that fail re-validation are killed, not indefinitely deferred
- Every KILL_MICRO and MONITOR_MICRO must record expected learnings
- Merge policy: [merge-policy.md](../playbooks/merge-policy.md)

## Legacy — startup_studio (frozen)

The following applied to the frozen studio path only. Do not use for new opportunities.

| Decision | Criteria |
|----------|----------|
| BUILD | `global_score >= 75` AND `opportunity_quality_index >= 70` |
| MONITOR | `global_score` 50–74, OR score qualifies but OQI < 70 |
| KILL | `global_score < 50` |

See [legacy-studio.md](legacy-studio.md) and [opportunity-quality-index.md](../playbooks/opportunity-quality-index.md).

## Related

- [Philosophy](philosophy.md)
- [Evaluation process](../playbooks/evaluation-process.md)
- [Portfolio strategy](portfolio-strategy.md)
- [Conventions](../CONVENTIONS.md)
