# Portfolio Metrics (v3-lite)

Lightweight KPIs for the solo micro-SaaS portfolio. Update after each decided OPP merge or monthly review.

| Metric | Value | Target | Updated |
|--------|-------|--------|---------|
| OPP evaluated (all time) | 0 | — | 2026-06-26 |
| Kill rate (all time) | — | 45–65% | 2026-06-26 |
| Median days draft→decided | — | ≤ 14 | 2026-06-26 |
| BUILD_MICRO active | 0 / 3 | ≤ 3 | 2026-06-26 |
| Maint budget (active BUILD) | 0 / 40 h/mo | ≤ 40 | 2026-06-26 |
| MONITOR_MICRO active | 0 / 5 | ≤ 5 | 2026-06-26 |
| MONITOR overdue | 0 | 0 | 2026-06-26 |

## How to update

1. After merge: run `python3 scripts/update_portfolio_metrics.py`.
2. Manually fill median days and overdue MONITOR when needed.

## Related

- [ADR v3-lite](../docs/decisions/2026-06-simplification-v3-lite.md)
- [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md)
