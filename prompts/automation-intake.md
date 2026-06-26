# Automation Intake Wrapper

## Current Version

**Active**: [automation-intake-v5.md](automation-intake-v5.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v5 | 2026-06-26 | active | Delegates to intake-v5 (solo_micro_saas default) |
| v4 | 2026-06-26 | deprecated | Allow `decided` catalogue; block only when active OPP exists |
| v3 | 2026-06-26 | deprecated | Required zero OPP files total |
| v2 | 2026-06-26 | deprecated | Wildcard `opp/**` |
| v1 | 2026-06-25 | deprecated | Branch `intake/**` |

## Usage

Used exclusively by Cursor Automation **CP — Intake** (see [docs/automations.md](../docs/automations.md)).

1. Create branch **`opp/pipeline`** from `master` (recreate after each merged idea).
2. Open PR with `## Intake` section in the PR body.
3. Add label `cp:intake` once (allowed when no active OPP on branch; catalogue `decided` OK).
4. Agent delegates to [intake-v5.md](intake-v5.md). Push triggers **CP — Eval** on `opp/pipeline`.

## Related

- [Intake](intake.md)
- [AGENTS.md](../AGENTS.md)
