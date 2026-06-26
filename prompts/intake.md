# Intake Prompt

## Current Version

**Active**: [intake-v6.md](intake-v6.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v6 | 2026-06-26 | active | `intake_complete` marker; handoff via label `cp:eval` |
| v5 | 2026-06-26 | deprecated | Default solo_micro_saas; fast-path prompt_versions |
| v4 | 2026-06-26 | deprecated | Catalogue `decided` coexists; one active OPP per run |
| v3 | 2026-06-26 | deprecated | Fixed branch `opp/pipeline`; zero OPP gate |
| v2 | 2026-06-26 | deprecated | Wildcard `opp/**` |
| v1 | 2026-06-25 | deprecated | Branch `intake/**` |

## Usage

Invoke when a new startup idea enters the studio — via PR + label, manual chat, or Cursor Automation **CP — Intake**.

1. Create branch **`opp/pipeline`** from `master` (one active idea at a time; recreate after merge).
2. Provide title and description in PR `## Intake` body (and optional owner, tags, links).
3. Add label `cp:intake` once for automation (see [docs/automations.md](../docs/automations.md)).
4. Agent creates `opportunities/OPP-YYYYMMDD-{slug}.md`, fills Discovery, sets `intake_complete: true`.
5. Add label **`cp:eval`** to run **CP — Eval** (full pipeline in one run).

Does not run validation or later stages in the intake run itself.

## Related

- [Discovery](discovery.md)
- [Pipeline orchestrator](pipeline-orchestrator.md)
- [AGENTS.md](../AGENTS.md)
- [Automations setup](../docs/automations.md)
