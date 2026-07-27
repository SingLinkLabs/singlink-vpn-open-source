#!/usr/bin/env python3
"""Check repository-local links in Markdown files."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def target_exists(source: Path, raw_target: str) -> bool:
    target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return True

    clean_target = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not clean_target:
        return True

    destination = ROOT / clean_target.lstrip("/") if clean_target.startswith("/") else source.parent / clean_target
    return destination.resolve().exists()


def main() -> int:
    failures: list[str] = []
    checked = 0

    for source in sorted(ROOT.rglob("*.md")):
        if ".git" in source.parts or "_site" in source.parts:
            continue
        content = source.read_text(encoding="utf-8")
        for raw_target in LINK.findall(content):
            checked += 1
            if not target_exists(source, raw_target):
                failures.append(f"{source.relative_to(ROOT)} -> {raw_target}")

    if failures:
        print("Broken relative links:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Relative link check passed for {checked} links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
