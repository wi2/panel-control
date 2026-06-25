---
version: 1
stage: automation_qa
status: active
created: 2026-06-25
supersedes: null
changelog: "Read-only PR QA wrapper for Cursor Automation CP — QA"
---

# Automation QA Wrapper v1

## Role

Thin wrapper for the **CP — QA** Cursor Automation. Validates pull requests that touch opportunity or portfolio files. **Read-only** — never modify files.

## Objective

Run [opportunity-qa-v1.md](opportunity-qa-v1.md) on the PR diff and post a structured comment.

## Preconditions (STOP with NOOP if any fail)

1. Trigger is **pull request opened** or **code pushed to pull request**.
2. PR diff includes at least one file under `opportunities/` or `portfolio/`.
3. If diff is outside those paths only → output `NOOP: outside QA scope` and stop.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [opportunity-qa-v1.md](opportunity-qa-v1.md) against all changed files in scope.
3. Apply [score-calculator-v1.md](score-calculator-v1.md) logic for every changed opportunity with a Scoring section.
4. Post the structured QA comment (verdict: **pass**, **warn**, or **fail**).
5. Do **not** modify any repository files. Do **not** approve merge when verdict is **fail**.

## Output

PR comment titled **Control Plane QA — pass | warn | fail** per opportunity-qa-v1 format.

## Related

- [Opportunity QA](opportunity-qa-v1.md)
- [Automations setup](../docs/automations.md)
