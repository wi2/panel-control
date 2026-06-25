# Evidence Classification

Every claim that influences scoring or portfolio decisions must include an evidence type.

## Allowed Values

| Type | Definition | When to use |
|------|------------|-------------|
| `verified` | Directly observed, sourced, reproducible | Paid behavior, experiment results, credible published data |
| `estimated` | Credible extrapolation from verified data | Market sizing from verified base stats, CAC modeled from verified conversion |
| `inferred` | Logical deduction from partial evidence | Practitioner opinion, small-sample interview patterns |
| `synthetic` | AI-generated, modeled, or hypothetical | Projections without source, LLM-generated market estimates |
| `unknown` | No supporting evidence | Unvalidated assumptions, missing data |

## Mapping from Evidence Hierarchy

See [principles](../docs/principles.md) for the underlying quality hierarchy:

| Principles tier | Evidence type |
|-----------------|---------------|
| 1. Paid customer behavior | `verified` |
| 2. Commitment signals (LOI, pilot, pre-order) | `verified` |
| 3. Structured interviews (5+ consistent signal) | `verified` or `inferred` (if < 5) |
| 4. Quantitative market data from credible sources | `verified` |
| 5. Expert or practitioner opinion (single source) | `inferred` |
| 6. Unverified hypothesis | `unknown` or `synthetic` |

## Claim Format

### YAML block (preferred for structured claims)

```yaml
market_size:
  value: "1.3M companies"
  evidence: verified
  source: "INSEE 2024"
  date: 2026-03-01
```

### Markdown table (inline claims)

```markdown
| Claim | Value | Evidence | Source | Date |
|-------|-------|----------|--------|------|
| market_size | 1.3M companies | verified | INSEE 2024 | 2026-03-01 |
| conversion_rate | 18% | synthetic | landing page model | 2026-06-01 |
```

### Blockquote (legacy, still valid when extended)

```markdown
> **Evidence** (verified): INSEE 2024 — 1.3M artisan companies in France, 2026-03-01
```

## Rules

1. **Every scoring input** must cite evidence type in rationale or claim table.
2. **Portfolio Manager** must down-weight or flag decisions dominated by `synthetic` or `unknown` evidence.
3. **OQI calculation** uses evidence-type distribution — see [opportunity-quality-index.md](opportunity-quality-index.md).
4. **Do not upgrade** evidence type without new supporting data. `inferred` does not become `verified` without direct observation.
5. **Label hypotheses explicitly** as `unknown` or `synthetic`, never as `verified`.

## Evidence Quality Weights (for OQI)

| Type | Weight in evidence_quality |
|------|---------------------------|
| verified | 1.0 |
| estimated | 0.8 |
| inferred | 0.5 |
| synthetic | 0.2 |
| unknown | 0.0 |

## Related

- [Principles](../docs/principles.md)
- [Conventions](../CONVENTIONS.md)
- [Opportunity quality index](opportunity-quality-index.md)
- [Scoring rules](scoring-rules.md)
