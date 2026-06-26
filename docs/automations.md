# Cursor Automations

Operational setup for the AI Startup Studio Brain control plane with [Cursor Automations](https://cursor.com/docs).

See [AGENTS.md](../AGENTS.md) for agent operating rules shared by all automations below.

## Architecture

Four automations — one job each, thin wrapper → versioned prompt:

```text
CP — QA      (read-only)  → prompts/automation-qa-v1.md       → opportunity-qa-v1
CP — Intake  (write)      → prompts/automation-intake-v2.md   → intake-v2
CP — Eval    (write)      → prompts/automation-eval-v2.md     → pipeline-orchestrator-v2
CP — Review  (write)      → prompts/automation-review-v1.md   → portfolio-review-runner-v1
```

One opportunity lifecycle = **one branch `opp/**`**, **one PR**, **one human label** (`cp:intake`). Eval advances automatically on each **push** (up to 5 stages per run) until `decided`.

## Prerequisites

Before enabling automations:

1. Push this repository to GitHub and connect it in Cursor.
2. Configure `gitConfig` in each automation: repo `wi2/panel-control`, branch `master`.
3. Create GitHub labels (see [GitHub labels](#github-labels)).
4. Enable **usage-based pricing** and a spend limit in Cursor (Background Agents require billing).
5. Work via pull requests — do not push directly to the default branch (see [AGENTS.md](../AGENTS.md)).
6. Enable **ignore draft PRs** on Git triggers where available.

**Remote**: `git@github.com:wi2/panel-control.git`

---

## GitHub labels

| Label | Color (suggested) | Automation | Purpose |
|-------|-------------------|------------|---------|
| `cp:intake` | `#0E8A16` | CP — Intake | Create OPP + Discovery (once per PR) |
| `cp:review` | `#D93F0B` | CP — Review | Portfolio review on demand |

**Removed**: `cp:eval` — Eval is **push-triggered** on `opp/**`, no label.

**Rules**

- Add `cp:intake` **once** at the start of a new idea on `opp/**`.
- QA runs automatically on PR open/push when paths match — no label.
- Review uses `cp:review` on `review/**` branches only.

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

You MUST post the QA verdict on this pull request using the Comment on PRs tool.
Do not mark the run complete until the comment is visible on the PR.
If the diff is outside opportunities/ or portfolio/, post NOOP: outside QA scope as a PR comment.
```

### Expected output

PR comment titled **Control Plane QA — pass | warn | fail**.

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

**Branch gate**: PR head branch must match `opp/**`.

**Precondition**: no `opportunities/OPP-*.md` on the branch yet.

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

Execute prompts/automation-intake-v2.md against this pull request.
Commit and push to the PR branch. Do not push to master.
```

### Expected output

New file under `opportunities/`, Discovery section filled, **Intake Complete** summary. Push triggers **CP — Eval** automatically.

---

## CP — Eval

Advances the pipeline in **batches of up to 5 stages** per push. **No label.**

| Setting | Value |
|---------|-------|
| **Name** | CP — Eval |
| **Description** | Pipeline batch (max 5 stages) on opp branch push |
| **Trigger** | Git — code **pushed to pull request** |
| **Branch scope** | `opp/**` (configure in Cursor if branch filter available) |
| **Tools** | None (agent commit + push on PR branch) |
| **Repo checkout** | `wi2/panel-control`, branch `master` |
| **ignoreDraftPrs** | `true` |

**Do not** use label `cp:eval`. Remove legacy label trigger if still configured.

**Branch gate**: PR head branch must match `opp/**`.

Resolve target OPP:

- `opp/OPP-YYYYMMDD-slug` → `opportunities/OPP-YYYYMMDD-slug.md`
- Otherwise exactly one `opportunities/OPP-*.md` on the branch

### Agent instructions

```text
You are running CP — Eval for the AI Startup Studio Brain control plane.

Execute prompts/automation-eval-v2.md against this pull request.
Commit and push to the PR branch. Up to 5 pipeline stages per run. Do not push to master.
```

### Expected output

**Pipeline Run Summary** with stages executed (≤5). If not `decided`, next push runs the next batch automatically. **CP — QA** runs on each push.

### Reconfigure from v1 (required)

If CP — Eval was set up with label `cp:eval`:

1. Open automation **CP — Eval** in Cursor Automations.
2. **Remove** trigger: label change `cp:eval`.
3. **Add** trigger: pull request **pushed**, repo `wi2/panel-control`.
4. Restrict to branches matching `opp/**` if the UI supports it.
5. Update instructions to reference `automation-eval-v2.md` (text above).
6. Save. Optionally delete GitHub label `cp:eval`.

Also update **CP — Intake** instructions to `automation-intake-v2.md` and branch gate `opp/**`.

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

---

## End-to-end flow (v2)

### New idea — one PR

```text
opp/mon-idee → PR + ## Intake body → label cp:intake (once)
  → CP — Intake: OPP + Discovery → push
  → CP — Eval: batch ≤5 stages → push
  → CP — Eval: batch ≤5 stages → push   (repeat until decided)
  → CP — QA on each push → merge when pass
```

Typical decision path after intake: ~2 Eval runs (9 stages post-discovery ÷ 5 per batch).

### Weekly review

```text
Cron Monday 09:00 → CP — Review → PR review/YYYY-MM-DD → CP — QA
```

Or manually: `review/YYYY-MM-DD` + label `cp:review`.

---

## Migration from v1

| Legacy | Action |
|--------|--------|
| Branch `intake/**` | Use `opp/**`; close or merge open intake PRs |
| Branch `eval/OPP-*` | Use same PR on `opp/**`; abandon eval branches |
| Label `cp:eval` | Remove from GitHub; remove from CP — Eval triggers |
| CP — Eval label trigger | Replace with PR **pushed** on `opp/**` |

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Eval never starts after intake | CP — Eval still on label trigger | Reconfigure per [CP — Eval](#cp--eval) |
| Eval NOOP on `intake/**` | Legacy branch | Rename branch to `opp/**` |
| Infinite Eval loop | Agent pushes with no stage progress | Check run log; gate blocker in summary |
| QA success, no PR comment | Comment on PRs tool disabled | Enable on CP — QA |
| Automation failed to start | Usage-based pricing off | Cursor dashboard → Settings → billing |
| Push does not trigger Eval | Branch not `opp/**` or automation scope | Verify branch name and trigger config |

---

## Security notes

| Automation | Writes files | Tools |
|------------|--------------|-------|
| CP — QA | **No** | Comment on PRs only |
| CP — Intake | Yes | Agent commit + push on PR branch |
| CP — Eval | Yes | Agent commit + push on PR branch |
| CP — Review | Yes | Agent commit + open PR |

- Write automations never push to `master` directly.
- Do not merge when **CP — QA** verdict is **fail**.

---

## Related

- [Contributing PR checklist](../CONTRIBUTING.md)
- [Prompts index](../prompts/README.md)
- [Conventions](../CONVENTIONS.md)
