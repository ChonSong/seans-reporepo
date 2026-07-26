---
repo: 'ChonSong/docker-tunnel-sidecar'
url: 'https://github.com/ChonSong/docker-tunnel-sidecar'
description: 'External token-v1 sidecar runtime for the Docker & Tunnel Manager Hermes WebUI extension.'
type: agent
status: active
language: Python
size_kb: 8
stars: 0
last_pushed: '2026-07-21'
license: unknown
tags:
  - ai
  - api
  - awesome-list
  - bot
  - docker
  - hermes-agent
  - ide
  - proxy
  - python
  - solver
  - web-app
topics: []
refreshed_at: '2026-07-26 23:00 UTC'
---

# docker-tunnel-sidecar

> External token-v1 sidecar runtime for the Docker & Tunnel Manager Hermes WebUI extension.

**URL:** [ChonSong/docker-tunnel-sidecar](https://github.com/ChonSong/docker-tunnel-sidecar)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** Python
- **Size:** 8 KB
- **Stars:** 0
- **Last Pushed:** 2026-07-21
- **License:** unknown
- **Tags:** ai, api, awesome-list, bot, docker, hermes-agent, ide, proxy, python, solver, web-app

## README Excerpt

# Docker & Tunnel Manager — External Sidecar Runtime

External `token-v1` sidecar for the Docker & Tunnel Manager Hermes WebUI
extension. Implements the language-neutral
[sidecar contract](https://github.com/hermes-webui/hermes-webui-extensions/blob/main/docs/SIDECAR_CONTRACT.md)
in Python.

This repo is the `repository` declared by the extension manifest's
`runtime.kind: "external"` entry. WebUI provisions a per-extension secret at
`STATE_DIR/sidecar-auth/docker-tunnel-manager.token` and injects it as
`X-Hermes-Sidecar-Token` on every proxied request.

## Contract scope — be honest

This sidecar exposes Docker container/image/volume mutations, host socket data,
and tunnel ingress information over `127.0.0.1:17900`. The `token-v1` mechanism
converts *"any local process that can send a loopback TCP packet"* into
*"processes that can read the user's WebUI state dir"* — the same protection
level WebUI's own auth already has. It does **not** defend against arbitrary
same-UID code: a process running as the same user can read the token file
directly, or just talk to the Docker socket itself. No mechanism available here
(token, HMAC, nonce, Unix socket with `0600`) changes that.

## Auth-off posture

WebUI authentication is off by default; `token-v1` is fail-closed in that state.
Both consent and proxy-target resolution return `403` until WebUI authentication
is enabled. Enable it via **Settings → Password** (or `HERMES_WEBUI_PASSWORD`).

## Token resolution order

`HERMES_EXT_SIDECAR_TOKEN_FILE` →
`$HERMES_WEBUI_STATE_DIR/sidecar-auth/docker-tunnel-manager.token` →
`$HERMES_HOME/webui/sidecar-auth/docker-tunnel-manager.token` → platform default
(`~/.hermes/webui/...`).

Re-read per request → rotation is live; constant-time comparison.

## Routes

| Method | Path | Description |
|---|---|---|
| GET/HEAD | `/health` | Liveness only. No token required. `ACAO: *`, `Cache-Control: no-store`. |
| GET | `/api/containers` | List all containers with live CPU/mem stats |
| POST | `...
