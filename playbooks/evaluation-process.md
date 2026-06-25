# Evaluation Process

Step-by-step workflow for evaluating a startup opportunity from discovery to portfolio decision.

## Overview

```text
Create opportunity → Run pipeline (9 stages) → Score → Decide → Update portfolio → Schedule review
```

Target timeline: **4–8 weeks** from draft to decision for most opportunities.

## Step 1: Create Opportunity

1. Copy [`templates/opportunity-template.md`](../templates/opportunity-template.md) to [`opportunities/`](../opportunities/).
2. Name the file: `OPP-YYYYMMDD-{slug}.md`.
3. Fill frontmatter: `id`, `title`, `owner`, `created`.
4. Set `status: draft`.

## Step 2: Run Pipeline

Set `status: evaluating`. Execute prompts in order. Paste each output into the matching opportunity section.

| Order | Prompt | Section | Time-box |
|-------|--------|---------|----------|
| 1 | [Discovery](../prompts/discovery.md) | Discovery | 1–2 weeks |
| 2 | [Validation](../prompts/validation.md) | Validation | 2–4 weeks |
| 3 | [Scoring](../prompts/scoring.md) | Scoring | 1–3 days |
| 4 | [Vision](../prompts/vision.md) | Product Vision | 2–3 days |
| 5 | [MVP](../prompts/mvp.md) | MVP Definition | 2–3 days |
| 6 | [Roadmap](../prompts/roadmap.md) | Roadmap | 2–3 days |
| 7 | [Architecture](../prompts/architecture.md) | Architecture Proposal | 2–3 days |
| 8 | [Success Contract](../prompts/success-contract.md) | Success Contract | 1–2 days |
| 9 | [Portfolio Manager](../prompts/portfolio-manager.md) | Final Decision | 1 day |

Record `prompt_versions` in frontmatter after completing the pipeline.

### Stage Gates

Do not advance to the next stage without minimum output:

- **Discovery → Validation**: problem statement, hypothesis, initial market signal documented
- **Validation → Scoring**: at least one experiment completed with recorded results
- **Scoring → Vision**: final score calculated with dimension breakdown
- **Vision → MVP**: target user and value proposition defined
- **MVP → Roadmap**: scope in/out and success metrics defined
- **Roadmap → Architecture**: phased milestones documented
- **Architecture → Success Contract**: high-level system sketch complete
- **Success Contract → Portfolio Manager**: measurable commitments and review dates set

## Step 3: Score

Apply [`scoring-rules.md`](scoring-rules.md):

1. Rate each dimension 0–10.
2. Apply weights to compute weighted total (0–100).
3. Record dimension scores and rationale in the **Scoring** section.
4. Update frontmatter `score`.

## Step 4: Decide

Map score to decision:

| Decision | Score | Action |
|----------|-------|--------|
| BUILD | >= 70 | Allocate build resources |
| MONITOR | 40–69 | Track with periodic re-evaluation |
| KILL | < 40 | Archive, no further investment |

Also check [`kill-rules.md`](kill-rules.md) for automatic kill triggers regardless of score.

Record in **Final Decision**: decision, rationale, date, next actions.

Update frontmatter: `decision`, `status: decided`, `updated`.

## Step 5: Update Portfolio

Add or move the opportunity in the appropriate portfolio file:

- BUILD → [`portfolio/active.md`](../portfolio/active.md)
- MONITOR → [`portfolio/monitoring.md`](../portfolio/monitoring.md)
- KILL → [`portfolio/archived.md`](../portfolio/archived.md)

Follow [`portfolio-rules.md`](portfolio-rules.md) for capacity and review scheduling.

## Step 6: Schedule Review

| Decision | Review cadence |
|----------|----------------|
| BUILD | Every 30 days |
| MONITOR | Every 90 days |
| KILL | None (archived) |

Set `Next Review` date in the portfolio entry.

## Re-Evaluation

MONITOR opportunities re-enter the pipeline at **Validation** (minimum) on each review cycle. If re-validation fails or score drops below 40, apply KILL.

BUILD opportunities are reviewed against their Success Contract. Failure to meet commitments triggers re-evaluation or kill per [`kill-rules.md`](kill-rules.md).

## Related

- [Scoring rules](scoring-rules.md)
- [Kill rules](kill-rules.md)
- [Portfolio rules](portfolio-rules.md)
- [Contributing](../CONTRIBUTING.md)
