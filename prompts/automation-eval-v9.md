---
version: 9
stage: automation_eval
status: deprecated
created: 2026-06-26
supersedes: automation-eval-v8
changelog: "Staged eval via orchestrator v7; one stage per cp:eval; re-add until decided"
---

# Automation Eval Wrapper v9

## Role

Thin wrapper for **CP — Eval**. Runs **one pipeline stage** per label **`cp:eval`** on branch **`opp/pipeline`**.

## Objective

Delegate to [pipeline-orchestrator-v7.md](pipeline-orchestrator-v7.md) after enforcing branch, label, and intake-readiness gates.

**Mid-pipeline success**: one stage complete + `Remaining stages` listed + instruct **re-add `cp:eval`**.

**Pipeline success**: `status: decided` + portfolio sync + `Remaining stages: none` — then remove `cp:eval`.

## Trigger

**Git — label change** — label **`cp:eval`** **added** (not removed).

**Do not** use push-to-branch trigger for CP — Eval.

## Terminology

| Term | Definition |
|------|------------|
| **Catalogue** | `opportunities/OPP-*.md` with frontmatter `status: decided` (typically inherited from `master`) |
| **Active OPP** | `opportunities/OPP-*.md` with frontmatter `status: draft` or `status: evaluating` |

Pattern `OPP-*.md` excludes [`_example-opportunity.md`](../opportunities/_example-opportunity.md).

## Preconditions (STOP with NOOP comment if any fail)

1. Label **`cp:eval`** was **added** on this PR (not removed).
2. PR head branch is **exactly** `opp/pipeline` (not `master`, not legacy branches).
3. **OPP resolution** — list all `opportunities/OPP-*.md` on the branch, then filter **active OPPs** (`status: draft` or `status: evaluating`):

   | Active count | Result |
   |--------------|--------|
   | 0 | NOOP: no pipeline OPP in progress (catalogue `decided` only) |
   | 1 | **Target file** for pipeline-orchestrator-v7 |
   | 2+ | NOOP: ambiguous — studio rule (one active OPP at a time) |

   In NOOP comments, report catalogue count (decided), active count, and list active filenames.

4. Target file **`intake_complete: true`** in frontmatter → else **NOOP: intake not complete — run CP — Intake first**.
5. Section **Discovery** is filled: no `<!-- Paste output -->` placeholder; `confidence_level` present in Discovery section.
6. Target file `status` must **not** be `decided`. If `decided` → NOOP: opportunity already decided — remove `cp:eval` label.

If preconditions fail, post a short PR comment explaining what is missing. Do not modify files.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [pipeline-orchestrator-v7.md](pipeline-orchestrator-v7.md) for the resolved active OPP only.
3. **Staged run** — execute **only** `next_stage` (one stage); one commit at end.
4. Post **Pipeline Run Summary** with `Mode: staged`.
5. If `Remaining stages` ≠ `none` and `Gate status: pass` → comment must say **re-add `cp:eval`** for next stage; **do not merge**.
6. If `Remaining stages: none` and `status: decided` → recommend **removing label `cp:eval`**; merge when CP — QA pass/warn on this push.
7. If `Gate status: blocked` → do not suggest re-add until blocker fixed.
8. Do **not** run QA in this automation — **CP — QA** runs separately on push.

## Expected cp:eval count (solo_micro_saas)

After intake, typically **3** labels until `decided`:

| Run | Stage |
|-----|-------|
| 1 | validation |
| 2 | micro_saas_evaluation |
| 3 | portfolio_manager_micro (+ sync) |

## Constraints

- Never push directly to the default branch.
- Do not edit `prompts/*` or `playbooks/*`.
- Studio capacity: **one active OPP** on `opp/pipeline` at a time; catalogue `decided` files are ignored for resolution.
- BUILD preparation stages are **not** in scope — manual after `decision: build`.

## Related

- [Pipeline orchestrator v7](pipeline-orchestrator-v7.md)
- [Automations setup](../docs/automations.md)
- Previous: [automation-eval-v8.md](automation-eval-v8.md)
