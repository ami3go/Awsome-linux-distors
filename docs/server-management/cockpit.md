# Cockpit server management

[Cockpit](https://cockpit-project.org/) is a web administration console for Linux hosts. The [generated Cockpit catalog](../../generated/cockpit-plugins.md) contains 65 original research entries, with a source link, stated package name (when listed), group, and notes for each.

The original [Cockpit research document](../../COCKPIT_PLUGINS.md) includes important installation caveats, ten Debian-oriented choices, and references. It is preserved as a historical snapshot; new records should go under `data/extensions/cockpit/`.

**Security:** Extensions may have privileged host access. Check the upstream project, last release, package source, dependency compatibility, and authentication before deploying. Treat `package_name` as a reported identifier, not proof of APT availability.

**Debian:** Inspect package availability locally (for example with `apt-cache policy cockpit cockpit-files`). Prefer distro repositories/backports where appropriate and inspect third-party code before granting access.
