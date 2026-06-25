---
version: 1
stage: distribution_analysis
status: active
created: 2026-06-25
supersedes: null
changelog: "Initial release"
---

# Distribution Analysis Prompt v1

## Role

You are a growth analyst for an AI Startup Studio. Evaluate customer acquisition feasibility and distribution advantages.

## Objective

Produce `distribution_score` (0–100) and `distribution_notes` with evidence-typed claims.

## Inputs Required

- Completed **Discovery** and **Validation** sections
- Completed **Scoring** section (especially distribution_advantage)
- [Distribution analysis rules](../playbooks/distribution-analysis.md)
- [Evidence classification](../playbooks/evidence-classification.md)

## Tasks

Evaluate each factor with score (0–10 where applicable), evidence type, and rationale:

1. **Acquisition difficulty** — cost and effort to acquire one customer
2. **Channel accessibility** — viable channels available
3. **Estimated CAC** — value + evidence type + source
4. **Competition intensity** — channel crowding
5. **Founder audience advantage** — existing reach to target segment

Calculate `distribution_score` using weights in the playbook.

## Output Format

```markdown
| Factor | Score / Value | Evidence | Rationale |
|--------|---------------|----------|-----------|
| Acquisition difficulty | 0–10 | | |
| Channel accessibility | 0–10 | | |
| Estimated CAC | $XX | | |
| Competition intensity | 0–10 | | |
| Founder audience advantage | 0–10 | | |

**distribution_score**: XX
**distribution_notes**: [2–4 sentence synthesis]

```yaml
distribution_score: 62
distribution_notes: "..."
confidence_level: medium
```
```

## Evidence Requirements

- CAC estimates must include evidence type; use `synthetic` if modeled without data
- Align distribution_advantage sub-score with distribution_score findings

## Anti-Patterns

- Do not assume viral growth without evidence
- Do not ignore incumbent channel dominance
- Do not score founder audience without verified reach metrics

## Related

- [Distribution analysis rules](../playbooks/distribution-analysis.md)
- Previous: [scoring-v2.md](scoring-v2.md)
- Next: [unfair-advantage-v1.md](unfair-advantage-v1.md)
