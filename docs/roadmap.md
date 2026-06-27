# Roadmap — panel-control

Operational roadmap for the **decision-only** control plane. Product development happens in separate repos per [ADR control-plane vs product-repo](decisions/2026-07-control-plane-vs-product-repo.md).

**Last updated:** 2026-06-27

## Vision

```text
panel-control  →  decide (BUILD / MONITOR / KILL)
product repo   →  build (vision → docs → code)
```

## Epic status

| Epic | Status | Goal |
|------|--------|------|
| 0 — Ops Go-Live | done | Cursor automations + smoke test (PR #17) |
| 1 — Governance | in progress | ADR, roadmap, merge policy |
| 2 — Reliability | pending | Branch protection, runbook |
| 3 — Portfolio Ops | pending | First review, metrics hygiene |
| 4 — Build Handoff | in progress | Bootstrap script + product template |
| 5 — First Product MVP | pending | In product repo, not here |
| 6 — Continuous | backlog | PyYAML, legacy archive |

---

## Epic 0 — Ops Go-Live

**Goal:** pipeline `Intake → cp:eval → decided` reliable.

| Story | Status | Deliverable |
|-------|--------|-------------|
| 0.1 Reconfigure Cursor automations (v8/v10/v6/v3) | done | [prod-cutover.md](prod-cutover.md) checked |
| 0.2 Smoke test end-to-end | done | [smoke-test.md](smoke-test.md) — PR #17 |
| 0.3 Fix doc drift | done | labels.yml, deprecated wrappers |

---

## Epic 1 — Governance

**Goal:** durable docs for long-term operation.

| Story | Status | Deliverable |
|-------|--------|-------------|
| 1.1 Roadmap | done | this file |
| 1.2 Merge policy | done | [playbooks/merge-policy.md](../playbooks/merge-policy.md) |
| 1.3 ADR stack Next.js | done | [decisions/2026-07-product-stack-nextjs.md](decisions/2026-07-product-stack-nextjs.md) |
| 1.4 ADR control vs product repo | done | [decisions/2026-07-control-plane-vs-product-repo.md](decisions/2026-07-control-plane-vs-product-repo.md) |
| 1.5 Prompts index | pending | [prompts/README.md](../prompts/README.md) deprecated table |

---

## Epic 2 — Reliability

| Story | Status | Deliverable |
|-------|--------|-------------|
| 2.1 Branch protection master | pending | GitHub settings |
| 2.2 Weekly runbook | done | [runbook-weekly.md](runbook-weekly.md) |
| 2.3 open_pipeline.sh | done | [scripts/open_pipeline.sh](../scripts/open_pipeline.sh) |

---

## Epic 3 — Portfolio Ops

| Story | Status | Deliverable |
|-------|--------|-------------|
| 3.1 First CP — Review | pending | `reviews/REVIEW-2026-Q3.md` |
| 3.2 Metrics refresh process | pending | runbook + CONTRIBUTING |

---

## Epic 4 — Build Handoff (panel-control scope only)

**Goal:** bootstrap product repo + copy OPP. **No post-BUILD agents here.**

| Story | Status | Deliverable |
|-------|--------|-------------|
| 4.1 build-handoff playbook | done | [playbooks/build-handoff.md](../playbooks/build-handoff.md) |
| 4.2 Product template | done | [templates/product-repo/](../templates/product-repo/) |
| 4.3 bootstrap_product_repo.sh | done | [scripts/bootstrap_product_repo.sh](../scripts/bootstrap_product_repo.sh) |
| 4.4 Product repo agents | pending | Configure in first product repo after bootstrap |

**Explicitly out of scope for panel-control:** CP — Build-Prep, vision/mvp agents, product CI beyond handoff script.

---

## Epic 5 — First Product MVP

Runs entirely in the **product repo** after Epic 4 handoff. See product repo `AGENTS.md`.

---

## Epic 6 — Backlog

- PyYAML frontmatter parser in CI scripts
- Move studio prompts to `prompts/legacy/`
- MSFI component rubric (partial deterministic scoring)
- Config verification checklist automation

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-27 | Initial roadmap; boundary ADR; removed CP Build-Prep from panel-control scope |

## Related

- [automations.md](automations.md)
- [prod-cutover.md](prod-cutover.md)
- [product-repo-conventions.md](product-repo-conventions.md)
