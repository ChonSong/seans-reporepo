---
repo: 'ChonSong/hermes-sync'
url: 'https://github.com/ChonSong/hermes-sync'
description: Hermes Agent state backup
type: monorepo
status: active
language: Python
size_kb: 72040
stars: 0
last_pushed: '2026-06-19'
license: unknown
tags:
  - agent
  - ai
  - api
  - backup
  - dashboard
  - docker
  - hermes-agent
  - sync
topics: []
refreshed_at: '2026-07-05 23:53 UTC'
---

# hermes-sync

> Hermes Agent state backup

**URL:** [ChonSong/hermes-sync](https://github.com/ChonSong/hermes-sync)

## Metadata

- **Type:** monorepo
- **Status:** active
- **Language:** Python
- **Size:** 72,040 KB
- **Stars:** 0
- **Last Pushed:** 2026-06-19
- **License:** unknown
- **Tags:** agent, ai, api, backup, dashboard, docker, hermes-agent, sync

## README Excerpt

# Hermes Agent — Complete State Backup & Container Docs

Automated backup of Hermes Agent state to GitHub. Runs every 6 hours via host cron.

## What's Synced (every 6h)

| Item | Description |
|------|-------------|
| `config.yaml`, `SOUL.md`, `auth.json`, `kanban.db` | Core state |
| `state.db.gz` | Compressed SQLite DB (all sessions, messages, tokens) — 269MB → 94MB |
| `skills/` | All skill definitions and references |
| `memory/` | MEMORY.md and USER.md |
| `sessions/` | Session JSON transcripts |
| `cron/` | Cron job definitions and output logs |
| `scripts/` | Sync and utility scripts |
| `plans/`, `workspace/`, `hooks/` | Plans, workspace files, hooks |
| `secrets/.env` | API keys |

## Recovery (Bare Machine)

```bash
# 1. Clone
git clone https://github.com/ChonSong/hermes-sync.git ~/hermes-recovery

# 2. Decompress state DB
gunzip ~/hermes-recovery/state.db.gz

# 3. Copy to hermes data dir
cp ~/hermes-recovery/config.yaml ~/.hermes/
cp ~/hermes-recovery/state.db ~/.hermes/
cp -r ~/hermes-recovery/skills ~/.hermes/
cp -r ~/hermes-recovery/memory ~/.hermes/
cp -r ~/hermes-recovery/sessions ~/.hermes/
cp -r ~/hermes-recovery/cron ~/.hermes/
cp -r ~/hermes-recovery/secrets/.env ~/.hermes/.env

# 4. Start container
docker run -v ~/.hermes:/opt/data ghcr.io/chonsong/hermes-sync:latest
```

---

## Container Architecture

**Image**: `hermes-sync:latest` (based on Hermes Agent v0.13.0, 2026.5.7)

### Services

| Service | Port | URL | Status Check |
|---------|------|-----|--------------|
| Gateway API | 8642 | http://localhost:8642/health | `curl -s localhost:8642/health` |
| Dashboard | 9119 | http://localhost:9119/ | `curl -s localhost:9119/` |

### Docker Compose

Located at `~/hermes-sync/docker/docker-compose.yml`:

```yaml
services:
  gateway:
    image: hermes-sync:latest
    container_name: hermes
    restart: unless-stopped
    network_mode: host
    volumes:
      - /home/sean/.hermes:/opt/data
      - /home/sean/hermes-sync:/opt/data/hermes-sync:ro
   ...
