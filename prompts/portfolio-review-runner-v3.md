---
version: 3
stage: portfolio_review_runner
status: active
created: 2026-06-26
supersedes: portfolio-review-runner-v2
changelog: "v3-lite solo only; fit_and_decide re-eval; no studio router"
---

# Portfolio Review Runner Prompt v3

## Role

Scheduled portfolio reviews for **solo_micro_saas** only. Studio path frozen — skip legacy registry files.

## Objective

Re-evaluate due MONITOR_MICRO and BUILD_MICRO entries in [`portfolio/micro-saas.md`](../portfolio/micro-saas.md).

## Inputs

- [portfolio/micro-saas.md](../portfolio/micro-saas.md)
- [fit-and-decide-v1.md](fit-and-decide-v1.md)
- [validation-v2.md](validation-v2.md)
- [scripts/msfi_calculator.py](../scripts/msfi_calculator.py)
- [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md)

## Steps

1. Find due rows (Next Review <= today) in Active and Monitoring tables.
2. Process max **3 MONITOR_MICRO** per run.
3. Re-run **validation** (minimum) then **fit_and_decide** for each due entry.
4. Apply MSFI-lite and hard gates via script logic.
5. Sync portfolio; set Next Review +30 days for continued MONITOR/BUILD.
6. Create [reviews/REVIEW-YYYY-QN.md](../reviews/README.md) when warranted.

## Kill triggers

Hard gate FAIL, MSFI < 50, monitor-timeout (60 days MONITOR without promotion), Success Contract failures for BUILD.

## Output

```markdown
## Portfolio Review Run

| ID | Prior | New | MSFI | Notes |
|----|-------|-----|------|-------|
```

## Related

- [automation-review-v3.md](automation-review-v3.md)
- Previous: [portfolio-review-runner-v2.md](portfolio-review-runner-v2.md)
