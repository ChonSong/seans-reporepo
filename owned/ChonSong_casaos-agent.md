---
repo: 'ChonSong/casaos-agent'
url: 'https://github.com/ChonSong/casaos-agent'
description: 'Agent-native CasaOS CLI — JSON output, --yes non-interactive, --watch streaming. Fork of CasaOS-CLI.'
type: agent
status: active
language: Go
size_kb: 108
stars: 0
last_pushed: '2026-04-05'
license: unknown
tags:
  - agent
  - api
  - awesome-list
  - cli
  - docker
  - go
  - nginx
  - rag
  - web-app
topics: []
refreshed_at: '2026-07-02 10:28 UTC'
---

# casaos-agent

> Agent-native CasaOS CLI — JSON output, --yes non-interactive, --watch streaming. Fork of CasaOS-CLI.

**URL:** [ChonSong/casaos-agent](https://github.com/ChonSong/casaos-agent)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** Go
- **Size:** 108 KB
- **Stars:** 0
- **Last Pushed:** 2026-04-05
- **License:** unknown
- **Tags:** agent, api, awesome-list, cli, docker, go, nginx, rag, web-app

## README Excerpt

# CasaOS Agent CLI

> **Status:** Phase 2 — Fork complete, real CasaOS-CLI wired with agent-native flags.  
> GitHub: https://github.com/ChonSong/casaos-agent

Agent-native CLI for managing a CasaOS instance. Fork of [IceWhaleTech/CasaOS-CLI](https://github.com/IceWhaleTech/CasaOS-CLI) with machine-readable output, non-interactive flags, and streaming support built in.

## Quick Start

```bash
# Build
cd CasaOS-CLI && go build -o bin/casaos-agent .

# Or install
go install github.com/ChonSong/casaos-agent@latest

# List installed apps (JSON output)
casaos-agent --json app-management list apps

# Install app (non-interactive)
casaos-agent --yes app-management install nginx --file docker-compose.yml

# System health check
casaos-agent --json healthcheck services

# Subscribe to MessageBus events as JSON
casaos-agent --json message-bus subscribe websocket \
  --source-id casaos-app-management
```

## Key Differences from upstream `casaos-cli`

| Feature | `casaos-cli` | `casaos-agent` |
|---------|-------------|----------------|
| Output format | Human-formatted tables | **Structured JSON** (with `--json`) |
| Interactive prompts | Yes (blocking) | **Bypass with `--yes`** |
| Streaming output | No | **`--watch` flag** |
| Error codes | No | Typed error codes in JSON envelope |

## Agent-Native Flags

```
--json, -j     Force structured JSON output for all commands
--yes, -y      Skip all confirmation prompts (auto-confirm)
--watch, -w    Stream output for long-running operations
--url, -u      CasaOS API root URL (default: localhost:80)
```

## JSON Output Format

Every command returns a consistent envelope:

```json
{
  "ok": true,
  "command": "app list",
  "data": { ... },
  "timestamp": "2026-04-05T17:00:00Z"
}
```

On error:

```json
{
  "ok": false,
  "command": "app install",
  "error": {
    "code": "ERROR",
    "message": "404 Not Found - is the casaos-app-management service running?"
  },
  "timestamp": "2026-04-05T17:00:00Z"
}
```

## Command Tree

```
casao...
