# Prompts

Versioned AI prompts for each stage of the evaluation pipeline.

## Current Versions

| Stage | Index | Active Version |
|-------|-------|----------------|
| Discovery | [discovery.md](discovery.md) | v1 |
| Validation | [validation.md](validation.md) | v1 |
| Scoring | [scoring.md](scoring.md) | v2 |
| Distribution Analysis | [distribution-analysis.md](distribution-analysis.md) | v1 |
| Unfair Advantage | [unfair-advantage.md](unfair-advantage.md) | v1 |
| Maintenance Evaluation | [maintenance-evaluation.md](maintenance-evaluation.md) | v1 |
| Risk Analysis | [risk-analysis.md](risk-analysis.md) | v1 |
| Portfolio Intelligence | [portfolio-intelligence.md](portfolio-intelligence.md) | v1 |
| Scenario Planning | [scenario-planning.md](scenario-planning.md) | v1 |
| Portfolio Manager | [portfolio-manager.md](portfolio-manager.md) | v2 |
| Product Vision | [vision.md](vision.md) | v1 |
| MVP Definition | [mvp.md](mvp.md) | v1 |
| Roadmap | [roadmap.md](roadmap.md) | v1 |
| Architecture | [architecture.md](architecture.md) | v1 |
| Success Contract | [success-contract.md](success-contract.md) | v1 |

### Orchestration (automation / agent)

| Stage | Index | Active Version |
|-------|-------|----------------|
| Pipeline Orchestrator | [pipeline-orchestrator.md](pipeline-orchestrator.md) | v2 |
| Score Calculator | [score-calculator.md](score-calculator.md) | v1 |
| Opportunity QA | [opportunity-qa.md](opportunity-qa.md) | v1 |
| Intake | [intake.md](intake.md) | v4 |
| Portfolio Review Runner | [portfolio-review-runner.md](portfolio-review-runner.md) | v1 |

### Automation wrappers (Cursor Automations)

Thin preconditions + delegation to orchestration prompts above. See [docs/automations.md](../docs/automations.md).

| Automation | Index | Active Version |
|------------|-------|----------------|
| CP — QA | [automation-qa.md](automation-qa.md) | v1 |
| CP — Intake | [automation-intake.md](automation-intake.md) | v4 |
| CP — Eval | [automation-eval.md](automation-eval.md) | v4 |
| CP — Review | [automation-review.md](automation-review.md) | v1 |

See [AGENTS.md](../AGENTS.md) for agent operating rules.

## Versioning

- **Canonical content** lives in `{stage}-v{N}.md`.
- **Index file** `{stage}.md` points to the current version and lists changelog.
- Integer versions only: `v1`, `v2`, `v3`, …
- Never delete deprecated prompts; mark `status: deprecated` and set `superseded_by`.

### When to Bump Version

| Change type | Action |
|-------------|--------|
| Typo or clarity fix (no output change) | Edit in place if unused; otherwise bump |
| New questions or criteria | Create v{N+1} |
| Changed output format | Create v{N+1} |
| Changed scoring weights referenced | Create v{N+1} |

### Prompt Frontmatter

```yaml
---
version: 1
stage: discovery
status: active
created: 2026-06-25
supersedes: null
changelog: "Initial release"
---
```

## Usage

1. Open the index file for the stage (e.g. `discovery.md`).
2. Follow the link to the active version (e.g. `discovery-v1.md`).
3. Provide the prompt to your AI assistant with the required inputs.
4. Paste the output into the matching section of the opportunity document.
5. Record the version used in opportunity frontmatter (`prompt_versions`).

## Pipeline Order

### Decision path (all opportunities)

```text
discovery → validation → scoring → distribution-analysis → unfair-advantage
  → maintenance-evaluation → risk-analysis → portfolio-intelligence
  → scenario-planning → portfolio-manager
```

### BUILD preparation (BUILD only)

```text
vision → mvp → roadmap → architecture → success-contract
```

See [evaluation process](../playbooks/evaluation-process.md).

## Related

- [Conventions](../CONVENTIONS.md)
- [Contributing](../CONTRIBUTING.md)
- [Migration v1 to v2](../playbooks/migration-v1-to-v2.md)
