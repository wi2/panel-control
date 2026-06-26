# ADR: Control Plane Simplification v3-lite

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-06-26 |
| **Branch** | `feat/v3-lite-simplification` |
| **Authors** | studio |

## Context

The control plane grew a dual-strategy model: `solo_micro_saas` (4-stage fast path) and `startup_studio` (10-stage legacy with OQI and `global_score`). In practice:

- Default thesis is **solo founder, ~20 AI micro-apps** — not venture studio economics.
- Documentation drifted (README, `prompts/README.md`, QA defaults) between strategies.
- ~91 prompt files; opportunity template ~450 lines with studio sections N/A for solo path.
- MSFI v2 used 7 LLM-judged components; validation relied on agent QA, not deterministic CI.
- Staged eval (`cp:eval` × 3) added operational friction for ~1 idea/week throughput.

## Decision

Adopt **eval engine v3-lite** as the sole active path:

1. **Pipeline** — 3 content stages after intake:
   - Discovery (intake)
   - Validation
   - Fit and Decide (hard gates + MSFI-lite + final decision + portfolio sync)

2. **Automation** — **full-run**: one `cp:eval` after intake runs validation + fit_and_decide → `status: decided`.

3. **Metrics** — MSFI-lite (3 components, Python-calculated):
   - `speed_score` 40% — time to revenue + automation
   - `economics_score` 35% — pricing, maintenance, MRR headroom
   - `reach_score` 25% — acquisition + competition in wedge

   Hard gates unchanged (6 gates). CI fails on MSFI/gate/decision mismatch when `status: decided`.

4. **Studio path frozen** — `startup_studio`, OQI, `global_score`, studio portfolio files are **read-only legacy**. No new opportunities with `portfolio_strategy != solo_micro_saas`. See [legacy-studio.md](../legacy-studio.md).

5. **Portfolio KPIs** — lightweight dashboard in [metrics/portfolio.md](../../metrics/portfolio.md).

6. **Prompt consolidation** — `fit-and-decide-v1` supersedes `micro_saas_evaluation` + `portfolio_manager_micro` on the active path. Deprecated prompt files retained for reproducibility.

## Consequences

### Positive

- Less agent confusion (one strategy, one template, one eval run).
- Deterministic MSFI/gate checks in CI.
- Faster pipeline: Intake → 1× `cp:eval` → merge.
- Smaller opportunity documents.

### Negative

- New venture-scale evaluations require manual legacy doc or migration.
- Existing studio-format OPP files remain valid but are not the template for new work.
- Cursor automations must be reconfigured after merge (Eval v10, QA v6, Intake v8, Review v3).

### Migration

| Asset | Action |
|-------|--------|
| Existing `decided` studio OPPs | Keep as-is; read-only reference |
| New OPPs | `eval_engine: v3-lite`, `portfolio_strategy: solo_micro_saas` only |
| `opp/pipeline` | Recreate from `master` after merge |
| Automations | Update wrapper prompt paths per [automations.md](../automations.md) |

## References

- [portfolio-strategy.md](../portfolio-strategy.md)
- [micro-saas-portfolio.md](../../playbooks/micro-saas-portfolio.md)
- [evaluation-process.md](../../playbooks/evaluation-process.md)
- [legacy-studio.md](../legacy-studio.md)
