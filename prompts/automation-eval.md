# Automation Eval Wrapper

## Current Version

**Active**: [automation-eval-v3.md](automation-eval-v3.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v3 | 2026-06-26 | active | Fixed branch `opp/pipeline`; push-to-branch trigger (Cursor exact name) |
| v2 | 2026-06-26 | deprecated | Wildcard `opp/**` — not supported by Cursor UI |
| v1 | 2026-06-25 | deprecated | Label `cp:eval` + branch `eval/OPP-*`; one stage per run |

## Usage

Used exclusively by Cursor Automation **CP — Eval** (see [docs/automations.md](../docs/automations.md)).

1. Use branch **`opp/pipeline`** (fixed studio branch; one OPP at a time).
2. Ensure exactly one `opportunities/OPP-*.md` exists on the branch (after **CP — Intake**).
3. **Push** to `opp/pipeline` — no label. Cursor trigger: **new push to branch** `opp/pipeline`.
4. Agent delegates to [pipeline-orchestrator-v2.md](pipeline-orchestrator-v2.md) — up to 5 stages per push until `decided`.

## Related

- [Pipeline orchestrator](pipeline-orchestrator.md)
- [AGENTS.md](../AGENTS.md)
