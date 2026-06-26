---
version: 6
stage: automation_eval
status: active
created: 2026-06-26
supersedes: automation-eval-v5
changelog: "Delegates to pipeline-orchestrator-v4 (strategy router, solo fast path)"
---

# Automation Eval Wrapper v6

## Role

Thin wrapper for **CP — Eval**. Advances up to **5 pipeline stages** per push on **`opp/pipeline`**.

## Objective

Delegate to [pipeline-orchestrator-v4.md](pipeline-orchestrator-v4.md) after preconditions.

## Trigger

**Git — new push to branch** `opp/pipeline`.

## Preconditions

Same as [automation-eval-v5.md](automation-eval-v5.md): branch `opp/pipeline`, exactly one active OPP, not already decided.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [pipeline-orchestrator-v4.md](pipeline-orchestrator-v4.md).
3. Up to 5 stages per run — single commit.
4. Push to `opp/pipeline`.
5. Post Pipeline Run Summary.

## Related

- [Pipeline orchestrator v4](pipeline-orchestrator-v4.md)
- Previous: [automation-eval-v5.md](automation-eval-v5.md)
