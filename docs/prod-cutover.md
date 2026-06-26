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
- [ ] Cursor automations updated per [automations.md](automations.md)
- [ ] First real OPP through full-run pipeline

## Related

- [automations.md](automations.md)
- [AGENTS.md](../AGENTS.md)
