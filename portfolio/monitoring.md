# Monitoring Portfolio (MONITOR)

Opportunities with `global_score` **50–74** (or score qualifies but OQI < 70) under periodic re-evaluation.

## Instructions

When an opportunity receives a MONITOR decision:

1. Add a row to this table.
2. Set **Next Review** to 90 days from decision date.
3. Link to the opportunity file in `opportunities/`.

On review:

1. Re-run validation (minimum) and re-score; recalculate OQI.
2. Promote to [active.md](active.md) if `global_score >= 75` AND `OQI >= 70`.
3. Move to [archived.md](archived.md) if `global_score < 50` or kill trigger met.
4. Update **Next Review** date.

Capacity limit: **10 monitoring opportunities** (see [portfolio rules](../playbooks/portfolio-rules.md)).

<!-- CP — QA smoke test: remove after automation verified -->

## Entries

| ID | Title | Global Score | OQI | Decision | Owner | Decision Date | Next Review | Link |
|----|-------|--------------|-----|----------|-------|---------------|-------------|------|
| OPP-20260615-ai-invoice-parser | AI Invoice Parser for SMB Accountants | 59 | 64 | monitor | studio-team | 2026-06-25 | 2026-09-25 | [opportunity](../opportunities/_example-opportunity.md) |
| OPP-20260625-relance-factures-freelance | Relance automatique des factures impayées pour freelances | 46 | 50 | monitor | studio-team | 2026-06-25 | 2026-09-25 | [opportunity](../opportunities/OPP-20260625-relance-factures-freelance.md) |
| OPP-20260625-veille-ao-pme-locales | Veille appels d'offres ultra ciblée pour PME locales | 50 | 53 | monitor | studio-team | 2026-06-25 | 2026-09-25 | [opportunity](../opportunities/OPP-20260625-veille-ao-pme-locales.md) |
| OPP-20260625-detection-opportunites-linkedin | Agent de détection d'opportunités commerciales sur LinkedIn | 51 | 53 | monitor | studio-team | 2026-06-25 | 2026-09-25 | [opportunity](../opportunities/OPP-20260625-detection-opportunites-linkedin.md) |
| OPP-20260625-local-pricing-intelligence-artisans | AI Local Pricing Intelligence for Artisans and Contractors | 52 | 51 | monitor | studio-team | 2026-06-25 | 2026-09-25 | [opportunity](../opportunities/OPP-20260625-local-pricing-intelligence-artisans.md) — Micro SaaS: MONITOR_MICRO (MSFI 67) → [micro-saas.md](micro-saas.md) |

## Related

- [Active](active.md)
- [Archived](archived.md)
- [Micro SaaS portfolio](micro-saas.md)
- [Kill rules](../playbooks/kill-rules.md)
