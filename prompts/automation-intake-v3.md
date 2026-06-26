---
version: 3
stage: automation_intake
status: active
created: 2026-06-26
supersedes: automation-intake-v2
changelog: "Fixed branch opp/pipeline — one OPP at a time on studio pipeline branch"
---

# Automation Intake Wrapper v3

## Role

Thin wrapper for the **CP — Intake** Cursor Automation. Creates a new opportunity file and runs Discovery from a PR description on branch **`opp/pipeline`**.

## Objective

Delegate to [intake-v3.md](intake-v3.md) after enforcing branch and label gates.

## Preconditions (STOP with NOOP comment if any fail)

1. Label **`cp:intake`** was **added** on this PR (not removed).
2. PR head branch is **exactly** `opp/pipeline`.
3. PR body contains a `## Intake` section with at least **Title** and **Description**.
4. **No** `opportunities/OPP-*.md` file exists on the branch yet. If OPP already exists → NOOP: use CP — Eval (push on `opp/pipeline`) instead.

If preconditions fail, post a short PR comment explaining what is missing. Do not modify files.

## Parse PR body

From the `## Intake` section extract:

| Field | Required | Default |
|-------|----------|---------|
| Title | yes | — |
| Description | yes | — |
| Owner | no | `studio-team` |
| Tags | no | `[]` |

Use these as inputs to intake-v3.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [intake-v3.md](intake-v3.md) with parsed inputs.
3. Commit and **push** to **`opp/pipeline`** (not `master`). Push triggers **CP — Eval** for the next pipeline batch.
4. Post **Intake Complete** summary from intake-v3 output format.
5. Do **not** run validation, scoring, or portfolio decisions in intake.

## Constraints

- One idea → one OPP file per run on `opp/pipeline`.
- Never push directly to the default branch.
- Do not edit `prompts/*` or `playbooks/*`.

## Related

- [Intake v3](intake-v3.md)
- [Automations setup](../docs/automations.md)
