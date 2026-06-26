# Pipeline Orchestrator Prompt

## Current Version

**Active**: [pipeline-orchestrator-v2.md](pipeline-orchestrator-v2.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v2 | 2026-06-26 | active | Batch mode — up to 5 stages per run, push-triggered auto-continue |
| v1 | 2026-06-25 | deprecated | Single stage per run; superseded by v2 |

## Usage

Use when advancing an opportunity through the decision path (manual or **CP — Eval** automation).

Requires:

- Target opportunity path
- [AGENTS.md](../AGENTS.md) conventions
- Active stage prompts from opportunity `prompt_versions`

Output: updated opportunity sections, frontmatter, optional portfolio sync after `portfolio_manager`. v2 executes up to **5 stages** per invocation with a single commit.

## Related

- [AGENTS.md](../AGENTS.md)
- [Score calculator](score-calculator.md)
- [Evaluation process](../playbooks/evaluation-process.md)
- [Automation eval](automation-eval.md)
