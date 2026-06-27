# Prompts (v3-lite active)

Versioned AI prompts for the **solo micro-SaaS** evaluation pipeline.

## Active Versions

| Stage | Index | Active Version |
|-------|-------|----------------|
| Discovery | [discovery.md](discovery.md) | v1 |
| Validation | [validation.md](validation.md) | v2 |
| Fit and Decide | [fit-and-decide.md](fit-and-decide.md) | v1 |
| Intake | [intake.md](intake.md) | v7 |
| Pipeline Orchestrator | [pipeline-orchestrator.md](pipeline-orchestrator.md) | v8 |
| Opportunity QA | [opportunity-qa.md](opportunity-qa.md) | v5 |
| Portfolio Review Runner | [portfolio-review-runner.md](portfolio-review-runner.md) | v3 |

### Automation wrappers

| Automation | Active Version |
|------------|----------------|
| CP — QA | [automation-qa-v6.md](automation-qa-v6.md) |
| CP — Intake | [automation-intake-v8.md](automation-intake-v8.md) |
| CP — Eval | [automation-eval-v10.md](automation-eval-v10.md) |
| CP — Review | [automation-review-v3.md](automation-review-v3.md) |

Legacy studio prompts: [docs/legacy-studio.md](../docs/legacy-studio.md).

Post-BUILD prompts (`vision`, `mvp`, `architecture`, etc.) are **historical reference** — product repos own build agents. ADR: [control-plane vs product-repo](../docs/decisions/2026-07-control-plane-vs-product-repo.md).

## Pipeline Order

```text
discovery → validation → fit_and_decide
```

Full automation: Intake → **1×** `cp:eval` → `decided`.

See [ADR v3-lite](../docs/decisions/2026-06-simplification-v3-lite.md).
