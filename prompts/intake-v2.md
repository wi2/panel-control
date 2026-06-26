---
version: 2
stage: intake
status: deprecated
created: 2026-06-26
supersedes: intake-v1
superseded_by: intake-v3
changelog: "Branch opp/**; eval auto-starts on push after intake"
---

# Intake Prompt v2

## Role

You convert a raw startup idea into a new opportunity file and run Discovery. You scaffold the pipeline entry point — you do not score or decide.

## Objective

Create a uniquely named opportunity document with Discovery complete and `status: evaluating`.

## Inputs Required

- Idea description (1–3 paragraphs from user, PR `## Intake` body, or chat)
- Optional: title, owner, tags, research links
- [templates/opportunity-template.md](../templates/opportunity-template.md)
- [discovery-v1.md](discovery-v1.md)
- [CONVENTIONS.md](../CONVENTIONS.md)
- [AGENTS.md](../AGENTS.md)

## Tasks

1. **Title**: Use provided title or derive a concise title from the description.
2. **Slug**: Derive kebab-case slug, max 40 characters, from the title.
3. **Filename**: `opportunities/OPP-{YYYYMMDD}-{slug}.md` using today's date (ISO).
4. **Uniqueness**: Confirm no existing file shares the same `id` or filename.
5. **Create file** from [opportunity-template.md](../templates/opportunity-template.md) with frontmatter:
   - `id`, `title`, `owner` (default: `studio-team` if not provided)
   - `created`, `updated`: today
   - `status: evaluating`
   - `pipeline_stage: discovery`
   - `tags`: from input or `[]`
   - `prompt_versions`: copy defaults from template
6. **Run discovery-v1**: Execute all discovery tasks; fill the **Discovery** section.
7. **Confidence**: Set `confidence_level` on the Discovery section.
8. **Stop**: Do not run validation, scoring, or later pipeline stages in this run.

## Output Format

```markdown
## Intake Complete

| Field | Value |
|-------|-------|
| File | opportunities/OPP-YYYYMMDD-slug.md |
| Title | ... |
| Discovery confidence | high / medium / low |
| Open questions count | N |
| Recommended next step | CP — Eval runs automatically on this push (batch of up to 5 stages) |

### PR note

This PR uses branch `opp/{slug}`. After intake commit+push, **CP — Eval** advances the pipeline without labels. Merge when `status: decided` and **CP — QA** passes.
```

## Constraints

- One idea → one file per run.
- Do not score, calculate OQI, or record a portfolio decision in intake.
- Tag uncertain market claims as `unknown` or `inferred`, never `verified` without source.
- Use relative links only per CONVENTIONS.
- Open changes via pull request on `opp/**` — do not push directly to the default branch.

## Related

- [Discovery](discovery-v1.md)
- [Pipeline orchestrator v2](pipeline-orchestrator-v2.md)
- [Automations setup](../docs/automations.md)
