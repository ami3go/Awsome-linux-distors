#!/usr/bin/env python3
"""Schema, taxonomy and cross-record consistency validation."""
import json
import sys
from urllib.parse import urlparse

from jsonschema import Draft202012Validator, FormatChecker
from catalog_common import ROOT, load_records


def validate():
    schema = json.loads((ROOT / "schemas/project.schema.json").read_text(encoding="utf-8"))
    categories = json.loads((ROOT / "schemas/categories.json").read_text(encoding="utf-8"))["categories"]
    allowed = {item["id"] for item in categories}
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors, seen, cockpit_count = [], set(), 0
    if set(schema["properties"]["category"]["enum"]) != allowed:
        errors.append("Category registry and JSON Schema disagree.")
    entries = load_records()
    for path, record in entries:
        rel = path.relative_to(ROOT).as_posix()
        for error in validator.iter_errors(record):
            location = ".".join(map(str, error.absolute_path))
            errors.append(f"{rel} [{location or 'record'}]: {error.message}")
        identifier = record.get("id")
        if identifier and path.stem != identifier:
            errors.append(f"{rel}: filename does not match ID {identifier!r}")
        if identifier in seen:
            errors.append(f"{rel}: duplicate ID {identifier!r}")
        seen.add(identifier)
        for field in ("website", "source_repo"):
            if record.get(field):
                url = urlparse(record[field])
                if url.scheme != "https" or not url.netloc:
                    errors.append(f"{rel}: {field} must use HTTPS")
        if record.get("kind") == "extension":
            cockpit_count += 1
            if not rel.startswith("data/extensions/cockpit/"):
                errors.append(f"{rel}: extension must live under data/extensions/cockpit/")
            if record.get("ecosystem") != "cockpit":
                errors.append(f"{rel}: extension ecosystem must be Cockpit")
            if record.get("group") == "historical" and record.get("listing_status") != "legacy":
                errors.append(f"{rel}: historical Cockpit component must be legacy")
        elif rel.startswith("data/extensions/"):
            errors.append(f"{rel}: non-extension stored under extensions")
    if cockpit_count != 65:
        errors.append(f"Cockpit evidence count changed (expected exactly 65, found {cockpit_count}).")
    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        return 1
    print(f"Validated {len(entries)} records in {len(allowed)} functional categories, including {cockpit_count} Cockpit components.")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
