---
version: 2
stage: automation_intake
status: deprecated
created: 2026-06-26
supersedes: automation-intake-v1
superseded_by: automation-intake-v3
changelog: "Intake on opp/** — same PR as eval; no cp:eval label"
---

# Automation Intake Wrapper v2

## Role

Thin wrapper for the **CP — Intake** Cursor Automation. Creates a new opportunity file and runs Discovery from a PR description on an `opp/**` branch.

## Objective

Delegate to [intake-v2.md](intake-v2.md) after enforcing branch and label gates.

## Preconditions (STOP with NOOP comment if any fail)

1. Label **`cp:intake`** was **added** on this PR (not removed).
2. PR head branch matches `opp/**` (e.g. `opp/mon-idee`, `opp/contract-reminders-tpe`).
3. PR body contains a `## Intake` section with at least **Title** and **Description**.
4. **No** `opportunities/OPP-*.md` file exists on the branch yet. If OPP already exists → NOOP: use CP — Eval (push-triggered) on this PR instead.

If preconditions fail, post a short PR comment explaining what is missing. Do not modify files.

## Parse PR body

From the `## Intake` section extract:

| Field | Required | Default |
|-------|----------|---------|
| Title | yes | — |
| Description | yes | — |
| Owner | no | `studio-team` |
| Tags | no | `[]` |

Use these as inputs to intake-v2.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [intake-v2.md](intake-v2.md) with parsed inputs.
3. Commit and **push** changes to the **PR branch** (not `master`). Push triggers **CP — Eval** for the next pipeline batch.
4. Post **Intake Complete** summary from intake-v2 output format.
5. Do **not** run validation, scoring, or portfolio decisions in intake.

## Constraints

- One idea → one OPP file per run.
- Never push directly to the default branch.
- Do not edit `prompts/*` or `playbooks/*`.

## Related

- [Intake v2](intake-v2.md)
- [Automations setup](../docs/automations.md)
