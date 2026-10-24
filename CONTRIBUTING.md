# Contributing to Awesome Linux Catalog

The authoritative records are YAML files under `data/`. Do **not** edit generated Markdown or JSON directly.

1. Choose the appropriate directory (`distributions`, `os-images`, `software`, `resources`, or `extensions/cockpit`).
2. Add one `id.yaml` file. Keep `id` stable, lowercase, and hyphen-separated; make filename match `id`.
3. Include a concise summary, at least one HTTPS project URL, and a `verification` block with the source and review date.
4. Document installation/package details only when verified for that distribution; otherwise use `package_availability: unverified`. Never imply an extension was tested merely because it was listed.
5. Execute the commands in the README; commit regenerated files alongside source changes.

## Evidence terminology

- `official-documentation`: project-controlled documentation was inspected.
- `repository-listing`: a project link was collected, but claims beyond that listing were not independently tested.
- `research-snapshot`: an entry inherited from the historical Cockpit catalog, with the recorded source and date.
- `functional_tested: false`: not installed, benchmarked, or hardware verified for this catalog.

Do not silently treat a package name as proof that a package is available in Debian APT.
Report links, outdated projects, and alternatives with source URLs and dates.
