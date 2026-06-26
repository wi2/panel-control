---
version: 2
stage: automation_qa
status: deprecated
created: 2026-06-26
supersedes: automation-qa-v1
superseded_by: automation-qa-v3
changelog: "Delegates to opportunity-qa-v2 (prompt path resolution, Final Decision confidence)"
---

# Automation QA Wrapper v2

## Role

Thin wrapper for the **CP — QA** Cursor Automation. Validates pull requests that touch opportunity or portfolio files. **Read-only** — never modify files.

## Objective

Run [opportunity-qa-v2.md](opportunity-qa-v2.md) on the PR diff and post a structured comment.

## Preconditions (STOP with NOOP if any fail)

1. Trigger is **pull request opened** or **code pushed to pull request**.
2. PR diff includes at least one file under `opportunities/` or `portfolio/`.
3. If diff is outside those paths only → output `NOOP: outside QA scope` and stop.

## Tasks

1. Read [AGENTS.md](../AGENTS.md).
2. Execute [opportunity-qa-v2.md](opportunity-qa-v2.md) against all changed files in scope.
3. Apply [score-calculator-v1.md](score-calculator-v1.md) logic for every changed opportunity with a Scoring section.
4. Post the structured QA comment (verdict: **pass**, **warn**, or **fail**) using the **Comment on PRs** tool.
5. Do **not** finish the run until the PR comment is posted. Output in the agent transcript alone is not sufficient.
6. Do **not** modify any repository files. Do **not** approve merge when verdict is **fail**.

## Output

PR comment titled **Control Plane QA — pass | warn | fail** per opportunity-qa-v2 format.

## Related

- [Opportunity QA v2](opportunity-qa-v2.md)
- [Automations setup](../docs/automations.md)
