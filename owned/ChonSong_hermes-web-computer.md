---
repo: 'ChonSong/hermes-web-computer'
url: 'https://github.com/ChonSong/hermes-web-computer'
description: 'Agent-OS v1.2: browser-native collaborative dev environment with Hermes + Fun-Audio-Chat'
type: agent
status: active
language: Svelte
size_kb: 13903
stars: 0
last_pushed: '2026-06-01'
license: unknown
tags:
  - agent
  - ai
  - audio
  - browser-automation
  - cli
  - docker
  - go
  - hermes-agent
  - sync
  - telemetry
  - terminal
  - voice
  - web-app
  - workflow-engine
---

# hermes-web-computer

> Agent-OS v1.2: browser-native collaborative dev environment with Hermes + Fun-Audio-Chat

**URL:** [ChonSong/hermes-web-computer](https://github.com/ChonSong/hermes-web-computer)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** Svelte
- **Size:** 13,903 KB
- **Stars:** 0
- **Last Pushed:** 2026-06-01
- **License:** unknown
- **Tags:** agent, ai, audio, browser-automation, cli, docker, go, hermes-agent, sync, telemetry, terminal, voice, web-app, workflow-engine

## README Excerpt

# hermes-web-computer

> **hermes-web-computer v1.2** — A browser-based tiling AI desktop for collaborative development between a human, Hermes (text/terminal agent), and Fun-Audio-Chat (voice agent). Web-native tiles (Svelte+Go) as primary model; xpra escape hatch for native Linux GUI apps.

[![Go](https://img.shields.io/badge/Go-1.21+-00ADD8?logo=go)](https://go.dev/)
[![Svelte](https://img.shields.io/badge/Svelte-5-FF3E00?logo=svelte)](https://svelte.dev/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/ChonSong/hermes-web-computer/actions/workflows/ci.yml/badge.svg)](https://github.com/ChonSong/hermes-web-computer/actions)

---

## Philosophy

**Lean but Powerful.** No Temporal, no CRDTs, no AST parsers, no heavy telemetry sync. Backend-owned truth, sub-100ms interrupt, zero protocol bloat.

## Quick Start

```bash
# SSH to host (EndeavourOS)
ssh -i /home/hermeswebui/.hermes/container_key sean@172.19.0.1

# Build backend
cd /home/sean/.hermes/hermes-web-computer/backend
go build -o /tmp/hwc-server ./cmd/server/

# Build frontend
cd /home/sean/.hermes/hermes-web-computer/frontend && npm run build

# Start server (port 3005)
HERMES_HWC_ROOT=/home/sean/.hermes/hermes-web-computer \
  nohup ./hwc-server --port 3005 > /tmp/hwc-server.log 2>&1 &

# Run Go tests
cd /home/sean/.hermes/hermes-web-computer/backend
go test ./... -count=1 -timeout=120s
```

Open `http://localhost:3005` (port 3005, not 3001).

## Architecture

```
┌──────────────────────┐    WebSocket (JSON-RPC Multiplexer)     ┌───────────────────┐
│   Svelte 5 SPA       │ ◄─────────────────────────────────────► │   Go Backend      │
│   (Capture Phase)    │  {"protocol":"ui|agent|audio", ...}    │   (Single Loop)   │
└──────────┬───────────┘                                       └─────────┬─────────┘
           │                                                             │
   ┌───────▼────────┐                                           ┌───────▼──────────...
