# Cockpit integration directory

[Back to Awesome Linux Homelab](../../README.md) · [Original Cockpit research](../../archive/cockpit-research-2026-10-19.md)

This is a **65-entry historical research catalog** organized by what each module does, rather than who publishes it. Package names are not proof of repository availability. No entries were installation-tested or hardware-qualified for this list.

## Installation & Boot (3)

- [Bootloader](https://github.com/openSUSE/cockpit-bootloader) - Bootloader configuration; pre-release. *suse; package: `cockpit-bootloader`.*
- [Cockpit Composer](https://github.com/osbuild/cockpit-composer) - Historical osbuild-composer image-building frontend. *historical; package: unconfirmed.*
- [Image Builder](https://github.com/osbuild/image-builder-frontend) - Build operating system images. *red-hat; package: `cockpit-image-builder`.*

## System Administration (10)

- [OSTree Updates](https://github.com/cockpit-project/cockpit-ostree) - OSTree/immutable OS updates. *first-party; package: `cockpit-ostree`.*
- [Package Manager](https://github.com/hatlabs/cockpit-package-manager) - PackageKit package browser. *cockpit-listed-third-party; package: unconfirmed.*
- [Packages](https://github.com/openSUSE/cockpit-packages) - Package install/remove. *suse; package: `cockpit-packages`.*
- [Pacman](https://github.com/pfeifferj/cockpit-pacman) - Arch Linux package management. *cockpit-listed-third-party; package: `cockpit-pacman`.*
- [Repositories](https://github.com/openSUSE/cockpit-repos) - SUSE package repositories. *suse; package: `cockpit-repos`.*
- [RHEL Subscription Manager](https://github.com/cockpit-project/subscription-manager-cockpit) - RHEL subscriptions; RHEL-specific. *red-hat; package: `subscription-manager-cockpit`.*
- [Software Updates](https://github.com/cockpit-project/cockpit) - PackageKit-based updates. *first-party; package: `cockpit-packagekit`.*
- [SUSE Subscriptions](https://github.com/openSUSE/cockpit-subscriptions) - SUSE subscriptions. *suse; package: `cockpit-subscriptions`.*
- [System Overview](https://github.com/cockpit-project/cockpit) - Core services, logs, users and system overview; normally bundled. *core-module; package: `cockpit-system`.*
- [Transactional Updates](https://github.com/openSUSE/cockpit-tukit) - SUSE transactional OS updates. *suse; package: `cockpit-tukit`.*

## Storage & Backups (18)

- [Backblaze B2 Backup](https://github.com/rabol/backblaze-b2) - Backblaze B2 backup UI. *cockpit-listed-third-party; package: unconfirmed.*
- [Benchmark](https://github.com/45Drives/cockpit-benchmark) - Storage benchmarking. *cockpit-listed-third-party; package: unconfirmed.*
- [Cockpit Files](https://github.com/cockpit-project/cockpit-files) - Integrated file manager. *first-party; package: `cockpit-files`.*
- [Download Superstation](https://github.com/dl-romero/cockpit-download-superstation) - Libtorrent downloader. *cockpit-listed-third-party; package: `cockpit-download-superstation`.*
- [Explorer](https://github.com/ismetozalp/explorer) - File manager, editors, AI CLI and system tools. *cockpit-listed-third-party; package: unconfirmed.*
- [File Sharing](https://github.com/45Drives/cockpit-file-sharing) - SMB/NFS and storage sharing. *cockpit-listed-third-party; package: unconfirmed.*
- [File Sharing (mietzen)](https://github.com/mietzen/cockpit-plugins) - Alternative SMB/NFS sharing; package name overlaps 45Drives. *independent-third-party; package: `cockpit-file-sharing`.*
- [Hangar](https://github.com/ismetozalp/hangar) - Restic backups, scheduling and restore. *cockpit-listed-third-party; package: unconfirmed.*
- [Manifest](https://github.com/ismetozalp/manifest) - Aria2 downloads including torrents. *cockpit-listed-third-party; package: unconfirmed.*
- [Navigator](https://github.com/45Drives/cockpit-navigator) - File manager. *cockpit-listed-third-party; package: unconfirmed.*
- [Older Samba Manager](https://github.com/enira/cockpit-smb-plugin) - Older Samba manager; README uses outdated Cockpit/Debian examples. *historical; package: unconfirmed.*
- [Original ZFS Manager](https://github.com/optimans/cockpit-zfs-manager) - Historical ZFS manager; compare newer alternatives. *historical; package: unconfirmed.*
- [Plakar Backup](https://github.com/RiddermanR/cockpit-plakar) - Plakar stores, snapshots and scheduled backups. *independent-third-party; package: unconfirmed.*
- [SnapRAID](https://github.com/sloraris/cockpit-snapraid) - SnapRAID monitoring; explicitly beta. *independent-third-party; package: unconfirmed.*
- [Storage](https://github.com/cockpit-project/cockpit) - Partitions, LUKS, RAID, NFS, iSCSI. *first-party; package: `cockpit-storaged`.*
- [ZFS Manager](https://github.com/45Drives/cockpit-zfs) - OpenZFS pools, datasets and snapshots. *cockpit-listed-third-party; package: `cockpit-zfs`.*
- [ZFS Manager (brycelarge)](https://github.com/brycelarge/cockpit-zfs-manager) - Alternate ZFS frontend with optional Sanoid. *independent-third-party; package: unconfirmed.*
- [ZFS Storage (mietzen)](https://github.com/mietzen/cockpit-plugins) - Alternative OpenZFS storage and SMART management. *independent-third-party; package: `cockpit-zfs-storage`.*

## Networking & Security (16)

- [389 Directory Server](https://github.com/389ds/389-ds-base) - 389 Directory Server LDAP UI; source project linked. *red-hat; package: `cockpit-389-ds`.*
- [BIND DNS](https://github.com/josephoaks/Cockpit-DNS_Bind) - BIND DNS management. *cockpit-listed-third-party; package: unconfirmed.*
- [Caddy](https://github.com/RXTX4816/cockpit-caddy) - Caddy reverse proxy; supports Debian .deb; requires Cockpit 300+. *independent-third-party; package: `cockpit-caddy`.*
- [Cloudflare tunnels](https://github.com/spotsnel/cockpit-cloudflared) - Cloudflared status; pre-release. *cockpit-listed-third-party; package: `cockpit-cloudflared`.*
- [Cockpit Security](https://github.com/Bia951/cockpit-security) - UFW, iptables, nftables, firewalld and Fail2Ban. *independent-third-party; package: unconfirmed.*
- [Headscale](https://github.com/spotsnel/cockpit-headscale) - Headscale server; pre-release. *cockpit-listed-third-party; package: `cockpit-headscale`.*
- [Networking](https://github.com/cockpit-project/cockpit) - NetworkManager networks and firewall. *first-party; package: `cockpit-networkmanager`.*
- [Port Forward Manager](https://github.com/kuznetz/cockpit-port-forward) - Firewalld port forwarding and masquerading. *cockpit-listed-third-party; package: unconfirmed.*
- [Router Management](https://github.com/LedoKun/cockpit-router) - DNSMasq, WireGuard, NUT, Fail2Ban, QoS and AP controls. *independent-third-party; package: unconfirmed.*
- [SCAP Compliance](https://github.com/pbuchan-rh/cockpit-scap) - OpenSCAP scans; RHEL 10 / CentOS Stream 10. *cockpit-listed-third-party; package: `cockpit-scap`.*
- [SELinux](https://github.com/cockpit-project/cockpit) - SELinux exceptions and audit reports. *first-party; package: `cockpit-selinux`.*
- [Session Recording](https://github.com/Scribery/cockpit-session-recording) - Session recording and playback. *red-hat; package: `cockpit-session-recording`.*
- [Sudo Manager](https://github.com/josephoaks/Cockpit-SUDO-Manager) - Sudo policies; SUSE-oriented. *cockpit-listed-third-party; package: unconfirmed.*
- [Tailscale (gbraad)](https://github.com/gbraad-cockpit/cockpit-tailscale) - Alternative Tailscale UI. *independent-third-party; package: unconfirmed.*
- [Tailscale (spotsnel)](https://github.com/spotsnel/cockpit-tailscale) - Tailscale settings; pre-release. *cockpit-listed-third-party; package: `cockpit-tailscale`.*
- [Tailscaled](https://github.com/Nicolazroyale/cockpit-tailscaled) - Tailscale peers, exit nodes, DNS and routing. *cockpit-listed-third-party; package: `cockpit-tailscaled`.*

## Containers & Virtualization (8)

- [Container Manager (mietzen)](https://github.com/mietzen/cockpit-plugins) - Docker/Podman/Compose and volumes/networks. *independent-third-party; package: `cockpit-container-manager`.*
- [Docker Compose](https://github.com/RXTX4816/cockpit-compose) - Docker/Podman Compose; indexed pre-release. *cockpit-listed-third-party; package: `cockpit-compose`.*
- [Docker Manager](https://github.com/chrisjbawden/cockpit-dockermanager) - Docker management; pre-release. *cockpit-listed-third-party; package: unconfirmed.*
- [High Availability Cluster](https://github.com/ClusterLabs/pcs-web-ui) - Pacemaker/PCS cluster management. *red-hat; package: `cockpit-ha-cluster`.*
- [MicroShift](https://github.com/lucamaf/cockpit-microshift-plugin) - MicroShift node and resource overview. *cockpit-listed-third-party; package: unconfirmed.*
- [Podman Containers](https://github.com/cockpit-project/cockpit-podman) - Podman container management; not Docker. *first-party; package: `cockpit-podman`.*
- [systemd-nspawn](https://github.com/realmcuser/cockpit-nspawn) - Systemd-nspawn system containers. *cockpit-listed-third-party; package: `cockpit-nspawn`.*
- [Virtual Machines](https://github.com/cockpit-project/cockpit-machines) - KVM/libvirt virtual machine management. *first-party; package: `cockpit-machines`.*

## Remote Access (2)

- [Pilot](https://github.com/ismetozalp/pilot) - Self-hosted RustDesk provisioning and control. *cockpit-listed-third-party; package: unconfirmed.*
- [VS Code Server (mietzen)](https://github.com/mietzen/cockpit-plugins) - Code-server service and web editor. *independent-third-party; package: `cockpit-code-server`.*

## Terminal & Monitoring (7)

- [Cockpit Top](https://github.com/ismetozalp/ctop) - Btop-like system/process monitor. *cockpit-listed-third-party; package: unconfirmed.*
- [Diagnostic Reports](https://github.com/cockpit-project/cockpit) - System diagnostic collection. *first-party; package: `cockpit-sosreport`.*
- [Kernel Dump](https://github.com/cockpit-project/cockpit) - Kdump configuration. *first-party; package: `cockpit-kdump`.*
- [PCP Metrics](https://github.com/cockpit-project/cockpit) - Performance Co-Pilot time series and metric history. *core-module; package: `cockpit-pcp`.*
- [ROS 2 Diagnostics](https://github.com/clearpathrobotics/cockpit-ros2-diagnostics) - ROS2 diagnostics. *cockpit-listed-third-party; package: `cockpit-ros2-diagnostics`.*
- [Sensors](https://github.com/ocristopfer/cockpit-sensors) - Lm-sensors hardware readings. *cockpit-listed-third-party; package: `cockpit-sensors`.*
- [Temperature History](https://github.com/cgillinger/cockpit_temp) - PCP/lm-sensors temperature charts; hobby project. *independent-third-party; package: unconfirmed.*

## Further Resources (1)

- [InFlight TV](https://github.com/ismetozalp/iftv) - IPTV with optional ffmpeg streaming. *cockpit-listed-third-party; package: unconfirmed.*

