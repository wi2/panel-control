# Discovery

Minimum outputs and gate criteria for the Discovery stage before advancing to Validation.

## Purpose

Establish whether a problem is real, who has it, what alternatives exist, and whether the idea warrants validation experiments.

## Required outputs

Before setting `pipeline_stage: discovery` complete and advancing to Validation:

| Output | Requirement |
|--------|-------------|
| Problem statement | One paragraph: who, pain, frequency/cost |
| Market signal | At least 3 claims in evidence table with types |
| Competitors / alternatives | Table with strengths and weaknesses |
| Initial hypothesis | "We believe [user] will [behavior] because [reason]" |
| Open questions | Checklist of what Validation must answer |

## Evidence requirements

- Every market claim must use an allowed evidence type per [evidence-classification.md](evidence-classification.md).
- Unsupported claims: `unknown` or `synthetic` — never `verified` without source and date.

## Gate: Discovery → Validation

**Pass** when all required outputs are present and hypothesis is testable within 2–4 weeks.

**Block** when problem statement is missing, hypothesis is not falsifiable, or market table has no evidence types.

## confidence_level guide

| Level | When |
|-------|--------|
| high | Multiple verified or estimated claims with sources |
| medium | Mix of inferred and verified; problem plausible |
| low | Mostly synthetic/unknown; idea-stage only |

## Related

- [Discovery prompt](../prompts/discovery.md)
- [Validation](validation.md)
- [Evaluation process](evaluation-process.md)
