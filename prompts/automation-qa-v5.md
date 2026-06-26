---
version: 5
stage: automation_qa
status: deprecated
created: 2026-06-26
supersedes: automation-qa-v4
changelog: "Push-to-PR trigger only; no PR opened; delegates to opportunity-qa-v4"
---

# Automation QA Wrapper v5

## Role

Thin wrapper for **CP — QA**. Read-only PR validation.

## Objective

Execute **[opportunity-qa-v4.md](opportunity-qa-v4.md)** only. Post structured comment. Never modify files.

## CRITICAL

- **Do not** use `opportunity-qa-v1.md`, `opportunity-qa-v2.md`, or `opportunity-qa-v3.md`.
- For `portfolio_strategy: solo_micro_saas`, **never** fail on empty Scoring / studio sections or missing `global_score` / OQI.
- Footer must cite: `automation-qa-v5 / opportunity-qa-v4`.

## Trigger (Cursor UI)

**Git — code pushed to pull request** only.

**Do not** configure **pull request opened** on CP — QA.

Path scope: changes under `opportunities/` or `portfolio/`.

If the push diff is outside scope → PR comment `NOOP: outside QA scope`.

Empty commits or pushes that do not touch `opportunities/` or `portfolio/` → NOOP.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [opportunity-qa-v4.md](opportunity-qa-v4.md) on the PR diff.
3. Post **Control Plane QA — pass | warn | fail** using the v4 output format.
4. Do not mark complete until the comment is visible on the PR.

## Related

- [Automations setup](../docs/automations.md)
- Previous: [automation-qa-v4.md](automation-qa-v4.md)
