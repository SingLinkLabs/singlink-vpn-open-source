import csv
import tempfile
import unittest
from pathlib import Path

from tools.validate_benchmark import REQUIRED_COLUMNS, validate


class BenchmarkValidatorTests(unittest.TestCase):
    def write_csv(self, rows):
        handle = tempfile.NamedTemporaryFile(mode="w", newline="", suffix=".csv", delete=False)
        with handle:
            writer = csv.DictWriter(handle, fieldnames=REQUIRED_COLUMNS)
            writer.writeheader()
            writer.writerows(rows)
        self.addCleanup(Path(handle.name).unlink)
        return Path(handle.name)

    def valid_row(self):
        return {
            "test_id": "example-001",
            "tested_at_utc": "2026-07-27T12:00:00Z",
            "client_version": "example",
            "platform": "example-platform",
            "protocol_label": "example-protocol",
            "country": "HK",
            "network_type": "fixed",
            "sample_count": "10",
            "latency_ms_median": "20",
            "jitter_ms_p95": "5",
            "packet_loss_pct": "0",
            "download_mbps_median": "100",
            "upload_mbps_median": "30",
            "connection_success_pct": "100",
            "reconnect_ms_median": "500",
            "methodology_version": "1.0",
            "evidence_level": "internal-test",
        }

    def test_header_only_template_is_valid(self):
        self.assertEqual(validate(self.write_csv([])), [])

    def test_valid_row(self):
        self.assertEqual(validate(self.write_csv([self.valid_row()])), [])

    def test_rejects_invalid_percentage(self):
        row = self.valid_row()
        row["packet_loss_pct"] = "101"
        self.assertTrue(any("packet_loss_pct" in error for error in validate(self.write_csv([row]))))

    def test_rejects_duplicate_test_ids(self):
        row = self.valid_row()
        errors = validate(self.write_csv([row, row]))
        self.assertTrue(any("duplicate test_id" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
