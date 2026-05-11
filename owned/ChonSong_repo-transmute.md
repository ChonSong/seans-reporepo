---
repo: 'ChonSong/repo-transmute'
url: 'https://github.com/ChonSong/repo-transmute'
description: 'AI-powered code transpilation engine'
type: agent
status: active
language: TypeScript
size_kb: 4220
stars: 0
last_pushed: '2026-05-10'
license: unknown
tags:
  - agent
  - ai
  - api
  - cli
  - ide
  - llm
  - multi-agent
  - python
  - solver
  - transpilation
  - typescript
  - vector-search
---

# repo-transmute

> AI-powered code transpilation engine

**URL:** [ChonSong/repo-transmute](https://github.com/ChonSong/repo-transmute)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** TypeScript
- **Size:** 4,220 KB
- **Stars:** 0
- **Last Pushed:** 2026-05-10
- **License:** unknown
- **Tags:** agent, ai, api, cli, ide, llm, multi-agent, python, solver, transpilation, typescript, vector-search

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
# Clone repo and extract blueprint
cd repo-transmute
PYTHONPATH=src python3 -m repo_transmute.cli ingest <owner/repo>

# Or run full pipeline (ingest + transpile + validate)
PYTHONPATH=src python3 -m repo_transmute.cli pipeline <owner/repo> --target typescript

# Check status
PYTHONPATH=src python3 -m repo_transmute.cli status
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
| Phase 7: Frontend Migration | ✅ Complete |

## CLI Commands

| Command | Description |
|---------|-------------|
| `ingest <repo>` | Clone repo, detect language, extract blueprint |
| `pipeline <repo> -t <target>` | Full pipeline: ingest → transpile → validate |
| `chunk <repo> -s <size>` | Split large repos into manageable chunks |
| `deps <repo>` | Analyze repository dependencies |
| `transpile <blueprint> -t <target>` | Convert blueprint to target language |
| `validate <file> -l <language>` | Validate transpiled code |
| `status` | Show cached repos and blueprints |
| **`frontend_blueprint <path>`** | **Extract frontend blueprint (components, routes, CSS, APIs)** |
| **`theme_analysis <src> -t <tgt>`** | **Analyze theme system compatibility** |
| **`api_analysis <src> -t <tgt>`** | **Generate API migration bl...
