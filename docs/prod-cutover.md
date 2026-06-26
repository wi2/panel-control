# Production Cutover

Bootstrap procedure for running the AI Startup Studio Brain control plane in production. This repository evaluates and manages opportunities — it does **not** ship customer-facing product code.

## Expected repository state (prod)

| Path | Prod state |
|------|------------|
| [`opportunities/`](../opportunities/) | No live `OPP-*.md` until first real intake; keep [`README.md`](../opportunities/README.md) and [`_example-opportunity.md`](../opportunities/_example-opportunity.md) |
| [`portfolio/micro-saas.md`](../portfolio/micro-saas.md) | Empty Active / Monitoring / Archived tables (canonical registry for `solo_micro_saas`) |
| [`portfolio/active.md`](../portfolio/active.md), [`monitoring.md`](../portfolio/monitoring.md), [`archived.md`](../portfolio/archived.md) | Empty Entries tables (legacy `startup_studio` mirrors) |
| [`reviews/`](../reviews/) | Empty until first portfolio review run |
| [`prompts/`](../prompts/), [`playbooks/`](../playbooks/) | Unchanged — versioned evaluation engine |
| [`scripts/validate_opportunities.py`](../scripts/validate_opportunities.py) | CI validation on PR and `master` |

Pipeline test fixtures (smoke-test OPP files used to validate Intake → Eval → QA) are removed at cutover. They are not part of the production portfolio.

## What is not in this repo

- Application code (SaaS products, landing pages, concierge tools)
- Customer data or production secrets
- Product repositories — build those in separate repos after `BUILD_MICRO` / `build` decisions

## First real opportunity

After cutover, evaluate new ideas via the automated pipeline on branch **`opp/pipeline`**. Full setup: [automations.md](automations.md).

```text
1. git checkout master && git pull
2. git push origin --delete opp/pipeline   # if exists
3. git checkout -b opp/pipeline master
4. git commit --allow-empty -m "chore: open pipeline PR for automation run"
5. git push -u origin opp/pipeline
6. Open PR opp/pipeline → master with ## Intake body (Title, Owner, Tags, Description)
7. CP — Intake runs on PR opened → Discovery + intake_complete: true
8. Push → CP — QA
9. Add label cp:eval — one stage per run (solo_micro_saas: typically validation → micro_saas_evaluation → portfolio_manager_micro)
10. Re-add cp:eval after each staged summary until status: decided
11. Merge when latest CP — QA = pass or warn on decided push only
12. Post-merge checklist below
13. Repeat from step 1 for the next idea
```

Default strategy for new opportunities: `portfolio_strategy: solo_micro_saas` ([portfolio-strategy.md](portfolio-strategy.md)).

## Post-merge checklist

After merging a decided opportunity PR:

- [ ] Remove label **`cp:eval`** from the PR (if still present) to avoid re-triggers
- [ ] Verify opportunity row appears in the correct [`portfolio/micro-saas.md`](../portfolio/micro-saas.md) table (or legacy studio file if `startup_studio`)
- [ ] Confirm latest **CP — QA** comment is **pass** or **warn** on the **decided** push — not mid-pipeline warn
- [ ] Delete remote branch: `git push origin --delete opp/pipeline`
- [ ] Recreate `opp/pipeline` from `master` only when starting the next intake

## Maintenance loop (post-decision)

Scheduled and on-demand portfolio reviews use **CP — Review** ([automations.md](automations.md)):

- Registry: [`portfolio/micro-saas.md`](../portfolio/micro-saas.md) for `solo_micro_saas`
- Cadence: **30 days** for MONITOR_MICRO and BUILD_MICRO
- Trigger: cron (Monday 09:00) or label **`cp:review`** on branch `review/**`
- Artifacts: [`reviews/REVIEW-YYYY-QN.md`](../reviews/README.md) when warranted

## Prod-ready checklist

Track cutover and prod-readiness steps:

- [ ] Test OPP fixtures removed from `opportunities/`
- [ ] Portfolio registries reset (empty tables)
- [ ] CP — Review v2 active (`portfolio-review-runner-v2`, `automation-review-v2`)
- [ ] [`validate_opportunities.py`](../scripts/validate_opportunities.py) includes portfolio registry checks
- [ ] Cursor automations configured per [automations.md](automations.md)
- [ ] GitHub labels synced ([`.github/labels.yml`](../.github/labels.yml))
- [ ] First real opportunity evaluated through full pipeline

## Related

- [Automations setup](automations.md)
- [AGENTS.md](../AGENTS.md)
- [Evaluation process](../playbooks/evaluation-process.md)
- [Micro SaaS portfolio](../playbooks/micro-saas-portfolio.md)
