# Portfolio Review Runner Prompt

## Current Version

**Active**: [portfolio-review-runner-v1.md](portfolio-review-runner-v1.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v1 | 2026-06-25 | active | Scheduled MONITOR and BUILD portfolio review |

## Usage

Run on a schedule (weekly cron) or on explicit request when portfolio entries are due for review.

1. Read today's date and portfolio files.
2. Process due MONITOR entries (max 3 per run): re-validate, re-score, re-decide.
3. Process due BUILD entries: Success Contract check.
4. Optionally create `reviews/REVIEW-{YYYY}-Q{N}.md`.

Used by Cursor Automation **Control Plane — MONITOR Review** (see [docs/automations.md](../docs/automations.md)).

## Related

- [Portfolio rules](../playbooks/portfolio-rules.md)
- [Kill rules](../playbooks/kill-rules.md)
- [Reviews](../reviews/README.md)
- [AGENTS.md](../AGENTS.md)
