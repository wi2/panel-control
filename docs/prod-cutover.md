# Production Cutover

Bootstrap for **eval engine v3-lite**. ADR: [decisions/2026-06-simplification-v3-lite.md](decisions/2026-06-simplification-v3-lite.md).

## Expected state

| Path | State |
|------|-------|
| `opportunities/` | Example only until first real intake |
| `portfolio/micro-saas.md` | Empty tables |
| `metrics/portfolio.md` | Initial KPI template |
| Legacy studio portfolio files | Frozen, empty |

## First real opportunity

```text
1. Recreate opp/pipeline from master
2. Open PR + ## Intake → CP — Intake
3. Add cp:eval once → full-run → decided
4. Merge when CP — QA pass/warn
5. python3 scripts/update_portfolio_metrics.py
6. Delete opp/pipeline; reconfigure Cursor automations to v8/v10/v6/v3
```

## Post-merge

- Remove `cp:eval` label
- Verify micro-saas.md row
- Delete `opp/pipeline`

## Prod-ready checklist

- [x] v3-lite prompts and scripts merged
- [x] Boundary ADR + build handoff + product template
- [ ] Cursor automations updated per [automations.md](automations.md)
- [ ] First OPP through full-run pipeline — [smoke-test.md](smoke-test.md)

## BUILD_MICRO handoff

When an OPP reaches `BUILD_MICRO`, use [playbooks/build-handoff.md](../playbooks/build-handoff.md) — not agents in this repo.

## Related

- [automations.md](automations.md)
- [roadmap.md](roadmap.md)
- [AGENTS.md](../AGENTS.md)
