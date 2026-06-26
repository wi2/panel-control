---
version: 2
stage: validation
status: active
created: 2026-06-26
supersedes: validation-v1
changelog: "v3-lite solo path — desk-only allowed for MONITOR; next stage fit_and_decide"
---

# Validation Prompt v2

## Role

Design and interpret validation experiments for a **solo micro-SaaS wedge**. Minimum time and cost; clear kill/continue signals before Fit and Decide.

## Objective

Produce evidence for or against the discovery hypothesis. Mark desk-only vs live validation — BUILD_MICRO requires live signal (enforced in fit_and_decide).

## Inputs Required

- Completed **Discovery** section
- [validation.md](../playbooks/validation.md)
- [evidence-classification.md](../playbooks/evidence-classification.md)

## Tasks

1. **Design experiments** — 1–2 time-boxed experiments (1–2 weeks each). Prefer interviews, landing pages, concierge over builds.
2. **Success criteria** — quantifiable thresholds per experiment.
3. **Record results** — summarize completed experiments with evidence types.
4. **Desk-only flag** — if no live customer contact yet, set `desk-only: true` in section metadata (YAML block at end). MONITOR_MICRO allowed; BUILD_MICRO blocked later.
5. **Kill/continue** — explicit signals.

## Output Format

Section heading: `## Validation`

```markdown
### Experiments

| # | Experiment | Method | Success Criteria | Status |
|---|------------|--------|------------------|--------|

### Results

| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|

### Kill / Continue Signals

- **Continue if**: ...
- **Kill if**: ...

```yaml
desk_only: true   # or false if live validation present
confidence_level: high / medium / low
```

## Constraints

- Do not build full products during validation.
- Do not treat vanity metrics as validation.
- Tag uncertain claims as `unknown` or `inferred`.

## Related

- Next: [fit-and-decide-v1.md](fit-and-decide-v1.md)
- Previous: [validation-v1.md](validation-v1.md)
