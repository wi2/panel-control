# Intake Prompt

## Current Version

**Active**: [intake-v2.md](intake-v2.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v2 | 2026-06-26 | active | Branch `opp/**`; eval auto on push |
| v1 | 2026-06-25 | deprecated | Branch `intake/**` |

## Usage

Invoke when a new startup idea enters the studio — via PR + label, manual chat, or Cursor Automation **CP — Intake**.

1. Provide title and description (and optional owner, tags, links).
2. Agent creates `opportunities/OPP-YYYYMMDD-{slug}.md` and fills Discovery.
3. Open a PR on branch `opp/{slug}`, add label `cp:intake` once (see [docs/automations.md](../docs/automations.md)).
4. After intake push, **CP — Eval** runs automatically in batches until `decided`.

Does not run validation or later stages in the intake run itself.

## Related

- [Discovery](discovery.md)
- [Pipeline orchestrator](pipeline-orchestrator.md)
- [AGENTS.md](../AGENTS.md)
- [Automations setup](../docs/automations.md)
