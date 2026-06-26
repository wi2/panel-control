# Micro SaaS Portfolio

**Canonical registry** for `portfolio_strategy: solo_micro_saas`. Studio files ([active.md](active.md), [monitoring.md](monitoring.md), [archived.md](archived.md)) are legacy mirrors only.

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
3. Link to the opportunity file; ensure `## Micro SaaS Portfolio Evaluation (Wedge)` is complete.

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
| OPP-20260625-local-pricing-intelligence-artisans | FR dept 69 × climatisation | 67 | MONITOR_MICRO | 87 | 8 | 500–1000 EUR | studio-team | 2026-06-25 | 2026-07-25 | | [opportunity](../opportunities/OPP-20260625-local-pricing-intelligence-artisans.md) |
| OPP-20260625-veille-ao-pme-locales | Veille AO PME locales wedge | — | MONITOR_MICRO | — | — | 500+ EUR | studio-team | 2026-06-25 | 2026-07-25 | pending micro re-eval | [opportunity](../opportunities/OPP-20260625-veille-ao-pme-locales.md) |
| OPP-20260626-suivi-conformite-artisans-btp | Conformité échéances BTP wedge | 65 | MONITOR_MICRO | 48 | 4 | 500–1000 EUR | studio-team | 2026-06-26 | 2026-07-26 | desk-only; sprint validation | [opportunity](../opportunities/OPP-20260626-suivi-conformite-artisans-btp.md) |
| OPP-20260626-stock-consommables-electriciens-tpe | Catalogue consommables + seuils + alertes réappro — 1 département, TPE sans magasinier | 64.3 | MONITOR_MICRO | 92 | 8 | 500–900 EUR | studio-team | 2026-06-26 | 2026-07-26 | desk-only; sprint validation | [opportunity](../opportunities/OPP-20260626-stock-consommables-electriciens-tpe.md) |

## Archived (KILL_MICRO)

| ID | Wedge | MSFI | Decision | Kill reason | Decision Date | Link |
|----|-------|------|----------|-------------|---------------|------|
| OPP-20260625-detection-opportunites-linkedin | LinkedIn signal wedge | — | KILL_MICRO | platform-tos-block | 2026-06-25 | [opportunity](../opportunities/OPP-20260625-detection-opportunites-linkedin.md) |
| OPP-20260625-relance-factures-freelance | WhatsApp relance wedge | — | KILL_MICRO | mrr-below-minimum | 2026-06-25 | [opportunity](../opportunities/OPP-20260625-relance-factures-freelance.md) |

## Related

- [Micro SaaS Portfolio playbook](../playbooks/micro-saas-portfolio.md)
- [Studio monitoring portfolio](monitoring.md)
- [Kill rules](../playbooks/kill-rules.md)
