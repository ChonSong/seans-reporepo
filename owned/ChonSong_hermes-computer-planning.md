---
repo: 'ChonSong/hermes-computer-planning'
url: 'https://github.com/ChonSong/hermes-computer-planning'
description: 'Analysis of computer-use repos vs Agent-OS v1.2 spec: coder-desktop-linux, kasm-mcp-server-v2, bytebot, cua'
type: library
status: active
language: other
size_kb: 6
stars: 0
last_pushed: '2026-05-11'
license: unknown
tags:
  - agent
  - ai
  - api
  - automation
  - awesome-list
  - bot
  - framework
  - go
  - hermes-agent
  - ide
  - mcp
  - monitoring
  - python
  - sync
  - typescript
  - vpn
  - web-app
---

# hermes-computer-planning

> Analysis of computer-use repos vs Agent-OS v1.2 spec: coder-desktop-linux, kasm-mcp-server-v2, bytebot, cua

**URL:** [ChonSong/hermes-computer-planning](https://github.com/ChonSong/hermes-computer-planning)

## Metadata

- **Type:** library
- **Status:** active
- **Language:** other
- **Size:** 6 KB
- **Stars:** 0
- **Last Pushed:** 2026-05-11
- **License:** unknown
- **Tags:** agent, ai, api, automation, awesome-list, bot, framework, go, hermes-agent, ide, mcp, monitoring, python, sync, typescript, vpn, web-app

## README Excerpt

# hermes-computer-planning

> Analysis of four computer-use repos against the Agent-OS v1.2 spec. Purpose: assess viability, identify gaps, and critique the "Lean & Powerful" specification.

## Repos Analyzed

| Repo | Stars | Language | License | Last Pushed | Relevance |
|------|-------|----------|---------|-------------|-----------|
| [`coder/coder-desktop-linux`](https://github.com/coder/coder-desktop-linux) | 4 | C# (.NET/Avalonia) | AGPL-3.0 | 2026-03-05 | Remote workspace connectivity |
| [`roguedev-ai/kasm-mcp-server-v2`](https://github.com/roguedev-ai/kasm-mcp-server-v2) | 3 | Python | MIT | 2025-09-12 | Kasm workspace MCP control |
| [`bytebot-ai/bytebot`](https://github.com/bytebot-ai/bytebot) | 11,003 | TypeScript | Apache-2.0 | 2025-09-12 | Full desktop AI agent |
| [`trycua/cua`](https://github.com/trycua/cua) | 15,833 | Python/Swift/TS | MIT | 2026-05-09 | Cross-OS computer-use infra |

---

## 1. `coder/coder-desktop-linux` — Remote Workspace Bridge

### What It Is
C# (.NET 8) + Avalonia desktop app providing VPN-like connectivity to Coder workspaces. Tray app, VPN service integration, file sync — the Linux slice of the broader Coder Desktop product.

### Architecture
```
[Linux Desktop] → [Avalonia Tray App] → [Coder Connect (VPN)] → [Remote Workspace]
                                      → [File Sync]
```

### Strengths
- **Avalonia** — mature cross-platform UI framework for Linux
- **VPN integration** — no port-forwarding needed, clean network model
- **File sync** — bidirectional workspace ↔ local file operations

### Weaknesses for v1.2
- **Wrong language**: C#/.NET — doesn't fit Go backend + SvelteKit
- **AGPL-3.0** — viral license, incompatible with commercial reuse
- **Tiny**: 4 stars, 2 contributors, last push 2 months ago
- **Narrow scope**: Only connectivity, not agent control or desktop automation
- **Depends on external Coder server** — not self-contained

### Verdict
**Not useful directly.** The VPN connectivity concept is interesting ...
