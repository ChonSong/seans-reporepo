---
repo: 'ChonSong/poker-parser'
url: 'https://github.com/ChonSong/poker-parser'
description: No description
type: cli
status: active
language: Python
size_kb: 70
stars: 0
last_pushed: '2026-07-29'
license: unknown
tags:
  - ai
  - awesome-list
  - cli
  - gaming
  - ide
  - video
topics: []
refreshed_at: '2026-10-09 22:21 UTC'
---

# poker-parser

> No description

**URL:** [ChonSong/poker-parser](https://github.com/ChonSong/poker-parser)

## Metadata

- **Type:** cli
- **Status:** active
- **Language:** Python
- **Size:** 70 KB
- **Stars:** 0
- **Last Pushed:** 2026-07-29
- **License:** unknown
- **Tags:** ai, awesome-list, cli, gaming, ide, video

## README Excerpt

# Poker Video Parser

Parse poker hands from YouTube videos and export clean CSV hand histories.

## Quick Start

```bash
uv run poker-parser --help
```

## Subcommands

| Command | Purpose | Status |
|---|---|---|
| `poker-parser fetch <url>` | Download video from YouTube | Stub |
| `poker-parser extract <video>` | Extract key frames via ffmpeg scene-detect | Stub |
| `poker-parser reconstruct <frames-dir>` | Reconstruct hands from existing frames | ✅ |
| `poker-parser profile list` | List available source profiles | ✅ |

## Roadmap

- **Phase 1** ✅ — Repo scaffold, Pydantic models, FSM, CSV export, CLI
- **Phase 2** — yt-dlp downloader + ffmpeg frame extraction + dHash dedup
- **Phase 3** — PaddleOCR integration + card CNN
- **Phase 4** — End-to-end pipeline wiring + source profiles
- **Phase 5** — 40+ tests, fixtures, 2-min test video

## Architecture

See [architecture diagram](https://excalidraw.com/#json=zhusIajVjYwfsHKEymGDR,ZHuRmt5toCE9L_mSXUBcow).

```
poker-parser/
├── src/poker_parser/
│   ├── cli.py                    # CLI entry point
│   ├── models/                   # Pydantic data models
│   │   ├── enums.py
│   │   └── hand.py               # Card, Action, PlayerState, Hand
│   ├── core/
│   │   └── state_machine.py      # FSM + EvidenceBuffer + PokerGrammar
│   ├── export/
│   │   └── csv_exporter.py       # 3 CSV export formats
│   ├── ingestion/                # (stubs) downloader, extractor, deduper
│   └── vision/                   # (stubs) OCR, card classifier, registration
├── profiles/                     # Source layout profiles (YAML)
├── tests/
│   ├── fixtures/                 # Ground truth + test frames
│   ├── test_state_machine.py
│   └── test_csv_export.py
└── pyproject.toml
```
...
