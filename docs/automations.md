# Cursor Automations

Operational setup for automating the AI Startup Studio Brain control plane with [Cursor Automations](https://cursor.com/docs).

See [AGENTS.md](../AGENTS.md) for agent operating rules shared by all automations below.

## Prerequisites

Before enabling automations:

1. Push this repository to GitHub or GitLab and connect it in Cursor.
2. Configure `gitConfig` in each automation with the target repo (`wi2/panel-control`) and branch (`master`).
3. Work via pull requests — do not push directly to the default branch (see [AGENTS.md](../AGENTS.md)).

**Remote**: `git@github.com:wi2/panel-control.git`

---

## Control Plane — PR QA

Validates pull requests that touch opportunity or portfolio files.

| Setting | Value |
|---------|-------|
| **Name** | Control Plane — PR QA |
| **Description** | Run control-plane QA checklist on PRs changing opportunities or portfolio entries |
| **Trigger** | Git — pull request opened |
| **Path scope** | Changes under `opportunities/` or `portfolio/` |
| **Tools** | Comment on PRs |
| **Repo checkout** | `wi2/panel-control`, branch `master` |

### Agent instructions

```text
You are reviewing a pull request for the AI Startup Studio Brain control plane.

1. Read AGENTS.md.
2. If the PR does not modify opportunities/ or portfolio/, stop with NOOP.
3. Execute prompts/opportunity-qa-v1.md against all changed files in those paths.
4. Apply score-calculator-v1 logic for every changed opportunity with a Scoring section.
5. Post the structured QA comment from opportunity-qa-v1 (verdict: pass, warn, or fail).
6. Do not modify files. Do not approve merge when verdict is fail.
```

### Expected output

A PR comment titled **Control Plane QA — pass | warn | fail** with check-group table, score audit summary, blocking issues, warnings, and suggested fixes.

### Related prompts

- [prompts/opportunity-qa.md](../prompts/opportunity-qa.md)
- [prompts/score-calculator.md](../prompts/score-calculator.md)

---

## Control Plane — Intake

Creates a new opportunity file and runs Discovery from a raw idea.

| Setting | Value |
|---------|-------|
| **Name** | Control Plane — Intake |
| **Description** | Convert incoming startup idea into OPP file with Discovery complete |
| **Trigger** | Webhook (copy URL and auth after saving in Automations editor) |
| **Tools** | None (agent commits via PR) |
| **Repo checkout** | `wi2/panel-control`, branch `master` |

### Webhook payload (suggested JSON)

```json
{
  "title": "Short opportunity title",
  "description": "1–3 paragraphs describing the problem and proposed angle.",
  "owner": "studio-team",
  "tags": ["b2b", "saas"]
}
```

### Agent instructions

```text
You are running intake for the AI Startup Studio Brain control plane.

1. Read AGENTS.md.
2. Parse title, description, owner, and tags from the webhook payload (or chat message).
3. Execute prompts/intake-v1.md: create opportunities/OPP-YYYYMMDD-slug.md from template, run Discovery, set status evaluating.
4. Do not run validation, scoring, or portfolio decisions.
5. Create branch intake/OPP-... and open a pull request with the Intake Complete summary.
6. Do not push directly to the default branch.
```

### Expected output

New file under `opportunities/`, Discovery section filled, PR opened for review.

### Related prompts

- [prompts/intake.md](../prompts/intake.md)
- [prompts/discovery.md](../prompts/discovery.md)

---

## Control Plane — MONITOR Review

Weekly scheduled review of due MONITOR (and BUILD) portfolio entries.

| Setting | Value |
|---------|-------|
| **Name** | Control Plane — MONITOR Review |
| **Description** | Re-evaluate overdue monitoring entries and sync portfolio |
| **Trigger** | Cron — `0 9 * * 1` (every Monday at 09:00) |
| **Tools** | None initially; open PR if files change |
| **Repo checkout** | `wi2/panel-control`, branch `master` |

### Agent instructions

```text
You are running a scheduled portfolio review for the AI Startup Studio Brain control plane.

1. Read AGENTS.md.
2. Execute prompts/portfolio-review-runner-v1.md using today's date.
3. Process due entries from portfolio/monitoring.md and portfolio/active.md (Next Review <= today).
4. Process at most 3 MONITOR opportunities per run; queue the remainder.
5. Re-run validation, scoring, and portfolio_manager for each processed MONITOR entry.
6. Apply kill-rules and score-calculator logic before updating frontmatter.
7. Sync portfolio files if decisions change.
8. Create or update reviews/REVIEW-YYYY-QN.md when quarter start or material actions occurred.
9. If no entries due, output NOOP and stop.
10. Open a pull request for any file changes. Do not push directly to the default branch.
```

### Expected output

**Portfolio Review Run** summary; optional `reviews/REVIEW-*.md`; PR with opportunity and portfolio updates.

### Related prompts

- [prompts/portfolio-review-runner.md](../prompts/portfolio-review-runner.md)
- [prompts/pipeline-orchestrator.md](../prompts/pipeline-orchestrator.md)
- [reviews/README.md](../reviews/README.md)

---

## Optional — Pipeline +1 (manual)

Advance one opportunity by a single pipeline stage without a dedicated automation:

1. Create branch `eval/OPP-YYYYMMDD-slug`.
2. Run [prompts/pipeline-orchestrator.md](../prompts/pipeline-orchestrator.md) against the target opportunity.
3. Open PR; merge after [opportunity-qa](prompts/opportunity-qa.md) passes.

Can be wired later to a Git push trigger on `eval/**` branches if needed.

---

## Related

- [Contributing PR checklist](../CONTRIBUTING.md)
- [Prompts index](../prompts/README.md)
- [Conventions](../CONVENTIONS.md)
