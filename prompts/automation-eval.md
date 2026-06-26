# Automation Eval Wrapper

## Current Version

**Active**: [automation-eval-v4.md](automation-eval-v4.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v4 | 2026-06-26 | active | Active OPP resolution; catalogue `decided` from `master` OK on `opp/pipeline` |
| v3 | 2026-06-26 | deprecated | Fixed branch `opp/pipeline`; counted all OPP files (broken with master catalogue) |
| v2 | 2026-06-26 | deprecated | Wildcard `opp/**` — not supported by Cursor UI |
| v1 | 2026-06-25 | deprecated | Label `cp:eval` + branch `eval/OPP-*`; one stage per run |

## Usage

Used exclusively by Cursor Automation **CP — Eval** (see [docs/automations.md](../docs/automations.md)).

1. Use branch **`opp/pipeline`** (fixed studio branch; one active OPP at a time).
2. Branch may contain catalogue of `decided` OPP files from `master`.
3. **Push** to `opp/pipeline` — no label. Cursor trigger: **new push to branch** `opp/pipeline`.
4. Agent resolves the single **active** OPP (`draft` or `evaluating`) and delegates to [pipeline-orchestrator-v2.md](pipeline-orchestrator-v2.md) — up to 5 stages per push until `decided`.

## Related

- [Pipeline orchestrator](pipeline-orchestrator.md)
- [AGENTS.md](../AGENTS.md)
