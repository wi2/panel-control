---
version: 7
stage: intake
status: active
created: 2026-06-26
supersedes: intake-v6
changelog: "v3-lite template; eval_engine; fit_and_decide prompt_versions; full-run cp:eval handoff"
---

# Intake Prompt v7

## Role

Convert a raw idea into an opportunity file with Discovery complete. **solo_micro_saas** only (`eval_engine: v3-lite`).

## Objective

Create opportunity with Discovery filled, `intake_complete: true`, `status: evaluating`.

## Studio branch rule

Branch **`opp/pipeline`**: one active OPP (`draft`/`evaluating`); catalogue of `decided` from `master` OK. Recreate branch after merge ([automations.md](../docs/automations.md)).

## Inputs Required

- Idea from PR `## Intake` body or chat
- [templates/opportunity-template.md](../templates/opportunity-template.md)
- [discovery-v1.md](discovery-v1.md)
- [CONVENTIONS.md](../CONVENTIONS.md)

## Tasks

1. Title, slug (kebab, max 40), filename `OPP-{YYYYMMDD}-{slug}.md`.
2. Create from **v3-lite template** with frontmatter:
   - `eval_engine: v3-lite`
   - `portfolio_strategy: solo_micro_saas`
   - `status: evaluating`, `intake_complete: false` initially
   - `pipeline_stage: discovery`
   - `prompt_versions`: discovery v1, validation v2, fit_and_decide v1
3. Run discovery-v1; fill **Discovery** section + `confidence_level`.
4. Set `intake_complete: true`, `automation_intake_at: today`, `updated: today`.
5. **Stop** — do not run validation or fit_and_decide.

## Output Format

```markdown
## Intake Complete

| Field | Value |
|-------|-------|
| File | opportunities/OPP-YYYYMMDD-slug.md |
| eval_engine | v3-lite |
| intake_complete | true |
| Recommended next step | Add label **`cp:eval`** once — full-run to `decided` |
```

## Related

- [Pipeline orchestrator v8](pipeline-orchestrator-v8.md)
- Previous: [intake-v6.md](intake-v6.md)
