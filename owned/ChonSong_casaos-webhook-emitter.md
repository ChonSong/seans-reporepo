---
repo: 'ChonSong/casaos-webhook-emitter'
url: 'https://github.com/ChonSong/casaos-webhook-emitter'
description: Webhook emitter sidecar for CasaOS — subscribes to MessageBus events and fans them out as HTTP webhooks to agent endpoints.
type: agent
status: active
language: Go
size_kb: 21
stars: 0
last_pushed: '2026-04-05'
license: unknown
tags:
  - agent
  - ai
  - api
  - awesome-list
  - go
  - ide
  - web-app
topics: []
refreshed_at: '2026-07-02 13:30 UTC'
---

# casaos-webhook-emitter

> Webhook emitter sidecar for CasaOS — subscribes to MessageBus events and fans them out as HTTP webhooks to agent endpoints.

**URL:** [ChonSong/casaos-webhook-emitter](https://github.com/ChonSong/casaos-webhook-emitter)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** Go
- **Size:** 21 KB
- **Stars:** 0
- **Last Pushed:** 2026-04-05
- **License:** unknown
- **Tags:** agent, ai, api, awesome-list, go, ide, web-app

## README Excerpt

# CasaOS Webhook Emitter

> **Status:** Phase 1 — Scaffolded. Awaiting MessageBus API research to wire real WebSocket subscription.

A small, long-running Go service that subscribes to the CasaOS-MessageBus WebSocket stream and fans out matching events as HTTP POST requests to registered webhook endpoints.

GitHub: https://github.com/ChonSong/casaos-webhook-emitter

## What It Does

```
CasaOS-MessageBus (WebSocket)
        │
        ▼
┌─────────────────────────┐
│  Webhook Emitter        │
│  • Subscribes to events │
│  • Matches to webhooks  │
│  • Delivers with retry  │
└─────────────────────────┘
        │
        ▼
  Registered Agent Webhooks
```

## Quick Start

```bash
# Build
make build

# Configure
cp webhook-emitter.yaml ~/.config/casaos-agent/webhook-emitter.yaml
nano ~/.config/casaos-agent/webhook-emitter.yaml

# Run
./casaos-webhook-emitter

# Or via systemd (recommended)
systemctl --user enable --now casaos-webhook-emitter
```

## Configuration

`~/.config/casaos-agent/webhook-emitter.yaml`:

```yaml
message_bus:
  url: "http://localhost:8080"
  token: ""           # from CasaOS auth config
  websocket_path: "/v2/message_bus/subscribe/event"

emitter:
  listen: "localhost:9393"
  max_concurrent_deliveries: 10
  delivery_timeout_seconds: 10
  retry_attempts: 3
  retry_backoff_seconds: [1, 5, 30]
  rate_limit_per_minute: 60

webhooks:
  config_path: "~/.config/casaos-agent/webhooks.json"
  hot_reload: true
```

## Webhook Registration

Agents register webhooks via the emitter's management API:

```bash
# Register
curl -X POST http://localhost:9393/webhooks \
  -H "Content-Type: application/json" \
  -d '{"url": "https://agent.example.com/hooks/casaos", "events": ["casaos:file:operate"]}'

# List
curl http://localhost:9393/webhooks

# Delete
curl -X DELETE http://localhost:9393/webhooks/wh_abc123xyz

# Test
curl -X POST http://localhost:9393/webhooks/wh_abc123xyz/test
```

Or use [casaos-agent](https://github.com/ChonSong/casaos-agent):

```bash
casaos-ag...
