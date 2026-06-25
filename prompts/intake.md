# Intake Prompt

## Current Version

**Active**: [intake-v1.md](intake-v1.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v1 | 2026-06-25 | active | Create OPP file and run Discovery from raw idea |

## Usage

Invoke when a new startup idea enters the studio — via PR + label, manual chat, or Cursor Automation **CP — Intake**.

1. Provide title and description (and optional owner, tags, links).
2. Agent creates `opportunities/OPP-YYYYMMDD-{slug}.md` and fills Discovery.
3. Open a PR on branch `intake/{slug}`, add label `cp:intake` for automation (see [docs/automations.md](../docs/automations.md)).

Does not run validation or later stages. Next step: [pipeline-orchestrator.md](pipeline-orchestrator.md) or manual validation.

## Related

- [Discovery](discovery.md)
- [AGENTS.md](../AGENTS.md)
- [Automations setup](../docs/automations.md)
