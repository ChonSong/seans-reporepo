---
repo: 'ChonSong/hermes-bootstrap'
url: 'https://github.com/ChonSong/hermes-bootstrap'
description: 'Hermes one-command bootstrap'
type: agent
status: active
language: Shell
size_kb: 6
stars: 0
last_pushed: '2026-05-19'
license: unknown
tags:
  - agent
  - ai
  - browser-automation
  - docker
  - hermes-agent
  - sync
  - tui
  - web-app
topics: []
refreshed_at: '2026-07-02 13:30 UTC'
---

# hermes-bootstrap

> Hermes one-command bootstrap

**URL:** [ChonSong/hermes-bootstrap](https://github.com/ChonSong/hermes-bootstrap)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** Shell
- **Size:** 6 KB
- **Stars:** 0
- **Last Pushed:** 2026-05-19
- **License:** unknown
- **Tags:** agent, ai, browser-automation, docker, hermes-agent, sync, tui, web-app

## README Excerpt

# Hermes Bootstrap

One-command install for the full Hermes stack on any Linux machine.

## What it installs

- **hermes-agent** -- autonomous AI agent with memory, skills, cron
- **hermes-webui** -- browser chat interface (localhost:8787)
- **hermes-sync** (private) -- config, skills, memories, workspace

## One-liner

```bash
GITHUB_TOKEN=ghp_your_token_here curl -fsSL https://raw.githubusercontent.com/ChonSong/hermes-bootstrap/main/setup.sh | bash
```

Get your token at https://github.com/settings/tokens — needs **repo** (full) scope for private repos.

## After install

| Service | URL |
|---------|-----|
| WebUI | http://localhost:8787 |
| TUI | docker exec hermes /opt/hermes/.venv/bin/hermes --tui |
| Logs | docker logs hermes -f |
...
