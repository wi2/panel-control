# Smoke Test — Full Pipeline

Reproducible verification that panel-control automations work end-to-end.

Run after configuring Cursor automations or changing wrapper prompts.

## Prerequisites

- [docs/automations.md](automations.md) onboarding checklist complete
- `gh` CLI authenticated
- Cursor Background Agents enabled

## Procedure

### 1. Open pipeline

```bash
./scripts/open_pipeline.sh
```

### 2. Create PR

```bash
gh pr create --base master --head opp/pipeline --title "smoke: test widget tracker" --body "$(cat <<'EOF'
## Intake

**Title:** Test Widget Tracker (smoke)
**Owner:** studio-team
**Tags:** smoke-test

### Description

Fictional idea for pipeline smoke test. Kill after verification.
EOF
)"
```

### 3. Verify Intake

| Check | Expected |
|-------|----------|
| CP — Intake runs | New `opportunities/OPP-*.md` |
| Discovery filled | Non-empty section |
| Frontmatter | `intake_complete: true`, `status: evaluating` |
| CP — QA on push | Comment posted |

### 4. Run Eval

Add label `cp:eval` once.

| Check | Expected |
|-------|----------|
| CP — Eval runs | Validation + Fit and Decide filled |
| Frontmatter | `status: decided`, decision set |
| Portfolio | Row in micro-saas.md |
| Pipeline summary | `Mode: full-run`, `Remaining stages: none` |

### 5. Merge gate

```bash
python3 scripts/validate_opportunities.py
```

| Check | Expected |
|-------|----------|
| CI / local validate | exit 0 |
| CP — QA | pass or warn on decided push |

### 6. Cleanup

- Merge or close PR
- KILL or delete smoke OPP if merged to master
- `git push origin --delete opp/pipeline`
- Remove `cp:eval` label if still present

## Results log

| Run | Date | Operator | Intake | Eval | QA | CI | Notes |
|-----|------|----------|--------|------|----|----|-------|
| 1 | | | | | | | |

## Related

- [prod-cutover.md](prod-cutover.md)
