# Micro SaaS Portfolio

**Primary decision engine** when `portfolio_strategy: solo_micro_saas`. Asset allocator for AI micro-businesses — not a venture startup evaluator.

Evaluate the **wedge scope** only (solo-buildable slice). Full platform vision may fail gates while a reduced wedge passes.

## Operating constraints

| Constraint | Target |
|------------|--------|
| MRR horizon | €500–10 k/mo per wedge at maturity |
| Maintenance | ≤ 10 h/mo at M6 |
| Initial build | ≤ 100 h MVP |
| Team | 1 person (no mandatory hire) |
| Automation | Maximize; avoid recurring manual ops |
| Time to revenue | Prefer ≤ 60 days to first € |

## Relationship to startup_studio

| Strategy | Pipeline | Primary decision | Registry |
|----------|----------|------------------|----------|
| `solo_micro_saas` | 4-stage fast path | BUILD_MICRO / MONITOR_MICRO / KILL_MICRO | [`portfolio/micro-saas.md`](../portfolio/micro-saas.md) |
| `startup_studio` | 10-stage path | build / monitor / kill | active / monitoring / archived |

For `solo_micro_saas`, studio `global_score` and OQI are **diagnostic only** — never gate BUILD_MICRO.

## Hard gates (absolute)

Any **FAIL** → **KILL_MICRO**. **No override** for `solo_micro_saas`.

Evaluate gates in order (fail-fast):

| # | Gate | Rule | Measurement |
|---|------|------|-------------|
| 1 | `build_hours` | ≤ 100 h | MVP wedge for one person incl. seed data and deploy |
| 2 | `maintenance_hours` | ≤ 10 h/mo at M6 | Support, ops, data refresh, billing admin |
| 3 | `solo_operable` | must be true | No mandatory hire for product, support, or distribution in 12 mo |
| 4 | `monthly_revenue_potential` | ≥ **500 €/mo** | Natural ceiling at maturity for wedge scope (not platform TAM) |
| 5 | `distribution_cost` | ≤ **7** | From `distribution_channel` cost map (see below) |
| 6 | Platform / ToS | if `platform_dependency == high` → `alternative_data_source` must be true | API, license, or compliant hybrid — not scraping-only |

### MRR potential signal

| MRR potentiel (€/mo) | Signal |
|----------------------|--------|
| < 500 | **KILL** (hard gate) |
| 500 – 2 000 | good |
| 2 000 – 10 000 | excellent |
| > 10 000 | bonus |

### Distribution channel

Frontmatter:

```yaml
distribution_channel: seo   # enum
distribution_cost: 2          # computed — do not hand-edit without rationale
```

Allowed values: `seo` | `communities` | `outbound` | `ads` | `marketplace` | `existing_audience`

| Channel | `distribution_cost` |
|---------|---------------------|
| existing_audience | 1 |
| seo | 2 |
| communities | 3 |
| marketplace | 4 |
| outbound | 8 |
| ads | 9 |

```text
IF distribution_cost > 7  →  KILL_MICRO
```

Products requiring daily cold email, LinkedIn prospecting, or permanent outbound are not passive software assets.

### ToS / platform risk (hard gate)

```text
IF tos_risk == high
AND platform_dependency == high
AND alternative_data_source == false
THEN KILL_MICRO
```

Fields: `tos_risk`, `platform_dependency`, `alternative_data_source` (documented in Micro SaaS Evaluation section).

### Borderline gates

If exactly **one** gate is within **10%** of threshold (e.g. build 108 h, maint 11 h/mo):

- Default **MONITOR_MICRO** with remediation plan (30 days)
- Not eligible for BUILD_MICRO until gate passes

Two or more borderline failures, or any hard FAIL → **KILL_MICRO**.

## MSFI-lite (v3-lite) — soft score

Hard gates filter; MSFI-lite ranks survivors. Computed in [scripts/msfi_calculator.py](../scripts/msfi_calculator.py).

```text
MSFI = 0.40 × speed_score + 0.35 × economics_score + 0.25 × reach_score
```

| Component | Definition |
|-----------|------------|
| `speed_score` | Time to revenue + automation potential (0–100) |
| `economics_score` | Pricing power, maintenance burden, MRR headroom (0–100) |
| `reach_score` | Acquisition at declared channel + wedge competition (0–100) |

Store in frontmatter: `msfi`, `speed_score`, `economics_score`, `reach_score`.

### Legacy MSFI v2

Seven-component MSFI v2 (deprecated): see git history before 2026-06-26 or [ADR v3-lite](../docs/decisions/2026-06-simplification-v3-lite.md).

## Decision thresholds

| Decision | Criteria |
|----------|----------|
| **BUILD_MICRO** | All hard gates PASS + MSFI ≥ 70 + **live validation** complete (no desk-only) |
| **MONITOR_MICRO** | All hard gates PASS + MSFI 50–69, OR 1 borderline gate with remediation |
| **KILL_MICRO** | Any hard gate FAIL OR MSFI < 50 |

### Capacity blocking

When opportunity qualifies for BUILD_MICRO but portfolio capacity is full:

```yaml
decision: MONITOR_MICRO
capacity_blocked: true
```

Never use `decision: CAPACITY_BLOCKED` as a fourth state.

Triggers:

- Sum of active BUILD_MICRO `maintenance_hours` ≥ 40 h/mo
- Active BUILD_MICRO count ≥ 3

## Validation rules

| Decision | Desk research | Live validation |
|----------|---------------|-----------------|
| MONITOR_MICRO | Allowed (`desk-only: true`, confidence low) | Not required |
| BUILD_MICRO | **Not allowed** | Required — ≥1 of: interviews, concierge, waitlist, LOI, revenue |
| KILL_MICRO | Allowed | Not required |

## Portfolio capacity (solo_micro_saas)

| Parameter | Default |
|-----------|---------|
| `max_concurrent_build_micro` | 3 |
| `max_monitor_micro` | 5 |
| `target_portfolio_size` | 20 |
| `max_total_maintenance_hours` | 40 |

Review cadence: MONITOR_MICRO every **30 days**; BUILD_MICRO every **30 days** for first 6 months.

## Opportunity frontmatter

```yaml
portfolio_strategy: solo_micro_saas
decision: null   # BUILD_MICRO | MONITOR_MICRO | KILL_MICRO
capacity_blocked: false
time_to_first_revenue_days: null
monthly_revenue_potential: null
distribution_channel: null
distribution_cost: null
micro_saas:
  decision: null
  msfi: null
  build_hours_estimate: null
  maintenance_hours_estimate: null
  mrr_target_12m: ""
  wedge: ""
```

## Validation sprint (MONITOR_MICRO)

Default 30-day sprint before BUILD_MICRO promotion:

| # | Experiment | Success criteria |
|---|------------|------------------|
| 1 | Landing + waitlist | e.g. 100 emails |
| 2 | Problem interviews | ≥4/5 confirm wedge pain |
| 3 | Concierge / manual delivery | ≥70% usefulness rating |
| 4 | Seed data feasibility | Within build budget hours |

Kill wedge if: zero waitlist after outreach; ≥3/5 say incumbents sufficient; seed data > 15 h.

## Recording in portfolio

Canonical registry: [`portfolio/micro-saas.md`](../portfolio/micro-saas.md).

## Related

- [Portfolio strategy](../docs/portfolio-strategy.md)
- [Evaluation process](evaluation-process.md)
- [Kill rules](kill-rules.md)
- [Portfolio rules](portfolio-rules.md)
- [Validation](validation.md)
