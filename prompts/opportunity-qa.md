# Opportunity QA Prompt

## Current Version

**Active**: [opportunity-qa-v1.md](opportunity-qa-v1.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v1 | 2026-06-25 | active | PR validation for opportunities/ and portfolio/ changes |

## Usage

Run when a pull request modifies files under `opportunities/` or `portfolio/`.

Typical invocation:

1. Read [AGENTS.md](../AGENTS.md)
2. Execute [opportunity-qa-v1.md](opportunity-qa-v1.md) against the PR diff
3. Post the structured comment; block merge on **fail**

Also used by Cursor Automation **CP — QA** via [automation-qa-v1.md](automation-qa-v1.md) (see [docs/automations.md](../docs/automations.md)).

## Related

- [Score calculator](score-calculator.md)
- [Contributing PR checklist](../CONTRIBUTING.md)
- [Conventions](../CONVENTIONS.md)
