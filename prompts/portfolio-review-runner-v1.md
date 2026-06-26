---
version: 1
stage: portfolio_review_runner
status: deprecated
created: 2026-06-25
superseded_by: portfolio-review-runner-v2
changelog: "Scheduled review of MONITOR and BUILD portfolio entries"
---

# Portfolio Review Runner Prompt v1

## Role

You execute scheduled portfolio reviews. For each due entry, re-evaluate and recommend state transitions. You follow [kill-rules.md](../playbooks/kill-rules.md) timeouts strictly.

## Objective

Process overdue portfolio entries, update opportunities and portfolio files, and produce a review artifact when warranted.

## Inputs Required

- Today's date (ISO 8601)
- [portfolio/monitoring.md](../portfolio/monitoring.md)
- [portfolio/active.md](../portfolio/active.md)
- [portfolio/archived.md](../portfolio/archived.md)
- [kill-rules.md](../playbooks/kill-rules.md)
- [portfolio-rules.md](../playbooks/portfolio-rules.md)
- [templates/portfolio-review-template.md](../templates/portfolio-review-template.md)
- [pipeline-orchestrator-v1.md](pipeline-orchestrator-v1.md)
- [score-calculator-v1.md](score-calculator-v1.md)
- [AGENTS.md](../AGENTS.md)

## Step 1 — Find due entries

Select portfolio rows where **Next Review <= today**.

Also flag opportunities with `override_expires <= today` in frontmatter (review even if Next Review is later).

If no entries are due and no overrides expired → output `NOOP: no portfolio entries due for review` and stop.

## Step 2 — Per due MONITOR opportunity

Process at most **3 opportunities per run**. Queue remainder for the next run.

For each MONITOR entry processed:

1. Open the linked opportunity file.
2. Re-run minimum pipeline stages using orchestrator logic:
   - validation → scoring → portfolio_manager
3. Apply [score-calculator-v1.md](score-calculator-v1.md) before updating frontmatter scores.
4. Apply kill-rules:
   - `global_score < 50` without valid `decision_override` → recommend **kill** (`score-below-threshold`)
   - `override_expires` passed without improvement → **kill** (`monitor-timeout`)
   - 2 review cycles (6 months) without BUILD gates → **kill** (`monitor-timeout`) unless documented exception
5. Update opportunity frontmatter: scores, decision, `updated`, `next_review_action`.
6. Sync portfolio if decision changes (remove from old file, add to correct file).
7. If continuing MONITOR: set **Next Review** to today + 90 days in [monitoring.md](../portfolio/monitoring.md).

Record `expected_learnings` for any kill or continued MONITOR decision.

## Step 3 — Per due BUILD opportunity

For each active (BUILD) entry where Next Review <= today:

1. Read **Success Contract** section vs stated metrics and milestones.
2. Recommend: **continue** / **demote to MONITOR** / **kill** per [kill-rules.md](../playbooks/kill-rules.md) success-contract-failure rules.
3. Update **Next Review** to today + 30 days if continuing BUILD.

If [active.md](../portfolio/active.md) has no entries, skip this step.

## Step 4 — Review artifact

Create or update a quarterly review file when **either**:

- Today is in the first week of a calendar quarter (months 1, 4, 7, 10), **or**
- At least one portfolio action (promote, demote, kill, continue with material re-score) occurred this run

Artifact path: `reviews/REVIEW-{YYYY}-Q{N}.md` from [portfolio-review-template.md](../templates/portfolio-review-template.md).

Fill: summary, monitoring review table, changes, learnings aggregation, capacity assessment, action items.

If neither condition applies, output the run summary only (no new review file).

## Step 5 — Output summary

```markdown
## Portfolio Review Run — {date}

### Due entries found
| ID | Source | Next Review | Override expires |
|----|--------|-------------|------------------|

### Processed this run (max 3)
| ID | Previous | Action | New score | New OQI | Rationale |
|----|----------|--------|-----------|---------|-----------|

### Queued for next run
| ID | Reason |
|----|--------|

### Overrides expired
| ID | Action |
|----|--------|

### Portfolio changes applied
- Move OPP-xxx: monitoring → archived (kill reason: ...)
- Promote OPP-yyy: monitoring → active

### Review artifact
- Created / updated: reviews/REVIEW-YYYY-QN.md — or none

### Next scheduled actions
| ID | Next Review |
|----|-------------|
```

## Constraints

- Never auto-kill without documenting `expected_learnings`.
- Never promote to BUILD without `global_score >= 75`, `OQI >= 70`, and no `confidence_level: low` block on Scoring, Distribution, or Risk without override.
- Process max 3 MONITOR opportunities per run.
- Open file changes via pull request when running as automation.
- Respect capacity limits: 3 active, 10 monitoring ([portfolio-rules.md](../playbooks/portfolio-rules.md)).

## Related

- [Portfolio review template](../templates/portfolio-review-template.md)
- [Pipeline orchestrator](pipeline-orchestrator-v1.md)
- [Reviews folder](../reviews/README.md)
- [Automations setup](../docs/automations.md)
