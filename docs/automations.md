# Cursor Automations

Operational setup for automating the AI Startup Studio Brain control plane with [Cursor Automations](https://cursor.com/docs).

See [AGENTS.md](../AGENTS.md) for agent operating rules shared by all automations below.

## Prerequisites

Before enabling automations:

1. Push this repository to GitHub or GitLab and connect it in Cursor.
2. Configure `gitConfig` in each automation with the target repo and default branch.
3. Work via pull requests — do not push directly to the default branch (see [AGENTS.md](../AGENTS.md)).

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
| **Repo checkout** | This repository, default branch |

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

## Planned automations (Phase 3)

| Automation | Trigger | Prompt |
|------------|---------|--------|
| Intake idée | Webhook / Slack | `intake-v1` (not yet created) |
| Revue MONITOR | Cron weekly | `portfolio-review-runner-v1` (not yet created) |
| Pipeline +1 | Push on eval branch | `pipeline-orchestrator-v1` |

See the project roadmap in repository commits and [CONTRIBUTING.md](../CONTRIBUTING.md).

## Related

- [Contributing PR checklist](../CONTRIBUTING.md)
- [Prompts index](../prompts/README.md)
- [Conventions](../CONVENTIONS.md)
