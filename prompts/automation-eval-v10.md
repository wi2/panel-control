---
version: 10
stage: automation_eval
status: active
created: 2026-06-26
supersedes: automation-eval-v9
changelog: "v3-lite full-run via orchestrator v8; one cp:eval to decided"
---

# Automation Eval Wrapper v10

## Role

Thin wrapper for **CP — Eval**. **Full-run** on branch **`opp/pipeline`** — one label **`cp:eval`** runs validation + fit_and_decide.

## Objective

Delegate to [pipeline-orchestrator-v8.md](pipeline-orchestrator-v8.md).

## Trigger

**Git — label change** — label **`cp:eval`** added. No push trigger.

## Preconditions (NOOP if fail)

1. Label `cp:eval` added.
2. PR head branch = `opp/pipeline`.
3. Exactly one active OPP (`status: draft` or `evaluating`).
4. `intake_complete: true`; Discovery filled.
5. `status` not `decided`.
6. `portfolio_strategy: solo_micro_saas` (or missing on old file — warn to migrate).

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [pipeline-orchestrator-v8.md](pipeline-orchestrator-v8.md).
3. Commit and push to `opp/pipeline`.
4. Post **Pipeline Run Summary** — `Mode: full-run`, `Remaining stages: none` on success.

## Related

- [Pipeline orchestrator v8](pipeline-orchestrator-v8.md)
- Previous: [automation-eval-v9.md](automation-eval-v9.md)
