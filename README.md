# AI Startup Studio Brain

Documentation-first control plane for evaluating, documenting, comparing, and managing startup opportunities.

This repository is the brain of an AI Startup Studio. It does **not** build software products. It evaluates ideas, records evidence, scores opportunities, and manages portfolio decisions to maximize return on time, attention, and capital.

## Philosophy

- Documentation first
- Business before code
- Evidence before opinions
- Portfolio management over emotional attachment
- Small experiments, fast validation, fast termination of weak ideas

Read the full philosophy in [`docs/philosophy.md`](docs/philosophy.md).

## Decision Path

```text
Discovery → Validation → Scoring → Distribution Analysis → Unfair Advantage
  → Maintenance Evaluation → Risk Analysis → Portfolio Intelligence
  → Scenario Planning → Portfolio Management
```

BUILD-only preparation (after BUILD decision):

```text
Product Vision → MVP Definition → Roadmap → Architecture → Success Contract
```

Each stage is driven by a versioned prompt in [`prompts/`](prompts/). Outputs are recorded in opportunity documents using [`templates/opportunity-template.md`](templates/opportunity-template.md).

| Stage | Prompt |
|-------|--------|
| Discovery | [prompts/discovery.md](prompts/discovery.md) |
| Validation | [prompts/validation.md](prompts/validation.md) |
| Scoring | [prompts/scoring.md](prompts/scoring.md) |
| Distribution Analysis | [prompts/distribution-analysis.md](prompts/distribution-analysis.md) |
| Unfair Advantage | [prompts/unfair-advantage.md](prompts/unfair-advantage.md) |
| Maintenance Evaluation | [prompts/maintenance-evaluation.md](prompts/maintenance-evaluation.md) |
| Risk Analysis | [prompts/risk-analysis.md](prompts/risk-analysis.md) |
| Portfolio Intelligence | [prompts/portfolio-intelligence.md](prompts/portfolio-intelligence.md) |
| Scenario Planning | [prompts/scenario-planning.md](prompts/scenario-planning.md) |
| Portfolio Management | [prompts/portfolio-manager.md](prompts/portfolio-manager.md) |

## Decision Thresholds

| Decision | Criteria | Portfolio file |
|----------|----------|----------------|
| **BUILD** | `global_score >= 75` AND `OQI >= 70` | [`portfolio/active.md`](portfolio/active.md) |
| **MONITOR** | `global_score` 50–74 | [`portfolio/monitoring.md`](portfolio/monitoring.md) |
| **KILL** | `global_score < 50` | [`portfolio/archived.md`](portfolio/archived.md) |

Micro SaaS wedge decisions (independent lens): [`portfolio/micro-saas.md`](portfolio/micro-saas.md). See [`playbooks/micro-saas-portfolio.md`](playbooks/micro-saas-portfolio.md).

Scoring dimensions, weights, and OQI: [`playbooks/scoring-rules.md`](playbooks/scoring-rules.md), [`playbooks/opportunity-quality-index.md`](playbooks/opportunity-quality-index.md).

## Intelligence Framework

| Analysis | Output | Playbook |
|----------|--------|----------|
| Evidence classification | Typed claims on every assertion | [`playbooks/evidence-classification.md`](playbooks/evidence-classification.md) |
| Multi-dimensional scoring | 10 sub-scores → `global_score` | [`playbooks/scoring-rules.md`](playbooks/scoring-rules.md) |
| Distribution | `distribution_score`, `distribution_notes` | [`playbooks/distribution-analysis.md`](playbooks/distribution-analysis.md) |
| Unfair advantage | `unfair_advantages`, `moat_score` | [`playbooks/unfair-advantage-analysis.md`](playbooks/unfair-advantage-analysis.md) |
| Maintenance | `maintenance_score` (1–10 burden) | [`playbooks/maintenance-evaluation.md`](playbooks/maintenance-evaluation.md) |
| Risk | `risks`, `risk_exposure_score` | [`playbooks/risk-analysis.md`](playbooks/risk-analysis.md) |
| Portfolio intelligence | `portfolio_fit_score` | [`playbooks/portfolio-intelligence.md`](playbooks/portfolio-intelligence.md) |
| Scenario planning | Optimistic / realistic / pessimistic + probabilities | [`playbooks/scenario-planning.md`](playbooks/scenario-planning.md) |
| Opportunity quality | `opportunity_quality_index` (0–100) | [`playbooks/opportunity-quality-index.md`](playbooks/opportunity-quality-index.md) |
| Micro SaaS Portfolio | `msfi` (0–100), wedge hard-gates | [`playbooks/micro-saas-portfolio.md`](playbooks/micro-saas-portfolio.md) |

Every section includes `confidence_level: high | medium | low`.

## Quick Start

1. Copy [`templates/opportunity-template.md`](templates/opportunity-template.md) to [`opportunities/`](opportunities/) with name `OPP-YYYYMMDD-{slug}.md`.
2. Run decision-path prompts in order; paste outputs into the opportunity document.
3. Score using [`playbooks/scoring-rules.md`](playbooks/scoring-rules.md); calculate OQI.
4. Record the decision in **Final Decision** with scenarios and expected learnings.
5. Update the appropriate [`portfolio/`](portfolio/) file.
6. If BUILD, complete BUILD preparation sections.

Full workflow: [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`playbooks/evaluation-process.md`](playbooks/evaluation-process.md).

See [`opportunities/_example-opportunity.md`](opportunities/_example-opportunity.md) for a worked example.

## Repository Structure

| Folder | Description |
|--------|-------------|
| [`prompts/`](prompts/) | Versioned AI prompts for each pipeline stage |
| [`templates/`](templates/) | Copy-paste scaffolds for opportunities, reviews, and decisions |
| [`opportunities/`](opportunities/) | One markdown file per evaluated opportunity |
| [`portfolio/`](portfolio/) | Living registry split by decision outcome |
| [`playbooks/`](playbooks/) | Evaluation flow, scoring, intelligence analyses, portfolio governance |
| [`reviews/`](reviews/) | Quarterly portfolio review artifacts |
| [`docs/`](docs/) | Foundational reference: philosophy, principles, glossary, automations |

## Standards

- Agent operating rules: [`AGENTS.md`](AGENTS.md)
- Markdown conventions and naming: [`CONVENTIONS.md`](CONVENTIONS.md)
- Contribution workflow: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Glossary: [`docs/glossary.md`](docs/glossary.md)
- v1 migration: [`playbooks/migration-v1-to-v2.md`](playbooks/migration-v1-to-v2.md)

## Future Extensibility

| Extension | Purpose |
|-----------|---------|
| `experiments/` | Raw experiment logs per opportunity |
| `metrics/` | Studio KPIs (kill rate, time-to-decision, OQI calibration) |
| Frontmatter `tags` | Portfolio filtering by theme |

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for details.
