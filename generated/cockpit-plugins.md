# Cockpit modules and extensions

Historical research snapshot, **not** an endorsement or verified APT installation guide. Browse [Cockpit by purpose](../integrations/cockpit/README.md).

| Project | Functional category | Source group | Package (unverified) | Upstream link | Notes |
| --- | --- | --- | --- | --- | --- |
| 389 Directory Server | networking-security | red-hat | cockpit-389-ds | [Source](https://github.com/389ds/389-ds-base) | 389 Directory Server LDAP UI; source project linked |
| Backblaze B2 Backup | storage-backups | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/rabol/backblaze-b2) | Backblaze B2 backup UI |
| Benchmark | storage-backups | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/45Drives/cockpit-benchmark) | Storage benchmarking |
| BIND DNS | networking-security | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/josephoaks/Cockpit-DNS_Bind) | BIND DNS management |
| Bootloader | installation-boot | suse | cockpit-bootloader | [Source](https://github.com/openSUSE/cockpit-bootloader) | Bootloader configuration; pre-release |
| Caddy | networking-security | independent-third-party | cockpit-caddy | [Source](https://github.com/RXTX4816/cockpit-caddy) | Caddy reverse proxy; supports Debian .deb; requires Cockpit 300+ |
| Cloudflare tunnels | networking-security | cockpit-listed-third-party | cockpit-cloudflared | [Source](https://github.com/spotsnel/cockpit-cloudflared) | Cloudflared status; pre-release |
| Cockpit Composer | installation-boot | historical | Not confirmed | [Source](https://github.com/osbuild/cockpit-composer) | Historical osbuild-composer image-building frontend |
| Container Manager (mietzen) | containers-virtualization | independent-third-party | cockpit-container-manager | [Source](https://github.com/mietzen/cockpit-plugins) | Docker/Podman/Compose and volumes/networks |
| Diagnostic Reports | terminal-monitoring | first-party | cockpit-sosreport | [Source](https://github.com/cockpit-project/cockpit) | System diagnostic collection |
| Docker Compose | containers-virtualization | cockpit-listed-third-party | cockpit-compose | [Source](https://github.com/RXTX4816/cockpit-compose) | Docker/Podman Compose; indexed pre-release |
| Docker Manager | containers-virtualization | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/chrisjbawden/cockpit-dockermanager) | Docker management; pre-release |
| Download Superstation | storage-backups | cockpit-listed-third-party | cockpit-download-superstation | [Source](https://github.com/dl-romero/cockpit-download-superstation) | libtorrent downloader |
| Explorer | storage-backups | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/ismetozalp/explorer) | File manager, editors, AI CLI and system tools |
| File Sharing | storage-backups | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/45Drives/cockpit-file-sharing) | SMB/NFS and storage sharing |
| File Sharing (mietzen) | storage-backups | independent-third-party | cockpit-file-sharing | [Source](https://github.com/mietzen/cockpit-plugins) | Alternative SMB/NFS sharing; package name overlaps 45Drives |
| Cockpit Files | storage-backups | first-party | cockpit-files | [Source](https://github.com/cockpit-project/cockpit-files) | Integrated file manager |
| Hangar | storage-backups | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/ismetozalp/hangar) | restic backups, scheduling and restore |
| Headscale | networking-security | cockpit-listed-third-party | cockpit-headscale | [Source](https://github.com/spotsnel/cockpit-headscale) | Headscale server; pre-release |
| High Availability Cluster | containers-virtualization | red-hat | cockpit-ha-cluster | [Source](https://github.com/ClusterLabs/pcs-web-ui) | Pacemaker/PCS cluster management |
| Image Builder | installation-boot | red-hat | cockpit-image-builder | [Source](https://github.com/osbuild/image-builder-frontend) | Build operating system images |
| InFlight TV | further-resources | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/ismetozalp/iftv) | IPTV with optional ffmpeg streaming |
| Kernel Dump | terminal-monitoring | first-party | cockpit-kdump | [Source](https://github.com/cockpit-project/cockpit) | Kdump configuration |
| Manifest | storage-backups | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/ismetozalp/manifest) | aria2 downloads including torrents |
| MicroShift | containers-virtualization | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/lucamaf/cockpit-microshift-plugin) | MicroShift node and resource overview |
| Navigator | storage-backups | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/45Drives/cockpit-navigator) | File manager |
| Networking | networking-security | first-party | cockpit-networkmanager | [Source](https://github.com/cockpit-project/cockpit) | NetworkManager networks and firewall |
| Older Samba Manager | storage-backups | historical | Not confirmed | [Source](https://github.com/enira/cockpit-smb-plugin) | Older Samba manager; README uses outdated Cockpit/Debian examples |
| Original ZFS Manager | storage-backups | historical | Not confirmed | [Source](https://github.com/optimans/cockpit-zfs-manager) | Historical ZFS manager; compare newer alternatives |
| OSTree Updates | system-administration | first-party | cockpit-ostree | [Source](https://github.com/cockpit-project/cockpit-ostree) | OSTree/immutable OS updates |
| Package Manager | system-administration | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/hatlabs/cockpit-package-manager) | PackageKit package browser |
| Packages | system-administration | suse | cockpit-packages | [Source](https://github.com/openSUSE/cockpit-packages) | Package install/remove |
| Pacman | system-administration | cockpit-listed-third-party | cockpit-pacman | [Source](https://github.com/pfeifferj/cockpit-pacman) | Arch Linux package management |
| PCP Metrics | terminal-monitoring | core-module | cockpit-pcp | [Source](https://github.com/cockpit-project/cockpit) | Performance Co-Pilot time series and metric history |
| Pilot | remote-access | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/ismetozalp/pilot) | Self-hosted RustDesk provisioning and control |
| Plakar Backup | storage-backups | independent-third-party | Not confirmed | [Source](https://github.com/RiddermanR/cockpit-plakar) | Plakar stores, snapshots and scheduled backups |
| Podman Containers | containers-virtualization | first-party | cockpit-podman | [Source](https://github.com/cockpit-project/cockpit-podman) | Podman container management; not Docker |
| Port Forward Manager | networking-security | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/kuznetz/cockpit-port-forward) | Firewalld port forwarding and masquerading |
| Repositories | system-administration | suse | cockpit-repos | [Source](https://github.com/openSUSE/cockpit-repos) | SUSE package repositories |
| RHEL Subscription Manager | system-administration | red-hat | subscription-manager-cockpit | [Source](https://github.com/cockpit-project/subscription-manager-cockpit) | RHEL subscriptions; RHEL-specific |
| ROS 2 Diagnostics | terminal-monitoring | cockpit-listed-third-party | cockpit-ros2-diagnostics | [Source](https://github.com/clearpathrobotics/cockpit-ros2-diagnostics) | ROS2 diagnostics |
| Router Management | networking-security | independent-third-party | Not confirmed | [Source](https://github.com/LedoKun/cockpit-router) | DNSMasq, WireGuard, NUT, Fail2Ban, QoS and AP controls |
| SCAP Compliance | networking-security | cockpit-listed-third-party | cockpit-scap | [Source](https://github.com/pbuchan-rh/cockpit-scap) | OpenSCAP scans; RHEL 10 / CentOS Stream 10 |
| Cockpit Security | networking-security | independent-third-party | Not confirmed | [Source](https://github.com/Bia951/cockpit-security) | UFW, iptables, nftables, firewalld and Fail2Ban |
| SELinux | networking-security | first-party | cockpit-selinux | [Source](https://github.com/cockpit-project/cockpit) | SELinux exceptions and audit reports |
| Sensors | terminal-monitoring | cockpit-listed-third-party | cockpit-sensors | [Source](https://github.com/ocristopfer/cockpit-sensors) | lm-sensors hardware readings |
| Session Recording | networking-security | red-hat | cockpit-session-recording | [Source](https://github.com/Scribery/cockpit-session-recording) | Session recording and playback |
| SnapRAID | storage-backups | independent-third-party | Not confirmed | [Source](https://github.com/sloraris/cockpit-snapraid) | SnapRAID monitoring; explicitly beta |
| Software Updates | system-administration | first-party | cockpit-packagekit | [Source](https://github.com/cockpit-project/cockpit) | PackageKit-based updates |
| Storage | storage-backups | first-party | cockpit-storaged | [Source](https://github.com/cockpit-project/cockpit) | Partitions, LUKS, RAID, NFS, iSCSI |
| Sudo Manager | networking-security | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/josephoaks/Cockpit-SUDO-Manager) | Sudo policies; SUSE-oriented |
| SUSE Subscriptions | system-administration | suse | cockpit-subscriptions | [Source](https://github.com/openSUSE/cockpit-subscriptions) | SUSE subscriptions |
| System Overview | system-administration | core-module | cockpit-system | [Source](https://github.com/cockpit-project/cockpit) | Core services, logs, users and system overview; normally bundled |
| systemd-nspawn | containers-virtualization | cockpit-listed-third-party | cockpit-nspawn | [Source](https://github.com/realmcuser/cockpit-nspawn) | systemd-nspawn system containers |
| Tailscale (gbraad) | networking-security | independent-third-party | Not confirmed | [Source](https://github.com/gbraad-cockpit/cockpit-tailscale) | Alternative Tailscale UI |
| Tailscale (spotsnel) | networking-security | cockpit-listed-third-party | cockpit-tailscale | [Source](https://github.com/spotsnel/cockpit-tailscale) | Tailscale settings; pre-release |
| Tailscaled | networking-security | cockpit-listed-third-party | cockpit-tailscaled | [Source](https://github.com/Nicolazroyale/cockpit-tailscaled) | Tailscale peers, exit nodes, DNS and routing |
| Temperature History | terminal-monitoring | independent-third-party | Not confirmed | [Source](https://github.com/cgillinger/cockpit_temp) | PCP/lm-sensors temperature charts; hobby project |
| Cockpit Top | terminal-monitoring | cockpit-listed-third-party | Not confirmed | [Source](https://github.com/ismetozalp/ctop) | btop-like system/process monitor |
| Transactional Updates | system-administration | suse | cockpit-tukit | [Source](https://github.com/openSUSE/cockpit-tukit) | SUSE transactional OS updates |
| Virtual Machines | containers-virtualization | first-party | cockpit-machines | [Source](https://github.com/cockpit-project/cockpit-machines) | KVM/libvirt virtual machine management |
| VS Code Server (mietzen) | remote-access | independent-third-party | cockpit-code-server | [Source](https://github.com/mietzen/cockpit-plugins) | code-server service and web editor |
| ZFS Manager | storage-backups | cockpit-listed-third-party | cockpit-zfs | [Source](https://github.com/45Drives/cockpit-zfs) | OpenZFS pools, datasets and snapshots |
| ZFS Manager (brycelarge) | storage-backups | independent-third-party | Not confirmed | [Source](https://github.com/brycelarge/cockpit-zfs-manager) | Alternate ZFS frontend with optional Sanoid |
| ZFS Storage (mietzen) | storage-backups | independent-third-party | cockpit-zfs-storage | [Source](https://github.com/mietzen/cockpit-plugins) | Alternative OpenZFS storage and SMART management |
