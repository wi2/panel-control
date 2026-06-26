---
version: 7
stage: automation_eval
status: active
created: 2026-06-26
supersedes: automation-eval-v6
changelog: "Label cp:eval trigger; full pipeline run; intake_complete gate; inlined preconditions"
---

# Automation Eval Wrapper v7

## Role

Thin wrapper for **CP — Eval**. Runs the **full remaining pipeline** in one invocation when label **`cp:eval`** is added on branch **`opp/pipeline`**.

## Objective

Delegate to [pipeline-orchestrator-v5.md](pipeline-orchestrator-v5.md) after enforcing branch, label, and intake-readiness gates.

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
   | 1 | **Target file** for pipeline-orchestrator-v5 |
   | 2+ | NOOP: ambiguous — studio rule (one active OPP at a time) |

   In NOOP comments, report catalogue count (decided), active count, and list active filenames.

4. Target file **`intake_complete: true`** in frontmatter → else **NOOP: intake not complete — run CP — Intake first** (applies even if `cp:intake` and `cp:eval` were added simultaneously).
5. Section **Discovery** is filled: no `<!-- Paste output -->` placeholder; `confidence_level` present in Discovery section.
6. Target file `status` must **not** be `decided`. If `decided` → NOOP: opportunity already decided — remove `cp:eval` label.

If preconditions fail, post a short PR comment explaining what is missing. Do not modify files.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [pipeline-orchestrator-v5.md](pipeline-orchestrator-v5.md) for the resolved active OPP only.
3. **Full pipeline run** — all remaining stages for the active strategy — single commit at end.
4. Commit and **push** to **`opp/pipeline`** (not `master`).
5. Post the **Pipeline Run Summary** from pipeline-orchestrator-v5 output format.
6. In the PR comment, recommend **removing label `cp:eval`** after successful `decided` to avoid accidental re-trigger.
7. Do **not** run QA in this automation — **CP — QA** runs separately on push.

## Constraints

- Never push directly to the default branch.
- Do not edit `prompts/*` or `playbooks/*`.
- Studio capacity: **one active OPP** on `opp/pipeline` at a time; catalogue `decided` files are ignored for resolution.
- BUILD preparation stages are **not** in scope — manual after `decision: build`.

## Related

- [Pipeline orchestrator v5](pipeline-orchestrator-v5.md)
- [Automations setup](../docs/automations.md)
- Previous: [automation-eval-v6.md](automation-eval-v6.md)
