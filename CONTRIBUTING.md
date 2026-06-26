# Contributing (v3-lite)

Evaluate opportunities on the **solo micro-SaaS** path. ADR: [docs/decisions/2026-06-simplification-v3-lite.md](docs/decisions/2026-06-simplification-v3-lite.md).

## New Opportunity

1. Copy [templates/opportunity-template.md](templates/opportunity-template.md) → `opportunities/OPP-YYYYMMDD-{slug}.md`.
2. Set `eval_engine: v3-lite`, `portfolio_strategy: solo_micro_saas`, `status: draft`.

## Decision Path

| Step | Prompt | Section |
|------|--------|---------|
| 1 | [Discovery](prompts/discovery.md) | Discovery |
| 2 | [Validation](prompts/validation.md) | Validation |
| 3 | [Fit and Decide](prompts/fit-and-decide.md) | Fit and Decide + Final Decision (Micro SaaS) |

Set `status: evaluating` when pipeline starts. Record `prompt_versions`.

## Automations (`opp/pipeline`)

```text
PR + ## Intake → CP — Intake → cp:eval (once) → decided → merge → delete branch
```

See [docs/automations.md](docs/automations.md).

## MSFI-lite and CI

```bash
python3 scripts/msfi_calculator.py --speed 65 --economics 55 --reach 52
python3 scripts/validate_opportunities.py
python3 scripts/update_portfolio_metrics.py   # optional after merge
```

## Update Portfolio

Sync [portfolio/micro-saas.md](portfolio/micro-saas.md). Refresh [metrics/portfolio.md](metrics/portfolio.md).

## PR Checklist

- [ ] `eval_engine: v3-lite`
- [ ] MSFI-lite scores match [scripts/msfi_calculator.py](scripts/msfi_calculator.py)
- [ ] `confidence_level` on Discovery, Validation, Fit and Decide, Final Decision
- [ ] Portfolio row in micro-saas.md when `decided`
- [ ] `validate_opportunities.py` passes
- [ ] CP — QA pass or warn on decided push

## Prompt Changes

Create `{stage}-v{N+1}.md`; deprecate old version; update index. See [prompts/README.md](prompts/README.md).

## Legacy

Studio path frozen: [docs/legacy-studio.md](docs/legacy-studio.md).
