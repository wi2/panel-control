# Portfolio Strategy

Canonical operating thesis for this control plane. Every opportunity declares `portfolio_strategy` in frontmatter.

## Default strategy

```yaml
portfolio_strategy: solo_micro_saas
```

**Thesis:** Build and operate a portfolio of approximately **20 AI micro-apps** as a **solo founder**, with extremely low operational overhead.

**Not optimized for:** venture-scale startups, startup studio economics, or high-touch sales motions.

**Optimized for:**

- Fast validation
- Low maintenance (≤ 10 h/mo per product at M6)
- Solo operability (no mandatory hire in first 12 months)
- Portfolio scalability (20 cumulative products over 24–36 months)
- Time leverage (automated ops, passive distribution)

## Target operating model

| Parameter | Value |
|-----------|-------|
| Concurrent BUILD_MICRO | 3 max |
| Active MONITOR_MICRO | 5 max |
| Cumulative portfolio target | 20 products |
| Total maintenance budget | ≤ 40 h/mo across active BUILD_MICRO |
| Per-product maintenance | ≤ 10 h/mo |
| Per-product build (MVP wedge) | ≤ 100 h |

**Portfolio math:** 20 products × €500/mo average MRR ≈ **€10 k/mo** portfolio revenue target. Products capped below €500/mo natural ceiling force unsustainable SKU fragmentation (60–80 products).

## Supported strategies

| Value | Status | Decision engine | Registry |
|-------|--------|-----------------|----------|
| `solo_micro_saas` | **Active (default)** | Hard gates + MSFI → BUILD_MICRO / MONITOR_MICRO / KILL_MICRO | [`portfolio/micro-saas.md`](../portfolio/micro-saas.md) |
| `startup_studio` | Active (legacy) | global_score + OQI → build / monitor / kill | active / monitoring / archived |
| `vc_moonshot` | Stub | Routes to startup_studio until implemented | — |
| `cashflow_business` | Stub | Routes to startup_studio until implemented | — |

## solo_micro_saas pipeline

```text
discovery → validation → micro_saas_evaluation → portfolio_manager_micro
```

Studio stages (scoring, distribution, moat, maintenance, risk, portfolio intelligence, scenario planning) are **skipped** on the fast path. `global_score` and OQI may be generated as optional diagnostics but **never gate** micro decisions.

## Expected decision distribution

| Decision | Expected share |
|----------|----------------|
| BUILD_MICRO | 10–20% |
| MONITOR_MICRO | 25–35% |
| KILL_MICRO | 45–65% |

## Related

- [Micro SaaS portfolio playbook](../playbooks/micro-saas-portfolio.md)
- [Evaluation process](../playbooks/evaluation-process.md)
- [Portfolio rules](../playbooks/portfolio-rules.md)
- [AGENTS.md](../AGENTS.md)
