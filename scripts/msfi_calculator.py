#!/usr/bin/env python3
"""Deterministic MSFI v2 and hard-gate checks for solo_micro_saas opportunities."""

from __future__ import annotations

DISTRIBUTION_COST = {
    "existing_audience": 1,
    "seo": 2,
    "communities": 3,
    "marketplace": 4,
    "outbound": 8,
    "ads": 9,
}

MSFI_WEIGHTS = {
    "time_to_revenue_score": 0.15,
    "automation_score": 0.15,
    "maintenance_sustainability_score": 0.10,
    "acquisition_score": 0.15,
    "wedge_local_score": 0.15,
    "competition_score": 0.15,
    "pricing_power_score": 0.15,
}


def time_to_revenue_score(days: int | None) -> int:
    if days is None:
        return 50
    if days <= 60:
        return 100
    if days <= 120:
        return 50
    return 0


def compute_msfi(components: dict[str, float]) -> float:
    total = 0.0
    for key, weight in MSFI_WEIGHTS.items():
        total += components.get(key, 0) * weight
    return round(total, 1)


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
