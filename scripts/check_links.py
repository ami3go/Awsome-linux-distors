#!/usr/bin/env python3
"""Offline check that relative Markdown links in browsable docs resolve."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FILES = [ROOT / "README.md", ROOT / "CONTRIBUTING.md"]
FILES.extend((ROOT / "categories").glob("*.md"))
FILES.extend((ROOT / "integrations").glob("**/*.md"))
FILES.extend((ROOT / "docs").glob("**/*.md"))
FILES.extend((ROOT / "archive").glob("**/*.md"))
LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


def main():
    failures = []
    for path in FILES:
        content = path.read_text(encoding="utf-8")
        for match in LINK.finditer(content):
            url = match.group(1).strip()
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc or url.startswith("mailto:"):
                continue
            if not parsed.path:
                continue
            relative = unquote(parsed.path)
            if relative.startswith("/"):
                failures.append(f"{path}: absolute path {url}")
                continue
            target = (path.parent / relative).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                failures.append(f"{path.relative_to(ROOT)}: missing {url}")
    for failure in failures:
        print("ERROR:", failure, file=sys.stderr)
    print(f"Checked internal targets in {len(FILES)} Markdown files.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
