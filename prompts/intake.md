# Intake Prompt

## Current Version

**Active**: [intake-v3.md](intake-v3.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v3 | 2026-06-26 | active | Fixed branch `opp/pipeline`; one active OPP at a time |
| v2 | 2026-06-26 | deprecated | Wildcard `opp/**` |
| v1 | 2026-06-25 | deprecated | Branch `intake/**` |

## Usage

Invoke when a new startup idea enters the studio — via PR + label, manual chat, or Cursor Automation **CP — Intake**.

1. Create branch **`opp/pipeline`** from `master` (one idea at a time; recreate after merge).
2. Provide title and description in PR `## Intake` body (and optional owner, tags, links).
3. Add label `cp:intake` once for automation (see [docs/automations.md](../docs/automations.md)).
4. Agent creates `opportunities/OPP-YYYYMMDD-{slug}.md` and fills Discovery.
5. Push triggers **CP — Eval** automatically (batch up to 5 stages per push).

Does not run validation or later stages in the intake run itself.

## Related

- [Discovery](discovery.md)
- [Pipeline orchestrator](pipeline-orchestrator.md)
- [AGENTS.md](../AGENTS.md)
- [Automations setup](../docs/automations.md)
