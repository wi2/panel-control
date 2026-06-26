# Automation Intake Wrapper

## Current Version

**Active**: [automation-intake-v7.md](automation-intake-v7.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v7 | 2026-06-26 | active | PR opened + cp:intake label; anti double-run |
| v6 | 2026-06-26 | deprecated | intake_complete marker; cp:eval handoff; no eval on push |
| v5 | 2026-06-26 | deprecated | Delegates to intake-v5 (solo_micro_saas default) |
| v4 | 2026-06-26 | deprecated | Allow `decided` catalogue; block only when active OPP exists |
| v3 | 2026-06-26 | deprecated | Required zero OPP files total |
| v2 | 2026-06-26 | deprecated | Wildcard `opp/**` |
| v1 | 2026-06-25 | deprecated | Branch `intake/**` |

## Usage

Used exclusively by Cursor Automation **CP — Intake** (see [docs/automations.md](../docs/automations.md)).

1. Create branch **`opp/pipeline`** from `master` (empty commit + push).
2. Open PR with `## Intake` section in the PR body → **Intake runs on PR opened**.
3. Optional fallback: add label `cp:intake` once if PR-open trigger did not run.
4. Agent delegates to [intake-v6.md](intake-v6.md). Push triggers **CP — QA** (push only).
5. Add label **`cp:eval`** once to start **CP — Eval** (full pipeline run → `decided`).

## Related

- [Intake](intake.md)
- [AGENTS.md](../AGENTS.md)
