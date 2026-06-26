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
| MONITOR | `global_score` 50–74, OR score qualifies for BUILD but OQI < 70 |
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

Review all entries in [`portfolio/micro-saas.md`](portfolio/micro-saas.md) (canonical for `solo_micro_saas`) or legacy [`portfolio/active.md`](portfolio/active.md) and [`portfolio/monitoring.md`](portfolio/monitoring.md) for `startup_studio`. Aggregate `expected_learnings` from archived opportunities. Apply kill rules from [`playbooks/kill-rules.md`](playbooks/kill-rules.md) where triggers are met.

Scheduled reviews: use [prompts/portfolio-review-runner-v2.md](prompts/portfolio-review-runner-v2.md) via Cursor Automation **CP — Review** ([prompts/automation-review-v2.md](prompts/automation-review-v2.md); see [docs/automations.md](docs/automations.md)).

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
- [ ] `python scripts/validate_opportunities.py` passes locally (CI runs on PR)

Automated review: **CP — QA** runs [prompts/automation-qa-v5.md](prompts/automation-qa-v5.md) on **push to PR** only (see [docs/automations.md](docs/automations.md)). Do not merge when verdict is **fail** on a `status: decided` opportunity.

## GitHub labels and branch conventions

Used by Cursor Automations (see [docs/automations.md](docs/automations.md)):

| Label | Branch | Action |
|-------|--------|--------|
| `cp:intake` | **`opp/pipeline`** (exact) | Create OPP + Discovery from PR `## Intake` body (once) |
| `cp:eval` | **`opp/pipeline`** (exact) | Staged pipeline eval — **one stage per label**; re-add until `decided` (solo: ~3× after Intake) |
| `cp:review` | `review/**` | Run portfolio review on demand |

**Studio rule**: one **active** opportunity (`draft` / `evaluating`) on `opp/pipeline` at a time. Catalogue of `decided` OPP files inherited from `master` is normal. Recreate the branch from `master` after each merge.

Workflow: `cp:intake` → Intake Complete → `cp:eval` (staged, re-add until `decided`) → merge when QA pass/warn on **decided** push. Do not add both labels at once.

QA (`CP — QA`) runs automatically on PRs touching `opportunities/` or `portfolio/` — no label required. The first QA run on PR open may be a NOOP or incomplete; **use the latest QA comment after the Eval push** as the merge gate.

### Pipeline workflows: local vs automation

Same prompts and sections — different **who runs them** and **when labels apply**.

#### When to use which

| Goal | Use |
|------|-----|
| Fast iteration, full control, debug prompts | **Local / Cursor Agent** |
| Hands-off ops, test Background Agents end-to-end | **GitHub labels** (`cp:intake` → `cp:eval`) |
| Merge gate | **CP — QA** on every push (both flows) |

Default strategy for new opportunities: **`solo_micro_saas`** (4 stages after intake). See [evaluation-process.md](playbooks/evaluation-process.md).

#### Flow A — Local / Agent (no labels required)

Use when you execute prompts in Cursor chat or IDE Agent and commit yourself.

```text
1. git checkout master && git pull
2. git checkout -b opp/pipeline master
3. (Optional) Open PR early with ## Intake body for traceability — no pipeline commits yet
4. In Cursor: run prompts in order (solo_micro_saas fast path):
   intake-v6 / discovery-v1 → validation-v1 → micro-saas-evaluation-v2 → portfolio-manager-micro-v1
5. Fill opportunity sections; sync portfolio/micro-saas.md; update frontmatter → status: decided
6. python3 scripts/validate_opportunities.py
7. git commit && git push origin opp/pipeline
8. Merge when latest CP — QA = pass or warn
9. git push origin --delete opp/pipeline  # after merge; recreate for next idea
```

- Do **not** add `cp:intake` / `cp:eval` if the pipeline is already complete — both NOOP.
- Labels are optional in this flow; QA still runs on push.

#### Flow B — GitHub automation (labels required)

Use when Background Agents must create and evaluate the OPP from the PR alone.

```text
1. git checkout master && git pull
2. git push origin --delete opp/pipeline   # if branch exists from prior run
3. git checkout -b opp/pipeline master
4. git commit --allow-empty -m "chore: open pipeline PR for automation run"
5. git push -u origin opp/pipeline
6. Open PR opp/pipeline → master with ## Intake body (Title + Description) → **CP — Intake runs on PR opened**
7. Optional: label `cp:intake` if PR-open Intake did not run
8. Wait for Intake Complete (`intake_complete: true`)
9. Add label `cp:eval` — run **validation**; re-add after each **Pipeline Run Summary** until `Remaining stages: none` and `status: decided` (solo: typically 3×)
10. Merge when latest CP — QA = pass or warn on **decided** push (not on mid-pipeline warn)
11. Remove `cp:eval` label after success; delete opp/pipeline after merge
```

**GitHub PR requirement:** base and head must differ by at least one commit — use the **empty commit** in step 4 (touches no `opportunities/` or `portfolio/` files).

**Critical:** no manual commits to `opportunities/` or `portfolio/` on the branch **before** Intake runs. Pre-filled pipeline commits make `cp:intake` / `cp:eval` NOOP.

#### CP — QA timing (both flows)

| Event | QA behaviour |
|-------|----------------|
| PR opened (empty commit only) | **No QA** (push does not touch opportunities/portfolio) |
| Push after Intake | Validates Discovery + intake markers (warn OK) |
| Push after each staged Eval stage | QA **warn** expected while `status: evaluating` |
| Push after final Eval (`decided`) | **Authoritative merge gate** |

Do not merge on **fail**. **warn** is acceptable for MONITOR_MICRO desk-only runs.

#### Cron (online only)

**CP — Review** runs on cron `0 9 * * 1` (Mondays 09:00) in Cursor cloud — not local. On-demand: label `cp:review` on a PR whose head branch matches `review/**`.

### Intake PR template

```markdown
## Intake

**Title:** Short opportunity title
**Owner:** studio-team
**Tags:** b2b, saas

### Description

1–3 paragraphs describing the problem and proposed angle.
```

## Future Extensibility

Recommended extensions (not yet implemented):

| Extension | Purpose |
|-----------|---------|
| `experiments/` per opportunity | Raw experiment logs linked from Validation |
| `metrics/` | Aggregated studio KPIs (kill rate, time-to-decision, OQI calibration) |
| Frontmatter `tags` | Portfolio filtering by theme (e.g. `fintech`, `b2b`) |

Scoring calculators and application code are explicitly out of scope for this repository.
