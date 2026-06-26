# Agent Instructions — AI Startup Studio Brain

You operate inside a documentation-first control plane. You do **not** build product code here.

## Before any action

1. Read the target opportunity frontmatter (`status`, `decision`, `prompt_versions`, `pipeline_stage`).
2. Read [playbooks/evaluation-process.md](playbooks/evaluation-process.md) for stage order and gates.
3. Read [CONVENTIONS.md](CONVENTIONS.md) for naming and evidence rules.

## Pipeline stages (decision path)

Run in order; never skip a stage gate:

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

| status | Action |
|--------|--------|
| `draft` | Run discovery; set `status: evaluating` |
| `evaluating` | Find first empty or gate-failing section; run matching prompt from `prompts/{stage}-v{N}.md` |
| `decided` + `build` | Run first incomplete BUILD section |
| `decided` + `monitor` / `kill` | Do not re-run pipeline unless review trigger or explicit user request |

Use `prompt_versions` in frontmatter — never silently switch prompt versions.

For automated pipeline advancement, use Cursor Automation **CP — Eval** (push on `opp/**`, batches of up to 5 stages — [docs/automations.md](docs/automations.md)) or [prompts/pipeline-orchestrator.md](prompts/pipeline-orchestrator.md) manually.

## Decision rules (strict)

| Decision | Criteria |
|----------|----------|
| BUILD | `global_score >= 75` AND `OQI >= 70` AND capacity available |
| MONITOR | `global_score` 50–74, OR score qualifies but OQI < 70 |
| KILL | `global_score < 50` OR kill trigger from [playbooks/kill-rules.md](playbooks/kill-rules.md) |

**Override**: only if frontmatter has `decision_override: true` AND Final Decision documents rationale. Without override, never place `global_score < 50` in [portfolio/monitoring.md](portfolio/monitoring.md).

## Scoring and OQI

Before writing `global_score` or `opportunity_quality_index` to frontmatter, apply [prompts/score-calculator.md](prompts/score-calculator.md) logic.

## After completing a stage

1. Paste output into the matching opportunity section.
2. Set section `confidence_level`.
3. Tag evidence on every scoring claim.
4. Update frontmatter: `pipeline_stage`, `updated`.
5. On `portfolio_manager` completion: update decision fields, sync `portfolio/*.md`, set `status: decided`.

## Files you may modify

- `opportunities/OPP-*.md`
- `portfolio/active.md`, `monitoring.md`, `archived.md`, `micro-saas.md`
- `reviews/REVIEW-*.md` (when running portfolio review)

## Files you must NOT modify without version bump

- `prompts/*-v*.md` (create `v{N+1}` instead)
- `playbooks/` (propose changes via separate PR with rationale)

## References (load for scoring and decisions)

- [playbooks/scoring-rules.md](playbooks/scoring-rules.md)
- [playbooks/scoring-weights.md](playbooks/scoring-weights.md)
- [playbooks/opportunity-quality-index.md](playbooks/opportunity-quality-index.md)
- [playbooks/evidence-classification.md](playbooks/evidence-classification.md)
- [playbooks/kill-rules.md](playbooks/kill-rules.md)
- [playbooks/portfolio-rules.md](playbooks/portfolio-rules.md)

## Pull request QA

When a pull request modifies `opportunities/` or `portfolio/`:

1. Read [prompts/opportunity-qa.md](prompts/opportunity-qa.md) and execute the active version.
2. Apply [prompts/score-calculator.md](prompts/score-calculator.md) logic for score and decision checks.
3. Post a structured PR comment with verdict **pass**, **warn**, or **fail**.
4. Do **not** merge when verdict is **fail**.

Automated setup: [docs/automations.md](docs/automations.md) (**CP — QA**).

## Intake

When a new startup idea enters the studio (PR + label, chat, or manual request):

1. Read [prompts/intake.md](prompts/intake.md) and execute the active version (or **CP — Intake** via [docs/automations.md](docs/automations.md)).
2. Create `opportunities/OPP-YYYYMMDD-{slug}.md` and fill Discovery only.
3. Open a pull request on branch `opp/{slug}` — add label `cp:intake` once for automation. **CP — Eval** runs automatically on subsequent pushes (no eval label). Do not push directly to the default branch.

## Portfolio review

When portfolio entries are due (`Next Review <= today`) or on scheduled cron:

1. Read [prompts/portfolio-review-runner.md](prompts/portfolio-review-runner.md) and execute the active version (or **CP — Review** via [docs/automations.md](docs/automations.md)).
2. Process at most **3 MONITOR opportunities** per run; queue the rest.
3. Update portfolio files and optionally create `reviews/REVIEW-{YYYY}-Q{N}.md`.

Automated setup: four Cursor Automations in [docs/automations.md](docs/automations.md) — **CP — QA**, **CP — Intake**, **CP — Eval**, **CP — Review**.
