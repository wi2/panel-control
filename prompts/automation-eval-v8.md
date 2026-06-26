---
version: 8
stage: automation_eval
status: active
created: 2026-06-26
supersedes: automation-eval-v7
changelog: "Strict full run via orchestrator v6; success = decided only; no partial handoff"
---

# Automation Eval Wrapper v8

## Role

Thin wrapper for **CP — Eval**. Runs the **full remaining pipeline** in one invocation when label **`cp:eval`** is added on branch **`opp/pipeline`**.

## Objective

Delegate to [pipeline-orchestrator-v6.md](pipeline-orchestrator-v6.md) after enforcing branch, label, and intake-readiness gates.

**Success criterion**: one `cp:eval` → `status: decided` + portfolio sync + `Remaining stages: none` in summary.

**Failure criterion**: `Gate status: failed_incomplete` or `blocked` — operator must not merge; do not treat partial runs as success.

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
   | 1 | **Target file** for pipeline-orchestrator-v6 |
   | 2+ | NOOP: ambiguous — studio rule (one active OPP at a time) |

   In NOOP comments, report catalogue count (decided), active count, and list active filenames.

4. Target file **`intake_complete: true`** in frontmatter → else **NOOP: intake not complete — run CP — Intake first**.
5. Section **Discovery** is filled: no `<!-- Paste output -->` placeholder; `confidence_level` present in Discovery section.
6. Target file `status` must **not** be `decided`. If `decided` → NOOP: opportunity already decided — remove `cp:eval` label.

If preconditions fail, post a short PR comment explaining what is missing. Do not modify files.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [pipeline-orchestrator-v6.md](pipeline-orchestrator-v6.md) for the resolved active OPP only.
3. **Full pipeline run** — execute **all** remaining stages for the active strategy in **this single invocation**; one commit at end.
4. Before posting summary: confirm `status: decided` OR report `Gate status: failed_incomplete` / `blocked` per orchestrator v6.
5. Commit and **push** to **`opp/pipeline`** (not `master`).
6. Post the **Pipeline Run Summary** from pipeline-orchestrator-v6 output format.
7. On success only: recommend **removing label `cp:eval`**. On `failed_incomplete`: state **do not merge**.
8. **Never** post `Mode: single stage` or instruct operator to re-add `cp:eval` as normal next step.
9. Do **not** run QA in this automation — **CP — QA** runs separately on push.

## Constraints

- Never push directly to the default branch.
- Do not edit `prompts/*` or `playbooks/*`.
- Studio capacity: **one active OPP** on `opp/pipeline` at a time; catalogue `decided` files are ignored for resolution.
- BUILD preparation stages are **not** in scope — manual after `decision: build`.

## Related

- [Pipeline orchestrator v6](pipeline-orchestrator-v6.md)
- [Automations setup](../docs/automations.md)
- Previous: [automation-eval-v7.md](automation-eval-v7.md)
