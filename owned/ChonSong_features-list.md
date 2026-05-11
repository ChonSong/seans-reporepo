---
repo: 'ChonSong/features-list'
url: 'https://github.com/ChonSong/features-list'
description: No description
type: monorepo
status: active
language: HTML
size_kb: 1711
stars: 0
last_pushed: '2026-05-11'
license: unknown
tags:
  - agent
  - ai
  - analytics
  - api
  - awesome-list
  - backup
  - dashboard
  - docker
  - go
  - hermes-agent
  - infrastructure
  - mobile
  - monitoring
  - sync
  - terminal
  - transpilation
  - web-app
  - website
topics: []
refreshed_at: '2026-05-11 02:12 UTC'
---

# features-list

> No description

**URL:** [ChonSong/features-list](https://github.com/ChonSong/features-list)

## Metadata

- **Type:** monorepo
- **Status:** active
- **Language:** HTML
- **Size:** 1,711 KB
- **Stars:** 0
- **Last Pushed:** 2026-05-11
- **License:** unknown
- **Tags:** agent, ai, analytics, api, awesome-list, backup, dashboard, docker, go, hermes-agent, infrastructure, mobile, monitoring, sync, terminal, transpilation, web-app, website

## README Excerpt

# Hermes Workspace Features List

> Complete feature catalog — hermes-workspace + agent-os + repo-transmute v2

## Architecture Diagrams

| Diagram | Description |
|---------|-------------|
| [Agent-OS Architecture](screenshots/agent-os-architecture.html) | **Complete picture** — hermes-workspace features + agent-os infrastructure + migration engine |
| [System Architecture](screenshots/system-architecture.html) | hermes-workspace system architecture — Electron app, API routes, Hermes Agent, databases |
| [Chat Architecture](screenshots/chat-architecture.html) | Chat feature architecture — streaming, sessions, message rendering |
| [Dashboard Features](screenshots/dashboard-features.html) | Dashboard feature map — analytics, KPIs, operations intelligence |

## Screenshots

| Screenshot | Description |
|------------|-------------|
| ![SciFi Theme](screenshots/SciFi.png) | SciFi theme variant |
| ![Hermes World Landing](screenshots/hermes-world-landing-pass.png) | Hermes World landing page |
| ![Accessibility Desktop](screenshots/hermesworld-accessibility-desktop.png) | Desktop accessibility view |
| ![Accessibility Mobile](screenshots/hermesworld-accessibility-mobile.png) | Mobile accessibility view |
| ![SciFi Theme](screenshots/scifi-theme.png) | SciFi theme variant |

---

## agent-os Additions

### Infrastructure

| Component | Description |
|-----------|-------------|
| **Docker Stack** | 4 containers: backend, postgres, cloudflared, webhook-emitter (all healthy) |
| **Network** | agent-os_agent-net with host.docker.internal:8642 for Hermes |
| **Cloudflare Tunnel** | Argo tunnel with QUIC protocol (syd05/mel01) |
| **Webhook Emitter** | Go service subscribing to CasaOS MessageBus, Docker event fan-out |
| **CI/CD** | GitHub Actions: test → build → SSH deploy to ghcr.io/chonsong/agent-os |
| **Backup** | pg_dump daily at 3am → ~/.hermes/backups/postgres |
| **Sync** | hermes-sync cron every 6 hours → GitHub private repo |

### Frontend (22 pages)

| Page | Route...
