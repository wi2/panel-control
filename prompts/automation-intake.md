# Automation Intake Wrapper

## Current Version

**Active**: [automation-intake-v6.md](automation-intake-v6.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v6 | 2026-06-26 | active | intake_complete marker; cp:eval handoff; no eval on push |
| v5 | 2026-06-26 | deprecated | Delegates to intake-v5 (solo_micro_saas default) |
| v4 | 2026-06-26 | deprecated | Allow `decided` catalogue; block only when active OPP exists |
| v3 | 2026-06-26 | deprecated | Required zero OPP files total |
| v2 | 2026-06-26 | deprecated | Wildcard `opp/**` |
| v1 | 2026-06-25 | deprecated | Branch `intake/**` |

## Usage

Used exclusively by Cursor Automation **CP — Intake** (see [docs/automations.md](../docs/automations.md)).

1. Create branch **`opp/pipeline`** from `master` (recreate after each merged idea).
2. Open PR with `## Intake` section in the PR body.
3. Add label `cp:intake` once (allowed when no active OPP on branch; catalogue `decided` OK).
4. Agent delegates to [intake-v6.md](intake-v6.md). Push triggers **CP — QA** only.
5. Add label **`cp:eval`** to start **CP — Eval** (full pipeline run).

## Related

- [Intake](intake.md)
- [AGENTS.md](../AGENTS.md)
