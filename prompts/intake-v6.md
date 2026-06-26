---
version: 6
stage: intake
status: active
created: 2026-06-26
supersedes: intake-v5
changelog: "intake_complete marker; cp:eval handoff (no push-triggered eval)"
---

# Intake Prompt v6

## Role

Convert a raw idea into an opportunity file with Discovery complete. Default strategy: **solo_micro_saas**.

## Objective

Create opportunity with `portfolio_strategy: solo_micro_saas`, Discovery filled, `intake_complete: true`, and `status: evaluating`.

## Studio branch rule

All automated intake and eval use the **fixed branch** `opp/pipeline`:

- The branch may contain a **catalogue** of `decided` OPP files inherited from `master`.
- **One active opportunity** (`status: draft` or `status: evaluating`) per pipeline run at a time.
- After merge to `master`, delete and recreate `opp/pipeline` for the next idea (see [docs/automations.md](../docs/automations.md)).

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
   - `portfolio_strategy: solo_micro_saas`
   - `capacity_blocked: false`
   - `status: evaluating`
   - `intake_complete: false` initially (set `true` after Discovery)
   - `pipeline_stage: discovery`
   - `tags`: from input or `[]`
   - `prompt_versions`: discovery v1, validation v1, micro_saas_evaluation v2, portfolio_manager_micro v1 (plus studio keys from template for reproducibility)
6. **Run discovery-v1**: Execute all discovery tasks; fill the **Discovery** section.
7. **Confidence**: Set `confidence_level` on the Discovery section.
8. **Mark intake complete**: Update frontmatter:
   - `intake_complete: true`
   - `pipeline_stage: discovery`
   - `automation_intake_at: YYYY-MM-DD` (today)
   - `updated`: today
9. **Stop**: Do not run validation, scoring, micro eval, or portfolio decisions in this run.

## Output Format

```markdown
## Intake Complete

| Field | Value |
|-------|-------|
| File | opportunities/OPP-YYYYMMDD-slug.md |
| Title | ... |
| Discovery confidence | high / medium / low |
| intake_complete | true |
| Open questions count | N |
| Recommended next step | Add label **`cp:eval`** on this PR to start full pipeline evaluation |

### PR note

Branch is `opp/pipeline`. Catalogue of `decided` OPP files from `master` may coexist on this branch. After intake commit+push, add **`cp:eval`** once — **CP — Eval** runs all remaining stages in one run. Merge when `status: decided` and **CP — QA** passes. Recreate `opp/pipeline` from `master` for the next idea.
```

## Constraints

- One idea → one new file per run on `opp/pipeline`.
- Do not score, calculate MSFI/OQI, or record a portfolio decision in intake.
- Tag uncertain market claims as `unknown` or `inferred`, never `verified` without source.
- Use relative links only per CONVENTIONS.
- Open changes via pull request on **`opp/pipeline`** — do not push directly to the default branch.
- Tag `micro-saas` when wedge fits solo micro-app model.

## Related

- [Discovery](discovery-v1.md)
- [Pipeline orchestrator v6](pipeline-orchestrator-v6.md)
- [Automation intake v7](automation-intake-v7.md)
- Previous: [intake-v5.md](intake-v5.md)
