"""Synthetic Git checkout tests for the canonical integrity-index writer."""

from __future__ import annotations

import csv
import subprocess
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path

from tools.refresh_integrity_indexes import main


class IntegrityIndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)
        subprocess.run(["git", "init", "--quiet", str(self.root)], check=True)
        (self.root / "alpha.txt").write_text("initial\n", encoding="utf-8")
        (self.root / "spaced name.txt").write_text("second\n", encoding="utf-8")
        subprocess.run(
            ["git", "-C", str(self.root), "add", "alpha.txt", "spaced name.txt"],
            check=True,
        )

    def run_tool(self, option: str) -> int:
        with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            return main(["--root", str(self.root), option])

    def test_writing_and_verifying_a_clean_index(self) -> None:
        self.assertEqual(1, self.run_tool("--check"))
        self.assertEqual(0, self.run_tool("--write"))
        self.assertEqual(0, self.run_tool("--check"))

        with (self.root / "MANIFEST.csv").open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(["alpha.txt", "spaced name.txt"], [row["path"] for row in rows])
        self.assertEqual(2, len((self.root / "SHA256SUMS.txt").read_text().splitlines()))

    def test_content_changes_invalidate_both_indexes(self) -> None:
        self.assertEqual(0, self.run_tool("--write"))
        (self.root / "alpha.txt").write_text("modified\n", encoding="utf-8")
        self.assertEqual(1, self.run_tool("--check"))
        self.assertEqual(0, self.run_tool("--write"))
        self.assertEqual(0, self.run_tool("--check"))

    def test_new_tracked_files_invalidate_indexes(self) -> None:
        self.assertEqual(0, self.run_tool("--write"))
        (self.root / "new.txt").write_text("tracked", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.root), "add", "new.txt"], check=True)
        self.assertEqual(1, self.run_tool("--check"))
        self.assertEqual(0, self.run_tool("--write"))
        self.assertEqual(0, self.run_tool("--check"))


if __name__ == "__main__":
    unittest.main()
