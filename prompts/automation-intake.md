# Automation Intake Wrapper

## Current Version

**Active**: [automation-intake-v3.md](automation-intake-v3.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v3 | 2026-06-26 | active | Fixed branch `opp/pipeline`; one OPP at a time |
| v2 | 2026-06-26 | deprecated | Wildcard `opp/**` |
| v1 | 2026-06-25 | deprecated | Branch `intake/**` |

## Usage

Used exclusively by Cursor Automation **CP — Intake** (see [docs/automations.md](../docs/automations.md)).

1. Create branch **`opp/pipeline`** from `master` (recreate after each merged idea).
2. Open PR with `## Intake` section in the PR body.
3. Add label `cp:intake` once.
4. Agent delegates to [intake-v3.md](intake-v3.md). Push triggers **CP — Eval** on `opp/pipeline`.

## Related

- [Intake](intake.md)
- [AGENTS.md](../AGENTS.md)
