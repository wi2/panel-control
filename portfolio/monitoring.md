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

## Entries

| ID | Title | Global Score | OQI | Decision | Owner | Decision Date | Next Review | Link |
|----|-------|--------------|-----|----------|-------|---------------|-------------|------|
| OPP-20260615-ai-invoice-parser | AI Invoice Parser for SMB Accountants | 59 | 64 | monitor | studio-team | 2026-06-25 | 2026-09-25 | [opportunity](../opportunities/_example-opportunity.md) |

## Related

- [Active](active.md)
- [Archived](archived.md)
- [Kill rules](../playbooks/kill-rules.md)
