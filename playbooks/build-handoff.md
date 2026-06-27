# Build Handoff — panel-control → Product Repo

Transition a **BUILD_MICRO** decision from the control plane to a dedicated product repository.

ADR: [docs/decisions/2026-07-control-plane-vs-product-repo.md](../docs/decisions/2026-07-control-plane-vs-product-repo.md).

## Prerequisites

- OPP `status: decided` with `decision: BUILD_MICRO`
- Live validation (not desk-only)
- BUILD capacity available (< 3 active BUILD_MICRO in portfolio)
- CP — QA pass/warn + CI green on the decided merge

## What panel-control does (this repo only)

1. **Record decision** — already done via Fit and Decide + portfolio sync.
2. **Bootstrap product repo** — run the script below.
3. **Stop** — no vision, architecture, or code agents run here.

## Handoff steps

### 1. Bootstrap the product repository

From panel-control root:

```bash
./scripts/bootstrap_product_repo.sh OPP-20260626-coachbrief coachbrief ~/Projects/coachbrief
```

The script:

- Validates the OPP file exists and is `BUILD_MICRO`
- Copies [templates/product-repo/](../templates/product-repo/) to the target path
- Writes `docs/SOURCE-OPP.md` (snapshot of the opportunity report)
- Fills `README.md` with OPP metadata (id, wedge, MSFI, link back to panel-control)

### 2. Initialize git and remote (operator)

```bash
cd ~/Projects/coachbrief
git init
gh repo create wi2/coachbrief --private --source=. --remote=origin
git add -A && git commit -m "chore: bootstrap from panel-control OPP-20260626-coachbrief"
git push -u origin main
```

Adjust org/name as needed.

### 3. Continue in the product repo

All post-BUILD work happens in the product repo. Read its `AGENTS.md`.

**Agent order (product repo):**

```text
docs/SOURCE-OPP.md
  → Agent Vision      → docs/VISION.md
  → Agent MVP         → docs/MVP.md
  → Agent Roadmap     → docs/ROADMAP.md
  → Agent Technical   → docs/ARCHITECTURE.md
  → Agent Contract    → docs/SUCCESS-CONTRACT.md
  → [human gate]
  → Agent Code        → src/
```

Human review required between each agent stage. Do not start code before SUCCESS-CONTRACT is approved.

### 4. Update portfolio (panel-control)

Add product repo URL to the BUILD_MICRO row in [portfolio/micro-saas.md](../portfolio/micro-saas.md) Notes column.

## What NOT to do

- Do not run `vision-v1`, `mvp-v1`, etc. prompts from panel-control (legacy reference only).
- Do not add CP — Build-Prep automations to panel-control.
- Do not add BUILD preparation sections to the OPP file after bootstrap.

## Related

- [docs/product-repo-conventions.md](../docs/product-repo-conventions.md)
- [evaluation-process.md](evaluation-process.md)
- [legacy-studio.md](../docs/legacy-studio.md) — frozen prompts
