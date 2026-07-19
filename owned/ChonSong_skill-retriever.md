---
repo: 'ChonSong/skill-retriever'
url: 'https://github.com/ChonSong/skill-retriever'
description: 'AgentSkillOS-powered semantic skill retrieval for Hermes Agent.'
type: agent
status: active
language: HTML
size_kb: 35506
stars: 6
last_pushed: '2026-07-18'
license: unknown
tags:
  - agent
  - ai
  - api
  - cli
  - go
  - hermes-agent
  - ide
  - infrastructure
  - llm
  - plugin
  - python
  - rag
topics:
  - hermes-agent
  - skills
refreshed_at: '2026-07-19 23:34 UTC'
---

# skill-retriever

> AgentSkillOS-powered semantic skill retrieval for Hermes Agent.

**URL:** [ChonSong/skill-retriever](https://github.com/ChonSong/skill-retriever)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** HTML
- **Size:** 35,506 KB
- **Stars:** 6
- **Last Pushed:** 2026-07-18
- **License:** unknown
- **Tags:** agent, ai, api, cli, go, hermes-agent, ide, infrastructure, llm, plugin, python, rag

## README Excerpt

<p align="center">
  <img src="logo.png" alt="Skill Retriever" height="130">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
</p>

# Skill Retriever

> **Composer-based dynamic skill curation for Hermes Agent.**

Walks a YAML capability tree once to build a flat index (~50KB, ~400 skills), then uses a **single LLM call** to curate a query-specific bundle of 3-20 skills — complete with load levels (★/▸/·), confidence scores, and reasoning.

## Why Composer?

Old approach: recursive LLM tree descent (5 levels × branching 3 = **~243 calls/query**). Unusable for real-time.

New approach: flat index pre-filter → single LLM curation → **1 call/query**, sub-second latency.

## How It Works

```
User Query → flat index pre-filter (top 50) → LLM picks best 3-20 → inject hints
```

Each skill gets:

| Field | Meaning |
|-------|---------|
| `name` | Skill name (call `skill_view(name)` to load) |
| `load_as` | `must` ★ / `should` ▸ / `consider` · |
| `confidence` | `high` / `medium` / `low` |
| `reason` | Why this skill fits the query |

### Hint Block (injected into user message)

```
[Skill Capability Chain]

These skills are curated for this query.
Call skill_view('<name>') to load each one.

  ★ cloudflare-tunnel — Tunnel deployment + credential management
  ▸ infrastructure-as-code — Terraform for Cloudflare tunnels
  · devops — Broader deployment workflows
```

## Quick Start

```bash
pip install skill-retriever
skill-retriever install          # optional: install bundled community skills
```

No plugin development needed — the Hermes plugin is registered automatically.

## CLI

```bash
# Rebuild the flat index (after adding new skills)
skill-retriever rebuild

# Compose a bundle for a query
skill-retriever compose "deploy a cloudflare tunnel"

# Show index info
skill-retriever info
```

## Integration Points

| Point | What | W...
