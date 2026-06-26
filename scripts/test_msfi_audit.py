#!/usr/bin/env python3
"""Smoke tests for MSFI-lite audit (v3-lite CI guard)."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from msfi_calculator import audit_opportunity  # noqa: E402

BAD_OPP = """---
id: OPP-20990101-msfi-audit-fixture
title: MSFI audit fixture
eval_engine: v3-lite
portfolio_strategy: solo_micro_saas
status: decided
decision: BUILD_MICRO
msfi: 99
speed_score: 50
economics_score: 50
reach_score: 50
build_hours_estimate: 80
maintenance_hours_estimate: 5
monthly_revenue_potential: 800
distribution_channel: seo
distribution_cost: 2
---

# Fixture

## Validation

```yaml
desk_only: true
confidence_level: low
```

## Fit and Decide

```yaml
confidence_level: low
```

## Final Decision (Micro SaaS)

```yaml
confidence_level: low
```
"""


def main() -> int:
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", prefix="OPP-20990101-", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(BAD_OPP)
        path = Path(tmp.name)

    try:
        errors = audit_opportunity(path)
        if not errors:
            print("FAIL: audit_opportunity should reject incoherent MSFI/decision", file=sys.stderr)
            return 1
        print(f"OK: audit caught {len(errors)} error(s)")
        for err in errors:
            print(f"  - {err}")
        return 0
    finally:
        path.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())
