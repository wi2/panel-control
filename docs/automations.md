# Cursor Automations

Operational setup for the AI Startup Studio Brain control plane with [Cursor Automations](https://cursor.com/docs).

See [AGENTS.md](../AGENTS.md) for agent operating rules shared by all automations below.

## Architecture

Four small automations — one job each, thin wrapper → versioned prompt:

```text
CP — QA      (read-only)  → prompts/automation-qa-v1.md      → opportunity-qa-v1
CP — Intake  (write)      → prompts/automation-intake-v1.md  → intake-v1
CP — Eval    (write)      → prompts/automation-eval-v1.md    → pipeline-orchestrator-v1
CP — Review  (write)      → prompts/automation-review-v1.md  → portfolio-review-runner-v1
```

Replace the legacy single-purpose automations (**Control Plane — PR QA**, **Intake**, **MONITOR Review**) with these four. Disable legacy automations after enabling the new set to avoid duplicate runs.

## Prerequisites

Before enabling automations:

1. Push this repository to GitHub and connect it in Cursor.
2. Configure `gitConfig` in each automation: repo `wi2/panel-control`, branch `master`.
3. Create GitHub labels (see [GitHub labels](#github-labels)).
4. Work via pull requests — do not push directly to the default branch (see [AGENTS.md](../AGENTS.md)).
5. Enable **ignore draft PRs** on Git triggers where available.

**Remote**: `git@github.com:wi2/panel-control.git`

---

## GitHub labels

Create these labels in the GitHub repository settings:

| Label | Color (suggested) | Automation | Purpose |
|-------|-------------------|------------|---------|
| `cp:intake` | `#0E8A16` | CP — Intake | Create OPP + Discovery from PR body |
| `cp:eval` | `#1D76DB` | CP — Eval | Advance pipeline by one stage |
| `cp:review` | `#D93F0B` | CP — Review | Run portfolio review on demand |

**Rules**

- One action label per PR — do not combine `cp:intake` and `cp:eval` on the same PR.
- Write automations require **both** the label and the matching branch prefix (see each section below).
- QA does not use a label — it runs automatically on PR open/push when paths match.

---

## CP — QA

Read-only validation. **Never commits.**

| Setting | Value |
|---------|-------|
| **Name** | CP — QA |
| **Description** | Validate PRs changing opportunities or portfolio entries |
| **Trigger** | Git — pull request **opened** |
| **Trigger** | Git — code **pushed to pull request** |
| **Path scope** | Changes under `opportunities/` or `portfolio/` |
| **Tools** | Comment on PRs **only** |
| **Repo checkout** | `wi2/panel-control`, branch `master` |
| **ignoreDraftPrs** | `true` |

### Agent instructions

```text
You are running CP — QA for the AI Startup Studio Brain control plane.

Execute prompts/automation-qa-v1.md against this pull request.
Do not modify any files.
```

### Expected output

PR comment titled **Control Plane QA — pass | warn | fail**.

### Related prompts

- [prompts/automation-qa.md](../prompts/automation-qa.md)
- [prompts/opportunity-qa.md](../prompts/opportunity-qa.md)

---

## CP — Intake

Creates a new opportunity file and runs Discovery from a PR description.

| Setting | Value |
|---------|-------|
| **Name** | CP — Intake |
| **Description** | Create OPP file with Discovery from PR intake template |
| **Trigger** | Git — **label change** (label `cp:intake`) |
| **Tools** | None (agent commits via PR branch) |
| **Repo checkout** | `wi2/panel-control`, branch `master` |
| **ignoreDraftPrs** | `true` |

**Branch gate**: PR head branch must match `intake/**`.

### PR body template

```markdown
## Intake

**Title:** Short opportunity title
**Owner:** studio-team
**Tags:** b2b, saas

### Description

1–3 paragraphs describing the problem and proposed angle.
```

### Agent instructions

```text
You are running CP — Intake for the AI Startup Studio Brain control plane.

Execute prompts/automation-intake-v1.md against this pull request.
Commit to the PR branch. Do not push to master.
```

### Expected output

New file under `opportunities/`, Discovery section filled, **Intake Complete** summary comment.

### Workflow

1. Create branch `intake/{slug}`.
2. Open PR with the intake template in the description.
3. Add label `cp:intake`.
4. Merge after **CP — QA** passes.

### Related prompts

- [prompts/automation-intake.md](../prompts/automation-intake.md)
- [prompts/intake.md](../prompts/intake.md)

---

## CP — Eval

Advances one opportunity by exactly one pipeline stage.

| Setting | Value |
|---------|-------|
| **Name** | CP — Eval |
| **Description** | Pipeline +1 for one opportunity on eval branch |
| **Trigger** | Git — **label change** (label `cp:eval`) |
| **Tools** | None (agent commits via PR branch) |
| **Repo checkout** | `wi2/panel-control`, branch `master` |
| **ignoreDraftPrs** | `true` |

**Branch gate**: PR head branch must match `eval/OPP-YYYYMMDD-slug`.

The opportunity file `opportunities/OPP-YYYYMMDD-slug.md` must already exist on the branch.

### Agent instructions

```text
You are running CP — Eval for the AI Startup Studio Brain control plane.

Execute prompts/automation-eval-v1.md against this pull request.
Commit to the PR branch. One pipeline stage per run. Do not push to master.
```

### Expected output

Updated opportunity section, **Pipeline Run Summary** comment. **CP — QA** runs on the subsequent push.

### Workflow

1. Create branch `eval/OPP-YYYYMMDD-slug` from `master`.
2. Open PR (opportunity file must exist).
3. Add label `cp:eval` → one stage executes.
4. Re-add label `cp:eval` to advance the next stage, or merge and open a new eval PR.
5. Merge after **CP — QA** passes.

### Related prompts

- [prompts/automation-eval.md](../prompts/automation-eval.md)
- [prompts/pipeline-orchestrator.md](../prompts/pipeline-orchestrator.md)

---

## CP — Review

Scheduled and on-demand portfolio review of due MONITOR and BUILD entries.

| Setting | Value |
|---------|-------|
| **Name** | CP — Review |
| **Description** | Re-evaluate overdue monitoring and active portfolio entries |
| **Trigger** | Cron — `0 9 * * 1` (every Monday at 09:00) |
| **Trigger** | Git — **label change** (label `cp:review`) |
| **Tools** | None (agent commits via PR) |
| **Repo checkout** | `wi2/panel-control`, branch `master` |

**Label gate**: when triggered by label, PR head branch must match `review/**`.

### Agent instructions

```text
You are running CP — Review for the AI Startup Studio Brain control plane.

Execute prompts/automation-review-v1.md.
Process at most 3 MONITOR opportunities per run.
Open a pull request for any file changes. Do not push to master.
```

### Expected output

**Portfolio Review Run** summary; optional `reviews/REVIEW-*.md`; PR with opportunity and portfolio updates. **CP — QA** runs on the subsequent push.

### Manual trigger

1. Create branch `review/YYYY-MM-DD`.
2. Open PR, add label `cp:review`.

### Related prompts

- [prompts/automation-review.md](../prompts/automation-review.md)
- [prompts/portfolio-review-runner.md](../prompts/portfolio-review-runner.md)

---

## End-to-end flows

### New idea

```text
intake/mon-idee → PR + ## Intake body → label cp:intake
  → CP — Intake commits OPP → CP — QA comments → merge
```

### Pipeline advancement

```text
eval/OPP-20260625-slug → PR → label cp:eval (repeat per stage)
  → CP — Eval (+1 stage) → CP — QA → merge when decided
```

### Weekly review

```text
Cron Monday 09:00 → CP — Review → PR review/YYYY-MM-DD → CP — QA
```

Or manually: `review/YYYY-MM-DD` + label `cp:review`.

---

## Security notes

| Automation | Writes files | Tools |
|------------|--------------|-------|
| CP — QA | **No** | Comment on PRs only |
| CP — Intake | Yes | Agent commit on PR branch |
| CP — Eval | Yes | Agent commit on PR branch |
| CP — Review | Yes | Agent commit + open PR |

- Write automations never push to `master` directly.
- Branch prefix + label double-gate prevents accidental pipeline runs.
- Do not merge when **CP — QA** verdict is **fail**.

---

## Related

- [Contributing PR checklist](../CONTRIBUTING.md)
- [Prompts index](../prompts/README.md)
- [Conventions](../CONVENTIONS.md)
