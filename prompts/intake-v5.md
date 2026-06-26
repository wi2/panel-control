---
version: 5
stage: intake
status: active
created: 2026-06-26
supersedes: intake-v4
changelog: "Default portfolio_strategy solo_micro_saas; slim prompt_versions for fast path"
---

# Intake Prompt v5

## Role

Convert a raw idea into an opportunity file with Discovery complete. Default strategy: **solo_micro_saas**.

## Objective

Create opportunity with `portfolio_strategy: solo_micro_saas` and Discovery filled; `status: evaluating`.

## Tasks

Same as [intake-v4.md](intake-v4.md), plus:

5. **Frontmatter defaults**:
   - `portfolio_strategy: solo_micro_saas`
   - `capacity_blocked: false`
   - `prompt_versions`: discovery v1, validation v1, micro_saas_evaluation v2, portfolio_manager_micro v1 (plus studio keys from template for reproducibility)
6. **Run discovery-v1**; stop before validation.

## Constraints

- Do not score, MSFI, or decide in intake.
- Tag `micro-saas` when wedge fits solo micro-app model.

## Related

- [Intake v4](intake-v4.md)
- [Pipeline orchestrator v4](pipeline-orchestrator-v4.md)
