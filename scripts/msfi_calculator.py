#!/usr/bin/env python3
"""Deterministic MSFI-lite and hard-gate checks for solo_micro_saas (v3-lite)."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DISTRIBUTION_COST = {
    "existing_audience": 1,
    "seo": 2,
    "communities": 3,
    "marketplace": 4,
    "outbound": 8,
    "ads": 9,
}

MSFI_LITE_WEIGHTS = {
    "speed_score": 0.40,
    "economics_score": 0.35,
    "reach_score": 0.25,
}

VALID_DECISIONS = {"BUILD_MICRO", "MONITOR_MICRO", "KILL_MICRO"}


def compute_msfi_lite(components: dict[str, float]) -> float:
    total = 0.0
    for key, weight in MSFI_LITE_WEIGHTS.items():
        total += float(components.get(key, 0)) * weight
    return round(total, 1)


# Back-compat alias
compute_msfi = compute_msfi_lite


def distribution_cost_for_channel(channel: str | None) -> int | None:
    if not channel:
        return None
    return DISTRIBUTION_COST.get(channel.strip().lower())


def check_hard_gates(
    *,
    build_hours: float | None,
    maintenance_hours: float | None,
    solo_operable: bool | None,
    monthly_revenue_potential: float | None,
    distribution_cost: int | None,
    tos_risk: str | None,
    platform_dependency: str | None,
    alternative_data_source: bool | None,
) -> list[str]:
    failures: list[str] = []
    if build_hours is not None and build_hours > 110:
        failures.append("build_hours > 100 (non-borderline)")
    if maintenance_hours is not None and maintenance_hours > 11:
        failures.append("maintenance_hours > 10 (non-borderline)")
    if solo_operable is False:
        failures.append("solo_operable false")
    if monthly_revenue_potential is not None and monthly_revenue_potential < 500:
        failures.append("monthly_revenue_potential < 500")
    if distribution_cost is not None and distribution_cost > 7:
        failures.append("distribution_cost > 7")
    if (
        (tos_risk or "").lower() == "high"
        and (platform_dependency or "").lower() == "high"
        and alternative_data_source is False
    ):
        failures.append("platform ToS triple")
    return failures


def count_borderline_gates(
    *,
    build_hours: float | None,
    maintenance_hours: float | None,
) -> int:
    borderline = 0
    if build_hours is not None and 100 < build_hours <= 110:
        borderline += 1
    if maintenance_hours is not None and 10 < maintenance_hours <= 11:
        borderline += 1
    return borderline


def expected_decision(
    *,
    gate_failures: list[str],
    msfi: float,
    desk_only: bool,
    borderline_count: int,
    capacity_blocked: bool = False,
    build_qualified: bool = False,
) -> str:
    if gate_failures:
        return "KILL_MICRO"
    if msfi < 50:
        return "KILL_MICRO"
    if msfi >= 70 and not desk_only and borderline_count == 0:
        if capacity_blocked or not build_qualified:
            return "MONITOR_MICRO"
        return "BUILD_MICRO"
    if msfi >= 50 or borderline_count == 1:
        return "MONITOR_MICRO"
    return "KILL_MICRO"


def _parse_bool(val: str | None) -> bool | None:
    if val is None:
        return None
    v = val.strip().lower()
    if v in ("true", "yes"):
        return True
    if v in ("false", "no"):
        return False
    return None


def _parse_float(val: str | None) -> float | None:
    if val is None or val.strip() in ("", "null"):
        return None
    cleaned = re.sub(r"[^\d.]", "", val.replace(",", ""))
    if not cleaned:
        return None
    return float(cleaned)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" not in line or line.strip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip()
    return data


def extract_desk_only(body: str) -> bool:
    val_section = body.split("## Validation", 1)
    if len(val_section) < 2:
        return False
    chunk = val_section[1].split("## ", 1)[0]
    if re.search(r"desk_only:\s*true", chunk, re.I):
        return True
    if re.search(r"desk-only:\s*true", chunk, re.I):
        return True
    return False


def audit_opportunity(path: Path) -> list[str]:
    """Return list of validation errors for a decided solo_micro_saas OPP."""
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    body = text.split("---", 2)[2] if text.startswith("---") else text

    status = fm.get("status", "")
    ps = fm.get("portfolio_strategy", "solo_micro_saas")
    if status != "decided" or ps != "solo_micro_saas":
        return errors

    speed = _parse_float(fm.get("speed_score"))
    economics = _parse_float(fm.get("economics_score"))
    reach = _parse_float(fm.get("reach_score"))
    if speed is None or economics is None or reach is None:
        errors.append(f"{path.name}: missing speed_score/economics_score/reach_score in frontmatter")
        return errors

    computed_msfi = compute_msfi_lite(
        {"speed_score": speed, "economics_score": economics, "reach_score": reach}
    )
    fm_msfi = _parse_float(fm.get("msfi"))
    if fm_msfi is not None and abs(computed_msfi - fm_msfi) > 1:
        errors.append(
            f"{path.name}: msfi {fm_msfi} != computed {computed_msfi} from MSFI-lite components"
        )

    build_h = _parse_float(fm.get("build_hours_estimate"))
    maint_h = _parse_float(fm.get("maintenance_hours_estimate"))
    channel = fm.get("distribution_channel")
    dist_cost = _parse_float(fm.get("distribution_cost"))
    if dist_cost is None and channel:
        mapped = distribution_cost_for_channel(channel)
        dist_cost = float(mapped) if mapped is not None else None

    gate_failures = check_hard_gates(
        build_hours=build_h,
        maintenance_hours=maint_h,
        solo_operable=_parse_bool(fm.get("solo_operable")) if "solo_operable" in fm else True,
        monthly_revenue_potential=_parse_float(fm.get("monthly_revenue_potential")),
        distribution_cost=int(dist_cost) if dist_cost is not None else None,
        tos_risk=fm.get("tos_risk"),
        platform_dependency=fm.get("platform_dependency"),
        alternative_data_source=_parse_bool(fm.get("alternative_data_source")),
    )

    borderline = count_borderline_gates(build_hours=build_h, maintenance_hours=maint_h)
    desk_only = extract_desk_only(body)
    decision = fm.get("decision", "").strip()
    capacity_blocked = fm.get("capacity_blocked", "").lower() == "true"
    build_qualified = computed_msfi >= 70 and not desk_only and not gate_failures and borderline == 0

    expected = expected_decision(
        gate_failures=gate_failures,
        msfi=computed_msfi,
        desk_only=desk_only,
        borderline_count=borderline,
        capacity_blocked=capacity_blocked and build_qualified,
        build_qualified=build_qualified,
    )

    if gate_failures and decision != "KILL_MICRO":
        errors.append(f"{path.name}: hard gate failures {gate_failures} but decision={decision}")
    if decision == "BUILD_MICRO" and desk_only:
        errors.append(f"{path.name}: BUILD_MICRO with desk_only validation")
    if decision and decision in VALID_DECISIONS and decision != expected and not (
        decision == "MONITOR_MICRO" and capacity_blocked and expected == "MONITOR_MICRO"
    ):
        if not (decision == "MONITOR_MICRO" and expected == "BUILD_MICRO" and capacity_blocked):
            errors.append(f"{path.name}: decision {decision} != expected {expected} (MSFI={computed_msfi})")

    if fm.get("decision_override", "").lower() == "true":
        errors.append(f"{path.name}: decision_override not allowed for solo_micro_saas")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="MSFI-lite calculator and OPP audit")
    parser.add_argument("file", nargs="?", type=Path, help="Opportunity markdown file")
    parser.add_argument("--audit", action="store_true", help="Run full decision audit")
    parser.add_argument("--speed", type=float, help="speed_score 0-100")
    parser.add_argument("--economics", type=float, help="economics_score 0-100")
    parser.add_argument("--reach", type=float, help="reach_score 0-100")
    args = parser.parse_args()

    if args.file and args.audit:
        errs = audit_opportunity(args.file)
        if errs:
            for e in errs:
                print(e, file=sys.stderr)
            return 1
        print(f"Audit passed: {args.file.name}")
        return 0

    if args.speed is not None and args.economics is not None and args.reach is not None:
        msfi = compute_msfi_lite(
            {
                "speed_score": args.speed,
                "economics_score": args.economics,
                "reach_score": args.reach,
            }
        )
        print(f"MSFI-lite: {msfi}")
        return 0

    if args.file:
        fm = parse_frontmatter(args.file.read_text(encoding="utf-8"))
        speed = _parse_float(fm.get("speed_score"))
        economics = _parse_float(fm.get("economics_score"))
        reach = _parse_float(fm.get("reach_score"))
        if speed is not None and economics is not None and reach is not None:
            msfi = compute_msfi_lite(
                {"speed_score": speed, "economics_score": economics, "reach_score": reach}
            )
            print(f"MSFI-lite: {msfi} (from frontmatter)")
            return 0
        print("Missing component scores in frontmatter; use --speed --economics --reach", file=sys.stderr)
        return 1

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
