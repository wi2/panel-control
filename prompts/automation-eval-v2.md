---
version: 2
stage: automation_eval
status: deprecated
created: 2026-06-26
supersedes: automation-eval-v1
superseded_by: automation-eval-v3
changelog: "Push-triggered batch eval on opp/** — no cp:eval label"
---

# Automation Eval Wrapper v2

## Role

Thin wrapper for the **CP — Eval** Cursor Automation. Advances an opportunity by up to **5 pipeline stages** per push on an `opp/**` branch. No label required.

## Objective

Delegate to [pipeline-orchestrator-v2.md](pipeline-orchestrator-v2.md) after enforcing branch and opportunity resolution gates.

## Trigger

**Git — code pushed to pull request** on branch `opp/**`. Not label-triggered.

## Preconditions (STOP with NOOP comment if any fail)

1. Trigger is **code pushed to pull request** (not PR opened alone).
2. PR head branch matches `opp/**` (e.g. `opp/mon-idee`, `opp/OPP-20260626-slug`).
3. Resolve target opportunity file:

| Branch pattern | Resolution |
|----------------|------------|
| `opp/OPP-YYYYMMDD-slug` | `opportunities/OPP-YYYYMMDD-slug.md` |
| Other `opp/**` | Exactly **one** file matching `opportunities/OPP-*.md` on the branch |

If 0 files → NOOP: no opportunity file on branch.  
If 2+ files → NOOP: ambiguous — multiple OPP files on branch.

4. Target file exists and `status` is **not** `decided`. If `decided` → NOOP: opportunity already decided.
5. Skip if this push only changes paths outside `opportunities/` and `portfolio/` **and** the OPP file is unchanged since last eval (avoid doc-only loops). If OPP or portfolio files changed → proceed.

If preconditions fail, post a short PR comment explaining what is missing. Do not modify files.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [pipeline-orchestrator-v2.md](pipeline-orchestrator-v2.md) for the resolved file only.
3. **Up to 5 stages per run** — single commit at end of batch.
4. Commit and **push** to the **PR branch** (not `master`). Push re-triggers the next batch if pipeline not complete.
5. Post the **Pipeline Run Summary** from pipeline-orchestrator-v2 output format.
6. Do **not** run QA in this automation — **CP — QA** runs separately on push.

## Constraints

- Never push directly to the default branch.
- Do not edit `prompts/*` or `playbooks/*`.
- Do not run on `intake/**` or `eval/**` legacy branches — use `opp/**`.

## Related

- [Pipeline orchestrator v2](pipeline-orchestrator-v2.md)
- [Automations setup](../docs/automations.md)
