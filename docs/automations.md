# Cursor Automations

Operational setup for the AI Startup Studio Brain control plane with [Cursor Automations](https://cursor.com/docs).

See [AGENTS.md](../AGENTS.md) for agent operating rules shared by all automations below.

## Architecture

Four automations — one job each, thin wrapper → versioned prompt:

```text
CP — QA      (read-only)  → prompts/automation-qa-v1.md       → opportunity-qa-v1
CP — Intake  (write)      → prompts/automation-intake-v4.md   → intake-v4
CP — Eval    (write)      → prompts/automation-eval-v4.md     → pipeline-orchestrator-v2
CP — Review  (write)      → prompts/automation-review-v1.md   → portfolio-review-runner-v1
```

**Studio branch**: fixed name **`opp/pipeline`** — one **active** opportunity (`draft` / `evaluating`) at a time. Catalogue of `decided` OPP files from `master` may coexist on the branch. One PR, one label (`cp:intake`). Eval advances on each **push** to `opp/pipeline` (up to 5 stages per run) until `decided`.

## Cursor UI constraints

| Limitation | Workaround |
|------------|------------|
| No branch wildcards (`opp/**`) | Use exact branch name `opp/pipeline` |
| Branch field cannot be empty (defaults to `master`) | Set trigger branch to `opp/pipeline` explicitly |
| No reliable « PR pushed » trigger in all setups | Use **New push to branch** on `opp/pipeline` |

After each merged idea: delete `opp/pipeline`, recreate from `master` for the next intake.

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
| `cp:intake` | `#0E8A16` | CP — Intake | Create OPP + Discovery (once per pipeline run) |
| `cp:review` | `#D93F0B` | CP — Review | Portfolio review on demand |

**Removed**: `cp:eval` — Eval is push-triggered on `opp/pipeline`, no label.

**Rules**

- Add `cp:intake` **once** when starting a new idea on `opp/pipeline`.
- QA runs automatically on PR open/push when paths match — no label.
- Review uses `cp:review` on `review/**` branches only.

---

## Studio workflow (`opp/pipeline`)

```text
1. git checkout master && git pull
2. git checkout -b opp/pipeline master
3. git push -u origin opp/pipeline
4. Open PR + ## Intake body → label cp:intake (once)
5. CP — Intake → push → CP — Eval (batch) → push → … until decided
6. CP — QA on each push → merge when pass
7. git push origin --delete opp/pipeline   # optional cleanup
8. Next idea: repeat from step 1
```

Only **one active OPP** (`draft` or `evaluating`) on `opp/pipeline` at a time. Catalogue `decided` files inherited from `master` are normal.

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

**Branch gate**: PR head branch must be **exactly** `opp/pipeline`.

**Precondition**: no **active** OPP on the branch — no `opportunities/OPP-*.md` with `status: draft` or `status: evaluating`. Catalogue of `decided` OPP files from `master` is allowed.

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

Execute prompts/automation-intake-v4.md against this pull request.
Commit and push to opp/pipeline. Do not push to master.
```

### Expected output

New file under `opportunities/`, Discovery section filled, **Intake Complete** summary. Push triggers **CP — Eval**.

---

## CP — Eval

Advances the pipeline in **batches of up to 5 stages** per push. **No label.**

| Setting | Value |
|---------|-------|
| **Name** | CP — Eval |
| **Description** | Pipeline batch (max 5 stages) on opp/pipeline push |
| **Trigger** | Git — **new push to branch** |
| **Branch (exact)** | `opp/pipeline` |
| **Tools** | None (agent commit + push on PR branch) |
| **Repo checkout** | `wi2/panel-control`, branch `master` |
| **ignoreDraftPrs** | `true` (if PR triggers also configured) |

**Do not** use label `cp:eval`. **Do not** leave branch as `master` — Eval would never run on pipeline pushes.

**Branch gate**: push target / PR head branch must be **`opp/pipeline`**.

**OPP resolution**: exactly **one active** OPP among `opportunities/OPP-*.md` — frontmatter `status: draft` or `status: evaluating`. Ignore catalogue files with `status: decided`.

### Agent instructions

```text
You are running CP — Eval for the AI Startup Studio Brain control plane.

Execute prompts/automation-eval-v4.md against this pull request.
Commit and push to opp/pipeline. Up to 5 pipeline stages per run. Do not push to master.
```

### Expected output

**Pipeline Run Summary** with stages executed (≤5). If not `decided`, next push runs the next batch. **CP — QA** runs on each push.

### Cursor setup (required)

1. Open automation **CP — Eval**.
2. **Remove** any label `cp:eval` trigger.
3. **Add** trigger: **New push to branch**.
4. Repo: `wi2/panel-control`.
5. Branch: **`opp/pipeline`** (exact — no wildcard).
6. Paste agent instructions above.
7. Save.

Also update **CP — Intake** instructions to `automation-intake-v4.md`.

### Cursor reconfig (v4)

After merging v4 docs, update automation instructions only (triggers unchanged):

| Automation | Instructions file |
|------------|-------------------|
| **CP — Intake** | `prompts/automation-intake-v4.md` |
| **CP — Eval** | `prompts/automation-eval-v4.md` |

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

## End-to-end flow

```text
opp/pipeline → PR + ## Intake → cp:intake (once)
  → Intake → push → Eval batch → push → Eval batch → decided
  → QA each push → merge → delete opp/pipeline → next idea
```

---

## Migration

| Legacy | Action |
|--------|--------|
| `intake/**`, `eval/OPP-*`, `opp/{slug}` | Use `opp/pipeline` only |
| Label `cp:eval` | Remove from GitHub and CP — Eval |
| Trigger on `master` or `opp/automation-v2-smoke` | Change to `opp/pipeline` |
| Open smoke/test PRs on old branches | Close without merge |

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Eval never starts after Intake | Trigger branch is `master` or wrong name | Set CP — Eval to **push** → `opp/pipeline` |
| Eval NOOP: wrong branch | PR not on `opp/pipeline` | Recreate branch with exact name |
| Eval NOOP: ambiguous OPP | Multiple **active** OPPs (`draft`/`evaluating`) on branch | One active OPP per run; catalogue `decided` is OK |
| Eval NOOP: ambiguous (v3) | Total OPP count includes `decided` catalogue | Upgrade to v4 prompts; reconfigure Cursor |
| Intake NOOP: active OPP exists | Pipeline already in progress | Use **CP — Eval** (push); wait until `decided` |
| Intake NOOP: OPP exists (v3) | v3 blocked on any OPP file | Upgrade to v4 prompts |
| QA success, no PR comment | Comment on PRs disabled | Enable on CP — QA |
| Automation failed to start | Billing / spend limit | Cursor dashboard → Settings |

---

## Security notes

| Automation | Writes files | Tools |
|------------|--------------|-------|
| CP — QA | **No** | Comment on PRs only |
| CP — Intake | Yes | Agent commit + push on `opp/pipeline` |
| CP — Eval | Yes | Agent commit + push on `opp/pipeline` |
| CP — Review | Yes | Agent commit + open PR |

- Write automations never push to `master` directly.
- Do not merge when **CP — QA** verdict is **fail**.

---

## Smoke test (`opp/pipeline`)

Run after merging v4 docs to `master` and reconfiguring Cursor automations to v4.

### Prerequisites

1. Merge docs PR (v4 prompts + this file) to `master`.
2. **CP — Eval**: trigger **New push to branch** → `opp/pipeline`; instructions → `automation-eval-v4.md`.
3. **CP — Intake**: instructions → `automation-intake-v4.md`.
4. Close without merge (if still open): PRs on `opp/automation-v2-smoke`, `intake/automation-smoke-test`, `test/qa-smoke`.

### Retry on existing smoke PR

If intake already ran on an open `opp/pipeline` PR (e.g. `OPP-20260626-pipeline-smoke-test.md` with `status: evaluating`):

1. Merge v4 docs → `master`.
2. Reconfigure Cursor → v4 prompts (see [Cursor reconfig (v4)](#cursor-reconfig-v4)).
3. Merge `master` into `opp/pipeline` (or empty commit + push).
4. **CP — Eval** should resolve the single active OPP and post **Pipeline Run Summary** (not NOOP ambiguous).
5. **CP — QA** comments on each push.

### Steps (new smoke)

```bash
git checkout master && git pull
git checkout -b opp/pipeline master
git push -u origin opp/pipeline
```

1. Open PR from `opp/pipeline` → `master`.
2. PR body:

```markdown
## Intake

**Title:** Pipeline smoke test
**Owner:** studio-team
**Tags:** smoke-test

### Description

Minimal smoke test for opp/pipeline v4 flow. Safe to kill after verification.
```

3. Add label `cp:intake` once.
4. Wait for **Intake Complete** → verify one new active `opportunities/OPP-*.md` on branch (catalogue `decided` may coexist).
5. Each agent push should trigger **CP — Eval** (batch ≤5 stages) until `decided` or manual stop.
6. **CP — QA** should comment on each push.
7. After verification: close PR without merge (or merge if you want to keep the OPP), then:

```bash
git push origin --delete opp/pipeline
```

### Legacy branch cleanup

| Branch | Action |
|--------|--------|
| `opp/automation-v2-smoke` | Delete remote + local after smoke passes |
| `intake/automation-smoke-test` | Close PR; delete branch |
| `test/qa-smoke`, `test/qa-pr-automation` | Close if obsolete |

---

## Related

- [Contributing PR checklist](../CONTRIBUTING.md)
- [Prompts index](../prompts/README.md)
- [Conventions](../CONVENTIONS.md)
