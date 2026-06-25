# Micro SaaS Portfolio

Secondary evaluation lens for opportunities scoped as **solo-operated, low-maintenance SaaS wedges**. Complements the standard Control Plane decision path (`global_score`, OQI) without replacing it.

Use when the target operating model is:

| Constraint | Target |
|------------|--------|
| MRR horizon | €1–10 k/mo within 12 months |
| Maintenance | ≤ 10 h/mo at M6 |
| Initial build | ≤ 100 h MVP |
| Team | 1 person (no mandatory hire) |
| Automation | Maximize; avoid recurring manual ops |
| Horizon | 12 months to revenue signal |

The **full platform vision** of an opportunity may fail Micro SaaS gates while a **reduced wedge** passes. Evaluate the wedge only — do not score the platform scope against Micro SaaS criteria.

## Relationship to Control Plane

| Lens | Scope | Primary scores | Portfolio file |
|------|-------|----------------|----------------|
| Control Plane | Full opportunity | `global_score`, OQI | active / monitoring / archived |
| Micro SaaS Portfolio | Wedge only | `msfi`, hard-gates | [`portfolio/micro-saas.md`](../portfolio/micro-saas.md) |

Both decisions are recorded in the opportunity file. They may diverge (e.g. studio MONITOR + Micro SaaS MONITOR_MICRO).

## Hard Gates (PASS / FAIL)

All three must **PASS** for BUILD_MICRO or MONITOR_MICRO. Any **FAIL** → **KILL_MICRO** unless explicitly overridden with documented rationale.

| Gate | Threshold | Measurement |
|------|-----------|-------------|
| `build_hours` | ≤ 100 h | Estimated MVP build for one person, including seed data and deploy |
| `maintenance_hours` | ≤ 10 h/mo at M6 | Amortized support, ops, content, data refresh, billing admin |
| `solo_operable` | Yes | No mandatory hire for product, support, or distribution in first 12 months |

### Borderline gates

If a gate is within 10% of threshold (e.g. 105 h build, 11 h/mo maintenance), document as **borderline** — default decision is **MONITOR_MICRO** with remediation plan, not BUILD_MICRO.

## Micro SaaS Fit Index (MSFI)

Scale: **0–100**. Measures wedge fit for the solo Micro SaaS operating model.

### Formula

```text
MSFI = 0.25 × mrr_path_score
     + 0.25 × automation_score
     + 0.20 × build_feasibility_score
     + 0.15 × maintenance_sustainability_score
     + 0.15 × distribution_solo_score
```

### Components

| Component | Range | Definition |
|-----------|-------|------------|
| `mrr_path_score` | 0–100 | Likelihood of reaching **€1 k MRR** within 12 months via wedge scope; bonus if credible path to €10 k |
| `automation_score` | 0–100 | Share of operations automatable without recurring human intervention (billing, delivery, data refresh) |
| `build_feasibility_score` | 0–100 | `100 - max(0, (estimated_build_hours - 80) × 2)`, capped 0–100 |
| `maintenance_sustainability_score` | 0–100 | `100 - max(0, (estimated_monthly_hours - 8) × 10)`, capped 0–100 |
| `distribution_solo_score` | 0–100 | Organic SEO, community, or product-led growth reachable without outbound sales team |

### MRR path scoring guide

| Score | Criteria |
|-------|----------|
| 80–100 | €1 k MRR in ≤6 mo plausible; €10 k path visible with wedge alone |
| 60–79 | €1 k MRR in 12 mo plausible; €10 k requires expansion beyond wedge |
| 40–59 | €500–1 k MRR in 12 mo; €10 k improbable solo |
| 20–39 | <€500 MRR in 12 mo likely |
| 0–19 | No credible monetization path at wedge ARPU |

## Decision Thresholds

| Decision | Criteria | Portfolio file |
|----------|----------|----------------|
| **BUILD_MICRO** | 3/3 hard-gates PASS **AND** MSFI ≥ 70 | [`portfolio/micro-saas.md`](../portfolio/micro-saas.md) — Active |
| **MONITOR_MICRO** | Hard-gates PASS **AND** MSFI 50–69, **OR** 1 borderline gate with remediation plan | [`portfolio/micro-saas.md`](../portfolio/micro-saas.md) — Monitoring |
| **KILL_MICRO** | ≥1 hard-gate FAIL **OR** MSFI < 50 | [`portfolio/micro-saas.md`](../portfolio/micro-saas.md) — Archived |

Review cadence: **MONITOR_MICRO** every **30 days** during validation sprint; **BUILD_MICRO** every **30 days** for first 6 months.

## Opportunity File Requirements

Add to opportunity frontmatter:

```yaml
micro_saas:
  decision: build_micro | monitor_micro | kill_micro
  msfi: null
  build_hours_estimate: null
  maintenance_hours_estimate: null
  mrr_target_12m: ""
  wedge: ""
```

Add section `## Micro SaaS Portfolio Evaluation (Wedge)` with:

- Wedge definition (scope IN / OUT)
- Hard-gate summary
- MSFI breakdown with calculation
- MRR model (12 months)
- Build and maintenance hour budgets
- Micro SaaS risks
- Validation sprint (typically 30 days)
- Micro SaaS decision and next actions
- Note excluding full platform from Micro SaaS scope

Tag opportunities: `micro-saas`

## Validation Sprint (MONITOR_MICRO)

Default 30-day sprint before BUILD_MICRO promotion:

| # | Experiment | Success criteria |
|---|------------|------------------|
| 1 | Landing + waitlist | Target waitlist size (e.g. 100 emails) |
| 2 | Problem interviews | ≥4/5 confirm wedge pain |
| 3 | Concierge / manual delivery | ≥70% usefulness rating |
| 4 | Seed data feasibility | Data research within build budget hours |

Kill wedge if: zero waitlist signal after outreach; ≥3/5 say incumbents sufficient; seed data research exceeds 15 h for initial wedge.

## Recording in Portfolio

Registry format in [`portfolio/micro-saas.md`](../portfolio/micro-saas.md):

```markdown
| ID | Wedge | MSFI | Decision | Build h | Maint h/mo | MRR target 12m | Owner | Decision Date | Next Review | Link |
```

## Related

- [Maintenance evaluation](maintenance-evaluation.md)
- [Scoring rules](scoring-rules.md)
- [Kill rules](kill-rules.md)
- [Portfolio rules](portfolio-rules.md)
