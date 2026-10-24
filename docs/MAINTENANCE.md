# Catalog maintenance and evidence policy

The YAML records are the **source of truth**; Markdown and JSON in `generated/` are automatically produced. `COCKPIT_PLUGINS.md` remains an unchanged archival snapshot from 2026-10-19.

## Verification levels

- **Official documentation**: a fact checked on a project-controlled page; it is not an installation or performance test.
- **Repository listing**: an unverified link/listing captured from the previous README.
- **Research snapshot**: an entry transcribed from the previous 65-row Cockpit research catalog.
- **Functional tested**: true only after a documented local installation or hardware test, with environment/evidence tracked separately.

An upstream project's package name does **not** prove its availability in Debian, Ubuntu, Fedora, or any particular release. Check distro repositories before publishing packaging claims.

## Updating a record

Edit `data/**/*.yaml`; retain the historical catalog. Run `python scripts/validate_catalog.py`, `python scripts/build_indexes.py`, and `python -m unittest discover -s tests -v`. GitHub Actions checks schema validity, deterministic exports, and the migration's preservation of all 65 historical entries.

## Future work

Add optional periodic URL checks (external sites sometimes rate-limit requests); a maintenance-state dashboard with last-commit dates; and verified CPU/RAM compatibility measurements. Do not infer hardware suitability from marketing claims.
