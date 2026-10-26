"""Regression checks for evidence preservation and function-oriented Awesome output."""
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from catalog_common import load_records  # noqa: E402
from build_indexes import render_outputs  # noqa: E402


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = [r for _, r in load_records()]

    def test_cockpit_research_snapshot_preserved(self):
        source = (ROOT / "archive/cockpit-research-2026-10-19.md").read_text(encoding="utf-8")
        expected, in_table = set(), False
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
        actual = {(r["name"], r["source_repo"]) for r in self.items if r["kind"] == "extension"}
        self.assertEqual(65, len(expected))
        self.assertEqual(expected, actual)

    def test_six_ai_agents_still_present(self):
        expected = {
            "openclaw": "https://github.com/openclaw/openclaw",
            "hermes-agent": "https://github.com/NousResearch/hermes-agent",
            "agent-zero": "https://github.com/agent0ai/agent-zero",
            "openhands": "https://github.com/OpenHands/OpenHands",
            "paperclip": "https://github.com/paperclipai/paperclip",
            "buzz": "https://github.com/block/buzz",
        }
        actual = {r["id"]: r for r in self.items if r["category"] == "ai-agents"}
        self.assertEqual(set(expected), set(actual))
        for name, source in expected.items():
            self.assertEqual(source, actual[name]["source_repo"])
            self.assertFalse(actual[name]["verification"]["functional_tested"])

    def test_taxonomy_and_editorial_state(self):
        registry = json.loads((ROOT / "schemas/categories.json").read_text(encoding="utf-8"))
        allowed = {item["id"] for item in registry["categories"]}
        self.assertEqual(10, len(allowed))
        self.assertEqual(83, len(self.items))
        self.assertTrue(all(r["category"] in allowed for r in self.items))
        self.assertTrue(all(r["listing_status"] in {"highlighted", "research", "legacy"} for r in self.items))
        self.assertEqual(65, sum(r["kind"] == "extension" for r in self.items))
        self.assertEqual(len(self.items), len({r["id"] for r in self.items}))

    def test_category_pages_cover_every_entry_once(self):
        outputs = render_outputs()
        for record in self.items:
            page = outputs[f"categories/{record['category']}.md"]
            self.assertEqual(1, page.count(f"]({record.get('source_repo') or record.get('website')}) - {record['summary']}"),
                             f"Missing entry from category page: {record['id']}")
        self.assertEqual(65, outputs["integrations/cockpit/README.md"].count("; package:"))

    def test_generated_outputs_committed(self):
        for relative, content in render_outputs().items():
            with self.subTest(file=relative):
                self.assertEqual(content, (ROOT / relative).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
