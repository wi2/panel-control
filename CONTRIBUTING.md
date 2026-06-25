# Contributing

How to evaluate opportunities and maintain this control plane.

## New Opportunity

1. Copy [`templates/opportunity-template.md`](templates/opportunity-template.md) into [`opportunities/`](opportunities/).
2. Rename using the convention: `OPP-YYYYMMDD-{slug}.md` (see [`CONVENTIONS.md`](CONVENTIONS.md)).
3. Fill in frontmatter: `id`, `title`, `owner`, `created`.
4. Set `status: draft`.

## Run the Decision Path

Execute prompts in order. Paste outputs into the corresponding opportunity sections.

| Step | Prompt | Opportunity section |
|------|--------|---------------------|
| 1 | [Discovery](prompts/discovery.md) | Discovery |
| 2 | [Validation](prompts/validation.md) | Validation |
| 3 | [Scoring](prompts/scoring.md) | Scoring |
| 4 | [Distribution Analysis](prompts/distribution-analysis.md) | Distribution Analysis |
| 5 | [Unfair Advantage](prompts/unfair-advantage.md) | Unfair Advantage Analysis |
| 6 | [Maintenance Evaluation](prompts/maintenance-evaluation.md) | Maintenance Evaluation |
| 7 | [Risk Analysis](prompts/risk-analysis.md) | Risk Analysis |
| 8 | [Portfolio Intelligence](prompts/portfolio-intelligence.md) | Portfolio Intelligence |
| 9 | [Scenario Planning](prompts/scenario-planning.md) | Scenario Planning |
| 10 | [Portfolio Manager](prompts/portfolio-manager.md) | Final Decision |

Set `status: evaluating` when the pipeline starts. Record `prompt_versions` used in frontmatter.

See [`playbooks/evaluation-process.md`](playbooks/evaluation-process.md) for the full workflow.

## BUILD Preparation (BUILD only)

If primary decision is BUILD, complete:

| Step | Prompt | Opportunity section |
|------|--------|---------------------|
| 11 | [Vision](prompts/vision.md) | Product Vision |
| 12 | [MVP](prompts/mvp.md) | MVP Definition |
| 13 | [Roadmap](prompts/roadmap.md) | Roadmap |
| 14 | [Architecture](prompts/architecture.md) | Architecture Proposal |
| 15 | [Success Contract](prompts/success-contract.md) | Success Contract |

## Score, OQI, and Decide

1. Apply [`playbooks/scoring-rules.md`](playbooks/scoring-rules.md) for `global_score`.
2. Calculate OQI per [`playbooks/opportunity-quality-index.md`](playbooks/opportunity-quality-index.md).
3. Map to decision:

| Decision | Criteria |
|----------|----------|
| BUILD | `global_score >= 75` AND `OQI >= 70` |
| MONITOR | `global_score` 50–74 |
| KILL | `global_score < 50` |

4. Record primary decision, OQI breakdown, scenarios, and `expected_learnings` in **Final Decision**.
5. Update frontmatter: `decision`, `global_score`, `opportunity_quality_index`, `status: decided`, `updated`.

For standalone decision records, use [`templates/decision-template.md`](templates/decision-template.md).

Every claim must include evidence type per [`playbooks/evidence-classification.md`](playbooks/evidence-classification.md).

## Update Portfolio

Add or move the opportunity row in the appropriate portfolio file:

- **BUILD** → [`portfolio/active.md`](portfolio/active.md)
- **MONITOR** → [`portfolio/monitoring.md`](portfolio/monitoring.md)
- **KILL** → [`portfolio/archived.md`](portfolio/archived.md)

Follow [`playbooks/portfolio-rules.md`](playbooks/portfolio-rules.md).

## Prompt Changes

1. Do not edit an active prompt version in place after it has been used in an evaluation.
2. Create `{stage}-v{N+1}.md` with updated content.
3. Mark the old version `status: deprecated` and set `superseded_by`.
4. Update the index file (`{stage}.md`) to point to the new version.
5. Add a changelog entry in the index file.

See [`prompts/README.md`](prompts/README.md) for versioning details.

## Portfolio Reviews

Run quarterly reviews using [`templates/portfolio-review-template.md`](templates/portfolio-review-template.md). Save artifacts in [`reviews/`](reviews/) as `REVIEW-{YYYY}-Q{N}.md` (see [reviews/README.md](reviews/README.md)).

Review all entries in [`portfolio/active.md`](portfolio/active.md) and [`portfolio/monitoring.md`](portfolio/monitoring.md). Aggregate `expected_learnings` from archived opportunities. Apply kill rules from [`playbooks/kill-rules.md`](playbooks/kill-rules.md) where triggers are met.

Scheduled reviews: use [prompts/portfolio-review-runner.md](prompts/portfolio-review-runner.md) or the Cursor Automation in [docs/automations.md](docs/automations.md).

## Pull Request Checklist

When submitting changes via git:

- [ ] Opportunity ID is unique
- [ ] global_score and OQI match decision thresholds
- [ ] Evidence types on all scoring claims
- [ ] confidence_level on all decision-path sections
- [ ] expected_learnings recorded for MONITOR and KILL
- [ ] Portfolio file updated (if decision changed)
- [ ] `prompt_versions` recorded in opportunity frontmatter
- [ ] Prompt version bumps follow conventions (no in-place edits to used versions)
- [ ] Internal links use relative paths

Automated review: run [prompts/opportunity-qa.md](prompts/opportunity-qa.md) on the PR diff, or enable the Cursor Automation described in [docs/automations.md](docs/automations.md).

## Future Extensibility

Recommended extensions (not yet implemented):

| Extension | Purpose |
|-----------|---------|
| `experiments/` per opportunity | Raw experiment logs linked from Validation |
| `metrics/` | Aggregated studio KPIs (kill rate, time-to-decision, OQI calibration) |
| Frontmatter `tags` | Portfolio filtering by theme (e.g. `fintech`, `b2b`) |

Scoring calculators and application code are explicitly out of scope for this repository.
