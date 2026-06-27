# Agent Instructions — AI Startup Studio Brain

You operate inside a documentation-first control plane. You do **not** build product code here.

**Eval engine:** `v3-lite` — solo micro-SaaS only. Studio path frozen: [docs/legacy-studio.md](docs/legacy-studio.md). ADR: [docs/decisions/2026-06-simplification-v3-lite.md](docs/decisions/2026-06-simplification-v3-lite.md).

**Boundary:** This repo is **decision-only**. After `BUILD_MICRO`, bootstrap a product repo — [playbooks/build-handoff.md](playbooks/build-handoff.md). ADR: [docs/decisions/2026-07-control-plane-vs-product-repo.md](docs/decisions/2026-07-control-plane-vs-product-repo.md). No vision, architecture, or code agents run here.

## Before any action

1. Read opportunity frontmatter: `eval_engine`, `portfolio_strategy`, `status`, `decision`, `prompt_versions`, `pipeline_stage`.
2. Read [playbooks/evaluation-process.md](playbooks/evaluation-process.md).
3. Read [CONVENTIONS.md](CONVENTIONS.md) and [docs/portfolio-strategy.md](docs/portfolio-strategy.md).

## Pipeline (solo_micro_saas only)

```text
discovery (intake) → validation → fit_and_decide → portfolio/micro-saas.md
```

| Stage | Prompt | Section |
|-------|--------|---------|
| Discovery | [discovery-v1.md](prompts/discovery-v1.md) | Discovery |
| Validation | [validation-v2.md](prompts/validation-v2.md) | Validation |
| Fit and Decide | [fit-and-decide-v1.md](prompts/fit-and-decide-v1.md) | Fit and Decide + Final Decision (Micro SaaS) |

- **`decision_override`:** not allowed.
- **Capacity:** max 3 BUILD_MICRO, 40 h/mo maint → `MONITOR_MICRO` + `capacity_blocked: true`.
- **MSFI-lite:** 3 components — Python [scripts/msfi_calculator.py](scripts/msfi_calculator.py).

Hard gates: [playbooks/micro-saas-portfolio.md](playbooks/micro-saas-portfolio.md).

## How to pick the next stage

| status | Action |
|--------|--------|
| `draft` | Run intake / discovery |
| `evaluating` | First empty stage: validation → fit_and_decide |
| `decided` | No re-run unless portfolio review |

### Prompt path resolution

```text
prompts/{stage_key with _ replaced by -}-v{N}.md
```

Example: `fit_and_decide: v1` → `prompts/fit-and-decide-v1.md`.

## Automations

| Automation | Prompt | Trigger |
|------------|--------|---------|
| CP — Intake | [automation-intake-v8.md](prompts/automation-intake-v8.md) → intake-v7 | PR opened on `opp/pipeline` |
| CP — Eval | [automation-eval-v10.md](prompts/automation-eval-v10.md) → orchestrator-v8 | Label `cp:eval` **once** (full-run) |
| CP — QA | [automation-qa-v6.md](prompts/automation-qa-v6.md) → opportunity-qa-v5 | Push to PR |
| CP — Review | [automation-review-v3.md](prompts/automation-review-v3.md) → runner-v3 | Cron / `cp:review` |

Branch **`opp/pipeline`**: one active OPP. See [docs/automations.md](docs/automations.md).

## Decision rules

| Decision | Criteria |
|----------|----------|
| BUILD_MICRO | Hard gates PASS + MSFI-lite ≥ 70 + live validation (no desk-only) |
| MONITOR_MICRO | Gates PASS + MSFI 50–69, borderline gate, or capacity_blocked |
| KILL_MICRO | Hard gate FAIL or MSFI < 50 |

## After completing a stage

1. Paste output into matching section; set `confidence_level`.
2. Tag evidence on claims (Discovery, Validation, Fit and Decide).
3. Update frontmatter: `pipeline_stage`, `updated`.
4. On fit_and_decide: sync [portfolio/micro-saas.md](portfolio/micro-saas.md), `status: decided`.

## Files you may modify

- `opportunities/OPP-*.md`
- `portfolio/micro-saas.md`
- `metrics/portfolio.md`
- `reviews/REVIEW-*.md`

Do **not** modify legacy studio portfolio files except via explicit legacy migration.

## Files you must NOT modify without version bump

- `prompts/*-v*.md` (create `v{N+1}` instead)

## Pull request QA

1. Read [prompts/opportunity-qa-v5.md](prompts/opportunity-qa-v5.md).
2. Apply [scripts/msfi_calculator.py](scripts/msfi_calculator.py) for decided solo OPPs.
3. Verdict **pass**, **warn**, or **fail** — do not merge on **fail**.

## Intake

1. [prompts/intake-v7.md](prompts/intake-v7.md).
2. Branch `opp/pipeline`; one active OPP.
3. After Intake Complete: label **`cp:eval` once** → full-run to `decided`.

## Portfolio review

[prompts/portfolio-review-runner-v3.md](prompts/portfolio-review-runner-v3.md) — max 3 MONITOR_MICRO/run; **Next Review +30 days**.

## References

- [playbooks/micro-saas-portfolio.md](playbooks/micro-saas-portfolio.md)
- [playbooks/evaluation-process.md](playbooks/evaluation-process.md)
- [playbooks/build-handoff.md](playbooks/build-handoff.md)
- [docs/roadmap.md](docs/roadmap.md)
- [docs/legacy-studio.md](docs/legacy-studio.md)
- [docs/prod-cutover.md](docs/prod-cutover.md)
