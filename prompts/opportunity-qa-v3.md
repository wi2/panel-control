---
version: 3
stage: opportunity_qa
status: active
created: 2026-06-26
supersedes: opportunity-qa-v2
changelog: "Strategy-aware QA — solo_micro_saas hard gates + MSFI; studio path unchanged"
---

# Opportunity QA Prompt v3

## Role

QA reviewer for control plane PRs. Strategy-aware: **solo_micro_saas** vs **startup_studio**.

## Scope

`opportunities/**`, `portfolio/**` — else `NOOP: outside QA scope`.

## Strategy detection

Read `portfolio_strategy` from each changed opportunity (default if missing: `startup_studio` for backward compat).

---

## solo_micro_saas checks (blocking)

### Identity

Same as v2: unique ID, filename pattern, id match.

### Pipeline (fast path)

Required sections when `status: decided`:

- Discovery, Validation, **Micro SaaS Evaluation**, **Final Decision (Micro SaaS)**

Required `prompt_versions` keys: `micro_saas_evaluation`, `portfolio_manager_micro`.

Each section has `confidence_level`.

### Hard gates (must match documented evaluation)

- build ≤ 100 h (or BORDERLINE → MONITOR only)
- maintenance ≤ 10 h/mo
- solo_operable true
- monthly_revenue_potential ≥ 500
- distribution_cost ≤ 7 (channel from enum map in playbook)
- ToS triple → must be KILL_MICRO

### Decision coherence

| Condition | Expected decision |
|-----------|-------------------|
| Any hard gate FAIL | KILL_MICRO |
| MSFI < 50 | KILL_MICRO |
| MSFI ≥ 70 + live validation | BUILD_MICRO (if capacity OK) |
| MSFI 50–69 or desk-only | MONITOR_MICRO |
| Capacity full + BUILD qualified | MONITOR_MICRO + capacity_blocked: true |

- [ ] `decision` is uppercase: BUILD_MICRO, MONITOR_MICRO, or KILL_MICRO
- [ ] `decision_override: true` → **FAIL** for solo_micro_saas
- [ ] BUILD_MICRO with `desk-only: true` in Validation → **FAIL**
- [ ] Apply [scripts/msfi_calculator.py](../scripts/msfi_calculator.py) logic where MSFI components documented

### Portfolio sync (solo)

- [ ] `status: decided` → row in **exactly one** table in [portfolio/micro-saas.md](../portfolio/micro-saas.md)
- [ ] Decision column matches frontmatter
- [ ] Notes document `capacity_blocked` when true
- [ ] Studio monitoring/active rows for same ID → **warn** (legacy mirror)

---

## startup_studio checks

Run all blocking checks from [opportunity-qa-v2.md](opportunity-qa-v2.md) including score-calculator and OQI.

---

## Verdict

| Verdict | When |
|---------|------|
| fail | Any blocking check fails |
| warn | Pass with warnings |
| pass | All pass, no warnings |

## Output Format

Same structure as v2; add row **Strategy** per opportunity and **MSFI / hard gates** audit for solo path.

## Related

- [opportunity-qa-v2.md](opportunity-qa-v2.md)
- [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md)
