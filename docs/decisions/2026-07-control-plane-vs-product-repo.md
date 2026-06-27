# ADR: Control Plane vs Product Repository

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-06-27 |
| **Authors** | studio |
| **Supersedes** | — |

## Context

The panel-control repository (`wi2/panel-control`) orchestrates opportunity evaluation and portfolio decisions. Post-BUILD work (product vision, technical documentation, application code) requires a different lifecycle, tooling, and agent set.

Prior studio-era prompts (`vision`, `mvp`, `architecture`, etc.) lived in panel-control. That blurred the boundary between **deciding** and **building**.

## Decision

### panel-control — decision only

**Scope:** evaluate ideas, record decisions, manage portfolio.

| In scope | Out of scope |
|----------|--------------|
| Discovery, Validation, Fit and Decide | Product vision, MVP scope, roadmap |
| BUILD_MICRO / MONITOR_MICRO / KILL_MICRO | Application code, product CI/CD |
| Portfolio registry (`portfolio/micro-saas.md`) | Technical architecture docs |
| Agents: CP — Intake, Eval, QA, Review | Agents: Vision, Tech, Code |
| Handoff: bootstrap product repo + copy OPP report | Post-BUILD staged automations |

**Pipeline terminus:** `status: decided` on an opportunity file. No agent in panel-control runs after this point except portfolio review.

### Product repository — one repo per BUILD_MICRO

**Scope:** transform a validated decision into a shippable product.

| Agent (in product repo) | Output | Order |
|-------------------------|--------|-------|
| Product Vision | `docs/VISION.md` | 1 |
| MVP Scope | `docs/MVP.md` | 2 |
| Roadmap | `docs/ROADMAP.md` | 3 |
| Technical | `docs/ARCHITECTURE.md` | 4 |
| Success Contract | `docs/SUCCESS-CONTRACT.md` | 5 |
| Code | `src/` | 6 (after human gate) |

Each agent runs in the **product repo** with its own prompts, automations, and `AGENTS.md`. One stage at a time; human review between stages.

### Handoff contract

When `decision: BUILD_MICRO` is recorded:

1. Operator runs [scripts/bootstrap_product_repo.sh](../../scripts/bootstrap_product_repo.sh) from panel-control.
2. Script creates the product repo from [templates/product-repo/](../../templates/product-repo/).
3. Script copies the source OPP to `docs/SOURCE-OPP.md` in the product repo.
4. Operator works exclusively in the product repo from this point.

**Source of truth for the decision:** `opportunities/OPP-*.md` in panel-control (immutable after merge). Product repo holds a **snapshot** at bootstrap time.

### Legacy prompts in panel-control

Prompts under `prompts/vision-v1.md`, `mvp-v1.md`, etc. are **historical reference only**. New BUILD work must not invoke them from panel-control. Product repos define their own prompt versions.

## Consequences

### Positive

- Clear mental model: panel-control = portfolio brain; product repo = factory.
- Independent agent evolution per product without polluting the control plane.
- Product repos can use product-specific stacks (default Next.js per [2026-07-product-stack-nextjs.md](2026-07-product-stack-nextjs.md)).

### Negative

- Two repos to maintain per product.
- Handoff is manual (bootstrap script) until product-repo automations are mature.

### Explicitly rejected

- **CP — Build-Prep** automations in panel-control — post-BUILD agents belong in product repos.
- Full-run post-BUILD (vision → code in one agent invocation).
- BUILD preparation sections inside opportunity files beyond a link to the product repo.

## References

- [2026-06-simplification-v3-lite.md](2026-06-simplification-v3-lite.md)
- [2026-07-product-stack-nextjs.md](2026-07-product-stack-nextjs.md)
- [playbooks/build-handoff.md](../../playbooks/build-handoff.md)
- [docs/product-repo-conventions.md](../product-repo-conventions.md)
