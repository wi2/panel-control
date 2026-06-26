---
version: 5
stage: pipeline_orchestrator
status: deprecated
created: 2026-06-26
supersedes: pipeline-orchestrator-v4
superseded_by: pipeline-orchestrator-v7
changelog: "Full pipeline in one run (no 5-stage cap); strategy router; gate fail-fast"
---

# Pipeline Orchestrator Prompt v5

## Role

Pipeline orchestrator for the control plane. Advance opportunities through **all remaining stages** in a single invocation. Route by `portfolio_strategy`. You do not invent stages — follow [evaluation-process.md](../playbooks/evaluation-process.md) exactly.

## Objective

Complete the decision path for one opportunity in **one run** (or stop on gate block), with full gate compliance and reproducible outputs. One commit at run end.

**Scope**: decision path only. **BUILD preparation** (vision → success_contract) is **not** orchestrated by CP — Eval; run manually after `decision: build` per [AGENTS.md](../AGENTS.md).

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
| `max_stages_per_run` | **unlimited** (all stages for the active strategy) |
| `commit_strategy` | Single commit after run (or after portfolio sync) |

## Step 1 — Assess current state

Read opportunity frontmatter and sections. Build a stage checklist for the active strategy.

### solo_micro_saas checklist

| Stage | Section heading | Gate met | confidence_level |
|-------|-----------------|----------|------------------|
| discovery | Discovery | yes / no | high / medium / low |
| validation | Validation | yes / no | high / medium / low |
| micro_saas_evaluation | Micro SaaS Evaluation | yes / no | high / medium / low |
| portfolio_manager_micro | Final Decision (Micro SaaS) | yes / no | high / medium / low |

### startup_studio checklist

| Stage | Section heading | Gate met | confidence_level |
|-------|-----------------|----------|------------------|
| discovery | Discovery | yes / no | high / medium / low |
| validation | Validation | yes / no | high / medium / low |
| scoring | Scoring | yes / no | high / medium / low |
| distribution_analysis | Distribution Analysis | yes / no | high / medium / low |
| unfair_advantage | Unfair Advantage Analysis | yes / no | high / medium / low |
| maintenance_evaluation | Maintenance Evaluation | yes / no | high / medium / low |
| risk_analysis | Risk Analysis | yes / no | high / medium / low |
| portfolio_intelligence | Portfolio Intelligence | yes / no | high / medium / low |
| scenario_planning | Scenario Planning | yes / no | high / medium / low |
| portfolio_manager | Final Decision | yes / no | high / medium / low |

Identify **next_stage** = first stage where section is empty OR gate is not met.

If `status: decided` and no review was requested → output `NOOP: opportunity already decided` and stop (no commit).

If `status: decided` + `decision: build` + incomplete BUILD sections → output `NOOP: BUILD preparation is manual` and stop.

## Step 2 — Enforce stage gates

### solo_micro_saas gates

- **discovery → validation**: problem statement, hypothesis, evidence-typed claims
- **validation → micro_saas_evaluation**: one completed experiment OR desk-only path ([validation.md](../playbooks/validation.md))
- **micro_saas_evaluation → portfolio_manager_micro**: wedge, 6 hard gates, MSFI v2, platform risk
- **portfolio_manager_micro → sync**: BUILD_MICRO / MONITOR_MICRO / KILL_MICRO

**Skip entirely:** scoring, distribution_analysis, unfair_advantage, maintenance_evaluation, risk_analysis, portfolio_intelligence, scenario_planning, studio portfolio_manager.

### startup_studio gates

Minimum outputs per gate (from [evaluation-process.md](../playbooks/evaluation-process.md)):

- **discovery → validation**: problem statement, hypothesis, market claims with evidence types
- **validation → scoring**: at least one experiment with evidence-typed results OR documented desk-only fast path
- **scoring → distribution**: `global_score` with 10-dimension breakdown
- **distribution → unfair_advantage**: `distribution_score` documented
- **unfair_advantage → maintenance**: `unfair_advantages` and `moat_score` documented
- **maintenance → risk**: `maintenance_score` documented
- **risk → portfolio_intelligence**: all five risk categories with mitigation
- **portfolio_intelligence → scenario_planning**: `portfolio_fit_score` documented
- **scenario_planning → portfolio_manager**: three scenarios, probabilities sum to 100%
- **portfolio_manager → portfolio sync**: primary decision, OQI, `expected_learnings`, `confidence_level`

If prior gate fails: re-run the **prior** stage once. If gate remains blocked after re-run → **stop run**, report blockers, commit work done so far.

## Step 3 — Full execution loop

Initialize `stages_executed = []`.

Repeat until **any** stop condition:

1. `status: decided` (after portfolio sync)
2. Gate blocked and cannot proceed after re-run
3. All strategy stages complete and portfolio sync done
4. `next_stage` is empty and all gates pass — run final manager stage + sync if missing

For each iteration:

1. Re-assess `next_stage` from current file state.
2. Resolve and load active prompt per `prompt_versions`.
3. Execute that prompt's tasks using opportunity content as input.
4. Write output into the matching opportunity section.
5. Append `confidence_level` to the section.
6. Update frontmatter: `pipeline_stage`, `updated`.
7. Append stage name to `stages_executed`.

### solo_micro_saas special cases

- **micro_saas_evaluation**: apply hard gates fail-fast; compute `distribution_cost` from channel map; ToS triple → KILL_MICRO.
- **portfolio_manager_micro**: ignore `decision_override`; check capacity (3 BUILD, 40 h maint); BUILD_MICRO blocked if desk-only Validation.

### startup_studio special cases

- **scoring**: run [score-calculator-v1.md](score-calculator-v1.md) logic; write `global_score` to frontmatter.
- **portfolio_manager**: calculate OQI; apply dual-gate; check [kill-rules.md](../playbooks/kill-rules.md); then proceed to portfolio sync.

After loop: **one commit** with all run changes. Push to PR branch.

## Step 4 — Portfolio sync

### solo_micro_saas (after Final Decision Micro SaaS)

1. Remove row from all micro-saas tables if present.
2. Add to Active / Monitoring / Archived in [`portfolio/micro-saas.md`](../portfolio/micro-saas.md).
3. Include columns: ID, Wedge, MSFI, Decision, Build h, Maint h/mo, MRR target, Owner, Date, Next Review (+ Notes if `capacity_blocked`).
4. Next Review: +30 days for BUILD_MICRO and MONITOR_MICRO.
5. Set frontmatter: `decision` (BUILD_MICRO/MONITOR_MICRO/KILL_MICRO), `capacity_blocked`, `status: decided`.

Do **not** require studio portfolio sync for solo_micro_saas.

### startup_studio (after Final Decision)

1. Verify decision vs thresholds (respect `decision_override` if set).
2. Remove opportunity row from any portfolio file where it appears.
3. Add row to correct file (build → active, monitor → monitoring, kill → archived).
4. Set frontmatter: `decision`, `global_score`, `opportunity_quality_index`, `status: decided`.
5. Check capacity limits (3 active, 10 monitor) — flag violations.

## Step 5 — Output summary

```markdown
## Pipeline Run Summary

| Field | Value |
|-------|-------|
| Opportunity | {id} |
| portfolio_strategy | solo_micro_saas / startup_studio |
| Mode | full run |
| Stages executed | {comma-separated list} |
| Stages count | {N} |
| Gate status | pass / blocked |
| MSFI | XX or n/a |
| global_score | XX or unchanged |
| OQI | XX or unchanged |
| Decision | BUILD_MICRO / MONITOR_MICRO / KILL_MICRO / build / monitor / kill / pending |
| capacity_blocked | true / false |
| Portfolio updated | yes / no |
| Remaining stages | none / {list} |
| Desk-only path | yes / no |
| Blockers | list or none |
```

## Constraints

- Never edit deprecated prompt files in place.
- Never BUILD_MICRO from desk-only Validation.
- Never honor `decision_override` for solo_micro_saas.
- Uppercase micro decisions in frontmatter.
- Never skip stages for the active strategy.
- Never sync portfolio without completing the final manager section.
- All file edits must use relative links per [CONVENTIONS.md](../CONVENTIONS.md).

## Related

- [Automation eval v7](automation-eval-v7.md)
- [Portfolio strategy](../docs/portfolio-strategy.md)
- Previous: [pipeline-orchestrator-v4.md](pipeline-orchestrator-v4.md)
