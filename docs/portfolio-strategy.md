# Portfolio Strategy

Canonical operating thesis. Every opportunity uses **`eval_engine: v3-lite`** and **`portfolio_strategy: solo_micro_saas`**.

ADR: [decisions/2026-06-simplification-v3-lite.md](decisions/2026-06-simplification-v3-lite.md).

## Default strategy

```yaml
eval_engine: v3-lite
portfolio_strategy: solo_micro_saas
```

**Thesis:** ~20 AI micro-apps as **solo founder**, low operational overhead.

## Target operating model

| Parameter | Value |
|-----------|-------|
| Concurrent BUILD_MICRO | 3 max |
| Active MONITOR_MICRO | 5 max |
| Total maintenance budget | ≤ 40 h/mo |
| Per-product maintenance | ≤ 10 h/mo |
| Per-product build (MVP wedge) | ≤ 100 h |

## Pipeline

```text
discovery → validation → fit_and_decide
```

## Supported strategies

| Value | Status | Registry |
|-------|--------|----------|
| `solo_micro_saas` | **Active (only)** | [portfolio/micro-saas.md](../portfolio/micro-saas.md) |
| `startup_studio` | **Frozen** | [legacy-studio.md](legacy-studio.md) |
| `vc_moonshot`, `cashflow_business` | **Removed** | — |

## Related

- [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md)
- [metrics/portfolio.md](../metrics/portfolio.md)
