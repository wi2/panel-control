# Documentation Conventions

Standards for all markdown assets in this repository.

## Markdown Conventions

- Use ATX headings (`#`, `##`, `###`); one H1 per file (the title).
- Include YAML frontmatter on prompts, opportunities, and decision records.
- Use relative links only (e.g. `../opportunities/OPP-20260625-example.md`).
- Use tables for scores, portfolio entries, and comparisons.
- Use checklists (`- [ ]`) for action items and experiment tracking.
- Dates in ISO 8601 format (`YYYY-MM-DD`).
- No HTML. No embedded application code blocks.

## Naming Conventions

| Asset | Pattern | Example |
|-------|---------|---------|
| Opportunity | `OPP-YYYYMMDD-{slug}.md` | `OPP-20260625-ai-invoice-parser.md` |
| Prompt version | `{stage}-v{N}.md` | `discovery-v2.md` |
| Prompt index | `{stage}.md` | `discovery.md` |
| Slug | lowercase kebab-case, max 40 chars | `ai-invoice-parser` |
| Portfolio review | `REVIEW-YYYY-Q{N}.md` | `REVIEW-2026-Q2.md` |

## File Status Vocabulary

### Opportunities

| Status | Meaning |
|--------|---------|
| `draft` | Created, pipeline not started |
| `evaluating` | Pipeline in progress |
| `decided` | Final decision recorded |

### Prompts

| Status | Meaning |
|--------|---------|
| `draft` | Not yet approved for use |
| `active` | Current version for evaluations |
| `deprecated` | Superseded; retained for reproducibility |

### Decisions

| Decision | Criteria |
|----------|----------|
| `build` | `global_score >= 75` AND `opportunity_quality_index >= 70` |
| `monitor` | `global_score` 50–74, OR score qualifies but OQI < 70 |
| `kill` | `global_score < 50`, or automatic kill trigger |

## Prompt Versioning

- Canonical prompt content lives in versioned files: `{stage}-v{N}.md`.
- Index file `{stage}.md` points to the current version and lists changelog entries.
- Integer versions only (`v1`, `v2`, …).
- Material changes to questions, criteria, or output shape require a new version file.
- Never delete deprecated prompts; mark `status: deprecated` and set `superseded_by`.
- Each opportunity records `prompt_versions` in frontmatter for reproducibility.

### Prompt Frontmatter

```yaml
---
version: 1
stage: discovery
status: active
created: 2026-06-25
supersedes: null
changelog: "Initial release"
---
```

## Opportunity Frontmatter

```yaml
---
id: OPP-YYYYMMDD-slug
title: ""
status: draft
decision: null
global_score: null
opportunity_quality_index: null
scores: {}
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: ""
tags: []
prompt_versions:
  discovery: v1
  validation: v1
  scoring: v2
  distribution_analysis: v1
  unfair_advantage: v1
  maintenance_evaluation: v1
  risk_analysis: v1
  portfolio_intelligence: v1
  scenario_planning: v1
  portfolio_manager: v2
  vision: v1
  mvp: v1
  roadmap: v1
  architecture: v1
  success_contract: v1
---
```

## Evidence Standards

Every claim that influences scoring or decisions must include evidence type. See [evidence-classification.md](playbooks/evidence-classification.md).

### Allowed evidence types

`verified` | `estimated` | `inferred` | `synthetic` | `unknown`

### YAML claim format (preferred)

```yaml
market_size:
  value: "1.3M companies"
  evidence: verified
  source: "INSEE 2024"
  date: 2026-03-01
```

### Markdown table format

```markdown
| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| market_size | 1.3M companies | verified | INSEE 2024 | 2026-03-01 |
```

### Blockquote format (legacy, extended)

```markdown
> **Evidence** (verified): INSEE 2024 — 1.3M companies, 2026-03-01
```

Opinions without evidence are labeled `unknown` or `synthetic`, not `verified`.

## Confidence Levels

Every decision-path section must end with a confidence level:

```yaml
confidence_level: high | medium | low
```

| Level | When to use |
|-------|-------------|
| `high` | Multiple verified claims; consistent validation signal |
| `medium` | Mix of verified and estimated; partial validation |
| `low` | Mostly inferred/synthetic/unknown; early-stage |

Portfolio Manager must not BUILD when Scoring, Distribution, or Risk sections have `confidence_level: low` without documented override.

## Related

- [Evidence classification](playbooks/evidence-classification.md)
- [Opportunity quality index](playbooks/opportunity-quality-index.md)
- [Principles](docs/principles.md)
