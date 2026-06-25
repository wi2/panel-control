# Micro SaaS Portfolio

Opportunities evaluated under the [Micro SaaS Portfolio](../playbooks/micro-saas-portfolio.md) lens — solo-operated wedges targeting €1–10 k MRR in 12 months with ≤100 h build and ≤10 h/mo maintenance.

This registry is **independent** of the studio Control Plane decisions in [active.md](active.md), [monitoring.md](monitoring.md), and [archived.md](archived.md).

## Instructions

When a wedge receives a Micro SaaS decision:

1. Add a row to the appropriate table below.
2. Set **Next Review** to 30 days from decision date for MONITOR_MICRO and BUILD_MICRO.
3. Link to the opportunity file; ensure `## Micro SaaS Portfolio Evaluation (Wedge)` is complete.

On review:

1. Re-run wedge validation experiments (minimum).
2. Recalculate MSFI and hard-gates.
3. Promote to Active if MSFI ≥ 70 and validation sprint passed.
4. Move to Archived if KILL_MICRO triggered.

## Decision Thresholds

| Decision | Criteria |
|----------|----------|
| **BUILD_MICRO** | 3/3 hard-gates PASS AND MSFI ≥ 70 |
| **MONITOR_MICRO** | Hard-gates PASS AND MSFI 50–69 |
| **KILL_MICRO** | ≥1 hard-gate FAIL OR MSFI < 50 |

## Active (BUILD_MICRO)

| ID | Wedge | MSFI | Build h | Maint h/mo | MRR target 12m | Owner | Decision Date | Next Review | Link |
|----|-------|------|---------|------------|----------------|-------|---------------|-------------|------|

_No entries._

## Monitoring (MONITOR_MICRO)

| ID | Wedge | MSFI | Build h | Maint h/mo | MRR target 12m | Owner | Decision Date | Next Review | Link |
|----|-------|------|---------|------------|----------------|-------|---------------|-------------|------|
| OPP-20260625-local-pricing-intelligence-artisans | FR dept 69 × climatisation (PrixMétier) | 67 | 87 | 8 | 500–1000 EUR | studio-team | 2026-06-25 | 2026-07-25 | [opportunity](../opportunities/OPP-20260625-local-pricing-intelligence-artisans.md) |

## Archived (KILL_MICRO)

| ID | Wedge | MSFI | Kill reason | Decision Date | Link |
|----|-------|------|-------------|---------------|------|

_No entries._

## Related

- [Micro SaaS Portfolio playbook](../playbooks/micro-saas-portfolio.md)
- [Studio monitoring portfolio](monitoring.md)
- [Kill rules](../playbooks/kill-rules.md)
