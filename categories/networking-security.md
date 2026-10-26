# Networking & Security

[Back to the Awesome Linux Homelab list](../README.md)

Network configuration, VPNs, DNS, firewalls and host security.

Generated from the structured YAML catalog. Changes belong in `data/`, not in this page. **Highlighted** means editorial visibility, not installation, security or hardware validation.

## Highlighted starting points

- [Networking](https://github.com/cockpit-project/cockpit) - NetworkManager networks and firewall.

## Research and alternatives

- [389 Directory Server](https://github.com/389ds/389-ds-base) - 389 Directory Server LDAP UI; source project linked.
- [BIND DNS](https://github.com/josephoaks/Cockpit-DNS_Bind) - BIND DNS management.
- [Caddy](https://github.com/RXTX4816/cockpit-caddy) - Caddy reverse proxy; supports Debian .deb; requires Cockpit 300+.
- [Cloudflare tunnels](https://github.com/spotsnel/cockpit-cloudflared) - Cloudflared status; pre-release.
- [Cockpit Security](https://github.com/Bia951/cockpit-security) - UFW, iptables, nftables, firewalld and Fail2Ban.
- [Headscale](https://github.com/spotsnel/cockpit-headscale) - Headscale server; pre-release.
- [Port Forward Manager](https://github.com/kuznetz/cockpit-port-forward) - Firewalld port forwarding and masquerading.
- [Router Management](https://github.com/LedoKun/cockpit-router) - DNSMasq, WireGuard, NUT, Fail2Ban, QoS and AP controls.
- [SCAP Compliance](https://github.com/pbuchan-rh/cockpit-scap) - OpenSCAP scans; RHEL 10 / CentOS Stream 10.
- [SELinux](https://github.com/cockpit-project/cockpit) - SELinux exceptions and audit reports.
- [Session Recording](https://github.com/Scribery/cockpit-session-recording) - Session recording and playback.
- [Sudo Manager](https://github.com/josephoaks/Cockpit-SUDO-Manager) - Sudo policies; SUSE-oriented.
- [Tailscale (gbraad)](https://github.com/gbraad-cockpit/cockpit-tailscale) - Alternative Tailscale UI.
- [Tailscale (spotsnel)](https://github.com/spotsnel/cockpit-tailscale) - Tailscale settings; pre-release.
- [Tailscaled](https://github.com/Nicolazroyale/cockpit-tailscaled) - Tailscale peers, exit nodes, DNS and routing.

For Cockpit integration and package caveats, see the [Cockpit cross-index](../integrations/cockpit/README.md).
