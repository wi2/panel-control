# Micro SaaS Portfolio

**Canonical registry** for `portfolio_strategy: solo_micro_saas`.

> Legacy studio files ([active.md](active.md), [monitoring.md](monitoring.md), [archived.md](archived.md)) are **frozen** — see [legacy-studio.md](../docs/legacy-studio.md).

## Capacity (solo_micro_saas)

| Parameter | Limit |
|-----------|-------|
| Concurrent BUILD_MICRO | 3 |
| MONITOR_MICRO active | 5 |
| Total maintenance (Active BUILD) | ≤ 40 h/mo |
| Portfolio target (cumulative) | 20 products |

When capacity blocked: `decision: MONITOR_MICRO`, `capacity_blocked: true`.

Opportunities evaluated under the [Micro SaaS Portfolio](../playbooks/micro-saas-portfolio.md) lens — solo-operated wedges targeting €500–10 k MRR/mo with ≤100 h build and ≤10 h/mo maintenance.

## Instructions

When a wedge receives a Micro SaaS decision:

1. Add a row to the appropriate table below.
2. Set **Next Review** to 30 days from decision date for MONITOR_MICRO and BUILD_MICRO.
3. Link to the opportunity file; ensure `## Fit and Decide` is complete.

On review:

1. Re-run wedge validation experiments (minimum).
2. Recalculate MSFI and hard-gates.
3. Promote to Active if MSFI ≥ 70 and validation sprint passed.
4. Move to Archived if KILL_MICRO triggered.

## Decision Thresholds

| Decision | Criteria |
|----------|----------|
| **BUILD_MICRO** | All hard gates PASS + MSFI ≥ 70 + live validation |
| **MONITOR_MICRO** | Hard gates PASS + MSFI 50–69, borderline gate, or capacity_blocked |
| **KILL_MICRO** | Hard gate FAIL OR MSFI < 50 |

## Active (BUILD_MICRO)

| ID | Wedge | MSFI | Decision | Build h | Maint h/mo | MRR target 12m | Owner | Decision Date | Next Review | Notes | Link |
|----|-------|------|----------|---------|------------|----------------|-------|---------------|-------------|-------|------|

_No entries._

## Monitoring (MONITOR_MICRO)

| ID | Wedge | MSFI | Decision | Build h | Maint h/mo | MRR target 12m | Owner | Decision Date | Next Review | Notes | Link |
|----|-------|------|----------|---------|------------|----------------|-------|---------------|-------------|-------|------|
| OPP-20260626-coachbrief | CSV → weekly roster digest for solo endurance coaches | 63.5 | MONITOR_MICRO | 68 | 5 | €980/mo | studio-team | 2026-06-26 | 2026-07-26 | Desk-only; run interview + concierge sprint before BUILD | [OPP](../opportunities/OPP-20260626-coachbrief.md) |
| OPP-20260626-offre-alert | Multi-source AO digest (3–10 alerts) for local trade SMEs | 52.7 | MONITOR_MICRO | 88 | 8 | €1 500/mo | studio-team | 2026-06-27 | 2026-07-27 | Desk-only; AlertOffres overlap — prove differentiation before BUILD | [OPP](../opportunities/OPP-20260626-offre-alert.md) |
| OPP-20260627-renew-desk | AI PDF → notice-period alerts + shared renewal calendar for FR SMEs | 51.4 | MONITOR_MICRO | 78 | 7 | €900/mo | studio-team | 2026-06-27 | 2026-07-27 | Desk-only; TACIT overlap — prove accountant/compliance wedge before BUILD | [OPP](../opportunities/OPP-20260627-renew-desk.md) |

## Archived (KILL_MICRO)

| ID | Wedge | MSFI | Decision | Kill reason | Decision Date | Link |
|----|-------|------|----------|-------------|---------------|------|

_No entries._

## Related

- [Micro SaaS Portfolio playbook](../playbooks/micro-saas-portfolio.md)
- [Studio monitoring portfolio](monitoring.md)
- [Kill rules](../playbooks/kill-rules.md)
