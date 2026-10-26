# Contributing to Awesome Linux Homelab

This is a focused directory of Linux workstation, homelab, mini-server and self-hosted administration tools. Prefer well-documented software that solves a distinct use case. Do not add every search result: the list is **selective**, and research-only links are visibly marked as such.

## Suggesting an entry

1. Check the [full catalog](generated/software-index.md) for duplicates or alternatives.
2. Describe the Linux/homelab task the project solves, provide its upstream source link and explain why it belongs in the proposed category.
3. Supply evidence from official docs or a relevant project repository. Note software versions, tested distributions and dates when claiming compatibility.
4. Do not present undocumented packages as Debian-installable. Avoid benchmark claims without reproducible measurements.
5. Update or create a YAML record under `data/`. Set exactly one functional `category` and `listing_status` (`highlighted`, `research`, or `legacy`). A project can use tags and an `ecosystem` relation without duplicating the record in multiple categories.
6. Regenerate outputs and run all checks; submit the YAML, generated pages and tests in one pull request.

## Editorial status

- `highlighted` - A compact editorial starting point on reader-facing pages; not proof of hands-on testing or a security review.
- `research` - A documented alternative awaiting stronger independent verification or editorial selection.
- `legacy` - A historical reference retained for comparison, not a deployment suggestion.

The `verification` block separately records **what was actually checked**. Never confuse an official project description with a successful installation or hardware test.

## Local validation

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_catalog.py
python scripts/build_indexes.py
python scripts/build_indexes.py --check
python scripts/check_links.py
python -m unittest discover -s tests -v
npx awesome-lint
```

`data/` is authoritative. Do not manually edit `categories/`, `integrations/cockpit/README.md` or `generated/`. Keep legacy link compatibility for research relocated into `archive/`.

## Scope and licensing

Links to Linux platforms and self-hosted automation fit the scope; unrelated platforms belong under Further Resources or should be excluded. The repository's existing GPL-3.0 license has not been changed; changing it requires a separate review of documentation rights and code licensing.
