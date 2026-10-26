# Awesome Linux Catalog

A curated, source-linked catalog of Linux distributions, OS image ecosystems, administration software, AI-agent platforms, remote-access tools, utilities and Cockpit components.

> **Evidence policy:** A link is not evidence that software was installed, tested, maintained, secure, or available in Debian repositories. See [verification rules](docs/MAINTENANCE.md).

## Browse

| Area | Catalog | Guide |
| --- | --- | --- |
| Distributions and atomic-image ecosystems | [Distribution/software index](generated/software-index.md) | [Distribution notes](docs/distributions/index.md) |
| Linux tools and curated resource directories | [Software index](generated/software-index.md) | [Software notes](docs/software/index.md) |
| AI agents and orchestration | [AI agent entries](generated/software-index.md) | [AI agent guide](docs/software/ai-agents.md) |
| Cockpit server management | [65-entry Cockpit catalog](generated/cockpit-plugins.md) | [Cockpit guide](docs/server-management/cockpit.md) |
| Remote browser and desktop tools | [Remote-access entries](generated/software-index.md) | [Remote browser projects and screenshots](docs/remote-access/browser-in-browser.md) |
| Mini PC and headless deployments | [Software index](generated/software-index.md) | [Mini PC notes](docs/hardware/mini-pc.md) |

## The data model

- **`data/`** contains one YAML record per project, with a stable ID, category, URLs, and evidence.
- **`schemas/project.schema.json`** defines the allowed fields and categories.
- **`generated/`** contains reproducible [JSON](generated/catalog.json) and Markdown views.
- **`scripts/`** validates records and builds generated catalogs.
- **`COCKPIT_PLUGINS.md`** is retained unchanged as the original 19 October 2026 research snapshot. It is **not** the editable data source for future updates.

Cockpit's 65 research entries have individual records in [`data/extensions/cockpit/`](data/extensions/cockpit/). The original 10 Debian recommendations are guidance, **not** ten more independent plugins.

## Quick choices

- [Debian](https://www.debian.org/) — general-purpose distribution for desktops and servers.
- [Rhino Linux](https://rhinolinux.org/) — **Ubuntu-based**, rolling release. Not a direct Debian derivative.
- [Universal Blue](https://universal-blue.org/) — a **Fedora-based image ecosystem**, not one standalone distro.
- [Cockpit](https://cockpit-project.org/) — native Linux server web console.
- [Ventoy](https://www.ventoy.net/en/index.html) — prepare bootable USB media with multiple images.

## Contributing and validation

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [the schema](schemas/project.schema.json). Install Python dependencies and run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_catalog.py
python scripts/build_indexes.py
python scripts/build_indexes.py --check
python -m unittest discover -s tests -v
```

GitHub Actions performs the validation and regression checks for pull requests. The catalogs are discovery resources, not an endorsement or guarantee of package availability.
