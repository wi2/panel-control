# Documentation Conventions

Standards for all markdown assets in this repository.

## Markdown Conventions

- Use ATX headings (`#`, `##`, `###`); one H1 per file (the title).
- Include YAML frontmatter on prompts, opportunities, and decision records.
- Use relative links only (e.g. `../opportunities/OPP-20260625-example.md`).
- Use tables for scores, portfolio entries, and comparisons.
- Use checklists (`- [ ]`) for action items and experiment tracking.
- Format evidence using blockquote + bold label:

```markdown
> **Evidence**: [source, date, metric]
```

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

| Decision | Score threshold |
|----------|-----------------|
| `build` | >= 70 |
| `monitor` | 40–69 |
| `kill` | < 40 |

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
score: null
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: ""
prompt_versions:
  discovery: v1
  validation: v1
  scoring: v1
  vision: v1
  mvp: v1
  roadmap: v1
  architecture: v1
  success_contract: v1
  portfolio_manager: v1
---
```

## Evidence Standards

Every claim that influences scoring or decisions must include evidence:

1. **Source** — where the information came from (interview, data, experiment, publication).
2. **Date** — when the evidence was collected.
3. **Metric** — quantifiable result where possible.

Opinions without evidence are noted as hypotheses, not facts.
