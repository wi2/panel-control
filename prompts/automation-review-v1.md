---
version: 1
stage: automation_review
status: deprecated
created: 2026-06-25
superseded_by: automation-review-v2
changelog: "Portfolio review wrapper for Cursor Automation CP — Review"
---

# Automation Review Wrapper v1

## Role

Thin wrapper for the **CP — Review** Cursor Automation. Re-evaluates due MONITOR and BUILD portfolio entries.

## Objective

Delegate to [portfolio-review-runner-v1.md](portfolio-review-runner-v1.md) after identifying trigger mode.

## Trigger modes

| Mode | When | Branch |
|------|------|--------|
| **Cron** | Scheduled run (Monday 09:00) | Create or use `review/YYYY-MM-DD` |
| **Label** | Label **`cp:review`** added on PR | PR head branch must match `review/**` |

If label mode and branch does not match `review/**` → STOP with NOOP comment.

If cron mode and no entries due → output `NOOP: no portfolio entries due for review` and stop.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [portfolio-review-runner-v1.md](portfolio-review-runner-v1.md) using today's date (ISO 8601).
3. Process at most **3 MONITOR** opportunities per run; queue the remainder.
4. Apply [score-calculator-v1.md](score-calculator-v1.md) and [kill-rules.md](../playbooks/kill-rules.md) before updating frontmatter.
5. Sync portfolio files if decisions change.
6. Create or update `reviews/REVIEW-YYYY-QN.md` when warranted per portfolio-review-runner-v1.
7. Commit to `review/YYYY-MM-DD` branch; open or update a pull request if not already on one.
8. Post **Portfolio Review Run** summary from portfolio-review-runner-v1 output format.
9. Do **not** run QA in this automation — **CP — QA** runs separately on push.

## Constraints

- Never push directly to the default branch.
- Do not edit `prompts/*` or `playbooks/*`.

## Related

- [Portfolio review runner](portfolio-review-runner-v1.md)
- [Automations setup](../docs/automations.md)
