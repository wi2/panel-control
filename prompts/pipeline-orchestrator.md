# Pipeline Orchestrator Prompt

## Current Version

**Active**: [pipeline-orchestrator-v1.md](pipeline-orchestrator-v1.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v1 | 2026-06-25 | active | Single-agent pipeline driver for Cursor Automations |

## Usage

Use when advancing an opportunity by one pipeline stage in a single agent run (manual or automated).

Requires:

- Target opportunity path
- [AGENTS.md](../AGENTS.md) conventions
- Active stage prompts from opportunity `prompt_versions`

Output: updated opportunity section, frontmatter, and optional portfolio sync after `portfolio_manager`.

## Related

- [AGENTS.md](../AGENTS.md)
- [Score calculator](score-calculator.md)
- [Evaluation process](../playbooks/evaluation-process.md)
- First stage: [discovery.md](discovery.md)
- Final stage: [portfolio-manager.md](portfolio-manager.md)
