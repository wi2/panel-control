# Cursor Automations

Operational setup for the AI Startup Studio Brain control plane with [Cursor Automations](https://cursor.com/docs).

See [AGENTS.md](../AGENTS.md) for agent operating rules shared by all automations below.

## Architecture

Four automations — one job each, thin wrapper → versioned prompt:

```text
CP — QA      (read-only)  → prompts/automation-qa-v5.md       → opportunity-qa-v4
CP — Intake  (write)      → prompts/automation-intake-v7.md   → intake-v6
CP — Eval    (write)      → prompts/automation-eval-v9.md     → pipeline-orchestrator-v7
CP — Review  (write)      → prompts/automation-review-v2.md   → portfolio-review-runner-v2
```

**Studio branch**: fixed name **`opp/pipeline`** — one **active** opportunity (`draft` / `evaluating`) at a time. Catalogue of `decided` OPP files from `master` may coexist on the branch. **Intake** on PR opened (or label `cp:intake`); **`cp:eval`** staged — **one stage per label**, re-add until `decided`.

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
- After **Intake Complete**, add `cp:eval` — **one stage per run**; re-add after each staged summary until `Remaining stages: none` and `status: decided` (solo: typically 3×).
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
8. label cp:eval → validation → re-add → micro_saas → re-add → portfolio_manager → decided
9. Push after each stage → CP — QA (warn mid-pipeline OK; merge gate on decided push)
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

Execute prompts/automation-qa-v5.md against this pull request.
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

Execute prompts/automation-intake-v7.md against this pull request.
Commit and push to opp/pipeline. Do not push to master.
```

### Expected output

New file under `opportunities/`, Discovery section filled, `intake_complete: true`, **Intake Complete** summary. Push triggers **CP — QA** (push only) — add label **`cp:eval`** to start **validation** (staged path).

---

## CP — Eval

Runs **one pipeline stage** per label **`cp:eval`** (staged eval).

| Setting | Value |
|---------|-------|
| **Name** | CP — Eval |
| **Description** | Staged pipeline on opp/pipeline — one stage per cp:eval until decided |
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

Execute prompts/automation-eval-v9.md against this pull request.
Commit and push to opp/pipeline. Staged eval — one stage per invocation; re-add cp:eval until decided. Do not push to master.
```

### Expected output

**Pipeline Run Summary** with `Mode: staged`. Mid-pipeline: `Remaining stages: {list}` + instruction to **re-add `cp:eval`**. Final run: `Remaining stages: none`, `status: decided`. **Do not merge** while `status: evaluating`. **CP — QA** runs on push. Remove `cp:eval` after `decided`.

### Cursor setup (required)

1. Open automation **CP — Eval**.
2. **Remove** trigger **New push to branch** (if present).
3. **Add** trigger: **Label change** → label **`cp:eval`**.
4. Repo: `wi2/panel-control`.
5. Paste agent instructions above.
6. Save.

### Cursor reconfig (v7/v9)

After merging prompt updates, reconfigure Cursor automations:

| Automation | Trigger | Instructions file |
|------------|---------|-------------------|
| **CP — Intake** | PR **opened** + label `cp:intake` (optional) | `prompts/automation-intake-v7.md` |
| **CP — Eval** | Label `cp:eval` (not push) | `prompts/automation-eval-v9.md` |
| **CP — QA** | Push to PR only (**remove** PR opened) | `prompts/automation-qa-v5.md` |
| **CP — Review** | Cron + label `cp:review` | `prompts/automation-review-v2.md` |

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

Execute prompts/automation-review-v2.md.
Process at most 3 MONITOR_MICRO opportunities per run (solo_micro_saas registry).
Open a pull request for any file changes. Do not push to master.
```

---

## End-to-end flow

```text
opp/pipeline → empty commit → PR + ## Intake → Intake (PR opened)
  → Intake Complete → push → QA (push)
  → cp:eval (staged) → validation → re-add → micro_saas → re-add → manager → decided
  → QA on each push; merge gate on decided push only
  → merge → delete opp/pipeline → next idea
```

---

## Migration

| Legacy | Action |
|--------|--------|
| `intake/**`, `eval/OPP-*`, `opp/{slug}` | Use `opp/pipeline` only |
| CP — Eval push trigger on `opp/pipeline` | **Remove** — use label `cp:eval` only |
| `automation-eval-v8`, `pipeline-orchestrator-v6` | Upgrade to v9 / v7 (staged eval) |
| `automation-intake-v6`, `automation-qa-v4` | Upgrade to v7 / v5 |
| Eval full-run v6/v8 partial confusion | Use v7/v9 staged contract; re-add `cp:eval` until `decided` |
| `automation-review-v1`, `portfolio-review-runner-v1` | Upgrade to v2 — micro-saas registry, MSFI, 30-day cadence |
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
| Eval partial run (`Remaining stages` ≠ none) while `status: evaluating` | Expected under **staged v7/v9** — re-add `cp:eval` | Do not merge until `Remaining stages: none` |
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

Run after merging v7/v9 prompts to `master` and reconfiguring Cursor automations.

### Prerequisites

1. Merge docs PR to `master`.
2. **CP — Eval**: label `cp:eval` only; instructions → `automation-eval-v9.md`.
3. **CP — Intake**: PR opened + optional `cp:intake`; instructions → `automation-intake-v7.md`.
4. **CP — QA**: push to PR only (**no** PR opened); instructions → `automation-qa-v5.md`.
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

**Title:** Pipeline smoke test v7 staged
**Owner:** studio-team
**Tags:** smoke-test

### Description

Minimal smoke test — Intake on PR open, staged cp:eval (3× solo) → decided. Safe to kill after verification.
```

3. Wait for **Intake Complete** (PR opened trigger) — no `cp:intake` required.
4. **No QA** on PR open alone (empty commit only).
5. Add label `cp:eval` — re-add after each staged summary until `decided` (solo: 3×).
6. Wait for final **Pipeline Run Summary**: `Mode: staged`, `Remaining stages: none`, `decided`.
7. **CP — QA** on Intake push and Eval push (pass or warn).
8. After verification: merge or close, then:

```bash
git push origin --delete opp/pipeline
```

### Smoke verification matrix

| Step | Action | Expected |
|------|--------|----------|
| 1 | Open PR with ## Intake | Intake runs; OPP + Discovery |
| 2 | No cp:eval before Intake done | Eval not started |
| 3 | cp:eval staged after Intake | 3× solo (or N studio) → `decided`; mid-pipeline QA warn OK |
| 4 | `python3 scripts/validate_opportunities.py` | pass |
| 5 | CP — QA | pass or warn on Eval push only |

---

## Onboarding checklist

After configuring all four Cursor Automations, verify each item:

- [ ] `gh label list` shows `cp:intake`, `cp:eval`, and `cp:review` (or run **Sync GitHub labels** workflow)
- [ ] **CP — QA** uses `prompts/automation-qa-v5.md`; trigger **push to PR only** (no PR opened)
- [ ] **CP — Intake** uses `prompts/automation-intake-v7.md`; triggers PR **opened** + optional label `cp:intake`
- [ ] **CP — Eval** uses `prompts/automation-eval-v9.md`; trigger label `cp:eval` only (**no push trigger**)
- [ ] **CP — Review** uses `prompts/automation-review-v1.md`; cron + `cp:review` on `review/**`
- [ ] GitHub Action **Validate opportunities and portfolio** passes on PR
- [ ] Smoke test: staged cp:eval → `decided`; QA merge gate only on decided push

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
