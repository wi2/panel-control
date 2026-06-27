# Product Repository Conventions

Each **BUILD_MICRO** product lives in its own repository. panel-control bootstraps the repo; all build agents run there.

ADR: [decisions/2026-07-control-plane-vs-product-repo.md](decisions/2026-07-control-plane-vs-product-repo.md).

## Relationship to panel-control

| panel-control | Product repo |
|---------------|--------------|
| Source OPP (`opportunities/OPP-*.md`) | Snapshot at `docs/SOURCE-OPP.md` |
| Decision + MSFI + gates | Inherited in README frontmatter block |
| Portfolio row | Product URL in Notes |
| Eval agents (Intake, Eval, QA, Review) | Product agents (Vision, MVP, Tech, Code) |

## Required structure (bootstrap template)

```text
product-repo/
├── AGENTS.md                 # Product agent operating rules
├── README.md                 # Wedge summary + link to panel-control OPP
├── docs/
│   ├── SOURCE-OPP.md         # Snapshot from panel-control (handoff input)
│   ├── VISION.md             # Agent: Product Vision
│   ├── MVP.md                # Agent: MVP Scope
│   ├── ROADMAP.md            # Agent: Roadmap
│   ├── ARCHITECTURE.md       # Agent: Technical
│   └── SUCCESS-CONTRACT.md   # Agent: Success Contract
├── src/                      # Agent: Code (Next.js default)
├── package.json
└── .github/workflows/ci.yml  # lint + typecheck + build
```

## Agent pipeline (product repo)

| Stage | Input | Output | Human gate |
|-------|-------|--------|------------|
| Vision | SOURCE-OPP.md | VISION.md | Yes |
| MVP | VISION + SOURCE-OPP Validation | MVP.md | Yes |
| Roadmap | MVP + VISION | ROADMAP.md | Yes |
| Technical | MVP + OPP constraints | ARCHITECTURE.md | Yes |
| Contract | MVP + ROADMAP | SUCCESS-CONTRACT.md | Yes — required before code |
| Code | ARCHITECTURE + MVP scope in | src/ | Per PR |

Automations (Cursor or other) are configured **in the product repo**, not in panel-control.

## Default stack

Next.js 15 — see [decisions/2026-07-product-stack-nextjs.md](decisions/2026-07-product-stack-nextjs.md).

## Naming

| Item | Pattern | Example |
|------|---------|---------|
| GitHub repo | `{slug}` or `wi2/{slug}` | `coachbrief` |
| Branch (features) | `feat/{short-desc}` | `feat/auth-wedge` |

## Related

- [playbooks/build-handoff.md](../playbooks/build-handoff.md)
- [templates/product-repo/](../templates/product-repo/)
