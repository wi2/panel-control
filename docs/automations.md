# Cursor Automations

Operational setup for the AI Startup Studio Brain control plane with [Cursor Automations](https://cursor.com/docs).

See [AGENTS.md](../AGENTS.md) for agent operating rules shared by all automations below.

## Architecture

Four automations — one job each, thin wrapper → versioned prompt:

```text
CP — QA      (read-only)  → prompts/automation-qa-v6.md       → opportunity-qa-v5
CP — Intake  (write)      → prompts/automation-intake-v8.md   → intake-v7
CP — Eval    (write)      → prompts/automation-eval-v10.md    → pipeline-orchestrator-v8
CP — Review  (write)      → prompts/automation-review-v3.md   → portfolio-review-runner-v3
```

**Eval v3-lite:** Intake → **1×** `cp:eval` (full-run) → `decided`. See [decisions/2026-06-simplification-v3-lite.md](../docs/decisions/2026-06-simplification-v3-lite.md).

## Cursor UI constraints

| Limitation | Workaround |
|------------|------------|
| No branch wildcards (`opp/**`) | Use exact branch name `opp/pipeline` |
| Branch field cannot be empty (defaults to `master`) | Set PR head branch to `opp/pipeline` explicitly |
| Label vs push triggers | Intake = PR opened + optional `cp:intake`; Eval = `cp:eval` only; QA = push to PR only |

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
| `cp:intake` | `#0E8A16` | CP — Intake | Optional fallback if PR-open Intake did not run |
| `cp:eval` | `#1D76DB` | CP — Eval | Staged evaluation — one stage per label until `decided` |
| `cp:review` | `#D93F0B` | CP — Review | Portfolio review on demand |

Label definitions live in [`.github/labels.yml`](../.github/labels.yml). Sync via GitHub Actions workflow **Sync GitHub labels** or create manually in the repo settings.

**Rules**

- Open PR with `## Intake` on `opp/pipeline` → **CP — Intake** runs on PR opened.
- Label `cp:intake` is **optional** (fallback only).
- After **Intake Complete**, add `cp:eval` **once** — full-run to `decided`.
- Remove `cp:eval` after successful `decided` to avoid re-trigger.
- **CP — QA** runs on **push to PR** only (after Intake or Eval commits) — no label.
- Review uses `cp:review` on `review/**` branches only.
- Do **not** add `cp:intake` and `cp:eval` simultaneously — wait for Intake Complete.

---

## Studio workflow (`opp/pipeline`)

```text
1. git checkout master && git pull
2. git push origin --delete opp/pipeline   # if exists
3. git checkout -b opp/pipeline master
4. git commit --allow-empty -m "chore: open pipeline PR for automation run"
5. git push -u origin opp/pipeline
6. Open PR + ## Intake body → CP — Intake (PR opened)
7. Push after Intake → CP — QA
8. label cp:eval → full-run (validation + fit_and_decide) → decided
9. Push after eval → CP — QA (merge gate on decided push)
10. Merge when latest QA = pass or warn on **decided** push
11. git push origin --delete opp/pipeline
12. Next idea: repeat from step 1
```

Only **one active OPP** (`draft` or `evaluating`) on `opp/pipeline` at a time. Catalogue `decided` files inherited from `master` are normal.

---

## CP — QA

Read-only validation. **Never commits.**

| Setting | Value |
|---------|-------|
| **Name** | CP — QA |
| **Description** | Validate PRs changing opportunities or portfolio entries |
| **Trigger** | Git — code **pushed to pull request** |
| **Do not** | Git — pull request **opened** |
| **Path scope** | Changes under `opportunities/` or `portfolio/` |
| **Tools** | Comment on PRs **only** |
| **Repo checkout** | `wi2/panel-control`, branch `master` |
| **ignoreDraftPrs** | `true` |

### Agent instructions

```text
You are running CP — QA for the AI Startup Studio Brain control plane.

Execute prompts/automation-qa-v6.md against this pull request.
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
| **Trigger** | Git — pull request **opened** |
| **Trigger** | Git — **label change** (label `cp:intake`, optional) |
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

Execute prompts/automation-intake-v8.md against this pull request.
Commit and push to opp/pipeline. Do not push to master.
```

### Expected output

New file under `opportunities/`, Discovery section filled, `intake_complete: true`, **Intake Complete** summary. Push triggers **CP — QA**. Add label **`cp:eval` once** for full-run eval.

---

## CP — Eval

Runs **full pipeline** (validation + fit_and_decide) per label **`cp:eval`** on branch **`opp/pipeline`**.

| Setting | Value |
|---------|-------|
| **Name** | CP — Eval |
| **Description** | v3-lite full-run on opp/pipeline — one cp:eval to decided |
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

Execute prompts/automation-eval-v10.md against this pull request.
Commit and push to opp/pipeline. Full-run — one cp:eval to decided. Do not push to master.
```

### Expected output

**Pipeline Run Summary** with `Mode: full-run`. Success: `Remaining stages: none`, `status: decided`.

### Cursor setup (required)

1. Open automation **CP — Eval**.
2. **Remove** trigger **New push to branch** (if present).
3. **Add** trigger: **Label change** → label **`cp:eval`**.
4. Repo: `wi2/panel-control`.
5. Paste agent instructions above.
6. Save.

### Cursor reconfig (v3-lite)

After merging v3-lite to `master`, reconfigure Cursor automations:

| Automation | Trigger | Instructions file |
|------------|---------|-------------------|
| **CP — Intake** | PR **opened** + label `cp:intake` (optional) | `prompts/automation-intake-v8.md` |
| **CP — Eval** | Label `cp:eval` (not push) | `prompts/automation-eval-v10.md` |
| **CP — QA** | Push to PR only (**remove** PR opened) | `prompts/automation-qa-v6.md` |
| **CP — Review** | Cron + label `cp:review` | `prompts/automation-review-v3.md` |

Verify **CP — Eval** has **no** push trigger on `opp/pipeline`.
Verify **CP — QA** has **no** PR opened trigger.

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

Execute prompts/automation-review-v3.md.
Process at most 3 MONITOR_MICRO opportunities per run (solo_micro_saas registry).
Open a pull request for any file changes. Do not push to master.
```

---

## End-to-end flow

```text
opp/pipeline → empty commit → PR + ## Intake → Intake (PR opened)
  → Intake Complete → push → QA (push)
  → cp:eval (once, full-run) → validation + fit_and_decide → decided
  → QA on eval push; merge gate on decided push
  → merge → delete opp/pipeline → next idea
```

---

## Migration

| Legacy | Action |
|--------|--------|
| Staged eval (orchestrator v7, eval v9) | Upgrade to v8 / v10 — **one** `cp:eval` full-run |
| `micro_saas_evaluation` + `portfolio_manager_micro` | Replaced by `fit_and_decide` |
| Studio 10-stage path | Frozen — [legacy-studio.md](legacy-studio.md) |
| MSFI v2 (7 components) | MSFI-lite (3 components) — [msfi_calculator.py](../scripts/msfi_calculator.py) |
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
| Eval partial run while `status: evaluating` | Stale staged eval docs or agent used v7 | Upgrade to v10; one cp:eval should reach `decided` |
| Merged mid-pipeline | Ignored QA warn | Wait for `decided`; never merge on mid-pipeline warn |
| QA on empty PR open | PR opened trigger on CP — QA | Remove PR opened; push-only on CP — QA |
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

Run after merging v3-lite to `master` and reconfiguring Cursor automations.

### Prerequisites

1. Merge v3-lite PR to `master`.
2. **CP — Eval**: label `cp:eval` only; instructions → `automation-eval-v10.md`.
3. **CP — Intake**: PR opened + optional `cp:intake`; instructions → `automation-intake-v8.md`.
4. **CP — QA**: push to PR only; instructions → `automation-qa-v6.md`.
5. Sync labels: `gh label list | grep cp:` shows `cp:intake`, `cp:eval`, `cp:review`.

### Steps (new smoke)

```bash
git checkout master && git pull
git push origin --delete opp/pipeline 2>/dev/null || true
git checkout -b opp/pipeline master
git commit --allow-empty -m "chore: open pipeline PR for automation run"
git push -u origin opp/pipeline
```

1. Open PR from `opp/pipeline` → `master`.
2. PR body:

```markdown
## Intake

**Title:** Pipeline smoke test v3-lite full-run
**Owner:** studio-team
**Tags:** smoke-test

### Description

Minimal smoke — Intake on PR open, single cp:eval → decided. Safe to kill after verification.
```

3. Wait for **Intake Complete**.
4. Add label `cp:eval` **once**.
5. Wait for **Pipeline Run Summary**: `Mode: full-run`, `Remaining stages: none`, `decided`.
6. **CP — QA** pass or warn on Eval push.

```bash
git push origin --delete opp/pipeline
```

### Smoke verification matrix

| Step | Action | Expected |
|------|--------|----------|
| 1 | Open PR with ## Intake | Intake runs; OPP + Discovery |
| 2 | No cp:eval before Intake done | Eval not started |
| 3 | cp:eval once after Intake | full-run → `decided` |
| 4 | `python3 scripts/validate_opportunities.py` | pass |
| 5 | CP — QA | pass or warn on Eval push only |

---

## Onboarding checklist

After configuring all four Cursor Automations, verify each item:

- [ ] `gh label list` shows `cp:intake`, `cp:eval`, and `cp:review` (or run **Sync GitHub labels** workflow)
- [ ] **CP — QA** uses `prompts/automation-qa-v6.md`; trigger **push to PR only**
- [ ] **CP — Intake** uses `prompts/automation-intake-v8.md`; triggers PR **opened** + optional `cp:intake`
- [ ] **CP — Eval** uses `prompts/automation-eval-v10.md`; trigger label `cp:eval` only
- [ ] **CP — Review** uses `prompts/automation-review-v3.md`; cron + `cp:review` on `review/**`
- [ ] GitHub Action **Validate opportunities and portfolio** passes on PR
- [ ] Smoke test: single cp:eval → `decided`; QA merge gate on decided push

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
