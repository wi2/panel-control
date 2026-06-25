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
3. Run the [evaluation process](../playbooks/evaluation-process.md) decision path.
4. Update the appropriate [portfolio](../portfolio/) file after decision.
5. If BUILD, complete BUILD preparation sections.

## Example

See [`_example-opportunity.md`](_example-opportunity.md) for a fully worked fictional example with a MONITOR decision.

Files prefixed with `_` are reference examples, not live portfolio entries.

## Required Sections

### Decision path (all opportunities)

1. Discovery
2. Validation
3. Scoring
4. Distribution Analysis
5. Unfair Advantage Analysis
6. Maintenance Evaluation
7. Risk Analysis
8. Portfolio Intelligence
9. Scenario Planning
10. Final Decision

### BUILD preparation (BUILD only)

11. Product Vision
12. MVP Definition
13. Roadmap
14. Architecture Proposal
15. Success Contract

## Status Lifecycle

```text
draft → evaluating → decided
```

## Migration

Opportunities evaluated under scoring v1 require re-evaluation. See [`migration-v1-to-v2.md`](../playbooks/migration-v1-to-v2.md).

## Related

- [Conventions](../CONVENTIONS.md)
- [Contributing](../CONTRIBUTING.md)
- [Templates](../templates/opportunity-template.md)
