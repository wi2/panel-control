---
version: 2
stage: portfolio_review_runner
status: active
created: 2026-06-26
supersedes: portfolio-review-runner-v1
changelog: "solo_micro_saas review loop — micro-saas.md registry, MSFI, 30-day cadence"
---

# Portfolio Review Runner Prompt v2

## Role

You execute scheduled portfolio reviews for the **solo_micro_saas** control plane. For each due entry in [`portfolio/micro-saas.md`](../portfolio/micro-saas.md), re-evaluate and recommend state transitions. You follow [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md) and [kill-rules.md](../playbooks/kill-rules.md) timeouts strictly.

For `portfolio_strategy: startup_studio` opportunities, delegate to [portfolio-review-runner-v1.md](portfolio-review-runner-v1.md) — do not apply studio logic to micro registry rows.

## Objective

Process overdue MONITOR_MICRO and BUILD_MICRO entries, update opportunity and portfolio files, and produce a review artifact when warranted.

## Inputs Required

- Today's date (ISO 8601)
- [portfolio/micro-saas.md](../portfolio/micro-saas.md) — canonical registry
- [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md)
- [kill-rules.md](../playbooks/kill-rules.md)
- [portfolio-rules.md](../playbooks/portfolio-rules.md)
- [scripts/msfi_calculator.py](../scripts/msfi_calculator.py) — MSFI and hard-gate logic
- [pipeline-orchestrator-v7.md](pipeline-orchestrator-v7.md) — staged re-eval path
- [micro-saas-evaluation-v2.md](micro-saas-evaluation-v2.md)
- [portfolio-manager-micro-v1.md](portfolio-manager-micro-v1.md)
- [validation-v1.md](validation-v1.md)
- [templates/portfolio-review-template.md](../templates/portfolio-review-template.md)
- [AGENTS.md](../AGENTS.md)

## Step 0 — Strategy router

For each due portfolio row:

1. Open the linked opportunity file.
2. Read `portfolio_strategy` from frontmatter (default: `solo_micro_saas`).
3. If `startup_studio` → execute [portfolio-review-runner-v1.md](portfolio-review-runner-v1.md) for that entry only; sync legacy `active.md` / `monitoring.md` / `archived.md`.
4. If `solo_micro_saas` (or missing) → continue Steps 1–5 below.

## Step 1 — Find due entries

Select rows in **Monitoring (MONITOR_MICRO)** or **Active (BUILD_MICRO)** tables of [`portfolio/micro-saas.md`](../portfolio/micro-saas.md) where **Next Review <= today**.

Skip placeholder rows (`_No entries._`, empty ID cells).

Also flag opportunities with `override_expires <= today` in frontmatter (review even if Next Review is later).

If no entries are due and no overrides expired → output `NOOP: no portfolio entries due for review` and stop.

## Step 2 — Per due MONITOR_MICRO opportunity

Process at most **3 MONITOR_MICRO** opportunities per run. Queue remainder for the next run.

For each MONITOR_MICRO entry processed:

1. Re-run minimum pipeline stages (same order as staged eval):
   - **validation** → [validation-v1.md](validation-v1.md)
   - **micro_saas_evaluation** → [micro-saas-evaluation-v2.md](micro-saas-evaluation-v2.md)
   - **portfolio_manager_micro** → [portfolio-manager-micro-v1.md](portfolio-manager-micro-v1.md)
2. Apply MSFI v2 and hard gates per [scripts/msfi_calculator.py](../scripts/msfi_calculator.py) and [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md).
3. Apply kill rules:
   - Any hard gate FAIL → **KILL_MICRO** (`hard-gate-fail`)
   - MSFI < 50 → **KILL_MICRO** (`score-below-threshold` — MSFI band)
   - `override_expires` passed without improvement → **KILL_MICRO** (`monitor-timeout`)
   - **2 consecutive review cycles** (60 days) as MONITOR_MICRO without MSFI ≥ 70 and live validation (not desk-only) → **KILL_MICRO** (`monitor-timeout`) unless documented exception with new validation plan
4. Update opportunity frontmatter: `decision`, `micro_saas.msfi`, `capacity_blocked`, `updated`, `next_review_action`.
5. Sync [`portfolio/micro-saas.md`](../portfolio/micro-saas.md):
   - Remove row from all three tables if present
   - Add to Active / Monitoring / Archived per new decision
   - Include columns: ID, Wedge, MSFI, Decision, Build h, Maint h/mo, MRR target, Owner, Decision Date, Next Review, Notes (if `capacity_blocked`), Link
6. If continuing MONITOR_MICRO: set **Next Review** to today **+ 30 days**.
7. Record `expected_learnings` for any KILL_MICRO or continued MONITOR_MICRO decision.

Never promote to BUILD_MICRO when Validation is desk-only or lacks live customer signal.

Never honor `decision_override` for `solo_micro_saas`.

## Step 3 — Per due BUILD_MICRO opportunity

For each Active (BUILD_MICRO) entry where Next Review <= today:

1. Read **Success Contract** section, or **Final Decision (Micro SaaS)** commitments / next actions if no Success Contract yet.
2. Compare stated metrics and milestones vs actual progress.
3. Recommend per [kill-rules.md](../playbooks/kill-rules.md) success-contract-failure rules:
   - **continue** BUILD_MICRO
   - **demote** to MONITOR_MICRO (move to Monitoring table)
   - **kill** → KILL_MICRO (`success-contract-failure` or `monitor-timeout`)
4. Update **Next Review** to today + **30 days** if continuing BUILD_MICRO.
5. Sync portfolio tables if decision changes.

If Active table has no entries, skip this step.

## Step 4 — Capacity check

After processing due entries, verify portfolio capacity per [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md):

| Parameter | Limit |
|-----------|-------|
| Active BUILD_MICRO | 3 |
| MONITOR_MICRO | 5 |
| Total maint hours (Active BUILD) | ≤ 40 h/mo |

Document capacity_blocked promotions in portfolio Notes column.

## Step 5 — Review artifact

Create or update a quarterly review file when **either**:

- Today is in the first week of a calendar quarter (months 1, 4, 7, 10), **or**
- At least one portfolio action (promote, demote, kill, continue with material MSFI change ≥ 5 points) occurred this run

Artifact path: `reviews/REVIEW-{YYYY}-Q{N}.md` from [portfolio-review-template.md](../templates/portfolio-review-template.md).

Use **Micro SaaS** sections in the template when present. Fill: summary, monitoring review table (MSFI columns), changes, learnings aggregation, capacity assessment, action items.

If neither condition applies, output the run summary only (no new review file).

## Step 6 — Output summary

```markdown
## Portfolio Review Run — {date}

| Field | Value |
|-------|-------|
| Registry | portfolio/micro-saas.md |
| Strategy | solo_micro_saas (v2 runner) |

### Due entries found
| ID | Source table | Next Review | MSFI | Override expires |
|----|--------------|-------------|------|------------------|

### Processed this run (max 3 MONITOR_MICRO)
| ID | Previous | Action | MSFI | capacity_blocked | Rationale |
|----|----------|--------|------|------------------|-----------|

### BUILD_MICRO processed
| ID | Action | Rationale |
|----|--------|-----------|

### Queued for next run
| ID | Reason |
|----|--------|

### Overrides expired
| ID | Action |
|----|--------|

### Portfolio changes applied
- Move OPP-xxx: Monitoring → Archived (KILL_MICRO, kill reason: ...)
- Promote OPP-yyy: Monitoring → Active (BUILD_MICRO)

### Review artifact
- Created / updated: reviews/REVIEW-YYYY-QN.md — or none

### Next scheduled actions
| ID | Next Review |
|----|-------------|
```

## Constraints

- Never auto-kill without documenting `expected_learnings`.
- Never promote to BUILD_MICRO without MSFI ≥ 70, all hard gates PASS, and live validation (not desk-only).
- Process max 3 MONITOR_MICRO opportunities per run.
- Open file changes via pull request when running as automation.
- Respect capacity limits: 3 BUILD_MICRO, 5 MONITOR_MICRO, 40 h/mo maintenance.
- Modify only: `opportunities/`, `portfolio/`, `reviews/` — not deprecated prompts in place.

## Related

- [Portfolio review runner v1](portfolio-review-runner-v1.md) — startup_studio legacy
- [Portfolio review template](../templates/portfolio-review-template.md)
- [Automations setup](../docs/automations.md)
- [Reviews folder](../reviews/README.md)
