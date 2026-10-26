# Catalog architecture, curation and evidence

The root [README](../README.md) is the **hand-curated entry point**, organized by Linux/homelab use case and showing direct project links. It must not become a raw dump of the entire inventory.

The `data/` YAML files are the source of truth for 83 historical records (expandable). `categories/*.md`, `integrations/cockpit/README.md`, and `generated/*` are **generated views**. Run `python scripts/build_indexes.py` and commit all affected files together.

## Taxonomy

Exactly one `category` is required; categories and their descriptions live in `schemas/categories.json`. Classify Cockpit extensions according to what they **do**, not by vendor. The `ecosystem: cockpit` relation is used to build a cross-cutting Cockpit directory without duplicating source records.

`listing_status` is an editorial distinction (`highlighted`, `research`, or `legacy`) and not an installation test or endorsement. `verification.level` distinguishes `official-documentation`, `repository-listing`, and `research-snapshot`; `verification.functional_tested: false` means no functional qualification was performed.

## Archived evidence

The [original Cockpit study](../archive/cockpit-research-2026-10-19.md) is preserved verbatim, including Debian caveats and the original ten recommendations, distinct from the 65 entries. A compatibility pointer is retained in `COCKPIT_PLUGINS.md`.

## Required checks

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_catalog.py
python scripts/build_indexes.py --check
python scripts/check_links.py
python -m unittest discover -s tests -v
```

`awesome-lint` checks the main Awesome-style README separately in GitHub Actions. Internal Markdown targets must resolve. External link checks should be treated cautiously because host rate limits, network policies and provider outages can cause false positives.

## Known limitations

The license remains GPL-3.0 and is **not** the preferred CC license for inclusion in sindresorhus/awesome. The current catalog also contains untested third-party extensions; the highlights must not be mistaken for independently assessed installation recommendations.
