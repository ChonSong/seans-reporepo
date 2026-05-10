---
repo: 'ChonSong/agent-os'
url: 'https://github.com/ChonSong/agent-os'
description: 'Agentic OS — monorepo for CasaOS + nanobot + everything-dashboard'
type: monorepo
status: active
language: Python
size_kb: 10219
stars: 0
last_pushed: '2026-05-10'
license: unknown
tags:
  - agent
  - ai
  - api
  - bot
  - dashboard
  - database
  - docker
  - express
  - go
  - hermes-agent
  - ide
  - llm
  - react
  - web-app
---

# agent-os

> Agentic OS — monorepo for CasaOS + nanobot + everything-dashboard

**URL:** [ChonSong/agent-os](https://github.com/ChonSong/agent-os)

## Metadata

- **Type:** monorepo
- **Status:** active
- **Language:** Python
- **Size:** 10,219 KB
- **Stars:** 0
- **Last Pushed:** 2026-05-10
- **License:** unknown
- **Tags:** agent, ai, api, bot, dashboard, database, docker, express, go, hermes-agent, ide, llm, react, web-app

## README Excerpt

# agent-os

> Self-hosted AI agent dashboard — Express backend, React SPA, Hermes Agent, PostgreSQL, Cloudflare tunnel

**Dashboard:** [agent-os.nousresearch.com](https://agent-os.nousresearch.com) (via Cloudflare Tunnel)

---

## Quick Architecture Overview

```
                    Internet
                       │
              ┌────────▼─────────┐
              │  Cloudflare      │
              │  Tunnel (:443)   │
              └────────┬─────────┘
                       │
         ┌─────────────▼──────────────┐
         │  agent-os-backend (:3001)  │
         │  Express + Socket.IO       │
         │  Dockerode + PG pool       │
         │  Serves React SPA from     │
         │  frontend/dist             │
         └──┬──────────┬──────────┬───┘
            │          │          │
    ┌───────▼──┐  ┌───▼────┐  ┌─▼──────────────┐
    │ PostgreSQL│  │ Docker │  │ Hermes Agent    │
    │ (:5432)   │  │ Socket │  │ (host network)  │
    │           │  │(mgmt)  │  │ :8642 (API)     │
    │ sessions  │  └────────┘  │ :9119 (metrics) │
    │ events    │              │ via host.docker  │
    │ cron_jobs │              │  .internal:8642  │
    │ profiles  │              └────────┬────────┘
    │ skills    │                       │
    └───────────┘              ┌────────▼─────────┐
                               │ LLM Provider     │
                               │ (OpenAI-compat)  │
                               └──────────────────┘
```

**Key idea:** Hermes Agent runs as a host-level container (`network_mode: host`) independently of the docker-compose stack. The backend connects to it via `host.docker.internal:8642`.

---

## Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 19 + Vite + Tailwind CSS v4 + @nous-research/ui |
| Backend | Node.js/Express + Socket.IO + Dockerode + PostgreSQL |
| Agent | Hermes Agent (nousresearch/hermes-agent) — OpenAI-compatible `/v1/chat/completions` |
| Database | PostgreSQL 16-alpine |
| Tunnel | Cloudflare Tun...
