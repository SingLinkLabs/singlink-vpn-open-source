#!/usr/bin/env python3
"""Fail publication when the repository contains blocked files or secret-like data."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAX_PUBLIC_FILE_BYTES = 5 * 1024 * 1024

BLOCKED_EXTENSIONS = {
    ".7z", ".aab", ".apk", ".bak", ".backup", ".cer", ".crt", ".db", ".dmg",
    ".env", ".exe", ".gz", ".ipa", ".jks", ".key", ".keystore", ".mobileprovision",
    ".msi", ".p12", ".pem", ".pfx", ".pkg", ".sql", ".sqlite", ".sqlite3", ".tar",
    ".tgz", ".zip",
}

PRODUCT_SOURCE_EXTENSIONS = {
    ".c", ".cc", ".cpp", ".cs", ".dart", ".go", ".h", ".hpp", ".java", ".js",
    ".jsx", ".kt", ".kts", ".m", ".mm", ".php", ".rs", ".swift", ".ts", ".tsx",
    ".vue",
}

BLOCKED_BASENAMES = {
    ".env", "credentials", "credentials.json", "id_ed25519", "id_rsa",
    "production.json", "secrets.json", "service-account.json",
}

BLOCKED_PATH_PARTS = {
    "admin", "backend", "billing", "credentials", "internal", "nodes", "payment",
    "private", "production", "secrets",
}

CODE_ALLOWED_PREFIXES = ("tools/", "tests/")

SECRET_PATTERNS = {
    "private key block": re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
    "GitHub token": re.compile(r"(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}"),
    "GitHub fine-grained token": re.compile(r"github_pat_[A-Za-z0-9_]{50,}"),
    "Stripe live secret": re.compile(r"(?:sk|rk)_live_[A-Za-z0-9]{16,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
}

SCAN_EXCLUSIONS = {"tools/publication_guard.py"}

PUBLIC_IMAGE_EXTENSIONS = {".gif", ".jpeg", ".jpg", ".png", ".webp"}


def has_valid_public_image_signature(path: Path, suffix: str) -> bool:
    """Accept only known web-image formats instead of arbitrary binary files."""
    header = path.read_bytes()[:16]
    if suffix == ".png":
        return header.startswith(b"\x89PNG\r\n\x1a\n")
    if suffix in {".jpg", ".jpeg"}:
        return header.startswith(b"\xff\xd8\xff")
    if suffix == ".gif":
        return header.startswith((b"GIF87a", b"GIF89a"))
    if suffix == ".webp":
        return (
            len(header) >= 12
            and header.startswith(b"RIFF")
            and header[8:12] == b"WEBP"
        )
    return False


def repository_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [ROOT / line for line in result.stdout.splitlines() if line.strip()]


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_path(path: Path) -> list[str]:
    errors: list[str] = []
    rel = relative(path)
    lowered_parts = {part.lower() for part in Path(rel).parts[:-1]}
    suffix = path.suffix.lower()
    basename = path.name.lower()

    if path.is_symlink():
        errors.append(f"{rel}: symbolic links are not permitted")
        return errors

    if basename in BLOCKED_BASENAMES or basename.startswith(".env."):
        errors.append(f"{rel}: blocked sensitive filename")

    if suffix in BLOCKED_EXTENSIONS:
        errors.append(f"{rel}: blocked file type {suffix}")

    if lowered_parts.intersection(BLOCKED_PATH_PARTS):
        errors.append(f"{rel}: blocked private/internal path")

    if suffix in PRODUCT_SOURCE_EXTENSIONS and not rel.startswith(CODE_ALLOWED_PREFIXES):
        errors.append(f"{rel}: product-source file type is outside approved public tools")

    if path.stat().st_size > MAX_PUBLIC_FILE_BYTES:
        errors.append(f"{rel}: exceeds the 5 MiB public-file limit")

    if rel in SCAN_EXCLUSIONS or not path.is_file():
        return errors

    if suffix in PUBLIC_IMAGE_EXTENSIONS:
        if not has_valid_public_image_signature(path, suffix):
            errors.append(f"{rel}: invalid {suffix} image signature")
        return errors

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"{rel}: binary or non-UTF-8 content is not permitted")
        return errors

    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(content):
            errors.append(f"{rel}: possible {label}")

    return errors


def main() -> int:
    os.chdir(ROOT)
    files = repository_files()
    errors = [error for path in files for error in check_path(path)]

    if errors:
        print("Publication guard failed:", file=sys.stderr)
        for error in sorted(errors):
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Publication guard passed for {len(files)} public files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
