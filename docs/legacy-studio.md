# Legacy Studio Path (Frozen)

The **startup_studio** evaluation path is **frozen** as of [ADR v3-lite](decisions/2026-06-simplification-v3-lite.md) (2026-06-26).

## Rules

- **No new opportunities** with `portfolio_strategy: startup_studio`.
- Existing studio-format OPP files remain **read-only** historical records.
- Active work uses **`eval_engine: v3-lite`** and `solo_micro_saas` only.

## Frozen assets

| Asset | Purpose |
|-------|---------|
| [playbooks/scoring-rules.md](../playbooks/scoring-rules.md) | 10-dimension `global_score` |
| [playbooks/opportunity-quality-index.md](../playbooks/opportunity-quality-index.md) | OQI |
| [prompts/scoring-v2.md](../prompts/scoring-v2.md) through portfolio_manager | 10-stage pipeline |
| [portfolio/active.md](../portfolio/active.md), [monitoring.md](../portfolio/monitoring.md), [archived.md](../portfolio/archived.md) | Studio registries |

## Post-BUILD (moved to product repos)

After `BUILD_MICRO`, **all product work** happens in a **separate product repository** — not in panel-control.

| Step | Where |
|------|-------|
| Bootstrap repo + copy OPP | panel-control — [playbooks/build-handoff.md](../playbooks/build-handoff.md) |
| Vision, MVP, roadmap, architecture, code | Product repo — [product-repo-conventions.md](product-repo-conventions.md) |

Prompts below are **historical reference only**. Do not invoke from panel-control agents:

- [vision-v1.md](../prompts/vision-v1.md)
- [mvp-v1.md](../prompts/mvp-v1.md)
- [roadmap-v1.md](../prompts/roadmap-v1.md)
- [architecture-v1.md](../prompts/architecture-v1.md)
- [success-contract-v1.md](../prompts/success-contract-v1.md)

Product repos define their own prompt versions in their `AGENTS.md`.

## Related

- [decisions/2026-07-control-plane-vs-product-repo.md](decisions/2026-07-control-plane-vs-product-repo.md)
- [portfolio-strategy.md](portfolio-strategy.md)
- [evaluation-process.md](../playbooks/evaluation-process.md)
