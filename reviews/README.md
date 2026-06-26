# Portfolio Reviews

Quarterly and scheduled review artifacts for the AI Startup Studio Brain control plane.

## Naming

| Pattern | Example |
|---------|---------|
| `REVIEW-{YYYY}-Q{N}.md` | `REVIEW-2026-Q3.md` |

See [CONVENTIONS.md](../CONVENTIONS.md) for naming rules.

## Template

Copy [`templates/portfolio-review-template.md`](../templates/portfolio-review-template.md) when creating a new review file. Use **Micro SaaS** sections for `solo_micro_saas` reviews.

## When reviews are created

| Trigger | Creates review file? |
|---------|---------------------|
| Quarterly portfolio review (manual) | Yes |
| [portfolio-review-runner-v2.md](../prompts/portfolio-review-runner-v2.md) — first week of Q1/Q2/Q3/Q4 | Yes |
| portfolio-review-runner — material portfolio action in run | Yes |
| Weekly cron with no due entries | No (NOOP) |

## Automated generation

The [Portfolio Review Runner](../prompts/portfolio-review-runner.md) prompt v2 (Cursor Automation **CP — Review** via [automation-review-v2.md](../prompts/automation-review-v2.md)) processes due entries from:

- **[portfolio/micro-saas.md](../portfolio/micro-saas.md)** — canonical for `solo_micro_saas` (MONITOR_MICRO / BUILD_MICRO)
- [portfolio/monitoring.md](../portfolio/monitoring.md) and [portfolio/active.md](../portfolio/active.md) — legacy `startup_studio` only (via strategy router)

Then writes or updates review artifacts here when conditions are met.

## Related

- [Contributing — Portfolio Reviews](../CONTRIBUTING.md)
- [Micro SaaS portfolio](../playbooks/micro-saas-portfolio.md)
- [Portfolio rules](../playbooks/portfolio-rules.md)
- [Kill rules](../playbooks/kill-rules.md)
