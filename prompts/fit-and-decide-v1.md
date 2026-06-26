---
version: 1
stage: fit_and_decide
status: active
created: 2026-06-26
supersedes: null
changelog: "v3-lite — hard gates + MSFI-lite + final decision + portfolio sync"
---

# Fit and Decide Prompt v1

## Role

Asset allocator for a solo AI micro-app portfolio. Evaluate the **wedge**, apply hard gates, score MSFI-lite, issue final decision, sync [`portfolio/micro-saas.md`](../portfolio/micro-saas.md).

## Objective

Single stage replacing micro_saas_evaluation + portfolio_manager_micro. Output **Fit and Decide** section + **Final Decision (Micro SaaS)** + frontmatter + portfolio row.

## Inputs Required

- Discovery and Validation sections
- [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md)
- [scripts/msfi_calculator.py](../scripts/msfi_calculator.py) — MSFI-lite weights and gate logic
- Current [`portfolio/micro-saas.md`](../portfolio/micro-saas.md)

## Tasks

1. **Define wedge** — ≤100 h build, ≤10 h/mo maint, €500+ MRR ceiling at maturity, solo operable.
2. **Hard gates** (any FAIL → KILL_MICRO):
   - `build_hours` ≤ 100
   - `maintenance_hours` ≤ 10 h/mo at M6
   - `solo_operable` true
   - `monthly_revenue_potential` ≥ 500 €/mo
   - `distribution_cost` ≤ 7 (from channel map)
   - Platform/ToS triple per playbook
3. **Distribution** — set `distribution_channel` and `distribution_cost` from playbook map.
4. **MSFI-lite** — score 0–100 each:
   - `speed_score` — time to revenue + automation potential
   - `economics_score` — pricing power, maintenance burden, MRR headroom
   - `reach_score` — acquisition feasibility + competition in wedge
5. **Compute MSFI** — weighted: 40% speed + 35% economics + 25% reach (round 1 decimal).
6. **Decision logic** (strict order):
   - Any gate FAIL → KILL_MICRO
   - MSFI < 50 → KILL_MICRO
   - MSFI 50–69 or one borderline gate (10%) → MONITOR_MICRO
   - MSFI ≥ 70 + live validation (not desk-only) → BUILD_MICRO candidate
   - Capacity: BUILD count ≥ 3 or maint sum ≥ 40 h → MONITOR_MICRO + `capacity_blocked: true`
7. **Portfolio sync** — add row to correct table in `portfolio/micro-saas.md`.
8. **Frontmatter** — set `status: decided`, `decision`, `msfi`, component scores, `eval_engine: v3-lite`.

## Output Format

### Section: `## Fit and Decide`

```markdown
**Wedge scope**: [one sentence]

### Hard Gates

| Gate | Threshold | Estimate | Result |
|------|-----------|----------|--------|
| build_hours | ≤ 100 h | XX h | PASS / FAIL / BORDERLINE |
| maintenance_hours | ≤ 10 h/mo | XX h/mo | PASS / FAIL / BORDERLINE |
| solo_operable | Yes | Yes/No | PASS / FAIL |
| monthly_revenue_potential | ≥ 500 €/mo | XXX €/mo | PASS / FAIL |
| distribution_cost | ≤ 7 | X (channel: seo) | PASS / FAIL |
| platform / ToS | see playbook | … | PASS / FAIL |

### Platform Risk

| Field | Value |
|-------|-------|
| tos_risk | low / medium / high |
| platform_dependency | low / medium / high |
| alternative_data_source | true / false |

### MSFI-lite

| Component | Score |
|-----------|-------|
| speed_score | XX |
| economics_score | XX |
| reach_score | XX |
| **MSFI** | **XX** |

```yaml
confidence_level: high / medium / low
```

### Section: `## Final Decision (Micro SaaS)`

| Field | Value |
|-------|-------|
| **Primary Decision** | BUILD_MICRO / MONITOR_MICRO / KILL_MICRO |
| **MSFI** | XX |
| **capacity_blocked** | true / false |
| **Date** | YYYY-MM-DD |
| **Rationale** | |

### Expected Learnings

- [ ] Topic — Method — Applies to: MONITOR_MICRO / KILL_MICRO

### Next Actions

- [ ] ...

### Portfolio Update

- [ ] Added to portfolio/micro-saas.md
```

## Frontmatter updates

```yaml
eval_engine: v3-lite
decision: MONITOR_MICRO
capacity_blocked: false
status: decided
msfi: XX
speed_score: XX
economics_score: XX
reach_score: XX
time_to_first_revenue_days: XX
monthly_revenue_potential: XXX
distribution_channel: seo
distribution_cost: 2
build_hours_estimate: XX
maintenance_hours_estimate: XX
wedge: "..."
pipeline_stage: fit_and_decide
```

## Constraints

- MSFI never overrides hard gate FAIL.
- No `decision_override` for solo_micro_saas.
- Never BUILD_MICRO if Validation has `desk_only: true`.
- Uppercase decisions: BUILD_MICRO, MONITOR_MICRO, KILL_MICRO.

## Related

- [validation-v2.md](validation-v2.md)
- [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md)
