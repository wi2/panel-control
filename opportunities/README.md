# Opportunities

One markdown file per evaluated startup opportunity.

## Naming

```text
OPP-YYYYMMDD-{slug}.md
```

- **YYYYMMDD**: date the opportunity was created
- **slug**: lowercase kebab-case, max 40 characters

Example: `OPP-20260625-ai-invoice-parser.md`

## Getting Started

1. Copy [`templates/opportunity-template.md`](../templates/opportunity-template.md) into this folder.
2. Rename using the convention above.
3. Run the [evaluation pipeline](../playbooks/evaluation-process.md).
4. Update the appropriate [portfolio](../portfolio/) file after decision.

## Example

See [`_example-opportunity.md`](_example-opportunity.md) for a fully worked fictional example with a MONITOR decision (score 55).

Files prefixed with `_` are reference examples, not live portfolio entries.

## Required Sections

Every opportunity document must contain:

1. Discovery
2. Validation
3. Scoring
4. Product Vision
5. MVP Definition
6. Roadmap
7. Architecture Proposal
8. Success Contract
9. Final Decision

## Status Lifecycle

```text
draft → evaluating → decided
```

## Related

- [Conventions](../CONVENTIONS.md)
- [Contributing](../CONTRIBUTING.md)
- [Templates](../templates/opportunity-template.md)
