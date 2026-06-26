# Automation Eval Wrapper

## Current Version

**Active**: [automation-eval-v8.md](automation-eval-v8.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v8 | 2026-06-26 | active | Strict full run via orchestrator v6; decided-only success |
| v7 | 2026-06-26 | deprecated | Label `cp:eval`; full pipeline run; intake_complete gate |
| v6 | 2026-06-26 | deprecated | Push-triggered; delegates to pipeline-orchestrator-v4 (5-stage batch) |
| v5 | 2026-06-26 | deprecated | Delegates to pipeline-orchestrator-v3 |
| v4 | 2026-06-26 | deprecated | Active OPP resolution; catalogue `decided` from `master` OK on `opp/pipeline` |
| v3 | 2026-06-26 | deprecated | Fixed branch `opp/pipeline`; counted all OPP files (broken with master catalogue) |
| v2 | 2026-06-26 | deprecated | Wildcard `opp/**` — not supported by Cursor UI |
| v1 | 2026-06-25 | deprecated | Label `cp:eval` + branch `eval/OPP-*`; one stage per run |

## Usage

Used exclusively by Cursor Automation **CP — Eval** (see [docs/automations.md](../docs/automations.md)).

1. Use branch **`opp/pipeline`** (fixed studio branch; one active OPP at a time).
2. Branch may contain catalogue of `decided` OPP files from `master`.
3. After **CP — Intake** completes, add label **`cp:eval`** **once** on the PR.
4. Agent resolves the single **active** OPP and delegates to [pipeline-orchestrator-v6.md](pipeline-orchestrator-v6.md) — **all remaining stages** in one run until `decided` or explicit `failed_incomplete`.
5. Remove `cp:eval` after success to avoid re-trigger.

## Related

- [Pipeline orchestrator](pipeline-orchestrator.md)
- [AGENTS.md](../AGENTS.md)
