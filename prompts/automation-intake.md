# Automation Intake Wrapper

## Current Version

**Active**: [automation-intake-v2.md](automation-intake-v2.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v2 | 2026-06-26 | active | Branch `opp/**`; same PR as eval; push triggers eval batch |
| v1 | 2026-06-25 | deprecated | Branch `intake/**`; separate from eval |

## Usage

Used exclusively by Cursor Automation **CP — Intake** (see [docs/automations.md](../docs/automations.md)).

1. Open PR from branch `opp/{slug}` with `## Intake` section in the PR body.
2. Add label `cp:intake` once.
3. Agent delegates to [intake-v2.md](intake-v2.md). Push after intake triggers **CP — Eval** automatically.

## Related

- [Intake](intake.md)
- [AGENTS.md](../AGENTS.md)
