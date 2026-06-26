#!/usr/bin/env python3
"""Refresh metrics/portfolio.md counts from portfolio/micro-saas.md."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "portfolio" / "micro-saas.md"
METRICS = ROOT / "metrics" / "portfolio.md"

H2 = re.compile(r"^## (.+)", re.MULTILINE)


def section(body: str, name: str) -> str:
    marker = f"## {name}"
    if marker not in body:
        return ""
    rest = body.split(marker, 1)[1]
    m = H2.search(rest)
    return rest[: m.start()] if m else rest


def count_opps(sec: str) -> int:
    return len(re.findall(r"\bOPP-\d{8}-", sec))


def sum_maint(sec: str) -> float:
    total = 0.0
    for line in sec.splitlines():
        if not line.strip().startswith("|") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) > 5 and cells[0].startswith("OPP-"):
            val = re.sub(r"[^\d.]", "", cells[5])
            if val:
                total += float(val)
    return total


def main() -> None:
    text = REGISTRY.read_text(encoding="utf-8")
    build = count_opps(section(text, "Active (BUILD_MICRO)"))
    monitor = count_opps(section(text, "Monitoring (MONITOR_MICRO)"))
    archived = count_opps(section(text, "Archived (KILL_MICRO)"))
    total = build + monitor + archived
    kill_rate = f"{100 * archived / total:.0f}%" if total else "—"
    maint = sum_maint(section(text, "Active (BUILD_MICRO)"))
    today = date.today().isoformat()

    out = f"""# Portfolio Metrics (v3-lite)

Lightweight KPIs for the solo micro-SaaS portfolio. Update after each decided OPP merge or monthly review.

| Metric | Value | Target | Updated |
|--------|-------|--------|---------|
| OPP evaluated (all time) | {total} | — | {today} |
| Kill rate (all time) | {kill_rate} | 45–65% | {today} |
| Median days draft→decided | — | ≤ 14 | {today} |
| BUILD_MICRO active | {build} / 3 | ≤ 3 | {today} |
| Maint budget (active BUILD) | {maint:.0f} / 40 h/mo | ≤ 40 | {today} |
| MONITOR_MICRO active | {monitor} / 5 | ≤ 5 | {today} |
| MONITOR overdue | 0 | 0 | {today} |

## How to update

1. After merge: run `python3 scripts/update_portfolio_metrics.py`.
2. Manually fill median days and overdue MONITOR when needed.

## Related

- [ADR v3-lite](../docs/decisions/2026-06-simplification-v3-lite.md)
- [micro-saas-portfolio.md](../playbooks/micro-saas-portfolio.md)
"""
    METRICS.write_text(out, encoding="utf-8")
    print(f"Updated {METRICS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
