---
repo: 'ChonSong/hermes-workspace'
url: 'https://github.com/ChonSong/hermes-workspace'
description: 'Native web workspace for Hermes Agent — chat, terminal, memory, skills, inspector.'
type: monorepo
status: active
language: JavaScript
size_kb: 104418
stars: 0
last_pushed: '2026-07-07'
license: unknown
tags:
  - agent
  - ai
  - api
  - dashboard
  - docker
  - hermes-agent
  - mcp
  - multi-agent
  - orchestration
  - terminal
  - tui
  - web-app
topics: []
refreshed_at: '2026-07-15 00:23 UTC'
---

# hermes-workspace

> Native web workspace for Hermes Agent — chat, terminal, memory, skills, inspector.

**URL:** [ChonSong/hermes-workspace](https://github.com/ChonSong/hermes-workspace)

## Metadata

- **Type:** monorepo
- **Status:** active
- **Language:** JavaScript
- **Size:** 104,418 KB
- **Stars:** 0
- **Last Pushed:** 2026-07-07
- **License:** unknown
- **Tags:** agent, ai, api, dashboard, docker, hermes-agent, mcp, multi-agent, orchestration, terminal, tui, web-app

## README Excerpt

<div align="center">

<img src="./public/claude-avatar.webp" alt="Hermes Workspace" width="80" style="border-radius: 16px" />
<!-- avatar filename retained for cache stability — do not rename without coordinated cache-bust -->

# Hermes Workspace

**Your AI agent's command center — chat, files, memory, skills, and terminal in one place.**

[![CI](https://github.com/outsourc-e/hermes-workspace/actions/workflows/ci.yml/badge.svg)](https://github.com/outsourc-e/hermes-workspace/actions/workflows/ci.yml)
[![Security](https://github.com/outsourc-e/hermes-workspace/actions/workflows/security.yml/badge.svg)](https://github.com/outsourc-e/hermes-workspace/actions/workflows/security.yml)
[![Docker](https://github.com/outsourc-e/hermes-workspace/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/outsourc-e/hermes-workspace/actions/workflows/docker-publish.yml)
[![Version](https://img.shields.io/badge/version-2.3.0-2557b7.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Node](https://img.shields.io/badge/node-%3E%3D22.0.0-brightgreen.svg)](https://nodejs.org/)

> Not a chat wrapper. A complete workspace — orchestrate agents, browse memory, manage skills, and control everything from one interface.

> **v2 — zero-fork.** Clone, don't fork. Runs on vanilla [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent) installed via Nous's own installer. Chat, sessions, memory, skills, jobs, MCP, terminal, dashboard, Agent View, and Operations are all in vanilla parity. **Conductor** uses the dashboard mission API when available and falls back to Workspace-native Swarm dispatch (`mode: native-swarm`) when the dashboard endpoint is absent, preserving zero-fork behavior ([#262](https://github.com/outsourc-e/hermes-workspace/issues/262)).

![Hermes Workspace](./docs/screenshots/splash.png)

</div>

---

## Swarm Mode

Hermes Agent Swarm turns the workspace into a live control plane: unlimited Hermes Agents, ...
