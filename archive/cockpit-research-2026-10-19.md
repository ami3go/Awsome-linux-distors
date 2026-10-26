# Cockpit Web Console — Plugin and Extension Catalog

**Researched:** 19 October 2026  
**Catalog:** 65 source-linked entries across 7 sections.

> This is a broad, manually curated discovery snapshot, not a guaranteed exhaustive inventory or a claim that every project is currently maintained, secure, packaged for Debian, or compatible with your installed Cockpit release. Plugins were not installed or functionally tested.

Scope: [Cockpit Linux server web console](https://cockpit-project.org/) **not Cockpit CMS**. The third-party entries from the official Cockpit site are indexed there, but are not first-party Cockpit software.

## Research sources

- [Official Cockpit applications directory](https://cockpit-project.org/applications.html) — principal source for the first four sections.
- [Cockpit upstream organization](https://github.com/cockpit-project) and [Starter Kit](https://github.com/cockpit-project/starter-kit).
- [mietzen independent extension collection](https://github.com/mietzen/cockpit-plugins) — 4 distinct available packages.
- [Debian Trixie backports administrative packages](https://packages.debian.org/trixie-backports/admin/) — representative Debian package listings.
- [GitHub cockpit topic](https://github.com/topics/cockpit) — includes unrelated CMS and aviation repositories; do not treat every hit as a plugin.

**Package caveat:** A package name here reflects the source listing, not proof that it is available via Debian APT. A dash means the package identifier was not confirmed. Installing extensions can grant privileged host access. Inspect source, package provenance, releases, dependencies, and system compatibility before deployment.

## Cockpit project (first-party)

| Project | Source code | Package name (if documented) | Purpose / caution |
|---|---|---|---|
| Storage | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | `cockpit-storaged` | Partitions, LUKS, RAID, NFS, iSCSI |
| Networking | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | `cockpit-networkmanager` | NetworkManager networks and firewall |
| Software Updates | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | `cockpit-packagekit` | PackageKit-based updates |
| OSTree Updates | [cockpit-project/cockpit-ostree](https://github.com/cockpit-project/cockpit-ostree) | `cockpit-ostree` | OSTree/immutable OS updates |
| Virtual Machines | [cockpit-project/cockpit-machines](https://github.com/cockpit-project/cockpit-machines) | `cockpit-machines` | KVM/libvirt virtual machine management |
| Podman Containers | [cockpit-project/cockpit-podman](https://github.com/cockpit-project/cockpit-podman) | `cockpit-podman` | Podman container management; not Docker |
| SELinux | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | `cockpit-selinux` | SELinux exceptions and audit reports |
| Kernel Dump | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | `cockpit-kdump` | Kdump configuration |
| Diagnostic Reports | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | `cockpit-sosreport` | System diagnostic collection |
| Cockpit Files | [cockpit-project/cockpit-files](https://github.com/cockpit-project/cockpit-files) | `cockpit-files` | Integrated file manager |

## Red Hat-developed

| Project | Source code | Package name (if documented) | Purpose / caution |
|---|---|---|---|
| Image Builder | [osbuild/image-builder-frontend](https://github.com/osbuild/image-builder-frontend) | `cockpit-image-builder` | Build operating system images |
| 389 Directory Server | [389ds/389-ds-base](https://github.com/389ds/389-ds-base) | `cockpit-389-ds` | 389 Directory Server LDAP UI; source project linked |
| Session Recording | [Scribery/cockpit-session-recording](https://github.com/Scribery/cockpit-session-recording) | `cockpit-session-recording` | Session recording and playback |
| RHEL Subscription Manager | [cockpit-project/subscription-manager-cockpit](https://github.com/cockpit-project/subscription-manager-cockpit) | `subscription-manager-cockpit` | RHEL subscriptions; RHEL-specific |
| High Availability Cluster | [ClusterLabs/pcs-web-ui](https://github.com/ClusterLabs/pcs-web-ui) | `cockpit-ha-cluster` | Pacemaker/PCS cluster management |

## SUSE/openSUSE-developed

| Project | Source code | Package name (if documented) | Purpose / caution |
|---|---|---|---|
| Transactional Updates | [openSUSE/cockpit-tukit](https://github.com/openSUSE/cockpit-tukit) | `cockpit-tukit` | SUSE transactional OS updates |
| Repositories | [openSUSE/cockpit-repos](https://github.com/openSUSE/cockpit-repos) | `cockpit-repos` | SUSE package repositories |
| SUSE Subscriptions | [openSUSE/cockpit-subscriptions](https://github.com/openSUSE/cockpit-subscriptions) | `cockpit-subscriptions` | SUSE subscriptions |
| Packages | [openSUSE/cockpit-packages](https://github.com/openSUSE/cockpit-packages) | `cockpit-packages` | Package install/remove |
| Bootloader | [openSUSE/cockpit-bootloader](https://github.com/openSUSE/cockpit-bootloader) | `cockpit-bootloader` | Bootloader configuration; pre-release |

## Third-party plugins indexed by Cockpit

| Project | Source code | Package name (if documented) | Purpose / caution |
|---|---|---|---|
| ZFS Manager | [45Drives/cockpit-zfs](https://github.com/45Drives/cockpit-zfs) | `cockpit-zfs` | OpenZFS pools, datasets and snapshots |
| File Sharing | [45Drives/cockpit-file-sharing](https://github.com/45Drives/cockpit-file-sharing) | Not confirmed | SMB/NFS and storage sharing |
| Navigator | [45Drives/cockpit-navigator](https://github.com/45Drives/cockpit-navigator) | Not confirmed | File manager |
| Benchmark | [45Drives/cockpit-benchmark](https://github.com/45Drives/cockpit-benchmark) | Not confirmed | Storage benchmarking |
| Sensors | [ocristopfer/cockpit-sensors](https://github.com/ocristopfer/cockpit-sensors) | `cockpit-sensors` | lm-sensors hardware readings |
| Tailscale (spotsnel) | [spotsnel/cockpit-tailscale](https://github.com/spotsnel/cockpit-tailscale) | `cockpit-tailscale` | Tailscale settings; pre-release |
| Tailscaled | [Nicolazroyale/cockpit-tailscaled](https://github.com/Nicolazroyale/cockpit-tailscaled) | `cockpit-tailscaled` | Tailscale peers, exit nodes, DNS and routing |
| Headscale | [spotsnel/cockpit-headscale](https://github.com/spotsnel/cockpit-headscale) | `cockpit-headscale` | Headscale server; pre-release |
| Cloudflare tunnels | [spotsnel/cockpit-cloudflared](https://github.com/spotsnel/cockpit-cloudflared) | `cockpit-cloudflared` | Cloudflared status; pre-release |
| Docker Manager | [chrisjbawden/cockpit-dockermanager](https://github.com/chrisjbawden/cockpit-dockermanager) | Not confirmed | Docker management; pre-release |
| Backblaze B2 Backup | [rabol/backblaze-b2](https://github.com/rabol/backblaze-b2) | Not confirmed | Backblaze B2 backup UI |
| ROS 2 Diagnostics | [clearpathrobotics/cockpit-ros2-diagnostics](https://github.com/clearpathrobotics/cockpit-ros2-diagnostics) | `cockpit-ros2-diagnostics` | ROS2 diagnostics |
| Package Manager | [hatlabs/cockpit-package-manager](https://github.com/hatlabs/cockpit-package-manager) | Not confirmed | PackageKit package browser |
| Port Forward Manager | [kuznetz/cockpit-port-forward](https://github.com/kuznetz/cockpit-port-forward) | Not confirmed | Firewalld port forwarding and masquerading |
| Sudo Manager | [josephoaks/Cockpit-SUDO-Manager](https://github.com/josephoaks/Cockpit-SUDO-Manager) | Not confirmed | Sudo policies; SUSE-oriented |
| BIND DNS | [josephoaks/Cockpit-DNS_Bind](https://github.com/josephoaks/Cockpit-DNS_Bind) | Not confirmed | BIND DNS management |
| Pacman | [pfeifferj/cockpit-pacman](https://github.com/pfeifferj/cockpit-pacman) | `cockpit-pacman` | Arch Linux package management |
| Download Superstation | [dl-romero/cockpit-download-superstation](https://github.com/dl-romero/cockpit-download-superstation) | `cockpit-download-superstation` | libtorrent downloader |
| systemd-nspawn | [realmcuser/cockpit-nspawn](https://github.com/realmcuser/cockpit-nspawn) | `cockpit-nspawn` | systemd-nspawn system containers |
| Docker Compose | [RXTX4816/cockpit-compose](https://github.com/RXTX4816/cockpit-compose) | `cockpit-compose` | Docker/Podman Compose; indexed pre-release |
| SCAP Compliance | [pbuchan-rh/cockpit-scap](https://github.com/pbuchan-rh/cockpit-scap) | `cockpit-scap` | OpenSCAP scans; RHEL 10 / CentOS Stream 10 |
| Explorer | [ismetozalp/explorer](https://github.com/ismetozalp/explorer) | Not confirmed | File manager, editors, AI CLI and system tools |
| InFlight TV | [ismetozalp/iftv](https://github.com/ismetozalp/iftv) | Not confirmed | IPTV with optional ffmpeg streaming |
| Cockpit Top | [ismetozalp/ctop](https://github.com/ismetozalp/ctop) | Not confirmed | btop-like system/process monitor |
| Manifest | [ismetozalp/manifest](https://github.com/ismetozalp/manifest) | Not confirmed | aria2 downloads including torrents |
| MicroShift | [lucamaf/cockpit-microshift-plugin](https://github.com/lucamaf/cockpit-microshift-plugin) | Not confirmed | MicroShift node and resource overview |
| Pilot | [ismetozalp/pilot](https://github.com/ismetozalp/pilot) | Not confirmed | Self-hosted RustDesk provisioning and control |
| Hangar | [ismetozalp/hangar](https://github.com/ismetozalp/hangar) | Not confirmed | restic backups, scheduling and restore |

## Additional independently discovered third-party plugins

| Project | Source code | Package name (if documented) | Purpose / caution |
|---|---|---|---|
| ZFS Storage (mietzen) | [mietzen/cockpit-plugins](https://github.com/mietzen/cockpit-plugins) | `cockpit-zfs-storage` | Alternative OpenZFS storage and SMART management |
| File Sharing (mietzen) | [mietzen/cockpit-plugins](https://github.com/mietzen/cockpit-plugins) | `cockpit-file-sharing` | Alternative SMB/NFS sharing; package name overlaps 45Drives |
| Container Manager (mietzen) | [mietzen/cockpit-plugins](https://github.com/mietzen/cockpit-plugins) | `cockpit-container-manager` | Docker/Podman/Compose and volumes/networks |
| VS Code Server (mietzen) | [mietzen/cockpit-plugins](https://github.com/mietzen/cockpit-plugins) | `cockpit-code-server` | code-server service and web editor |
| Caddy | [RXTX4816/cockpit-caddy](https://github.com/RXTX4816/cockpit-caddy) | `cockpit-caddy` | Caddy reverse proxy; supports Debian .deb; requires Cockpit 300+ |
| Plakar Backup | [RiddermanR/cockpit-plakar](https://github.com/RiddermanR/cockpit-plakar) | Not confirmed | Plakar stores, snapshots and scheduled backups |
| Router Management | [LedoKun/cockpit-router](https://github.com/LedoKun/cockpit-router) | Not confirmed | DNSMasq, WireGuard, NUT, Fail2Ban, QoS and AP controls |
| Cockpit Security | [Bia951/cockpit-security](https://github.com/Bia951/cockpit-security) | Not confirmed | UFW, iptables, nftables, firewalld and Fail2Ban |
| SnapRAID | [sloraris/cockpit-snapraid](https://github.com/sloraris/cockpit-snapraid) | Not confirmed | SnapRAID monitoring; explicitly beta |
| Temperature History | [cgillinger/cockpit_temp](https://github.com/cgillinger/cockpit_temp) | Not confirmed | PCP/lm-sensors temperature charts; hobby project |
| Tailscale (gbraad) | [gbraad-cockpit/cockpit-tailscale](https://github.com/gbraad-cockpit/cockpit-tailscale) | Not confirmed | Alternative Tailscale UI |
| ZFS Manager (brycelarge) | [brycelarge/cockpit-zfs-manager](https://github.com/brycelarge/cockpit-zfs-manager) | Not confirmed | Alternate ZFS frontend with optional Sanoid |

## Legacy or historical projects (compatibility unconfirmed)

| Project | Source code | Package name (if documented) | Purpose / caution |
|---|---|---|---|
| Older Samba Manager | [enira/cockpit-smb-plugin](https://github.com/enira/cockpit-smb-plugin) | Not confirmed | Older Samba manager; README uses outdated Cockpit/Debian examples |
| Cockpit Composer | [osbuild/cockpit-composer](https://github.com/osbuild/cockpit-composer) | Not confirmed | Historical osbuild-composer image-building frontend |
| Original ZFS Manager | [optimans/cockpit-zfs-manager](https://github.com/optimans/cockpit-zfs-manager) | Not confirmed | Historical ZFS manager; compare newer alternatives |

## Core/distribution modules (not necessarily add-ons)

| Project | Source code | Package name (if documented) | Purpose / caution |
|---|---|---|---|
| PCP Metrics | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | `cockpit-pcp` | Performance Co-Pilot time series and metric history |
| System Overview | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | `cockpit-system` | Core services, logs, users and system overview; normally bundled |

## Best starting points for headless Debian

| Purpose | Recommended starting point | Qualification |
|---|---|---|
| File browser | [Cockpit Files](https://github.com/cockpit-project/cockpit-files) | Upstream Cockpit module |
| Storage/disks | [cockpit-storaged](https://github.com/cockpit-project/cockpit) | Install only if storage management is needed |
| Podman containers | [cockpit-podman](https://github.com/cockpit-project/cockpit-podman) | First-party Podman UI, **not Docker** |
| Docker/Compose | [Cockpit Compose](https://github.com/RXTX4816/cockpit-compose) or [mietzen Container Manager](https://github.com/mietzen/cockpit-plugins) | Community-maintained alternatives |
| Virtual machines | [cockpit-machines](https://github.com/cockpit-project/cockpit-machines) | Requires KVM/libvirt |
| LAN file shares | [45Drives file sharing](https://github.com/45Drives/cockpit-file-sharing) | Requires Samba/NFS setup |
| Hardware monitoring | [cockpit-sensors](https://github.com/ocristopfer/cockpit-sensors) | Requires lm-sensors |
| Web IDE | [mietzen code-server](https://github.com/mietzen/cockpit-plugins) | Browser-based development, additional runtime |
| HTTPS reverse proxy | [cockpit-caddy](https://github.com/RXTX4816/cockpit-caddy) | Privileged configuration; Cockpit 300+ |
| Encrypted backups | [Hangar](https://github.com/ismetozalp/hangar) | Test restore workflow before relying on it |

## Debian discovery commands

~~~bash
sudo apt update
apt-cache policy cockpit cockpit-files cockpit-storaged cockpit-networkmanager cockpit-packagekit cockpit-machines cockpit-podman cockpit-pcp
apt search '^cockpit-'
~~~

See the [official Debian installation instructions](https://cockpit-project.org/running#debian) and check whether suitable [Debian backports](https://packages.debian.org/trixie-backports/admin/) are enabled. Never blindly install unreviewed root-level scripts or combine conflicting packages from different third-party repositories.

## Notes on completeness and maintenance

- Multiple ZFS, file-sharing, Docker and Tailscale implementations **overlap**; pick one based on your OS and required functionality.
- "Pre-release" and "beta" markings above are based on the respective upstream descriptions when checked; absence of a warning **does not** mean production-ready.
- Cockpit's app directory and independent GitHub repositories can change; verify each application's last commit, open issues and installation instructions before deployment.
- Cockpit base features such as Terminal, Logs, Accounts and Services are already bundled in some distributions and are **not all distinct third-party extensions**.
- Excludes unrelated Cockpit CMS plugins, standalone monitoring/control panels without a Cockpit extension, and Starter Kit-only template repositories.
- To extend this catalog, include an original source link, describe functionality, identify distribution/package requirements and clearly label abandoned or experimental implementations.
