---
version: 1
stage: automation_eval
status: deprecated
created: 2026-06-25
supersedes: null
superseded_by: automation-eval-v2
changelog: "Pipeline +1 wrapper — branch + label gate for Cursor Automation CP — Eval"
---

# Automation Eval Wrapper v1

## Role

Thin wrapper for the **CP — Eval** Cursor Automation. Advances one opportunity by exactly one pipeline stage.

## Objective

Delegate to [pipeline-orchestrator-v1.md](pipeline-orchestrator-v1.md) after enforcing branch and label gates.

## Preconditions (STOP with NOOP comment if any fail)

1. Label **`cp:eval`** was **added** on this PR (not removed).
2. PR head branch matches `eval/OPP-YYYYMMDD-slug` (kebab-case slug after the date segment).

Resolve target opportunity file:

```text
branch eval/OPP-20260625-relance-factures
  → opportunities/OPP-20260625-relance-factures.md
```

3. Target file must exist on the PR branch. If missing → STOP with comment; do not create files in eval runs.

If preconditions fail, post a short PR comment explaining what is missing. Do not modify files.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [pipeline-orchestrator-v1.md](pipeline-orchestrator-v1.md) for the resolved file only.
3. **One stage per run** — do not chain multiple stages in a single trigger.
4. Commit changes to the **PR branch** (not `master`).
5. Post the **Pipeline Run Summary** from pipeline-orchestrator-v1 output format.
6. Do **not** run QA in this automation — **CP — QA** runs separately on push.

## Constraints

- Never push directly to the default branch.
- Never run intake and eval on the same PR.
- Do not edit `prompts/*` or `playbooks/*`.

## Related

- [Pipeline orchestrator](pipeline-orchestrator-v1.md)
- [Automations setup](../docs/automations.md)
