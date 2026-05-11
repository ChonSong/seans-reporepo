---
repo: 'ChonSong/hermes-web-computer'
url: 'https://github.com/ChonSong/hermes-web-computer'
description: 'Agent-OS v1.2: browser-native collaborative dev environment with Hermes + Fun-Audio-Chat'
type: monorepo
status: active
language: Go
size_kb: 5773
stars: 0
last_pushed: '2026-05-11'
license: unknown
tags:
  - agent
  - ai
  - audio
  - benchmarking
  - bot
  - browser-automation
  - docker
  - go
  - harness
  - hermes-agent
  - python
  - svelte
  - sync
  - telemetry
  - terminal
  - voice
  - web-app
  - workflow-engine
topics: []
refreshed_at: '2026-05-11 02:12 UTC'
---

# hermes-web-computer

> Agent-OS v1.2: browser-native collaborative dev environment with Hermes + Fun-Audio-Chat

**URL:** [ChonSong/hermes-web-computer](https://github.com/ChonSong/hermes-web-computer)

## Metadata

- **Type:** monorepo
- **Status:** active
- **Language:** Go
- **Size:** 5,773 KB
- **Stars:** 0
- **Last Pushed:** 2026-05-11
- **License:** unknown
- **Tags:** agent, ai, audio, benchmarking, bot, browser-automation, docker, go, harness, hermes-agent, python, svelte, sync, telemetry, terminal, voice, web-app, workflow-engine

## README Excerpt

# hermes-web-computer

> Agent-OS v1.2: browser-native, strictly tiled, keyboard-centric collaborative environment for a human developer, Hermes (text/terminal agent), and Fun-Audio-Chat (voice agent).

## Philosophy

**Lean but Powerful.** No Temporal, no CRDTs, no AST parsers, no heavy telemetry sync. Backend-owned truth, sub-100ms interrupt, zero protocol bloat.

## Architecture

```
┌─────────────────┐    WebSocket (JSON-RPC Multiplexer)    ┌─────────────────┐
│   Svelte 5 SPA  │ ◄───────────────────────────────────► │   Go Backend    │
│ (Capture Phase) │  {"protocol":"ui|agent|audio", ...}   │  (Single Loop)  │
└────────┬────────┘                                       └────────┬────────┘
         │                                                         │
   ┌─────▼─────┐                                           ┌───────▼────────┐
   │ Layout    │                                           │ PTY Supervisor │
   │ Renderer  │                                           │ Cgroups+PID NS │
   └───────────┘                                           └───────┬────────┘
                                                                   │
                                                          ┌────────▼────────┐
                                                          │ Hermes / Audio  │
                                                          │ Docker+Subproc  │
                                                          └─────────────────┘
```

## Monorepo Structure

```
├── backend/          # Go: multiplexer, PTY, state, security, audio, telemetry
│   ├── cmd/server/   # Entry point
│   ├── ws/           # WebSocket multiplexer + JSON-RPC routing
│   ├── pty/          # PTY supervisor + ring buffer + checkpoint
│   ├── state/        # Layout tree + session state + checkpoints
│   ├── security/     # YAML permissions + token-gated execution
│   ├── audio/        # Fun-Audio-Chat WebSocket relay
│   └── telemetry/    # JSONL ring buffer + async cloud sync
├── front...
