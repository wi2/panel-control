# Pipeline Orchestrator Prompt

## Current Version

**Active**: [pipeline-orchestrator-v5.md](pipeline-orchestrator-v5.md)

## Changelog

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v5 | 2026-06-26 | active | Full pipeline in one run; strategy router; gate fail-fast |
| v4 | 2026-06-26 | deprecated | Strategy router — solo_micro_saas fast path vs startup_studio |
| v3 | 2026-06-26 | deprecated | Prompt path resolution; desk-only; BUILD manual |
| v2 | 2026-06-26 | deprecated | Batch mode — up to 5 stages per run, push-triggered auto-continue |
| v1 | 2026-06-25 | deprecated | Single stage per run; superseded by v2 |

## Usage

Use when advancing an opportunity through the decision path (manual or **CP — Eval** automation via label `cp:eval`).

Requires:

- Target opportunity path
- [AGENTS.md](../AGENTS.md) conventions
- Active stage prompts from opportunity `prompt_versions`

Output: updated opportunity sections, frontmatter, portfolio sync after final manager stage. v5 executes **all remaining stages** per invocation with a single commit.

## Related

- [AGENTS.md](../AGENTS.md)
- [Score calculator](score-calculator.md)
- [Evaluation process](../playbooks/evaluation-process.md)
- [Automation eval](automation-eval.md)
