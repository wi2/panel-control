---
version: 8
stage: automation_intake
status: active
created: 2026-06-26
supersedes: automation-intake-v7
changelog: "Delegates to intake-v7; v3-lite template"
---

# Automation Intake Wrapper v8

## Role

Thin wrapper for **CP — Intake**.

## Objective

Execute [intake-v7.md](intake-v7.md). Commit and push to `opp/pipeline`.

## Trigger

PR opened + optional label `cp:eval` fallback `cp:intake`.

## Branch gate

PR head = `opp/pipeline`. No active OPP on branch.

## Related

- [Intake v7](intake-v7.md)
- Previous: [automation-intake-v7.md](automation-intake-v7.md)
