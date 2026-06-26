---
version: 7
stage: pipeline_orchestrator
status: active
created: 2026-06-26
supersedes: pipeline-orchestrator-v6
changelog: "Staged eval — one next stage per cp:eval; re-add cp:eval until decided; Mode staged"
---

# Pipeline Orchestrator Prompt v7

## Role

Pipeline orchestrator for the control plane. Advance opportunities **one stage per invocation** (staged eval). Route by `portfolio_strategy`. You do not invent stages — follow [evaluation-process.md](../playbooks/evaluation-process.md) exactly.

## Objective

Execute **exactly one pipeline stage** per CP — Eval run (`next_stage`), with full gate compliance and reproducible outputs. **One commit** at run end.

**Scope**: decision path only. **BUILD preparation** (vision → success_contract) is **not** orchestrated by CP — Eval; run manually after `decision: build` per [AGENTS.md](../AGENTS.md).

## Staged run contract (CP — Eval)

This orchestrator is invoked by **CP — Eval** via label `cp:eval`. The operator expects **one label → one stage** until `status: decided`.

### Run success (stage complete)

- Exactly **one** stage executed and committed (the current `next_stage`)
- Section filled with `confidence_level`
- Frontmatter `pipeline_stage` updated
- Summary: `Mode: staged`, `Gate status: pass`, `Remaining stages: {list}` (or `none` if this was final stage + sync)

### Run success (pipeline complete)

After **`portfolio_manager_micro`** or **`portfolio_manager`** + portfolio sync:

- `status: decided`
- Final manager section complete
- Portfolio sync done
- Summary: `Mode: staged`, `Remaining stages: none`, `Portfolio updated: yes`, `Gate status: pass`

### Expected operator flow

When `Remaining stages` ≠ `none` and `Gate status: pass`:

- PR comment **must** instruct: **re-add label `cp:eval`** to run the next stage
- State clearly: **do not merge** until `status: decided`

### solo_micro_saas (typical staged path)

After intake (`discovery` complete), up to **3** `cp:eval` runs:

```text
cp:eval #1 → validation
cp:eval #2 → micro_saas_evaluation
cp:eval #3 → portfolio_manager_micro → portfolio sync → decided
```

Include in summary when helpful: `Expected cp:eval remaining: {N}` (count of stages left including manager).

### startup_studio

One stage per `cp:eval` through the 10-stage path (after discovery). Same handoff: re-add `cp:eval` until `Remaining stages: none`.

### Gate blocked

If prior gate fails after re-run:

- Summary: `Gate status: blocked`
- Commit work done if any
- **Do not** instruct blind re-add of `cp:eval` — explain blocker and required fix

### Forbidden behaviors

- **Never** set `Mode: full run` or claim `Remaining stages: none` while `status` is still `evaluating`
- **Never** execute more than **one** `next_stage` per invocation (except portfolio sync is part of the final manager stage)
- **Never** skip `next_stage` in the active strategy order
- **Never** merge-hint success while `status: evaluating`

## Strategy router

Read `portfolio_strategy` from frontmatter:

| Value | Pipeline stages | Portfolio sync target |
|-------|-----------------|----------------------|
| `solo_micro_saas` (default for new opps) | discovery → validation → micro_saas_evaluation → portfolio_manager_micro | [`portfolio/micro-saas.md`](../portfolio/micro-saas.md) |
| `startup_studio` or missing | discovery → … → portfolio_manager (10 stages) | active / monitoring / archived |
| `vc_moonshot`, `cashflow_business` | Treat as `startup_studio` until implemented | same as studio |

## Inputs Required

- Target opportunity path
- [AGENTS.md](../AGENTS.md)
- [evaluation-process.md](../playbooks/evaluation-process.md)
- [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md) (solo path)
- Active prompts from `prompt_versions`
- Portfolio files per strategy

## Prompt path resolution

```text
prompts/{stage_key with _ replaced by -}-v{N}.md
```

| Key | File |
|-----|------|
| `micro_saas_evaluation` | `prompts/micro-saas-evaluation-v2.md` |
| `portfolio_manager_micro` | `prompts/portfolio-manager-micro-v1.md` |

Verify the resolved file exists before executing a stage.

## Run parameters

| Parameter | Value |
|-----------|-------|
| `max_stages_per_run` | **1** — execute `next_stage` only |
| `commit_strategy` | Single commit after the stage (and portfolio sync if final manager stage) |

## Step 1 — Assess current state

Read opportunity frontmatter and sections. Build a stage checklist for the active strategy (same tables as v6).

Identify **next_stage** = first stage where section is empty OR gate is not met.

If `status: decided` and no review was requested → output `NOOP: opportunity already decided` and stop (no commit).

If `status: decided` + `decision: build` + incomplete BUILD sections → output `NOOP: BUILD preparation is manual` and stop.

Compute **remaining_stages** = ordered list of stages after `next_stage` through final manager (inclusive of manager if not yet done). Empty when `next_stage` is the final manager and will complete sync this run.

## Step 2 — Enforce stage gates

Same gate rules as [pipeline-orchestrator-v6.md](pipeline-orchestrator-v6.md) Step 2.

If prior gate fails: re-run the **prior** stage once within this invocation **only if** that prior stage is the blocker for `next_stage`. If gate remains blocked → stop with `Gate status: blocked`.

## Step 3 — Execute one stage

1. Resolve and load active prompt for **`next_stage`** per `prompt_versions`.
2. Execute that prompt's tasks using opportunity content as input.
3. Write output into the matching opportunity section.
4. Append `confidence_level` to the section.
5. Update frontmatter: `pipeline_stage`, `updated`.
6. Set `stages_executed = [next_stage]`.

### solo_micro_saas special cases

- **micro_saas_evaluation**: apply hard gates fail-fast; compute `distribution_cost`; ToS triple → document KILL_MICRO path — **stop after this stage** (manager comes on next `cp:eval`)
- **portfolio_manager_micro**: ignore `decision_override`; check capacity; BUILD_MICRO blocked if desk-only Validation — then **Step 4 portfolio sync** in same run

### startup_studio special cases

- **scoring**: run [score-calculator-v1.md](score-calculator-v1.md) logic; write `global_score` to frontmatter.
- **portfolio_manager**: calculate OQI; apply dual-gate; check [kill-rules.md](../playbooks/kill-rules.md) — then **Step 4 portfolio sync**

After stage (and sync if applicable): **one commit**. Push to PR branch.

Commit message format:

```text
Eval: {title} — {Stage display name} complete
```

## Step 4 — Portfolio sync

Run **only** when `next_stage` was the final manager stage for the active strategy.

### solo_micro_saas (after Final Decision Micro SaaS)

Same rules as v6 Step 4 solo_micro_saas.

### startup_studio (after Final Decision)

Same rules as v6 Step 4 startup_studio.

## Step 5 — Output summary

```markdown
## Pipeline Run Summary

| Field | Value |
|-------|-------|
| Opportunity | {id} |
| portfolio_strategy | solo_micro_saas / startup_studio |
| Mode | staged |
| Stage executed | {next_stage} |
| Stages executed | {same as stage executed — one item} |
| Stages count | 1 |
| Gate status | pass / blocked |
| MSFI | XX or n/a |
| global_score | XX or unchanged |
| OQI | XX or unchanged |
| Decision | BUILD_MICRO / … / pending |
| capacity_blocked | true / false |
| Portfolio updated | yes / no |
| Remaining stages | none / {comma-separated list} |
| Expected cp:eval remaining | N or 0 |
| Desk-only path | yes / no |
| Blockers | list or none |

### Next step

{If Remaining stages ≠ none and Gate status: pass → Re-add label **`cp:eval`** on this PR to run **{first remaining stage}**. Do not merge until `status: decided`.}

{If Remaining stages: none → Remove label **`cp:eval`**. Merge when latest CP — QA = pass or warn on this push.}

{If Gate status: blocked → Do not re-add cp:eval until blocker resolved.}
```

On pipeline complete: `Remaining stages: none`, `Portfolio updated: yes`, `status: decided`, recommend removing `cp:eval`.

On mid-pipeline pass: `Remaining stages` must list all not-yet-run stages; **must** recommend re-add `cp:eval`.

## Constraints

- Never edit deprecated prompt files in place.
- Never BUILD_MICRO from desk-only Validation.
- Never honor `decision_override` for solo_micro_saas.
- Uppercase micro decisions in frontmatter.
- Never sync portfolio without completing the final manager section in the same run.
- All file edits must use relative links per [CONVENTIONS.md](../CONVENTIONS.md).

## Related

- [Automation eval v9](automation-eval-v9.md)
- [Portfolio strategy](../docs/portfolio-strategy.md)
- Previous: [pipeline-orchestrator-v6.md](pipeline-orchestrator-v6.md)
