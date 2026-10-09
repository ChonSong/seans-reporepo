---
repo: 'ChonSong/security-toolkit'
url: 'https://github.com/ChonSong/security-toolkit'
description: 'Custom security script suite — defensive monitoring, offensive recon, packet crafting, exploit dev, and privilege escalation enumeration. 22 scripts across 4 phases in Bash, Python, and Go.'
type: library
status: active
language: Shell
size_kb: 2718
stars: 0
last_pushed: '2026-08-08'
license: unknown
tags:
  - ai
  - awesome-list
  - go
  - monitoring
  - orchestration
  - python
  - vector-db
topics: []
refreshed_at: '2026-10-09 22:21 UTC'
---

# security-toolkit

> Custom security script suite — defensive monitoring, offensive recon, packet crafting, exploit dev, and privilege escalation enumeration. 22 scripts across 4 phases in Bash, Python, and Go.

**URL:** [ChonSong/security-toolkit](https://github.com/ChonSong/security-toolkit)

## Metadata

- **Type:** library
- **Status:** active
- **Language:** Shell
- **Size:** 2,718 KB
- **Stars:** 0
- **Last Pushed:** 2026-08-08
- **License:** unknown
- **Tags:** ai, awesome-list, go, monitoring, orchestration, python, vector-db

## README Excerpt

# Security Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Custom security script suite — defensive monitoring, offensive reconnaissance,
packet crafting, exploit development, and privilege escalation enumeration.
22 scripts across 4 phases in Bash, Python, and Go.

## ⚠️ Legal Notice

**All active scanning, exploitation, packet injection, and blocking
functionality in this toolkit may only be used on assets you own or have
explicit written authorization to test.** Misuse may be illegal.

See [SECURITY.md](SECURITY.md) for the vulnerability reporting policy and
full legal notice.

## Quick Start

```bash
git clone https://github.com/ChonSong/security-toolkit.git
cd security-toolkit

# Dry-run first
sudo ./deploy.sh --dry-run

# Full deployment
sudo ./deploy.sh --install

# Start all monitoring services
sudo systemctl start security-toolkit.target
```

## Toolkit Overview

| Phase | Directory | Language | Purpose |
|-------|-----------|----------|---------|
| 1 — Defensive | `defensive/` | Bash, Python | SSH brute blocking, FIM, network capture, osquery inventory, auth log anomaly detection |
| 2 — Recon | `recon/` | Bash, Go, Python | Automated nmap/ffuf/gobuster orchestration, subdomain discovery, HTTP fingerprinting, TCP scanning |
| 3a — Packet | `packet/` | Python (Scapy) | ICMP sweep, ARP spoof detection, SYN flood test, custom DNS queries |
| 3b — Exploit | `exploit/` | Python (Pwntools) | Buffer overflow template (GDB integration), TLS reverse shell handler |
| 4 — Privesc | `privesc/` | Bash | SUID hunter, credential harvester, cron misconfig, LinPEAS-lite (15 vectors), kernel exploit suggester |

## Safety by Design

Every destructive-capable tool defaults to **dry-run/alert-only mode** and
requires explicit opt-in (`--enable-blocking`, `--confirm`) to act:

- `--dry-run` / `--alert-only` — default on every script
- `--rate-limit N` — mandatory on scanning and flood tools
- `--target-list FILE` — explicit authorizat...
