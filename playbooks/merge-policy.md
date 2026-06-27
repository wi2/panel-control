# Merge Policy — Control Plane PRs

Rules for merging pull requests that touch `opportunities/` or `portfolio/` in panel-control.

## Verdict matrix

| CP — QA | CI (`validate_opportunities.py`) | Merge |
|---------|----------------------------------|-------|
| **pass** | green | Allowed |
| **warn-safe** | green | Allowed |
| **warn-review** | green | Allowed after human scan (see below) |
| **fail** | any | **Blocked** |
| any | red | **Blocked** |

**Golden rule:** CI must always be green. QA warn with CI red = do not merge.

## Warn taxonomy

CP — QA should tag warnings in the PR comment:

### warn-safe — merge without review

- Legacy `startup_studio` file untouched in diff
- Missing `eval_engine` on old file not modified substantively
- Cosmetic / link fixes only

### warn-review — scan QA comment before merge (~5 min)

Required human scan when any apply:

- `decision: BUILD_MICRO` (gateway to product repo handoff)
- `confidence_level: low` on Validation or Fit and Decide
- `desk_only: true` with `MONITOR_MICRO`
- MSFI-lite 50–69 (borderline)
- `capacity_blocked: true`

For **BUILD_MICRO**: confirm live validation evidence before running [build-handoff.md](build-handoff.md).

### fail — never merge

- MSFI / hard gate / decision mismatch on `decided` OPP
- `BUILD_MICRO` + `desk_only: true`
- `decision_override` present
- Missing required sections when `status: decided`
- Portfolio row missing or inconsistent

## Mid-pipeline PRs

When `status: evaluating`, QA may warn on incomplete sections. Do not merge until `decided` unless intentionally stopping the pipeline.

## Related

- [opportunity-qa-v5.md](../prompts/opportunity-qa-v5.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
- [docs/automations.md](../docs/automations.md)
