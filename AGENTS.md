# Agent Instructions — AI Startup Studio Brain

You operate inside a documentation-first control plane. You do **not** build product code here.

## Before any action

1. Read opportunity frontmatter: `portfolio_strategy`, `status`, `decision`, `prompt_versions`, `pipeline_stage`.
2. Read [playbooks/evaluation-process.md](playbooks/evaluation-process.md) for stage order (strategy-dependent).
3. Read [CONVENTIONS.md](CONVENTIONS.md) and [docs/portfolio-strategy.md](docs/portfolio-strategy.md).

## Strategy router

| `portfolio_strategy` | Pipeline | Decisions | Registry |
|---------------------|----------|-----------|----------|
| **`solo_micro_saas`** (default) | 4-stage fast path | BUILD_MICRO / MONITOR_MICRO / KILL_MICRO | [portfolio/micro-saas.md](portfolio/micro-saas.md) |
| **`startup_studio`** | 10-stage legacy | build / monitor / kill | active / monitoring / archived |

### solo_micro_saas fast path

```text
discovery → validation → micro_saas_evaluation → portfolio_manager_micro
```

- **Skip:** scoring through studio portfolio_manager.
- **`global_score` / OQI:** diagnostic only — never gate BUILD_MICRO.
- **`decision_override`:** ignored for solo_micro_saas.
- **Capacity:** max 3 BUILD_MICRO, 40 h/mo maint total → `MONITOR_MICRO` + `capacity_blocked: true`.

Hard gates (any FAIL → KILL_MICRO): see [playbooks/micro-saas-portfolio.md](playbooks/micro-saas-portfolio.md).

### startup_studio legacy path

```text
discovery → validation → scoring → distribution_analysis → unfair_advantage
→ maintenance_evaluation → risk_analysis → portfolio_intelligence
→ scenario_planning → portfolio_manager
```

BUILD-only (after `decision: build`):

```text
vision → mvp → roadmap → architecture → success_contract
```

## How to pick the next stage

| status | solo_micro_saas | startup_studio |
|--------|-----------------|----------------|
| `draft` | Run discovery | Run discovery |
| `evaluating` | First empty/failing stage in fast path | First empty/failing stage in 10-stage path |
| `decided` | No re-run unless review | Same |

Use `prompt_versions` — never silently switch prompt versions.

### Prompt path resolution

```text
prompts/{stage_key with _ replaced by -}-v{N}.md
```

Examples: `micro_saas_evaluation: v2` → `prompts/micro-saas-evaluation-v2.md`; `portfolio_manager_micro: v1` → `prompts/portfolio-manager-micro-v1.md`.

Automated advancement: **CP — Eval** on branch **`opp/pipeline`** via label **`cp:eval`** ([docs/automations.md](docs/automations.md)) using [prompts/pipeline-orchestrator-v5.md](prompts/pipeline-orchestrator-v5.md). Full pipeline in one run after Intake sets `intake_complete: true`.

## Decision rules

### solo_micro_saas

| Decision | Criteria |
|----------|----------|
| BUILD_MICRO | All hard gates PASS + MSFI ≥ 70 + live validation (no desk-only) |
| MONITOR_MICRO | Hard gates PASS + MSFI 50–69, borderline gate, or capacity wait |
| KILL_MICRO | Hard gate FAIL or MSFI < 50 |

### startup_studio

| Decision | Criteria |
|----------|----------|
| BUILD | `global_score >= 75` AND `OQI >= 70` AND capacity |
| MONITOR | `global_score` 50–74, OR score qualifies but OQI < 70 |
| KILL | `global_score < 50` OR kill trigger |

Studio override: `decision_override: true` with rationale (not applicable to solo_micro_saas).

## After completing a stage

1. Paste output into matching section.
2. Set section `confidence_level`.
3. Tag evidence on decision-relevant claims.
4. Update frontmatter: `pipeline_stage`, `updated`.
5. On final micro/studio manager: sync portfolio registry, set `status: decided`.

## Files you may modify

- `opportunities/OPP-*.md`
- `portfolio/micro-saas.md` (canonical for solo_micro_saas)
- `portfolio/active.md`, `monitoring.md`, `archived.md` (startup_studio / legacy)
- `reviews/REVIEW-*.md`

## Files you must NOT modify without version bump

- `prompts/*-v*.md` (create `v{N+1}` instead)

## Pull request QA

When a PR modifies `opportunities/` or `portfolio/`:

1. Read [prompts/opportunity-qa.md](prompts/opportunity-qa.md) (active v3).
2. For startup_studio: apply [prompts/score-calculator.md](prompts/score-calculator.md).
3. For solo_micro_saas: apply [scripts/msfi_calculator.py](scripts/msfi_calculator.py) logic.
4. Verdict **pass**, **warn**, or **fail** — do not merge on **fail**.

## Intake

1. Read [prompts/intake.md](prompts/intake.md) (v6).
2. Branch **`opp/pipeline`**; one active OPP at a time.
3. Default `portfolio_strategy: solo_micro_saas`.
4. Label `cp:intake` once; then label **`cp:eval`** after Intake Complete for full pipeline run.

## Portfolio review

1. [prompts/portfolio-review-runner.md](prompts/portfolio-review-runner.md) or **CP — Review**.
2. Max 3 MONITOR / MONITOR_MICRO per run.

Automations: **CP — QA**, **CP — Intake**, **CP — Eval**, **CP — Review** — [docs/automations.md](docs/automations.md).

## References

- [playbooks/micro-saas-portfolio.md](playbooks/micro-saas-portfolio.md)
- [playbooks/evaluation-process.md](playbooks/evaluation-process.md)
- [playbooks/kill-rules.md](playbooks/kill-rules.md)
- [playbooks/portfolio-rules.md](playbooks/portfolio-rules.md)
