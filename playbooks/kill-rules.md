# Kill Rules

When and how to terminate an opportunity. Fast termination of weak ideas is a feature, not a failure.

## Philosophy

- Kill early when evidence is negative or absent
- Do not defer kills indefinitely under MONITOR
- Archived opportunities are learning assets — every kill must produce `expected_learnings`
- Sunk cost is never a reason to continue

See [philosophy](../docs/philosophy.md).

## Score-Based Kill

Automatic kill when `global_score` is **< 50**.

| Decision | Criteria |
|----------|----------|
| KILL | `global_score < 50` |

Record in [`portfolio/archived.md`](../portfolio/archived.md) with kill reason: `score-below-threshold`.

## Automatic Kill Triggers

Kill regardless of score when any trigger is met:

### Validation Failures

- **No customer signal** after 2 completed experiment cycles (each 2–4 weeks)
- **Consistent negative signal** from 5+ target-user interviews
- **Zero commitment signals** (no LOI, pilot, pre-order, or paid usage) after structured outreach to 20+ prospects

### Market Triggers

- **Incumbent launches equivalent** feature at lower price within validation window
- **Regulatory change** blocks the proposed approach with no viable alternative
- **Market contraction** reduces addressable market below studio minimum threshold

### Execution Triggers

- **Team gap unfillable** within 90 days for critical capability
- **MVP estimate exceeds 6 months** with no path to smaller testable slice
- **Dependency on unavailable technology** with no workaround

### Portfolio Triggers

- **Capacity exhausted** and opportunity ranks lowest among MONITOR set for 2 consecutive reviews
- **Strategic pivot** makes opportunity misaligned with studio thesis

### Success Contract Failures (BUILD only)

- **Missed milestone** by > 30 days without recovery plan
- **Success metric** below 50% of contract target at first review date
- **Exit trigger** condition met as defined in Success Contract

## Kill Process

1. Document kill reason in opportunity **Final Decision** section
2. Record `expected_learnings` — required for all kills and recommended for MONITOR
3. Update frontmatter: `decision: kill`, `status: decided`, `updated`, `global_score`, `opportunity_quality_index`
4. Move row from active or monitoring to [`portfolio/archived.md`](../portfolio/archived.md)
5. Record kill reason in the **Kill reason** column
6. Capture learnings in portfolio review **Key Learning** column

## Expected Learnings (Required)

Every KILL and MONITOR decision must include:

```yaml
expected_learnings:
  - topic: pricing_sensitivity
    method: "A/B price test in validation re-run"
    applies_to: [monitor, kill]
  - topic: acquisition_channel_efficiency
    method: "Test outbound vs content channel with $500 budget"
    applies_to: [monitor]
```

Even failed projects must improve portfolio intelligence. Learnings feed quarterly reviews and playbook calibration.

## MONITOR-Specific Rules

MONITOR opportunities must be re-evaluated every **90 days**.

After **2 review cycles** (6 months total) without `global_score >= 75` AND `OQI >= 70`:

- Automatic kill unless documented exception with new validation plan

After **3 review cycles** (9 months total):

- Automatic kill, no exceptions

## Kill Reason Vocabulary

Use consistent labels in portfolio archived entries:

| Reason | When |
|--------|------|
| `score-below-threshold` | global_score < 50 |
| `oqi-below-threshold` | OQI < 70 blocking BUILD; reclassified to kill on timeout |
| `no-customer-signal` | Validation trigger |
| `negative-validation` | Consistent negative interviews |
| `market-change` | Incumbent, regulation, contraction |
| `execution-infeasible` | Team, timeline, or technology blockers |
| `portfolio-capacity` | Capacity or ranking trigger |
| `success-contract-failure` | BUILD milestone or metric miss |
| `monitor-timeout` | MONITOR exceeded review cycles without improvement |
| `manual` | Document specific rationale |

## Related

- [Scoring rules](scoring-rules.md)
- [Opportunity quality index](opportunity-quality-index.md)
- [Portfolio rules](portfolio-rules.md)
- [Evaluation process](evaluation-process.md)
