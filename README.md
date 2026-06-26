# AI Startup Studio Brain

Documentation-first control plane for evaluating and managing **solo micro-SaaS** opportunities.

**Eval engine v3-lite** — see [ADR](docs/decisions/2026-06-simplification-v3-lite.md). Studio venture path frozen: [legacy-studio.md](docs/legacy-studio.md).

## Philosophy

- Documentation first
- Business before code
- Evidence before opinions
- Portfolio management over emotional attachment
- Small experiments, fast validation, fast termination of weak ideas

Read [docs/philosophy.md](docs/philosophy.md).

## Decision Path (v3-lite)

```text
Discovery → Validation → Fit and Decide → portfolio/micro-saas.md
```

Automation: Intake (PR open) → **1×** `cp:eval` (full-run) → merge. [docs/automations.md](docs/automations.md).

| Stage | Prompt |
|-------|--------|
| Discovery | [prompts/discovery.md](prompts/discovery.md) |
| Validation | [prompts/validation.md](prompts/validation.md) |
| Fit and Decide | [prompts/fit-and-decide.md](prompts/fit-and-decide.md) |

## Decision Thresholds

| Decision | Criteria | Registry |
|----------|----------|----------|
| **BUILD_MICRO** | Hard gates PASS + MSFI-lite ≥ 70 + live validation | [portfolio/micro-saas.md](portfolio/micro-saas.md) Active |
| **MONITOR_MICRO** | Gates PASS + MSFI 50–69 or capacity_blocked | Monitoring |
| **KILL_MICRO** | Gate FAIL or MSFI < 50 | Archived |

Hard gates and MSFI-lite: [playbooks/micro-saas-portfolio.md](playbooks/micro-saas-portfolio.md). CI: [scripts/msfi_calculator.py](scripts/msfi_calculator.py).

## Quick Start

1. Copy [templates/opportunity-template.md](templates/opportunity-template.md) → `opportunities/OPP-YYYYMMDD-{slug}.md`.
2. Run prompts in order (or use `opp/pipeline` automations).
3. Update [portfolio/micro-saas.md](portfolio/micro-saas.md).
4. Refresh [metrics/portfolio.md](metrics/portfolio.md).

Example: [opportunities/_example-opportunity.md](opportunities/_example-opportunity.md).

## Repository Structure

| Folder | Description |
|--------|-------------|
| [prompts/](prompts/) | Versioned AI prompts |
| [opportunities/](opportunities/) | One markdown file per opportunity |
| [portfolio/micro-saas.md](portfolio/micro-saas.md) | Canonical registry |
| [playbooks/](playbooks/) | Evaluation and portfolio rules |
| [metrics/](metrics/) | Lightweight KPIs |
| [docs/decisions/](docs/decisions/) | Architecture decision records |

## Standards

- [AGENTS.md](AGENTS.md)
- [CONVENTIONS.md](CONVENTIONS.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)

Production bootstrap: [docs/prod-cutover.md](docs/prod-cutover.md).
