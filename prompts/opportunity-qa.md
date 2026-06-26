# Opportunity QA Prompt

## Current Version

**Active**: [opportunity-qa-v2.md](opportunity-qa-v2.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v2 | 2026-06-26 | active | Prompt path resolution; Final Decision confidence; example portfolio guard |
| v1 | 2026-06-25 | deprecated | PR validation for opportunities/ and portfolio/ changes |

## Usage

Run when a pull request modifies files under `opportunities/` or `portfolio/`.

Typical invocation:

1. Read [AGENTS.md](../AGENTS.md)
2. Execute [opportunity-qa-v2.md](opportunity-qa-v2.md) against the PR diff
3. Post the structured comment; block merge on **fail**

Also used by Cursor Automation **CP — QA** via [automation-qa-v2.md](automation-qa-v2.md) (see [docs/automations.md](../docs/automations.md)).

## Related

- [Score calculator](score-calculator.md)
- [Contributing PR checklist](../CONTRIBUTING.md)
- [Conventions](../CONVENTIONS.md)
