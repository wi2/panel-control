---
version: 4
stage: pipeline_orchestrator
status: deprecated
created: 2026-06-26
supersedes: pipeline-orchestrator-v3
superseded_by: pipeline-orchestrator-v5
changelog: "Strategy router — solo_micro_saas fast path (4 stages) vs startup_studio legacy (10 stages)"
---

# Pipeline Orchestrator Prompt v4

**Superseded by [pipeline-orchestrator-v5.md](pipeline-orchestrator-v5.md)** — full pipeline in one run.

## Role

Pipeline orchestrator for the control plane. Advance opportunities in **batches** (up to 5 stages). Route by `portfolio_strategy`.

## Objective

Advance one opportunity by up to **5 stages** per run. One commit at batch end.

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

## solo_micro_saas fast path

### Stage checklist

| Stage | Section heading |
|-------|-----------------|
| discovery | Discovery |
| validation | Validation |
| micro_saas_evaluation | Micro SaaS Evaluation |
| portfolio_manager_micro | Final Decision (Micro SaaS) |

### Gates

- **discovery → validation**: problem statement, hypothesis, evidence-typed claims
- **validation → micro_saas_evaluation**: one completed experiment OR desk-only path ([validation.md](../playbooks/validation.md))
- **micro_saas_evaluation → portfolio_manager_micro**: wedge, 6 hard gates, MSFI v2, platform risk
- **portfolio_manager_micro → sync**: BUILD_MICRO / MONITOR_MICRO / KILL_MICRO

**Skip entirely:** scoring, distribution_analysis, unfair_advantage, maintenance_evaluation, risk_analysis, portfolio_intelligence, scenario_planning, studio portfolio_manager.

### Special cases

- **micro_saas_evaluation**: apply hard gates fail-fast; compute `distribution_cost` from channel map; ToS triple → KILL_MICRO.
- **portfolio_manager_micro**: ignore `decision_override`; check capacity (3 BUILD, 40 h maint); BUILD_MICRO blocked if desk-only Validation.

### Portfolio sync (solo)

After Final Decision (Micro SaaS):

1. Remove row from all micro-saas tables if present.
2. Add to Active / Monitoring / Archived in [`portfolio/micro-saas.md`](../portfolio/micro-saas.md).
3. Include columns: ID, Wedge, MSFI, Decision, Build h, Maint h/mo, MRR target, Owner, Date, Next Review (+ Notes if `capacity_blocked`).
4. Next Review: +30 days for BUILD_MICRO and MONITOR_MICRO.
5. Set frontmatter: `decision` (BUILD_MICRO/MONITOR_MICRO/KILL_MICRO), `capacity_blocked`, `status: decided`.

Do **not** require studio portfolio sync for solo_micro_saas.

## startup_studio legacy path

Follow [pipeline-orchestrator-v3.md](pipeline-orchestrator-v3.md) logic for all 10 stages, OQI, dual-gate, and active/monitoring/archived sync.

## Batch parameters

| Parameter | Value |
|-----------|-------|
| `max_stages_per_run` | **5** |
| `commit_strategy` | Single commit after batch |

## Stop conditions

- `status: decided` (no review requested) → NOOP
- `len(stages_executed) >= 5`
- Gate blocked
- Portfolio sync complete

## Output summary

Include: `portfolio_strategy`, `MSFI`, `Decision` (BUILD_MICRO/…), `capacity_blocked`, `Desk-only path`, `Remaining stages`.

## Constraints

- Never BUILD_MICRO from desk-only Validation.
- Never honor `decision_override` for solo_micro_saas.
- Uppercase micro decisions in frontmatter.

## Related

- [Automation eval v6](automation-eval-v6.md)
- [Portfolio strategy](../docs/portfolio-strategy.md)
- Previous: [pipeline-orchestrator-v3.md](pipeline-orchestrator-v3.md)
