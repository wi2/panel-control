# Validation

Experiment design, gate criteria, and the desk-only fast path before advancing to Scoring.

## Purpose

Produce evidence for or against the discovery hypothesis with minimum time and cost.

## Standard path (preferred)

Before advancing to Scoring:

| Requirement | Detail |
|-------------|--------|
| Experiments | 2–3 time-boxed experiments designed |
| Completed experiment | At least **one** with status `completed` and evidence-typed results |
| Kill/continue signals | Documented thresholds |

Typical experiments: problem interviews, landing page, concierge MVP, smoke tests of distribution channel.

## Gate: Validation → Scoring (strict)

**Pass** when at least one experiment is `completed` with quantified or qualitative results tagged with evidence types.

**Block** when all experiments are `planned` only.

## Desk-only fast path (exception)

Use only when live customer validation is impractical before a desk evaluation (e.g. internal process verification, catalogue triage, smoke tests).

Requirements — all must be true:

1. Document in Validation section: `desk-only: true` with one-line rationale.
2. At least one **completed** experiment — may be internal/process (automation smoke, repo verification, operator checklist).
3. Set Validation `confidence_level: low`.
4. **Never BUILD** from a desk-only path without re-running Validation with live experiments on portfolio review.

The orchestrator and [evaluation-process.md](evaluation-process.md) allow Scoring after desk-only when the above are met. Portfolio Manager must default to **MONITOR** or **KILL**, not BUILD, unless live validation is completed later.

## solo_micro_saas validation gates

For `portfolio_strategy: solo_micro_saas`, gate is **Validation → micro_saas_evaluation** (not Scoring).

| Target | Desk-only | Live validation |
|--------|-----------|-----------------|
| MONITOR_MICRO | Allowed | Not required |
| BUILD_MICRO | **Not allowed** | Required — interviews, concierge, waitlist, LOI, or revenue |
| KILL_MICRO | Allowed | Not required |

## Kill / continue signals

Every Validation section must state:

- **Continue if**: …
- **Kill if**: …

## confidence_level guide

| Level | When |
|-------|--------|
| high | Multiple completed experiments; consistent signal |
| medium | One completed experiment; partial signal |
| low | Desk-only path or zero live customer experiments |

## Related

- [Validation prompt](../prompts/validation.md)
- [Discovery](discovery.md)
- [Evaluation process](evaluation-process.md)
- [Evidence classification](evidence-classification.md)
