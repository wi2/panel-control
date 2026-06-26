# Cursor Automations

Operational setup for the AI Startup Studio Brain control plane with [Cursor Automations](https://cursor.com/docs).

See [AGENTS.md](../AGENTS.md) for agent operating rules shared by all automations below.

## Architecture

Four automations — one job each, thin wrapper → versioned prompt:

```text
CP — QA      (read-only)  → prompts/automation-qa-v3.md       → opportunity-qa-v3
CP — Intake  (write)      → prompts/automation-intake-v6.md   → intake-v6
CP — Eval    (write)      → prompts/automation-eval-v7.md     → pipeline-orchestrator-v5
CP — Review  (write)      → prompts/automation-review-v1.md   → portfolio-review-runner-v1
```

**Studio branch**: fixed name **`opp/pipeline`** — one **active** opportunity (`draft` / `evaluating`) at a time. Catalogue of `decided` OPP files from `master` may coexist on the branch. Labels: **`cp:intake`** (once) then **`cp:eval`** (once) for full pipeline in a single Eval run.

## Cursor UI constraints

| Limitation | Workaround |
|------------|------------|
| No branch wildcards (`opp/**`) | Use exact branch name `opp/pipeline` |
| Branch field cannot be empty (defaults to `master`) | Set PR head branch to `opp/pipeline` explicitly |
| Label vs push triggers | Intake = label `cp:intake`; Eval = label `cp:eval` (not push) |

After each merged idea: delete `opp/pipeline`, recreate from `master` for the next intake.

## Prerequisites

Before enabling automations:

1. Push this repository to GitHub and connect it in Cursor.
2. Configure `gitConfig` in each automation: repo `wi2/panel-control`, branch `master`.
3. Create GitHub labels — run workflow [Sync GitHub labels](../.github/workflows/sync-labels.yml) or apply [`.github/labels.yml`](../.github/labels.yml) manually (`gh label list` to verify).
4. Enable **usage-based pricing** and a spend limit in Cursor (Background Agents require billing).
5. Work via pull requests — do not push directly to the default branch (see [AGENTS.md](../AGENTS.md)).
6. Enable **ignore draft PRs** on Git triggers where available.

**Remote**: `git@github.com:wi2/panel-control.git`

---

## GitHub labels

| Label | Color (suggested) | Automation | Purpose |
|-------|-------------------|------------|---------|
| `cp:intake` | `#0E8A16` | CP — Intake | Create OPP + Discovery (once per pipeline run) |
| `cp:eval` | `#1D76DB` | CP — Eval | Full pipeline evaluation (all remaining stages → `decided`) |
| `cp:review` | `#D93F0B` | CP — Review | Portfolio review on demand |

Label definitions live in [`.github/labels.yml`](../.github/labels.yml). Sync via GitHub Actions workflow **Sync GitHub labels** or create manually in the repo settings.

**Rules**

- Add `cp:intake` **once** when starting a new idea on `opp/pipeline`.
- After **Intake Complete**, add `cp:eval` **once** to run the full pipeline.
- Remove `cp:eval` after successful `decided` to avoid re-trigger.
- QA runs automatically on PR open/push when paths match — no label.
- Review uses `cp:review` on `review/**` branches only.
- Do **not** add `cp:intake` and `cp:eval` simultaneously — wait for Intake Complete.

---

## Studio workflow (`opp/pipeline`)

```text
1. git checkout master && git pull
2. git checkout -b opp/pipeline master
3. git push -u origin opp/pipeline          # does NOT trigger Eval
4. Open PR + ## Intake body → label cp:intake (once)
5. CP — Intake → push (QA only)
6. label cp:eval → CP — Eval (full run → decided) → push
7. CP — QA on each push → merge when pass
8. git push origin --delete opp/pipeline   # optional cleanup
9. Next idea: repeat from step 1
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

Execute prompts/automation-qa-v3.md against this pull request.
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

Execute prompts/automation-intake-v6.md against this pull request.
Commit and push to opp/pipeline. Do not push to master.
```

### Expected output

New file under `opportunities/`, Discovery section filled, `intake_complete: true`, **Intake Complete** summary. Push triggers **CP — QA** only — add label **`cp:eval`** to start evaluation.

---

## CP — Eval

Runs the **full remaining pipeline** in one invocation when label **`cp:eval`** is added.

| Setting | Value |
|---------|-------|
| **Name** | CP — Eval |
| **Description** | Full pipeline run on opp/pipeline (all remaining stages → decided) |
| **Trigger** | Git — **label change** (label `cp:eval`) |
| **Tools** | None (agent commit + push on PR branch) |
| **Repo checkout** | `wi2/panel-control`, branch `master` |
| **ignoreDraftPrs** | `true` |

**Do not** use push-to-branch trigger for CP — Eval.

**Branch gate**: PR head branch must be **`opp/pipeline`**.

**OPP resolution**: exactly **one active** OPP among `opportunities/OPP-*.md` — frontmatter `status: draft` or `status: evaluating`. Ignore catalogue files with `status: decided`.

**Intake gate**: active OPP must have `intake_complete: true` and filled Discovery section.

### Agent instructions

```text
You are running CP — Eval for the AI Startup Studio Brain control plane.

Execute prompts/automation-eval-v7.md against this pull request.
Commit and push to opp/pipeline. Full pipeline run (all remaining stages). Do not push to master.
```

### Expected output

**Pipeline Run Summary** with all stages executed and `Remaining stages: none` when `decided`. **CP — QA** runs on push. Recommend removing `cp:eval` label after success.

### Cursor setup (required)

1. Open automation **CP — Eval**.
2. **Remove** trigger **New push to branch** (if present).
3. **Add** trigger: **Label change** → label **`cp:eval`**.
4. Repo: `wi2/panel-control`.
5. Paste agent instructions above.
6. Save.

Also update **CP — Intake** instructions to `automation-intake-v6.md`.

### Cursor reconfig (v5 pipeline)

After merging v5 docs, reconfigure Cursor automations:

| Automation | Trigger | Instructions file |
|------------|---------|-------------------|
| **CP — Intake** | Label `cp:intake` | `prompts/automation-intake-v6.md` |
| **CP — Eval** | Label `cp:eval` (not push) | `prompts/automation-eval-v7.md` |
| **CP — QA** | PR open/push | `prompts/automation-qa-v3.md` (unchanged) |
| **CP — Review** | Cron + label `cp:review` | `prompts/automation-review-v1.md` (unchanged) |

Verify **CP — Eval** has **no** push trigger on `opp/pipeline`.

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
  → Intake Complete (intake_complete: true) → push → QA
  → cp:eval (once) → full Eval run → decided → push → QA
  → merge → delete opp/pipeline → next idea
```

---

## Migration

| Legacy | Action |
|--------|--------|
| `intake/**`, `eval/OPP-*`, `opp/{slug}` | Use `opp/pipeline` only |
| CP — Eval push trigger on `opp/pipeline` | **Remove** — use label `cp:eval` only |
| `automation-eval-v6.md`, `pipeline-orchestrator-v4.md` | Upgrade to v7 / v5 |
| `automation-intake-v5.md`, `intake-v5.md` | Upgrade to v6 |
| Open smoke/test PRs on old branches | Close without merge |

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Eval starts before Intake | Push trigger still enabled on CP — Eval | Remove push trigger; use label `cp:eval` only |
| Eval NOOP: intake not complete | `cp:eval` added before Intake finished | Wait for Intake Complete; verify `intake_complete: true` |
| Eval never starts after Intake | `cp:eval` label not added | Add label after Intake Complete |
| Eval NOOP: wrong branch | PR not on `opp/pipeline` | Recreate branch with exact name |
| Eval NOOP: ambiguous OPP | Multiple **active** OPPs (`draft`/`evaluating`) on branch | One active OPP per run; catalogue `decided` is OK |
| Intake NOOP: active OPP exists | Pipeline already in progress | Add `cp:eval` or wait until `decided` |
| Eval re-runs on decided OPP | `cp:eval` label still present | Remove label; Eval NOOPs on `decided` |
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

Run after merging v5 pipeline docs to `master` and reconfiguring Cursor automations.

### Prerequisites

1. Merge docs PR (v5/v6/v7 prompts + this file) to `master`.
2. **CP — Eval**: trigger **Label change** → `cp:eval` only; **remove** push trigger; instructions → `automation-eval-v7.md`.
3. **CP — Intake**: instructions → `automation-intake-v6.md`.
4. Sync labels: `gh label list | grep cp:` shows `cp:intake`, `cp:eval`, `cp:review`.

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

**Title:** Pipeline smoke test v5
**Owner:** studio-team
**Tags:** smoke-test

### Description

Minimal smoke test for opp/pipeline v5 flow (cp:eval, full run). Safe to kill after verification.
```

3. Add label `cp:intake` once.
4. Wait for **Intake Complete** → verify `intake_complete: true`, Discovery OK, **no** Validation section yet.
5. Push to branch alone must **not** trigger Eval.
6. Add label `cp:eval` once.
7. Wait for **Pipeline Run Summary** with `decided` in one run (solo path: 3 stages post-intake).
8. **CP — QA** should comment on each push (after intake and after eval).
9. After verification: close PR without merge (or merge if you want to keep the OPP), then:

```bash
git push origin --delete opp/pipeline
```

### Smoke verification matrix

| Step | Action | Expected |
|------|--------|----------|
| 1 | Push `opp/pipeline` without labels | No Eval run |
| 2 | `cp:intake` | OPP + Discovery + `intake_complete: true` |
| 3 | `cp:eval` before Intake done (optional race test) | NOOP: intake not complete |
| 4 | `cp:eval` after Intake Complete | Full run → `decided` |
| 5 | `python3 scripts/validate_opportunities.py` | pass |
| 6 | CP — QA | pass or warn |

---

## Onboarding checklist

After configuring all four Cursor Automations, verify each item:

- [ ] `gh label list` shows `cp:intake`, `cp:eval`, and `cp:review` (or run **Sync GitHub labels** workflow)
- [ ] **CP — QA** uses `prompts/automation-qa-v3.md`; test with a PR touching `opportunities/`
- [ ] **CP — Intake** uses `prompts/automation-intake-v6.md`; trigger label `cp:intake`
- [ ] **CP — Eval** uses `prompts/automation-eval-v7.md`; trigger label `cp:eval` only (**no push trigger**)
- [ ] **CP — Review** uses `prompts/automation-review-v1.md`; cron + `cp:review` on `review/**`
- [ ] GitHub Action **Validate opportunities and portfolio** passes on PR
- [ ] Smoke test procedure completes with `decided` on a test OPP

### Post-setup verification commands

```bash
gh label list | grep cp:
python3 scripts/validate_opportunities.py
```

---

## Related

- [Contributing PR checklist](../CONTRIBUTING.md)
- [Prompts index](../prompts/README.md)
- [Conventions](../CONVENTIONS.md)
