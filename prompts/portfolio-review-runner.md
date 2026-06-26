# Portfolio Review Runner Prompt

## Current Version

**Active**: [portfolio-review-runner-v2.md](portfolio-review-runner-v2.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v2 | 2026-06-26 | active | solo_micro_saas — micro-saas.md registry, MSFI, 30-day cadence |
| v1 | 2026-06-25 | deprecated | startup_studio — active/monitoring/archived, global_score/OQI |

## Usage

Run on a schedule (weekly cron) or on explicit request when portfolio entries are due for review.

**solo_micro_saas** (default):

1. Read today's date and [`portfolio/micro-saas.md`](../portfolio/micro-saas.md).
2. Process due MONITOR_MICRO entries (max 3 per run): re-validate → micro_saas_evaluation → portfolio_manager_micro.
3. Process due BUILD_MICRO entries: Success Contract check.
4. Optionally create `reviews/REVIEW-{YYYY}-Q{N}.md`.

**startup_studio** (legacy): use [portfolio-review-runner-v1.md](portfolio-review-runner-v1.md) via strategy router in v2.

Used by Cursor Automation **CP — Review** via [automation-review-v2.md](automation-review-v2.md) (see [docs/automations.md](../docs/automations.md)).

## Related

- [Portfolio rules](../playbooks/portfolio-rules.md)
- [Micro SaaS portfolio](../playbooks/micro-saas-portfolio.md)
- [Kill rules](../playbooks/kill-rules.md)
- [Reviews](../reviews/README.md)
- [AGENTS.md](../AGENTS.md)
