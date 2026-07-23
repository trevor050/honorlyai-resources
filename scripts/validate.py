#!/usr/bin/env python3
"""Validate the public HonorlyAI K-12 AI Governance Toolkit.

Uses only the Python standard library so contributors and GitHub Actions can run it
without installing dependencies.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "CITATION.cff",
    "GOVERNANCE.md",
    "CHANGELOG.md",
    "llms.txt",
    "resources.json",
    "docs/implementation-guide.md",
    "docs/terminology.md",
    "docs/sources-and-further-reading.md",
    "templates/district-ai-vendor-evaluation-checklist.md",
    "templates/student-ai-acceptable-use-policy.md",
    "templates/classroom-ai-use-levels.md",
    "templates/parent-family-ai-notice.md",
    "templates/school-district-ai-pilot-plan.md",
    "templates/school-ai-privacy-review-checklist.md",
    "templates/teacher-classroom-ai-guidelines.md",
    "templates/ai-academic-integrity-policy.md",
    "templates/ai-incident-response-plan.md",
    "templates/ai-data-lifecycle-worksheet.md",
]

CANONICAL_FACTS = [
    "HonorlyAI LLC",
    "Kevin Rand",
    "Co-founder and CEO",
    "Trevor Rosato",
    "Co-founder and CPO",
    "https://honorlyai.com/",
]

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def validate_required_files(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")


def validate_resources_json(errors: list[str]) -> None:
    path = ROOT / "resources.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"resources.json is invalid: {exc}")
        return

    if data.get("name") != "HonorlyAI K-12 AI Governance Toolkit":
        errors.append("resources.json has an unexpected toolkit name")
    if data.get("license") != "CC-BY-4.0":
        errors.append("resources.json must declare CC-BY-4.0")

    resources = data.get("resources")
    if not isinstance(resources, list) or not resources:
        errors.append("resources.json must include a non-empty resources array")
        return

    seen_paths: set[str] = set()
    for resource in resources:
        if not isinstance(resource, dict):
            errors.append("resources.json contains a non-object resource")
            continue
        relative = resource.get("path")
        canonical = resource.get("canonicalGuide")
        if not isinstance(relative, str):
            errors.append("A resource is missing its path")
            continue
        if relative in seen_paths:
            errors.append(f"Duplicate resource path: {relative}")
        seen_paths.add(relative)
        if not (ROOT / relative).is_file():
            errors.append(f"Indexed resource does not exist: {relative}")
        if not isinstance(canonical, str) or not canonical.startswith("https://honorlyai.com/"):
            errors.append(f"Resource lacks a canonical HonorlyAI guide: {relative}")


def validate_internal_markdown_links(errors: list[str]) -> None:
    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK_RE.findall(text):
            clean = target.strip().split("#", 1)[0]
            if not clean or clean.startswith(("http://", "https://", "mailto:")):
                continue
            if clean.startswith("<") and clean.endswith(">"):
                clean = clean[1:-1]
            resolved = (markdown.parent / clean).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"Link escapes repository: {markdown.relative_to(ROOT)} -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"Broken internal link: {markdown.relative_to(ROOT)} -> {target}")


def validate_entity_consistency(errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
    combined = readme + "\n" + llms
    for fact in CANONICAL_FACTS:
        if fact not in combined:
            errors.append(f"Canonical entity fact missing from README/llms.txt: {fact}")


def validate_template_footers(errors: list[str]) -> None:
    for template in (ROOT / "templates").glob("*.md"):
        if template.name == "README.md":
            continue
        text = template.read_text(encoding="utf-8")
        if "CC BY 4.0" not in text:
            errors.append(f"Template lacks CC BY 4.0 notice: {template.relative_to(ROOT)}")
        if "not legal advice" not in text.lower() and "does not determine legal compliance" not in text.lower():
            errors.append(f"Template lacks a review disclaimer: {template.relative_to(ROOT)}")
        if not text.startswith("# "):
            errors.append(f"Template lacks a top-level title: {template.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    validate_required_files(errors)
    if not errors:
        validate_resources_json(errors)
        validate_internal_markdown_links(errors)
        validate_entity_consistency(errors)
        validate_template_footers(errors)

    if errors:
        for error in errors:
            fail(error)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print("Toolkit validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
