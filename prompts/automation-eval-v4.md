---
version: 4
stage: automation_eval
status: active
created: 2026-06-26
supersedes: automation-eval-v3
changelog: "Active OPP resolution — catalogue decided from master coexists on opp/pipeline"
---

# Automation Eval Wrapper v4

## Role

Thin wrapper for the **CP — Eval** Cursor Automation. Advances an opportunity by up to **5 pipeline stages** per push on branch **`opp/pipeline`**. No label required.

## Objective

Delegate to [pipeline-orchestrator-v2.md](pipeline-orchestrator-v2.md) after enforcing branch and opportunity resolution gates.

## Trigger

**Git — new push to branch** `opp/pipeline` (exact name; Cursor Automations does not support wildcards). Not label-triggered.

## Terminology

| Term | Definition |
|------|------------|
| **Catalogue** | `opportunities/OPP-*.md` with frontmatter `status: decided` (typically inherited from `master`) |
| **Active OPP** | `opportunities/OPP-*.md` with frontmatter `status: draft` or `status: evaluating` |

Pattern `OPP-*.md` excludes [`_example-opportunity.md`](../opportunities/_example-opportunity.md).

## Preconditions (STOP with NOOP comment if any fail)

1. Trigger is **new push to branch** (not PR opened alone).
2. PR head branch is **exactly** `opp/pipeline` (not `opp/{slug}`, not `master`, not legacy `intake/**` or `eval/**`).
3. **OPP resolution** — list all `opportunities/OPP-*.md` on the branch, then filter **active OPPs** (`status: draft` or `status: evaluating`):

   | Active count | Result |
   |--------------|--------|
   | 0 | NOOP: no pipeline OPP in progress (catalogue `decided` only) |
   | 1 | **Target file** for pipeline-orchestrator-v2 |
   | 2+ | NOOP: ambiguous — studio rule (one active OPP at a time) |

   In NOOP comments, report catalogue count (decided), active count, and list active filenames.

4. Target file `status` must **not** be `decided` (guard; should not occur via active filter). If `decided` → NOOP: opportunity already decided.

5. Skip if this push only changes paths outside `opportunities/` and `portfolio/` **and** the active OPP file is unchanged since last eval (avoid doc-only loops). If the active OPP or portfolio files changed → proceed.

If preconditions fail, post a short PR comment explaining what is missing. Do not modify files.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [pipeline-orchestrator-v2.md](pipeline-orchestrator-v2.md) for the resolved active OPP only.
3. **Up to 5 stages per run** — single commit at end of batch.
4. Commit and **push** to **`opp/pipeline`** (not `master`). Push re-triggers the next batch if pipeline not complete.
5. Post the **Pipeline Run Summary** from pipeline-orchestrator-v2 output format.
6. Do **not** run QA in this automation — **CP — QA** runs separately on push.

## Constraints

- Never push directly to the default branch.
- Do not edit `prompts/*` or `playbooks/*`.
- Studio capacity: **one active OPP** on `opp/pipeline` at a time; catalogue `decided` files are ignored for resolution.

## Related

- [Pipeline orchestrator v2](pipeline-orchestrator-v2.md)
- [Automations setup](../docs/automations.md)
