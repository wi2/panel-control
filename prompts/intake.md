# Intake Prompt

## Current Version

**Active**: [intake-v1.md](intake-v1.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v1 | 2026-06-25 | active | Create OPP file and run Discovery from raw idea |

## Usage

Invoke when a new startup idea enters the studio — via webhook, manual chat, or Cursor Automation **Control Plane — Intake**.

1. Provide title and description (and optional owner, tags, links).
2. Agent creates `opportunities/OPP-YYYYMMDD-{slug}.md` and fills Discovery.
3. Open a PR on branch `intake/OPP-...` for review.

Does not run validation or later stages. Next step: [pipeline-orchestrator.md](pipeline-orchestrator.md) or manual validation.

## Related

- [Discovery](discovery.md)
- [AGENTS.md](../AGENTS.md)
- [Automations setup](../docs/automations.md)
