# Weekly Operator Runbook

One-page checklist for panel-control operations. Full detail: [automations.md](../docs/automations.md).

## Weekly rhythm

| Day | Action |
|-----|--------|
| **Monday** | Portfolio review — CP — Review cron or `cp:review` on `review/YYYY-MM-DD` |
| **Tue–Thu** | Optional: one new idea via `opp/pipeline` if capacity allows |
| **Friday** | Refresh metrics; delete stale `opp/pipeline` branch if merged |

## Open a new pipeline PR

```bash
./scripts/open_pipeline.sh
# Then open PR with ## Intake body → CP — Intake runs
```

## After Intake Complete

1. Add label `cp:eval` **once**
2. Wait for `status: decided` + Pipeline Run Summary
3. Remove `cp:eval` label
4. Verify CP — QA + CI green — see [merge-policy.md](merge-policy.md)

## Merge checklist

- [ ] `status: decided`
- [ ] CI green (`validate-opportunities`)
- [ ] QA pass or warn-safe; warn-review scanned if BUILD_MICRO
- [ ] Portfolio row synced in `micro-saas.md`

## Post-merge

```bash
python3 scripts/update_portfolio_metrics.py
git push origin --delete opp/pipeline   # if not auto-deleted
```

## BUILD_MICRO handoff

Do **not** run vision/architecture agents in panel-control.

```bash
./scripts/bootstrap_product_repo.sh OPP-YYYYMMDD-slug slug ~/Projects/slug
```

Then continue in product repo — [build-handoff.md](build-handoff.md).

## Troubleshooting (top 3)

| Symptom | Fix |
|---------|-----|
| Eval never starts | Add `cp:eval` after Intake Complete |
| Eval re-runs on decided OPP | Remove `cp:eval` label |
| QA silent | Enable "Comment on PRs" on CP — QA |

## Related

- [roadmap.md](../docs/roadmap.md)
- [merge-policy.md](merge-policy.md)
