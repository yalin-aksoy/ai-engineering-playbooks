#!/usr/bin/env python3
"""Check that playbook Markdown files contain the required sections."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PLAYBOOKS_DIR = ROOT / "playbooks"
REQUIRED_SECTIONS = (
    "Objective",
    "When to use",
    "Preconditions",
    "Execution steps",
    "Constraints",
    "Critical events",
    "Verification",
    "Expected output",
)


def main() -> int:
    files = sorted(PLAYBOOKS_DIR.glob("*.md"))
    if not files:
        print(f"No playbook Markdown files found in {PLAYBOOKS_DIR}", file=sys.stderr)
        return 1

    failures = 0
    for path in files:
        content = path.read_text(encoding="utf-8")
        headings = {
            match.group(1).strip().casefold()
            for match in re.finditer(r"^##\s+(.+?)\s*#*\s*$", content, re.MULTILINE)
        }
        missing = [section for section in REQUIRED_SECTIONS if section.casefold() not in headings]
        if missing:
            failures += 1
            print(f"{path.relative_to(ROOT)}: missing sections: {', '.join(missing)}")
        else:
            print(f"{path.relative_to(ROOT)}: OK")

    if failures:
        print(f"Validation failed: {failures} playbook(s) need attention.", file=sys.stderr)
        return 1

    print(f"Validated {len(files)} playbook(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
