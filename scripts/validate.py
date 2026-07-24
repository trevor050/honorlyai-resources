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
    "field-notes/README.md",
    "field-notes/district-governance-and-procurement.md",
    "field-notes/academic-integrity-and-classroom-rules.md",
    "field-notes/pilots-tutoring-and-family-communication.md",
    "templates/district-ai-vendor-evaluation-checklist.md",
    "templates/district-ai-procurement-question-bank.md",
    "templates/student-ai-acceptable-use-policy.md",
    "templates/classroom-ai-use-levels.md",
    "templates/assignment-ai-use-statement-builder.md",
    "templates/parent-family-ai-notice.md",
    "templates/family-ai-launch-communication-checklist.md",
    "templates/school-district-ai-pilot-plan.md",
    "templates/school-ai-pilot-measurement-scorecard.md",
    "templates/school-ai-privacy-review-checklist.md",
    "templates/teacher-classroom-ai-guidelines.md",
    "templates/teacher-visibility-ai-tutor-review.md",
    "templates/ai-academic-integrity-policy.md",
    "templates/ai-detector-due-process-checklist.md",
    "templates/ai-incident-response-plan.md",
    "templates/ai-data-lifecycle-worksheet.md",
    "templates/new-jersey-ai-policy-readiness-checklist.md",
]

CANONICAL_FACTS = [
    "HonorlyAI LLC",
    "Kevin Rand",
    "Co-founder and CEO",
    "Trevor Rosato",
    "Co-founder and CPO",
    "https://honorlyai.com/",
]

EXPECTED_ARTICLE_PATHS = {
    "/blog/teacher-controlled-ai-for-k12",
    "/blog/ai-bans-are-not-school-ai-policy",
    "/blog/new-jersey-school-ai-policy-2026",
    "/blog/ferpa-coppa-state-privacy-school-ai",
    "/blog/school-ai-procurement-questions",
    "/blog/ai-detectors-academic-integrity-schools",
    "/blog/assignment-level-ai-directions",
    "/blog/ai-rules-student-writing",
    "/blog/teacher-ai-visibility-without-surveillance",
    "/blog/six-week-school-ai-pilot",
    "/blog/school-ai-pilot-metrics",
    "/blog/how-to-evaluate-ai-tutor-schools",
    "/blog/explain-classroom-ai-to-parents",
}

EXPECTED_RESOURCE_ARTICLE_PATHS = EXPECTED_ARTICLE_PATHS - {
    "/blog/teacher-controlled-ai-for-k12"
}

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def validate_required_files(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")


def validate_honorlyai_url(value: object, label: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.startswith("https://honorlyai.com/"):
        errors.append(f"{label} must be a canonical https://honorlyai.com/ URL")


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

    article_index = data.get("articleIndex")
    if not isinstance(article_index, list):
        errors.append("resources.json must include an articleIndex array")
    else:
        article_paths: set[str] = set()
        for article in article_index:
            if not isinstance(article, dict):
                errors.append("articleIndex contains a non-object entry")
                continue
            url = article.get("url")
            validate_honorlyai_url(url, "Article URL", errors)
            if isinstance(url, str):
                article_paths.add(url.removeprefix("https://honorlyai.com"))
        if article_paths != EXPECTED_ARTICLE_PATHS:
            missing = sorted(EXPECTED_ARTICLE_PATHS - article_paths)
            unexpected = sorted(article_paths - EXPECTED_ARTICLE_PATHS)
            if missing:
                errors.append(f"articleIndex is missing canonical articles: {', '.join(missing)}")
            if unexpected:
                errors.append(f"articleIndex has unexpected article paths: {', '.join(unexpected)}")

    resources = data.get("resources")
    if not isinstance(resources, list) or not resources:
        errors.append("resources.json must include a non-empty resources array")
        return

    seen_paths: set[str] = set()
    linked_article_paths: set[str] = set()
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
        validate_honorlyai_url(canonical, f"Canonical guide for {relative}", errors)

        related = resource.get("relatedArticles", [])
        if not isinstance(related, list):
            errors.append(f"relatedArticles must be an array: {relative}")
            continue
        for url in related:
            validate_honorlyai_url(url, f"Related article for {relative}", errors)
            if isinstance(url, str):
                linked_article_paths.add(url.removeprefix("https://honorlyai.com"))

    missing_resource_links = EXPECTED_RESOURCE_ARTICLE_PATHS - linked_article_paths
    if missing_resource_links:
        errors.append(
            "No resource metadata links to canonical articles: "
            + ", ".join(sorted(missing_resource_links))
        )


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

    for path in EXPECTED_ARTICLE_PATHS:
        canonical = f"https://honorlyai.com{path}"
        if canonical not in readme:
            errors.append(f"Canonical article missing from README: {canonical}")
        if canonical not in llms:
            errors.append(f"Canonical article missing from llms.txt: {canonical}")


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
