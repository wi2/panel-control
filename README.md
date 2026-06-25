# AI Startup Studio Brain

Documentation-first control plane for evaluating, documenting, comparing, and managing startup opportunities.

This repository is the brain of an AI Startup Studio. It does **not** build software products. It evaluates ideas, records evidence, scores opportunities, and manages portfolio decisions.

## Philosophy

- Documentation first
- Business before code
- Evidence before opinions
- Portfolio management over emotional attachment
- Small experiments, fast validation, fast termination of weak ideas

Read the full philosophy in [`docs/philosophy.md`](docs/philosophy.md).

## Evaluation Pipeline

```text
Discovery → Validation → Scoring → Product Vision → MVP Definition
    → Roadmap → Architecture → Success Contract → Portfolio Management
```

Each stage is driven by a versioned prompt in [`prompts/`](prompts/). Outputs are recorded in opportunity documents using [`templates/opportunity-template.md`](templates/opportunity-template.md).

| Stage | Prompt |
|-------|--------|
| Discovery | [prompts/discovery.md](prompts/discovery.md) |
| Validation | [prompts/validation.md](prompts/validation.md) |
| Scoring | [prompts/scoring.md](prompts/scoring.md) |
| Product Vision | [prompts/vision.md](prompts/vision.md) |
| MVP Definition | [prompts/mvp.md](prompts/mvp.md) |
| Roadmap | [prompts/roadmap.md](prompts/roadmap.md) |
| Architecture | [prompts/architecture.md](prompts/architecture.md) |
| Success Contract | [prompts/success-contract.md](prompts/success-contract.md) |
| Portfolio Management | [prompts/portfolio-manager.md](prompts/portfolio-manager.md) |

## Decision Thresholds

| Decision | Score | Portfolio file |
|----------|-------|----------------|
| **BUILD** | >= 70 | [`portfolio/active.md`](portfolio/active.md) |
| **MONITOR** | 40–69 | [`portfolio/monitoring.md`](portfolio/monitoring.md) |
| **KILL** | < 40 | [`portfolio/archived.md`](portfolio/archived.md) |

Scoring dimensions and rubrics: [`playbooks/scoring-rules.md`](playbooks/scoring-rules.md).

## Quick Start

1. Copy [`templates/opportunity-template.md`](templates/opportunity-template.md) to [`opportunities/`](opportunities/) with name `OPP-YYYYMMDD-{slug}.md`.
2. Run prompts in pipeline order; paste outputs into the opportunity document.
3. Score using [`playbooks/scoring-rules.md`](playbooks/scoring-rules.md).
4. Record the decision in **Final Decision**.
5. Update the appropriate [`portfolio/`](portfolio/) file.

Full workflow: [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`playbooks/evaluation-process.md`](playbooks/evaluation-process.md).

See [`opportunities/_example-opportunity.md`](opportunities/_example-opportunity.md) for a worked example.

## Repository Structure

| Folder | Description |
|--------|-------------|
| [`prompts/`](prompts/) | Versioned AI prompts for each pipeline stage; unversioned files are indexes to the current version |
| [`templates/`](templates/) | Copy-paste scaffolds for opportunities, reviews, and decisions |
| [`opportunities/`](opportunities/) | One markdown file per evaluated opportunity (evidence + decisions) |
| [`portfolio/`](portfolio/) | Living registry split by decision outcome (active / monitoring / archived) |
| [`playbooks/`](playbooks/) | Evaluation flow, scoring rules, kill criteria, portfolio governance |
| [`docs/`](docs/) | Foundational reference: philosophy, principles, glossary |

## Standards

- Markdown conventions and naming: [`CONVENTIONS.md`](CONVENTIONS.md)
- Contribution workflow: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Glossary: [`docs/glossary.md`](docs/glossary.md)

## Future Extensibility

| Extension | Purpose |
|-----------|---------|
| `reviews/` | Quarterly portfolio review artifacts |
| `experiments/` | Raw experiment logs per opportunity |
| `metrics/` | Studio KPIs (kill rate, time-to-decision) |
| Markdown lint CI | Automated markdown quality checks |
| MCP / agent integration | Wire prompts to Cursor automations |
| Frontmatter `tags` | Portfolio filtering by theme |

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for details.
