#!/usr/bin/env python3
"""Validate the frozen Time as Finality full-persona panel.

This validates coverage and response structure. Persona agreement remains
interpretive evidence and cannot promote a scientific or source claim.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "explorations" / "2026-07-14-time-as-finality-full-persona-panel"
INDIVIDUAL = PANEL / "individual"

EXPECTED_HEADINGS = [
    "Steelman thesis",
    "Summary of understanding",
    "Strongest insight",
    "Strongest criticism",
    "Hidden assumptions",
    "Rose",
    "Bud",
    "Thorn",
    "Confidence",
    "Suggested experiment",
    "Suggested theorem or mathematical direction",
    "Suggested falsification test",
    "Relationship classification",
]
ALLOWED_RELATIONSHIPS = {"analogy", "homology", "reduction", "equivalence", "none/undetermined"}


def main() -> int:
    errors: list[str] = []
    common_brief = PANEL / "00-common-brief.md"
    addendum = PANEL / "01-posture-addendum-after-panel-freeze.md"

    if not common_brief.is_file():
        errors.append("missing frozen common brief")
    else:
        brief_text = common_brief.read_text(encoding="utf-8")
        if "target_revision: eec6f4a5f0eb" not in brief_text:
            errors.append("common brief must preserve target revision eec6f4a5f0eb")
        if "panel_size: 63" not in brief_text:
            errors.append("common brief must preserve panel size 63")

    if not addendum.is_file():
        errors.append("missing post-freeze North-Star posture addendum")

    files = sorted(INDIVIDUAL.glob("P*.md")) if INDIVIDUAL.is_dir() else []
    if len(files) != 63:
        errors.append(f"expected 63 persona responses, found {len(files)}")

    seen: set[int] = set()
    for path in files:
        match = re.match(r"^P(\d{2})-[a-z0-9-]+\.md$", path.name)
        if not match:
            errors.append(f"invalid persona filename: {path.name}")
            continue

        number = int(match.group(1))
        if number in seen:
            errors.append(f"duplicate persona number P{number:02d}")
        seen.add(number)

        text = path.read_text(encoding="utf-8")
        headings = re.findall(r"^## (.+?)\s*$", text, flags=re.MULTILINE)
        if headings != EXPECTED_HEADINGS:
            errors.append(f"{path.name}: required 13 headings are missing, extra, or out of order")

        word_count = len(re.findall(r"\b\w+[\w'-]*\b", text))
        if not 500 <= word_count <= 1000:
            errors.append(f"{path.name}: word count {word_count} is outside 500-1000")

        confidence = section(text, "Confidence")
        score_match = re.search(r"(?<!\d)(10|[1-9])\s*(?:/\s*10|out of 10)?", confidence, flags=re.IGNORECASE)
        if not score_match:
            errors.append(f"{path.name}: Confidence must contain an integer from 1 to 10")

        relationship = section(text, "Relationship classification").lower()
        if not any(re.search(rf"\b{re.escape(label)}\b", relationship) for label in ALLOWED_RELATIONSHIPS):
            errors.append(f"{path.name}: missing allowed relationship classification")

        if re.search(r"[A-Za-z]:\\", text):
            errors.append(f"{path.name}: public response leaks an absolute Windows path")

    expected_numbers = set(range(1, 64))
    if seen != expected_numbers:
        missing = sorted(expected_numbers - seen)
        extra = sorted(seen - expected_numbers)
        errors.append(f"persona number coverage mismatch; missing={missing}, extra={extra}")

    if errors:
        print(f"FAIL: {len(errors)} persona-panel validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: 63/63 persona responses; exact 13-heading structure; confidence and relationship fields valid")
    return 0


def section(text: str, heading: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


if __name__ == "__main__":
    sys.exit(main())
