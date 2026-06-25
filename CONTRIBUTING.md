# Contributing

How to evaluate opportunities and maintain this control plane.

## New Opportunity

1. Copy [`templates/opportunity-template.md`](templates/opportunity-template.md) into [`opportunities/`](opportunities/).
2. Rename using the convention: `OPP-YYYYMMDD-{slug}.md` (see [`CONVENTIONS.md`](CONVENTIONS.md)).
3. Fill in frontmatter: `id`, `title`, `owner`, `created`.
4. Set `status: draft`.

## Run the Pipeline

Execute prompts in order. Paste outputs into the corresponding opportunity sections.

| Step | Prompt | Opportunity section |
|------|--------|---------------------|
| 1 | [Discovery](prompts/discovery.md) | Discovery |
| 2 | [Validation](prompts/validation.md) | Validation |
| 3 | [Scoring](prompts/scoring.md) | Scoring |
| 4 | [Vision](prompts/vision.md) | Product Vision |
| 5 | [MVP](prompts/mvp.md) | MVP Definition |
| 6 | [Roadmap](prompts/roadmap.md) | Roadmap |
| 7 | [Architecture](prompts/architecture.md) | Architecture Proposal |
| 8 | [Success Contract](prompts/success-contract.md) | Success Contract |
| 9 | [Portfolio Manager](prompts/portfolio-manager.md) | Final Decision |

Set `status: evaluating` when the pipeline starts. Record `prompt_versions` used in frontmatter.

See [`playbooks/evaluation-process.md`](playbooks/evaluation-process.md) for the full workflow.

## Score and Decide

1. Apply [`playbooks/scoring-rules.md`](playbooks/scoring-rules.md).
2. Map score to decision:

| Decision | Score |
|----------|-------|
| BUILD | >= 70 |
| MONITOR | 40–69 |
| KILL | < 40 |

3. Record the decision in the **Final Decision** section.
4. Update frontmatter: `decision`, `score`, `status: decided`, `updated`.

For standalone decision records, use [`templates/decision-template.md`](templates/decision-template.md).

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

Run quarterly reviews using [`templates/portfolio-review-template.md`](templates/portfolio-review-template.md).

Review all entries in [`portfolio/active.md`](portfolio/active.md) and [`portfolio/monitoring.md`](portfolio/monitoring.md). Apply kill rules from [`playbooks/kill-rules.md`](playbooks/kill-rules.md) where triggers are met.

## Pull Request Checklist

When submitting changes via git:

- [ ] Opportunity ID is unique
- [ ] Score matches decision threshold
- [ ] Portfolio file updated (if decision changed)
- [ ] `prompt_versions` recorded in opportunity frontmatter
- [ ] Evidence cited for scoring claims
- [ ] Prompt version bumps follow conventions (no in-place edits to used versions)
- [ ] Internal links use relative paths

## Future Extensibility

Recommended extensions (not yet implemented):

| Extension | Purpose |
|-----------|---------|
| `reviews/` folder | Quarterly portfolio review artifacts |
| `experiments/` per opportunity | Raw experiment logs linked from Validation |
| `metrics/` | Aggregated studio KPIs (kill rate, time-to-decision) |
| Markdown lint CI | `markdownlint-cli2` on pull requests |
| `prompts/CHANGELOG.md` | Track output-shaping prompt changes |
| MCP / agent integration | Wire prompts to Cursor automations |
| Frontmatter `tags` | Portfolio filtering by theme (e.g. `fintech`, `b2b`) |

Scoring calculators and application code are explicitly out of scope for this repository.
