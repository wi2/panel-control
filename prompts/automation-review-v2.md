---
version: 2
stage: automation_review
status: deprecated
created: 2026-06-26
supersedes: automation-review-v1
changelog: "Portfolio review wrapper v2 — delegates to portfolio-review-runner-v2 for solo_micro_saas"
---

# Automation Review Wrapper v2

## Role

Thin wrapper for the **CP — Review** Cursor Automation. Re-evaluates due MONITOR_MICRO and BUILD_MICRO portfolio entries in [`portfolio/micro-saas.md`](../portfolio/micro-saas.md). Routes `startup_studio` entries to the legacy runner via [portfolio-review-runner-v2.md](portfolio-review-runner-v2.md) Step 0.

## Objective

Delegate to [portfolio-review-runner-v2.md](portfolio-review-runner-v2.md) after identifying trigger mode.

## Trigger modes

| Mode | When | Branch |
|------|------|--------|
| **Cron** | Scheduled run (Monday 09:00) | Create or use `review/YYYY-MM-DD` |
| **Label** | Label **`cp:review`** added on PR | PR head branch must match `review/**` |

If label mode and branch does not match `review/**` → STOP with NOOP comment.

If cron mode and no entries due → output `NOOP: no portfolio entries due for review` and stop.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [portfolio-review-runner-v2.md](portfolio-review-runner-v2.md) using today's date (ISO 8601).
3. Process at most **3 MONITOR_MICRO** opportunities per run; queue the remainder.
4. Apply MSFI and hard gates per [scripts/msfi_calculator.py](../scripts/msfi_calculator.py) and [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md) before updating frontmatter.
5. Apply [kill-rules.md](../playbooks/kill-rules.md) monitor-timeout rules (30-day cadence, 2 cycles without BUILD_MICRO qualification).
6. Sync [`portfolio/micro-saas.md`](../portfolio/micro-saas.md) (and legacy studio files only when processing `startup_studio` entries).
7. Create or update `reviews/REVIEW-YYYY-QN.md` when warranted per portfolio-review-runner-v2.
8. Commit to `review/YYYY-MM-DD` branch; open or update a pull request if not already on one.
9. Post **Portfolio Review Run** summary from portfolio-review-runner-v2 output format.
10. Do **not** run QA in this automation — **CP — QA** runs separately on push.

## Constraints

- Never push directly to the default branch.
- Modify only `opportunities/`, `portfolio/`, and `reviews/` — do not edit versioned prompts or playbooks in place.
- Never honor `decision_override` for `solo_micro_saas`.
- Never BUILD_MICRO from desk-only Validation.

## Related

- [Portfolio review runner v2](portfolio-review-runner-v2.md)
- [Portfolio review runner v1](portfolio-review-runner-v1.md) — startup_studio legacy via router
- [Automations setup](../docs/automations.md)
