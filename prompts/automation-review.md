# Automation Review Wrapper

## Current Version

**Active**: [automation-review-v1.md](automation-review-v1.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v1 | 2026-06-25 | active | Portfolio review wrapper for Cursor Automation **CP — Review** |

## Usage

Used exclusively by Cursor Automation **CP — Review** (see [docs/automations.md](../docs/automations.md)).

- **Scheduled**: cron every Monday 09:00.
- **Manual**: PR from branch `review/YYYY-MM-DD` + label `cp:review`.

Delegates to [portfolio-review-runner-v1.md](portfolio-review-runner-v1.md).

## Related

- [Portfolio review runner](portfolio-review-runner.md)
- [AGENTS.md](../AGENTS.md)
