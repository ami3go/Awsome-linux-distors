"""Regression checks for the original 65-entry Cockpit research snapshot."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from catalog_common import load_records  # noqa: E402
from build_indexes import render_outputs  # noqa: E402


class CatalogTests(unittest.TestCase):
    def test_original_cockpit_research_preserved(self):
        source = (ROOT / "COCKPIT_PLUGINS.md").read_text(encoding="utf-8")
        expected = set()
        in_table = False
        for line in source.splitlines():
            if line.startswith("## "):
                in_table = line[3:].strip() not in (
                    "Research sources", "Best starting points for headless Debian",
                    "Debian discovery commands", "Notes on completeness and maintenance")
            if not in_table or not line.startswith("| ") or line.startswith("| ---") or line.startswith("| Project"):
                continue
            cells = [c.strip() for c in line.split("|")[1:-1]]
            match = re.search(r"\]\((https?://[^)]+)\)", cells[1])
            if match:
                expected.add((cells[0], match.group(1)))
        actual = {(r["name"], r["source_repo"]) for _, r in load_records()
                  if r.get("kind") == "extension"}
        self.assertEqual(65, len(expected), "Unexpected source snapshot size")
        self.assertEqual(expected, actual, "Entry names/source URLs changed or were lost")

    def test_generated_outputs_committed(self):
        for relative, content in render_outputs().items():
            with self.subTest(path=relative):
                self.assertEqual(content, (ROOT / relative).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
