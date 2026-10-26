#!/usr/bin/env python3
"""Validate catalog records against the JSON Schema and catalog invariants."""
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

from jsonschema import Draft202012Validator, FormatChecker
from catalog_common import ROOT, load_records


def validate():
    schema = json.loads((ROOT / "schemas/project.schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    seen = set()
    components = 0
    items = load_records()
    for path, record in items:
        rel = path.relative_to(ROOT).as_posix()
        for error in validator.iter_errors(record):
            location = ".".join(map(str, error.absolute_path))
            errors.append(f"{rel} [{location or 'record'}]: {error.message}")
        identifier = record.get("id")
        if identifier and path.stem != identifier:
            errors.append(f"{rel}: filename does not match id {identifier!r}")
        if identifier in seen:
            errors.append(f"{rel}: duplicate id {identifier!r}")
        seen.add(identifier)
        for field in ("website", "source_repo"):
            if record.get(field):
                url = urlparse(record[field])
                if url.scheme != "https" or not url.netloc:
                    errors.append(f"{rel}: {field} must use HTTPS")
        kind = record.get("kind")
        if kind == "extension":
            components += 1
            if not rel.startswith("data/extensions/cockpit/"):
                errors.append(f"{rel}: extension must live under data/extensions/cockpit/")
            if record.get("ecosystem") != "cockpit":
                errors.append(f"{rel}: extension ecosystem must be cockpit")
        if kind != "extension" and rel.startswith("data/extensions/"):
            errors.append(f"{rel}: non-extension stored in extensions directory")
    if components < 65:
        errors.append(f"Cockpit migration lost entries: expected at least 65, found {components}")
    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        return 1
    print(f"Validated {len(items)} records, including {components} Cockpit components.")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
