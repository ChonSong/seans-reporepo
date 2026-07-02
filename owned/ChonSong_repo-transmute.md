---
repo: 'ChonSong/repo-transmute'
url: 'https://github.com/ChonSong/repo-transmute'
description: 'AI-powered code transpilation engine'
type: library
status: active
language: TypeScript
size_kb: 4032
stars: 0
last_pushed: '2026-05-24'
license: unknown
tags:
  - agent
  - ai
  - cli
  - framework
  - ide
  - llm
  - multi-agent
  - python
  - react
  - solver
  - svelte
  - transpilation
  - typescript
  - vector-search
topics: []
refreshed_at: '2026-07-02 10:28 UTC'
---

# repo-transmute

> AI-powered code transpilation engine

**URL:** [ChonSong/repo-transmute](https://github.com/ChonSong/repo-transmute)

## Metadata

- **Type:** library
- **Status:** active
- **Language:** TypeScript
- **Size:** 4,032 KB
- **Stars:** 0
- **Last Pushed:** 2026-05-24
- **License:** unknown
- **Tags:** agent, ai, cli, framework, ide, llm, multi-agent, python, react, solver, svelte, transpilation, typescript, vector-search

## README Excerpt

# RepoTransmute - AI-Powered Code Transpilation Engine

> Automated repository ingestion → compatibility checking → blueprint generation → transpilation

## Vision

AI-powered code transpilation engine that:
1. Ingests repositories (clone + analyze)
2. Validates compatibility (source → target routing)
3. Generates language-agnostic blueprints
4. Transpiles to target languages (with multi-agent review)
5. Provides semantic search (txtai)
6. Unifies frontends via screenshot reconstruction

## Quick Start

```bash
# v2 (recommended) — Vision-driven migration
cd repo-transmute
PYTHONPATH=src python3 -m repo_transmute.v2.cli ingest <owner/repo>

# Legacy v1 pipeline
cd repo-transmute
PYTHONPATH=src python3 -m repo_transmute.cli ingest <owner/repo>

# Legacy v1 full pipeline
PYTHONPATH=src python3 -m repo_transmute.cli pipeline <owner/repo> --target typescript
```

## Current Status

| Phase | Status |
|-------|--------|
| Phase 1: MVP | ✅ Complete |
| Phase 2: LLM Transpilation | ✅ Complete |
| Phase 3: Compatibility & Safety | ✅ Complete |
| Phase 4: Multi-Agent Pipeline | 🔄 In Progress |
| Phase 5: Dependency Resolution | ⏳ Pending |
| Phase 6: TXTAI Semantic Layer | ⏳ Pending |
| Phase 7: Frontend Migration | ✅ Complete (v2) |

---

# v2 CLI Commands (Recommended)

v2 uses vision-driven migration with AST extraction, Playwright screenshots, LLM code generation, and self-healing verification.

## Commands

| Command | Description |
|---------|-------------|
| `v2 ingest <repo>` | Clone repo, detect framework (React/Vue/Svelte), extract AST blueprint |
| `v2 ingest --local /path` | Use local path instead of GitHub repo |
| `v2 screenshot <repo>` | Capture Playwright screenshots for visual reference |
| `v2 migrate <source> <target>` | Full migration: extract → migrate → verify → iterate |
| `v2 verify <src_ss> <tgt_ss>` | Compare source vs target screenshots (visual verification) |
| `v2 qa <reference.png>` | Autonomous QA: screenshot → compare → report → iterate |

###...
