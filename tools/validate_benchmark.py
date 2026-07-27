#!/usr/bin/env python3
"""Validate a public SingLink VPN benchmark CSV without third-party packages."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path

REQUIRED_COLUMNS = [
    "test_id",
    "tested_at_utc",
    "client_version",
    "platform",
    "protocol_label",
    "country",
    "network_type",
    "sample_count",
    "latency_ms_median",
    "jitter_ms_p95",
    "packet_loss_pct",
    "download_mbps_median",
    "upload_mbps_median",
    "connection_success_pct",
    "reconnect_ms_median",
    "methodology_version",
    "evidence_level",
]

NON_NEGATIVE_FIELDS = {
    "latency_ms_median",
    "jitter_ms_p95",
    "download_mbps_median",
    "upload_mbps_median",
    "reconnect_ms_median",
}

PERCENT_FIELDS = {"packet_loss_pct", "connection_success_pct"}
EVIDENCE_LEVELS = {"internal-test", "reproduced-result", "third-party-assessment"}


def parse_utc(value: str) -> None:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp must include a UTC offset")


def validate_row(row: dict[str, str], row_number: int, seen_ids: set[str]) -> list[str]:
    errors: list[str] = []

    for field in REQUIRED_COLUMNS:
        if not row.get(field, "").strip():
            errors.append(f"row {row_number}: {field} is required")

    test_id = row.get("test_id", "").strip()
    if test_id:
        if test_id in seen_ids:
            errors.append(f"row {row_number}: duplicate test_id {test_id}")
        seen_ids.add(test_id)

    try:
        parse_utc(row.get("tested_at_utc", ""))
    except (ValueError, TypeError):
        errors.append(f"row {row_number}: tested_at_utc must be an ISO-8601 timestamp with offset")

    try:
        if int(row.get("sample_count", "0")) < 1:
            raise ValueError
    except ValueError:
        errors.append(f"row {row_number}: sample_count must be a positive integer")

    for field in NON_NEGATIVE_FIELDS:
        try:
            if float(row.get(field, "-1")) < 0:
                raise ValueError
        except ValueError:
            errors.append(f"row {row_number}: {field} must be a non-negative number")

    for field in PERCENT_FIELDS:
        try:
            value = float(row.get(field, "-1"))
            if not 0 <= value <= 100:
                raise ValueError
        except ValueError:
            errors.append(f"row {row_number}: {field} must be between 0 and 100")

    evidence_level = row.get("evidence_level", "")
    if evidence_level not in EVIDENCE_LEVELS:
        errors.append(
            f"row {row_number}: evidence_level must be one of {sorted(EVIDENCE_LEVELS)}"
        )

    return errors


def validate(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        actual = reader.fieldnames or []
        if actual != REQUIRED_COLUMNS:
            return ["CSV header does not exactly match the published schema"]

        errors: list[str] = []
        seen_ids: set[str] = set()
        for row_number, row in enumerate(reader, start=2):
            errors.extend(validate_row(row, row_number, seen_ids))
        return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()

    errors = validate(args.csv_file)
    if errors:
        for error in errors:
            print(error)
        return 1

    print(f"Valid benchmark CSV: {args.csv_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
