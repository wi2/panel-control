---
version: 1
stage: automation_intake
status: deprecated
created: 2026-06-25
supersedes: null
superseded_by: automation-intake-v2
changelog: "Intake wrapper — PR branch + label gate for Cursor Automation CP — Intake"
---

# Automation Intake Wrapper v1

## Role

Thin wrapper for the **CP — Intake** Cursor Automation. Creates a new opportunity file and runs Discovery from a PR description.

## Objective

Delegate to [intake-v1.md](intake-v1.md) after enforcing branch and label gates.

## Preconditions (STOP with NOOP comment if any fail)

1. Label **`cp:intake`** was **added** on this PR (not removed).
2. PR head branch matches `intake/**` (e.g. `intake/mon-idee`, `intake/OPP-20260625-slug`).
3. PR body contains a `## Intake` section with at least **Title** and **Description**.

If preconditions fail, post a short PR comment explaining what is missing. Do not modify files.

## Parse PR body

From the `## Intake` section extract:

| Field | Required | Default |
|-------|----------|---------|
| Title | yes | — |
| Description | yes | — |
| Owner | no | `studio-team` |
| Tags | no | `[]` |

Use these as inputs to intake-v1 (equivalent to webhook or chat payload).

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [intake-v1.md](intake-v1.md) with parsed inputs.
3. Commit changes to the **PR branch** (not `master`).
4. Post **Intake Complete** summary from intake-v1 output format.
5. Do **not** run validation, scoring, or portfolio decisions.

## Constraints

- One idea → one OPP file per run.
- Never push directly to the default branch.
- Do not edit `prompts/*` or `playbooks/*`.

## Related

- [Intake](intake-v1.md)
- [Automations setup](../docs/automations.md)
