#!/usr/bin/env python3
"""Validate opportunity and portfolio markdown files (read-only CI check)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OPPORTUNITIES = ROOT / "opportunities"
PORTFOLIO = ROOT / "portfolio"
PROMPTS = ROOT / "prompts"

REQUIRED_FRONTMATTER = {"id", "title", "status", "prompt_versions"}
VALID_STATUS = {"draft", "evaluating", "decided"}
VALID_MICRO_DECISIONS = {"BUILD_MICRO", "MONITOR_MICRO", "KILL_MICRO"}
VALID_PORTFOLIO_STRATEGY = {"solo_micro_saas", "startup_studio", "vc_moonshot", "cashflow_business"}
OPP_FILENAME = re.compile(r"^OPP-\d{8}-[a-z0-9-]+\.md$")
LINK_PATTERN = re.compile(r"\]\(([^)]+)\)")
H2_SECTION = re.compile(r"^## .+", re.MULTILINE)
TABLE_SEP = re.compile(r"^\|[-:\s|]+\|$")
MICRO_SAAS_SECTIONS: dict[str, str] = {
    "Active (BUILD_MICRO)": "BUILD_MICRO",
    "Monitoring (MONITOR_MICRO)": "MONITOR_MICRO",
    "Archived (KILL_MICRO)": "KILL_MICRO",
}


def h2_section(body: str, heading: str) -> str:
    """Return content under a level-2 heading until the next level-2 heading."""
    marker = f"## {heading}"
    if marker not in body:
        return ""
    rest = body.split(marker, 1)[1]
    match = H2_SECTION.search(rest)
    if match:
        return rest[: match.start()]
    return rest


def parse_frontmatter(text: str) -> tuple[dict | None, str]:
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    block = text[3:end].strip()
    data: dict = {}
    for line in block.splitlines():
        if ":" not in line or line.strip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip()
    return data, text[end + 4 :]


def resolve_prompt_path(stage_key: str, version: str) -> Path:
    slug = stage_key.replace("_", "-")
    ver = version if version.startswith("v") else f"v{version}"
    return PROMPTS / f"{slug}-{ver}.md"


def check_links(content: str, source: Path) -> list[str]:
    errors: list[str] = []
    for match in LINK_PATTERN.finditer(content):
        target = match.group(1).strip()
        if target.startswith("http") or target.startswith("#"):
            continue
        if target.startswith("mailto:"):
            continue
        resolved = (source.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{source.relative_to(ROOT)}: link escapes repo: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{source.relative_to(ROOT)}: broken link: {target}")
    return errors


def validate_opportunity(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)

    if path.name.startswith("OPP-"):
        if not OPP_FILENAME.match(path.name):
            errors.append(f"{rel}: filename does not match OPP-YYYYMMDD-slug.md")
        opp_id = path.stem
        if path.name == "_example-opportunity.md":
            pass
        elif not path.name.startswith(opp_id if False else ""):
            pass

    fm, body = parse_frontmatter(text)
    if fm is None:
        errors.append(f"{rel}: missing YAML frontmatter")
        return errors

    missing = REQUIRED_FRONTMATTER - set(fm.keys())
    if missing and path.name.startswith("OPP-"):
        errors.append(f"{rel}: missing frontmatter keys: {sorted(missing)}")

    status = fm.get("status", "").strip()
    if status and status not in VALID_STATUS:
        errors.append(f"{rel}: invalid status '{status}'")

    opp_id = fm.get("id", "")
    if path.name.startswith("OPP-") and opp_id and opp_id != path.stem:
        errors.append(f"{rel}: frontmatter id '{opp_id}' does not match filename")

    if "prompt_versions:" in text and path.name.startswith("OPP-"):
        in_pv = False
        for line in text.splitlines():
            if line.strip() == "prompt_versions:":
                in_pv = True
                continue
            if in_pv:
                if line.startswith("  ") and ":" in line:
                    key, _, val = line.strip().partition(":")
                    key, val = key.strip(), val.strip()
                    prompt_path = resolve_prompt_path(key, val)
                    if not prompt_path.exists():
                        errors.append(
                            f"{rel}: prompt_versions.{key}: {val} → missing {prompt_path.relative_to(ROOT)}"
                        )
                elif line.startswith("---") or (line and not line.startswith(" ")):
                    break


    ps = fm.get("portfolio_strategy", "").strip()
    if ps and ps not in VALID_PORTFOLIO_STRATEGY:
        errors.append(f"{rel}: invalid portfolio_strategy '{ps}'")
    if ps == "solo_micro_saas" and status == "decided":
        dec = fm.get("decision", "").strip()
        if dec and dec not in VALID_MICRO_DECISIONS:
            errors.append(f"{rel}: solo_micro_saas decision must be BUILD_MICRO/MONITOR_MICRO/KILL_MICRO, got '{dec}'")
        if fm.get("decision_override", "").strip() == "true":
            errors.append(f"{rel}: decision_override not allowed for solo_micro_saas")

    if status == "decided" and "<!-- Paste output -->" in body:
        errors.append(f"{rel}: decided file contains unresolved template placeholder")

    if status == "decided":
        if ps == "solo_micro_saas":
            micro_section = h2_section(body, "Final Decision (Micro SaaS)")
            if micro_section and "confidence_level" not in micro_section:
                errors.append(f"{rel}: Final Decision (Micro SaaS) section missing confidence_level")
            elif not micro_section and h2_section(body, "Micro SaaS Evaluation"):
                micro_eval = h2_section(body, "Micro SaaS Evaluation")
                if "confidence_level" not in micro_eval and "Micro SaaS Decision" not in body:
                    warnings.append(
                        f"{rel}: solo_micro_saas decided without Final Decision (Micro SaaS) section"
                    )
        else:
            studio_section = h2_section(body, "Final Decision")
            if studio_section and "confidence_level" not in studio_section:
                errors.append(f"{rel}: Final Decision section missing confidence_level")

    intake_complete = fm.get("intake_complete", "").strip().lower()
    if status == "evaluating":
        if intake_complete == "true":
            discovery_part = body.split("## Discovery", 1)
            if len(discovery_part) < 2 or "<!-- Paste output -->" in discovery_part[1].split("## ", 1)[0]:
                warnings.append(f"{rel}: intake_complete but Discovery section empty or has template placeholder")
        elif intake_complete != "false" and not intake_complete:
            warnings.append(f"{rel}: evaluating without intake_complete — CP — Eval will NOOP until intake finishes")

    errors.extend(check_links(text, path))
    return errors, warnings


def parse_table_rows(section_text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        if TABLE_SEP.match(stripped):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        rows.append(cells)
    return rows


def parse_micro_saas_registry(text: str) -> dict[str, tuple[str, str, str]]:
    """Return opp_id -> (section_heading, table_decision, expected_decision)."""
    registry: dict[str, tuple[str, str, str]] = {}
    for heading, expected in MICRO_SAAS_SECTIONS.items():
        section = h2_section(text, heading)
        if not section:
            continue
        for cells in parse_table_rows(section):
            if not cells:
                continue
            opp_id = cells[0]
            if not opp_id.startswith("OPP-"):
                continue
            table_decision = cells[3] if len(cells) > 3 else ""
            registry[opp_id] = (heading, table_decision, expected)
    return registry


def validate_micro_saas_registry(
    registry: dict[str, tuple[str, str, str]],
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for opp_id, (section, table_decision, expected) in registry.items():
        opp_path = OPPORTUNITIES / f"{opp_id}.md"
        if not opp_path.exists():
            errors.append(
                f"portfolio/micro-saas.md: {opp_id} in {section} but missing {opp_path.relative_to(ROOT)}"
            )
            continue

        fm, _ = parse_frontmatter(opp_path.read_text(encoding="utf-8"))
        if fm is None:
            errors.append(f"{opp_path.relative_to(ROOT)}: missing YAML frontmatter (linked from micro-saas.md)")
            continue

        fm_id = fm.get("id", "").strip()
        if fm_id and fm_id != opp_id:
            errors.append(
                f"portfolio/micro-saas.md: row id '{opp_id}' does not match "
                f"{opp_path.relative_to(ROOT)} frontmatter id '{fm_id}'"
            )

        fm_decision = fm.get("decision", "").strip()
        if fm_decision and fm_decision != expected:
            errors.append(
                f"portfolio/micro-saas.md: {opp_id} in {section} expects decision {expected}, "
                f"frontmatter has '{fm_decision}'"
            )

        if table_decision and table_decision != expected:
            errors.append(
                f"portfolio/micro-saas.md: {opp_id} Decision column '{table_decision}' "
                f"does not match section {expected}"
            )

    return errors, warnings


def validate_orphan_micro_opportunities(registry_ids: set[str]) -> list[str]:
    warnings: list[str] = []
    for path in sorted(OPPORTUNITIES.glob("OPP-*.md")):
        fm, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fm is None:
            continue
        status = fm.get("status", "").strip()
        ps = fm.get("portfolio_strategy", "solo_micro_saas").strip() or "solo_micro_saas"
        if status != "decided" or ps != "solo_micro_saas":
            continue
        opp_id = fm.get("id", path.stem).strip()
        if opp_id not in registry_ids:
            warnings.append(
                f"{path.relative_to(ROOT)}: decided solo_micro_saas not listed in portfolio/micro-saas.md"
            )
    return warnings


def validate_portfolio(path: Path) -> tuple[list[str], list[str], set[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    registry_ids: set[str] = set()
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)

    if path.name == "micro-saas.md":
        registry = parse_micro_saas_registry(text)
        registry_ids = set(registry.keys())
        reg_errors, reg_warnings = validate_micro_saas_registry(registry)
        errors.extend(reg_errors)
        warnings.extend(reg_warnings)

    if "_example-opportunity.md" in text and path.name == "monitoring.md":
        in_entries = False
        for line in text.splitlines():
            if line.startswith("## Entries"):
                in_entries = True
            if in_entries and line.startswith("## ") and "Entries" not in line:
                in_entries = False
            if in_entries and "_example-opportunity.md" in line:
                errors.append(
                    f"{rel}: fictional example must not appear in Entries table (use Example section)"
                )
                break

    errors.extend(check_links(text, path))
    return errors, warnings, registry_ids


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    registry_ids: set[str] = set()

    for path in sorted(OPPORTUNITIES.glob("*.md")):
        if path.name == "README.md":
            continue
        opp_errors, opp_warnings = validate_opportunity(path)
        errors.extend(opp_errors)
        warnings.extend(opp_warnings)

    for path in sorted(PORTFOLIO.glob("*.md")):
        port_errors, port_warnings, port_registry = validate_portfolio(path)
        errors.extend(port_errors)
        warnings.extend(port_warnings)
        registry_ids |= port_registry

    warnings.extend(validate_orphan_micro_opportunities(registry_ids))

    if warnings:
        print("Validation warnings:\n")
        for warn in warnings:
            print(f"  - {warn}")
        print()

    if errors:
        print("Validation FAILED:\n")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
