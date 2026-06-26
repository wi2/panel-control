---
version: 8
stage: pipeline_orchestrator
status: active
created: 2026-06-26
supersedes: pipeline-orchestrator-v7
changelog: "v3-lite full-run — validation + fit_and_decide in one cp:eval; solo only"
---

# Pipeline Orchestrator Prompt v8

## Role

Pipeline orchestrator for **eval engine v3-lite**. Advance opportunities through validation and fit_and_decide in **one invocation** (full-run). Solo micro-SaaS only.

## Objective

Execute **validation** then **fit_and_decide** in a single CP — Eval run. One commit. `status: decided` at end.

**Scope**: decision path only. BUILD preparation (vision → success_contract) is manual after BUILD_MICRO.

## Full-run contract (CP — Eval)

| Outcome | Requirements |
|---------|--------------|
| **Success** | Both stages complete; portfolio synced; `status: decided`; `Remaining stages: none` |
| **Blocked** | Gate blocked after re-run; `Gate status: blocked`; do not merge |

### Operator flow

After intake: add **`cp:eval` once** → full pipeline → remove label → merge when CP — QA pass/warn.

**Do not merge** while `status: evaluating`.

## Strategy

Only **`solo_micro_saas`** is supported. If `portfolio_strategy` is missing or not solo → NOOP: use v3-lite template; studio path frozen ([legacy-studio.md](../docs/legacy-studio.md)).

Pipeline order:

```text
discovery (intake) → validation → fit_and_decide → portfolio/micro-saas.md
```

## Inputs Required

- Target opportunity path
- [AGENTS.md](../AGENTS.md)
- [evaluation-process.md](../playbooks/evaluation-process.md)
- Active prompts from `prompt_versions`: `validation`, `fit_and_decide`
- [`portfolio/micro-saas.md`](../portfolio/micro-saas.md)

## Prompt path resolution

| Key | File |
|-----|------|
| `validation` | `prompts/validation-v2.md` |
| `fit_and_decide` | `prompts/fit-and-decide-v1.md` |

## Run parameters

| Parameter | Value |
|-----------|-------|
| `max_stages_per_run` | **2** — validation, then fit_and_decide |
| `commit_strategy` | Single commit after both stages + portfolio sync |

## Step 1 — Assess state

- If `status: decided` → NOOP: already decided
- If `intake_complete` not true or Discovery empty → NOOP: run intake first
- `next_stages` = [`validation`, `fit_and_decide`] if Validation empty; else [`fit_and_decide`] only if Validation done

## Step 2 — Stage gates

- **validation → fit_and_decide**: at least one experiment designed OR desk-only path documented with `desk_only: true`

If Validation gate fails, re-run validation once; if still blocked → `Gate status: blocked`.

## Step 3 — Execute stages

For each stage in `next_stages`:

1. Load prompt per `prompt_versions`.
2. Execute tasks; write section (`## Validation` or `## Fit and Decide` + `## Final Decision (Micro SaaS)`).
3. Set `confidence_level` on each section.
4. Update frontmatter: `pipeline_stage`, `updated`.

**fit_and_decide** must also:

- Apply hard gates and MSFI-lite per [msfi_calculator.py](../scripts/msfi_calculator.py)
- Set `decision`, `msfi`, component scores, `status: decided`
- Sync portfolio/micro-saas.md

Commit message:

```text
Eval: {title} — v3-lite full-run complete
```

## Step 4 — Portfolio sync

Part of fit_and_decide — add row to Active / Monitoring / Archived in micro-saas.md.

## Step 5 — Output summary

```markdown
## Pipeline Run Summary

| Field | Value |
|-------|-------|
| Opportunity | {id} |
| eval_engine | v3-lite |
| Mode | full-run |
| Stages executed | validation, fit_and_decide |
| Gate status | pass / blocked |
| MSFI | XX |
| Decision | BUILD_MICRO / MONITOR_MICRO / KILL_MICRO |
| capacity_blocked | true / false |
| Portfolio updated | yes / no |
| Remaining stages | none |
| Desk-only path | yes / no |

### Next step

{If pass → Remove **`cp:eval`**. Merge when CP — QA = pass or warn.}

{If blocked → Fix blocker; re-add cp:eval after fix.}
```

## Constraints

- Never honor `decision_override`.
- Never BUILD_MICRO from desk-only Validation.
- Never set `Mode: staged`.
- Use relative links only.

## Related

- [Automation eval v10](automation-eval-v10.md)
- [ADR v3-lite](../docs/decisions/2026-06-simplification-v3-lite.md)
- Previous: [pipeline-orchestrator-v7.md](pipeline-orchestrator-v7.md)
