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
OPP_FILENAME = re.compile(r"^OPP-\d{8}-[a-z0-9-]+\.md$")
LINK_PATTERN = re.compile(r"\]\(([^)]+)\)")


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


def validate_opportunity(path: Path) -> list[str]:
    errors: list[str] = []
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

    if status == "decided" and "<!-- Paste output -->" in body:
        errors.append(f"{rel}: decided file contains unresolved template placeholder")

    if status == "decided" and "confidence_level" not in body.split("## Final Decision")[-1]:
        errors.append(f"{rel}: Final Decision section missing confidence_level")

    errors.extend(check_links(text, path))
    return errors


def validate_portfolio(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)

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
    return errors


def main() -> int:
    errors: list[str] = []

    for path in sorted(OPPORTUNITIES.glob("*.md")):
        if path.name == "README.md":
            continue
        errors.extend(validate_opportunity(path))

    for path in sorted(PORTFOLIO.glob("*.md")):
        errors.extend(validate_portfolio(path))

    if errors:
        print("Validation FAILED:\n")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
