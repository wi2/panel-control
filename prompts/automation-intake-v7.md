---
version: 7
stage: automation_intake
status: deprecated
created: 2026-06-26
supersedes: automation-intake-v6
changelog: "PR opened trigger + cp:intake label; same preconditions; anti double-run"
---

# Automation Intake Wrapper v7

## Role

Thin wrapper for **CP — Intake**. Creates a new opportunity file and runs Discovery from a PR description on branch **`opp/pipeline`**.

## Objective

Delegate to [intake-v6.md](intake-v6.md) after enforcing branch, trigger, and readiness gates.

## Triggers (Cursor UI — configure both on CP — Intake)

| Trigger | When it runs |
|---------|----------------|
| **Git — pull request opened** | PR created on `opp/pipeline` with `## Intake` body |
| **Git — label change** | Label **`cp:intake`** **added** (optional fallback) |

## Terminology

| Term | Definition |
|------|------------|
| **Catalogue** | `opportunities/OPP-*.md` with `status: decided` (inherited from `master`) — allowed |
| **Active OPP** | `opportunities/OPP-*.md` with `status: draft` or `status: evaluating` |

## Preconditions (STOP with NOOP comment if any fail)

1. PR head branch is **exactly** `opp/pipeline`.
2. PR body contains a `## Intake` section with at least **Title** and **Description**.
3. **No active OPP** on the branch: no `opportunities/OPP-*.md` with `status: draft` or `status: evaluating`.

   - Catalogue of `decided` OPP files from `master` is **allowed**.
   - If an active OPP exists → NOOP: use **CP — Eval** (add label `cp:eval`) instead.
   - In NOOP comments, list active filenames if any.

4. **Label gate** (label trigger only): label **`cp:intake`** was **added** on this PR (not removed). When triggered by **PR opened**, this gate is skipped.

5. **Anti double-run**: if an OPP file for this pipeline run already exists with `intake_complete: true` on the branch → NOOP: intake already complete — add `cp:eval`.

If preconditions fail, post a short PR comment explaining what is missing. Do not modify files.

## Parse PR body

From the `## Intake` section extract:

| Field | Required | Default |
|-------|----------|---------|
| Title | yes | — |
| Description | yes | — |
| Owner | no | `studio-team` |
| Tags | no | `[]` |

Use these as inputs to intake-v6.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [intake-v6.md](intake-v6.md) with parsed inputs.
3. Commit and **push** to **`opp/pipeline`** (not `master`). Push triggers **CP — QA** (push only) — **not** CP — Eval.
4. Post **Intake Complete** summary from intake-v6 output format.
5. Remind in the PR comment: add label **`cp:eval`** to run **validation** (re-add after each staged summary until `decided`).
6. Do **not** run validation, scoring, or portfolio decisions in intake.

## Constraints

- One idea → one new OPP file per run on `opp/pipeline`.
- Never push directly to the default branch.
- Do not edit `prompts/*` or `playbooks/*`.

## Related

- [Intake v6](intake-v6.md)
- [Automations setup](../docs/automations.md)
- Previous: [automation-intake-v6.md](automation-intake-v6.md)
