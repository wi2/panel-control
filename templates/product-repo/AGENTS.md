# Product Repository — Agent Instructions

You operate inside a **product repository** bootstrapped from panel-control. You **build** the product — you do not re-run opportunity evaluation.

**Source decision:** [docs/SOURCE-OPP.md](docs/SOURCE-OPP.md) (snapshot from panel-control).

ADR (panel-control): control-plane vs product-repo boundary.

## Pipeline (product repo only)

```text
SOURCE-OPP → Vision → MVP → Roadmap → Architecture → Success Contract → Code
```

| Stage | Agent role | Output | Human gate before next |
|-------|------------|--------|------------------------|
| 1 | Product Vision | `docs/VISION.md` | Yes |
| 2 | MVP Scope | `docs/MVP.md` | Yes |
| 3 | Roadmap | `docs/ROADMAP.md` | Yes |
| 4 | Technical | `docs/ARCHITECTURE.md` | Yes |
| 5 | Success Contract | `docs/SUCCESS-CONTRACT.md` | Yes — required before code |
| 6 | Code | `src/` | Per PR |

Run **one stage at a time**. Do not skip Success Contract before writing feature code.

## Default stack

Next.js 15 App Router, TypeScript, Tailwind — see panel-control ADR `2026-07-product-stack-nextjs.md`. Override only in `docs/ARCHITECTURE.md` with documented rationale.

## Inputs

- `docs/SOURCE-OPP.md` — full opportunity report (Discovery, Validation, Fit and Decide, Final Decision)
- Completed prior stage docs in `docs/`

## Rules

- Do not modify `docs/SOURCE-OPP.md` — it is an immutable handoff snapshot
- Scope code to `docs/MVP.md` "Scope In" only
- Success Contract defines measurable 30/60/90 day criteria — code must serve those metrics
- No product code in panel-control; no eval pipeline in this repo

## Automations

Configure Cursor automations **in this repo** (not in panel-control). Suggested pattern: one label per stage, same as panel-control eval staged model.

## Related

- Panel-control handoff: `playbooks/build-handoff.md` (in panel-control repo)
- Conventions: `docs/product-repo-conventions.md` (in panel-control repo)
