---
version: 4
stage: automation_intake
status: deprecated
created: 2026-06-26
superseded_by: automation-intake-v8
supersedes: automation-intake-v3
changelog: "Allow decided OPP catalogue on opp/pipeline; block only when active OPP exists"
---

# Automation Intake Wrapper v4

## Role

Thin wrapper for the **CP — Intake** Cursor Automation. Creates a new opportunity file and runs Discovery from a PR description on branch **`opp/pipeline`**.

## Objective

Delegate to [intake-v4.md](intake-v4.md) after enforcing branch and label gates.

## Terminology

| Term | Definition |
|------|------------|
| **Catalogue** | `opportunities/OPP-*.md` with `status: decided` (inherited from `master`) — allowed |
| **Active OPP** | `opportunities/OPP-*.md` with `status: draft` or `status: evaluating` |

## Preconditions (STOP with NOOP comment if any fail)

1. Label **`cp:intake`** was **added** on this PR (not removed).
2. PR head branch is **exactly** `opp/pipeline`.
3. PR body contains a `## Intake` section with at least **Title** and **Description**.
4. **No active OPP** on the branch: no `opportunities/OPP-*.md` with `status: draft` or `status: evaluating`.

   - Catalogue of `decided` OPP files from `master` is **allowed**.
   - If an active OPP exists → NOOP: use **CP — Eval** (push on `opp/pipeline`) instead.
   - In NOOP comments, list active filenames if any.

If preconditions fail, post a short PR comment explaining what is missing. Do not modify files.

## Parse PR body

From the `## Intake` section extract:

| Field | Required | Default |
|-------|----------|---------|
| Title | yes | — |
| Description | yes | — |
| Owner | no | `studio-team` |
| Tags | no | `[]` |

Use these as inputs to intake-v4.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [intake-v4.md](intake-v4.md) with parsed inputs.
3. Commit and **push** to **`opp/pipeline`** (not `master`). Push triggers **CP — Eval** for the next pipeline batch.
4. Post **Intake Complete** summary from intake-v4 output format.
5. Do **not** run validation, scoring, or portfolio decisions in intake.

## Constraints

- One idea → one new OPP file per run on `opp/pipeline`.
- Never push directly to the default branch.
- Do not edit `prompts/*` or `playbooks/*`.

## Related

- [Intake v4](intake-v4.md)
- [Automations setup](../docs/automations.md)
