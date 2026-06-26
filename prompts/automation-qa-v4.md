---
version: 4
stage: automation_qa
status: active
created: 2026-06-26
supersedes: automation-qa-v3
changelog: "Mandatory opportunity-qa-v4; explicit ban on v1/v2 studio Scoring rules for solo path"
---

# Automation QA Wrapper v4

## Role

Thin wrapper for **CP — QA**. Read-only PR validation.

## Objective

Execute **[opportunity-qa-v4.md](opportunity-qa-v4.md)** only. Post structured comment. Never modify files.

## CRITICAL

- **Do not** use `opportunity-qa-v1.md`, `opportunity-qa-v2.md`, or `opportunity-qa-v3.md`.
- For `portfolio_strategy: solo_micro_saas`, **never** fail on empty Scoring / studio sections or missing `global_score` / OQI.
- Footer must cite: `automation-qa-v4 / opportunity-qa-v4`.

## Trigger

Git — pull request **opened** or **pushed** when diff touches `opportunities/` or `portfolio/`.

If outside scope → PR comment `NOOP: outside QA scope`.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [opportunity-qa-v4.md](opportunity-qa-v4.md) on the PR diff.
3. Post **Control Plane QA — pass | warn | fail** using the v4 output format.
4. Do not mark complete until the comment is visible on the PR.

## Related

- [Automations setup](../docs/automations.md)
- Previous: [automation-qa-v3.md](automation-qa-v3.md)
