# Automation Eval Wrapper

## Current Version

**Active**: [automation-eval-v1.md](automation-eval-v1.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v1 | 2026-06-25 | active | Pipeline +1 wrapper for Cursor Automation **CP — Eval** |

## Usage

Used exclusively by Cursor Automation **CP — Eval** (see [docs/automations.md](../docs/automations.md)).

1. Open PR from branch `eval/OPP-YYYYMMDD-slug`.
2. Ensure `opportunities/OPP-YYYYMMDD-slug.md` exists on the branch.
3. Add label `cp:eval`.
4. Agent delegates to [pipeline-orchestrator-v1.md](pipeline-orchestrator-v1.md) — one stage per run.

## Related

- [Pipeline orchestrator](pipeline-orchestrator.md)
- [AGENTS.md](../AGENTS.md)
