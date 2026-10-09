---
repo: ChonSong/riptide
url: 'https://github.com/ChonSong/riptide'
description: No description
type: agent
status: active
language: Python
size_kb: 2791
stars: 0
last_pushed: '2026-10-09'
license: unknown
tags:
  - ai
  - api
  - bot
  - ide
  - orchestration
  - python
  - web-app
topics: []
refreshed_at: '2026-10-09 22:21 UTC'
---

# riptide

> No description

**URL:** [ChonSong/riptide](https://github.com/ChonSong/riptide)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** Python
- **Size:** 2,791 KB
- **Stars:** 0
- **Last Pushed:** 2026-10-09
- **License:** unknown
- **Tags:** ai, api, bot, ide, orchestration, python, web-app

## README Excerpt

<img width="600" height="300" alt="Riptide Banner" src="https://github.com/user-attachments/assets/a57103c0-a98a-41f1-b7b1-fc9b4a23e27e" />

# Riptide Review Pipeline

Automated code review for GitHub PRs using a three-bot system.

## Quick Start

```bash
# Run locally
python3 server.py

# Run with production config
python3 server.py --prod

# Run tests
python3 -m pytest riptide/tests/ -q
```

## Architecture

### Three-Bot System

| Bot | Trigger | What it does |
|-----|---------|--------------|
| **Companion** | PR opened/updated | Posts instant TL;DR + ELI5 with blast-radius analysis |
| **Deepthink** | Cron (15 min) or `@riptide-bot review` | Full deep-think review with findings |
| **Proofshotter** | Cron (10 min) | Posts visual evidence (GIF/screenshots) for UI changes |

### Data Flow

```text
riptide/
├── riptide/                    # the application package
│   ├── webhook.py              # FastAPI server, GitHub webhook handler
│   ├── companion.py            # Bot 1: TL;DR + ELI5 + timing footer
│   ├── deepthink.py            # Bot 2: Cron + @riptide-bot review spawner
│   ├── proofshotter.py         # Bot 3: Visual verification (GIF/screenshots)
│   ├── fixer.py                # Bot 2b: Autonomous fix via @riptide-bot fix
│   ├── poller.py               # Cron entry point for Bot 2/3 discovery
│   ├── state.py                # SQLite-backed state (dedup, jobs, reservations)
│   ├── labeler.py              # GitHub label engine
│   ├── assemble_review.py      # Structured findings assembly + sign-off
│   ├── diff_analyzer.py        # Deterministic complexity/defect scan
│   ├── depth.py                # ReviewDepth enum + classifier
│   ├── pipeline/               # Conductor review pipeline, one module per role
│   │   ├── conductor.py        #   workstream orchestration, canonical output paths
│   │   ├── probe.py            #   ws-1 PR context
│   │   ├── judge.py            #   ws-2 findings (stamps `ju...
