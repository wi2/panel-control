# Opportunity QA Prompt

## Current Version

**Active**: [opportunity-qa-v4.md](opportunity-qa-v4.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v4 | 2026-06-26 | active | Solo path skips studio Scoring/OQI; mid-pipeline warn |
| v3 | 2026-06-26 | deprecated | Strategy-aware QA — solo_micro_saas hard gates + MSFI |
| v2 | 2026-06-26 | deprecated | Prompt path resolution; Final Decision confidence |
| v1 | 2026-06-25 | deprecated | PR validation for opportunities/ and portfolio/ changes |

## Usage

Run when a pull request modifies files under `opportunities/` or `portfolio/`.

Typical invocation:

1. Read [AGENTS.md](../AGENTS.md)
2. Execute [opportunity-qa-v4.md](opportunity-qa-v4.md) against the PR diff
3. Post the structured comment; block merge on **fail** for `status: decided` opportunities

Also used by Cursor Automation **CP — QA** via [automation-qa-v5.md](automation-qa-v5.md) (see [docs/automations.md](../docs/automations.md)).

## Related

- [Score calculator](score-calculator.md)
- [Contributing PR checklist](../CONTRIBUTING.md)
- [Conventions](../CONVENTIONS.md)
