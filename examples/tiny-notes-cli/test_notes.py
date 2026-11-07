"""Stdlib tests for the tiny notes CLI. Run: python -m unittest test_notes.py"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

NOTES = Path(__file__).resolve().parent / "notes.py"


def run_cli(*args: str, store: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(NOTES), "--file", str(store), *args],
        check=False,
        capture_output=True,
        text=True,
    )


class NotesCliTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.store = Path(self.tmp.name) / "notes.json"

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_add_list_and_done(self) -> None:
        added = run_cli("add", "buy milk", store=self.store)
        self.assertEqual(added.returncode, 0)
        self.assertIn("added #1", added.stdout)

        listed = run_cli("list", store=self.store)
        self.assertEqual(listed.returncode, 0)
        self.assertIn("1. [ ] buy milk", listed.stdout)

        done = run_cli("done", "1", store=self.store)
        self.assertEqual(done.returncode, 0)
        self.assertIn("done #1", done.stdout)

        after = run_cli("list", store=self.store)
        self.assertIn("1. [x] buy milk", after.stdout)

    def test_missing_id_exits_nonzero(self) -> None:
        result = run_cli("done", "9", store=self.store)
        self.assertEqual(result.returncode, 1)
        self.assertIn("no note #9", result.stderr)

    def test_empty_list(self) -> None:
        result = run_cli("list", store=self.store)
        self.assertEqual(result.returncode, 0)
        self.assertIn("no notes", result.stdout)


if __name__ == "__main__":
    unittest.main()
