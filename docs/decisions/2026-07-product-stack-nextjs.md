# ADR: Default Product Stack — Next.js

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-06-27 |
| **Authors** | studio |
| **Applies to** | Product repositories only (not panel-control) |

## Context

Solo micro-SaaS wedges target ≤ 100 h build, ≤ 10 h/mo maintenance, single operator. Product repos need a default stack that minimizes time-to-MVP without locking out edge cases.

## Decision

**Default stack for new product repos:**

| Layer | Default |
|-------|---------|
| Framework | Next.js 15 App Router |
| Language | TypeScript (strict) |
| UI | Tailwind CSS + shadcn/ui |
| Auth | Clerk or NextAuth.js |
| Database | Supabase Postgres or Neon |
| Deploy | Vercel |
| Billing | Stripe or Lemon Squeezy |

Bootstrap template: [templates/product-repo/](../../templates/product-repo/).

## Escape hatch criteria

Document the alternative in `docs/ARCHITECTURE.md` when any criterion applies:

| Criterion | Alternative |
|-----------|-------------|
| Build > 80 h with heavy backend/API logic | FastAPI or Hono backend + separate frontend |
| No UI — pure automation/API product | Python or Node script + cron (no Next.js) |
| Native mobile primary surface | Expo / React Native |

Escape hatch requires explicit note in product repo `docs/ARCHITECTURE.md` referencing this ADR.

## Consequences

- Product template ships Next.js scaffold.
- panel-control hard gates and MSFI do not prescribe stack — only feasibility estimates in Fit and Decide.
- Agents in product repos assume Next.js unless ARCHITECTURE.md states otherwise.

## References

- [2026-07-control-plane-vs-product-repo.md](2026-07-control-plane-vs-product-repo.md)
- [docs/product-repo-conventions.md](../product-repo-conventions.md)
