---
version: 3
stage: automation_review
status: active
created: 2026-06-26
supersedes: automation-review-v2
changelog: "portfolio-review-runner-v3; solo only"
---

# Automation Review Wrapper v3

## Role

Thin wrapper for **CP — Review**.

## Objective

Execute [portfolio-review-runner-v3.md](portfolio-review-runner-v3.md). Max 3 MONITOR_MICRO per run. Open PR for changes.

## Trigger

Cron Monday 09:00 + label `cp:review` on `review/**`.

## Related

- Previous: [automation-review-v2.md](automation-review-v2.md)
