# Evaluation Process (v3-lite)

Step-by-step workflow for evaluating a solo micro-SaaS wedge.

ADR: [docs/decisions/2026-06-simplification-v3-lite.md](../docs/decisions/2026-06-simplification-v3-lite.md).

## Overview

```text
Discovery (intake) → Validation → Fit and Decide → portfolio/micro-saas.md
```

Target timeline: **1–2 weeks** draft to decision.

## Step 1: Create Opportunity

1. Copy [templates/opportunity-template.md](../templates/opportunity-template.md).
2. Name: `OPP-YYYYMMDD-{slug}.md`.
3. Set `eval_engine: v3-lite`, `portfolio_strategy: solo_micro_saas`, `status: draft`.

## Step 2: Discovery

Run [discovery-v1.md](../prompts/discovery-v1.md) or **CP — Intake**. Set `intake_complete: true`, `status: evaluating`.

## Step 3: Validation + Fit and Decide

Run [validation-v2.md](../prompts/validation-v2.md) then [fit-and-decide-v1.md](../prompts/fit-and-decide-v1.md).

**Automation:** one **`cp:eval`** runs both via [pipeline-orchestrator-v8.md](../prompts/pipeline-orchestrator-v8.md).

## Step 4: Decide and sync

Fit and Decide sets `decision`, MSFI-lite scores, `status: decided`, and syncs [portfolio/micro-saas.md](../portfolio/micro-saas.md).

| Decision | Criteria |
|----------|----------|
| BUILD_MICRO | Gates PASS + MSFI ≥ 70 + live validation |
| MONITOR_MICRO | Gates PASS + MSFI 50–69 or capacity_blocked |
| KILL_MICRO | Gate FAIL or MSFI < 50 |

## Step 5: Post-BUILD (manual)

After BUILD_MICRO, use BUILD prep prompts in [legacy-studio.md](../docs/legacy-studio.md) or separate product repos.

## Review

MONITOR_MICRO and BUILD_MICRO: **30 days**. [portfolio-review-runner-v3.md](../prompts/portfolio-review-runner-v3.md).

## Legacy

Studio 10-stage path: [docs/legacy-studio.md](../docs/legacy-studio.md) (frozen).

## Related

- [micro-saas-portfolio.md](micro-saas-portfolio.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
