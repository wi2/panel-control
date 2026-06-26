# Automation Eval Wrapper

## Current Version

**Active**: [automation-eval-v2.md](automation-eval-v2.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v2 | 2026-06-26 | active | Push-triggered on `opp/**`; batch up to 5 stages; no `cp:eval` label |
| v1 | 2026-06-25 | deprecated | Label `cp:eval` + branch `eval/OPP-*`; one stage per run |

## Usage

Used exclusively by Cursor Automation **CP — Eval** (see [docs/automations.md](../docs/automations.md)).

1. Use branch `opp/**` with an existing `opportunities/OPP-*.md` (typically after **CP — Intake** on the same PR).
2. **Push** to the PR — no label required.
3. Agent delegates to [pipeline-orchestrator-v2.md](pipeline-orchestrator-v2.md) — up to 5 stages per push until `decided`.

## Related

- [Pipeline orchestrator](pipeline-orchestrator.md)
- [AGENTS.md](../AGENTS.md)
