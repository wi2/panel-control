---
version: 6
stage: automation_qa
status: active
created: 2026-06-26
supersedes: automation-qa-v5
changelog: "Delegates to opportunity-qa-v5; v3-lite"
---

# Automation QA Wrapper v6

## Role

Thin wrapper for **CP — QA**. Read-only.

## Objective

Execute [opportunity-qa-v5.md](opportunity-qa-v5.md). Post PR comment. Never modify files.

## Trigger

Push to PR only (not PR opened).

## CRITICAL

- Footer: `automation-qa-v6 / opportunity-qa-v5`
- Do not use opportunity-qa-v4 or earlier for blocking rules

## Related

- Previous: [automation-qa-v5.md](automation-qa-v5.md)
