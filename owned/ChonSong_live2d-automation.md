---
repo: 'ChonSong/live2d-automation'
url: 'https://github.com/ChonSong/live2d-automation'
description: Live2D Automation MCP Server
type: cli
status: active
language: Python
size_kb: 391
stars: 0
last_pushed: '2026-08-03'
license: unknown
tags:
  - ai
  - automation
  - cli
  - ide
  - mcp
  - python
  - solver
topics: []
refreshed_at: '2026-10-09 22:21 UTC'
---

# live2d-automation

> Live2D Automation MCP Server

**URL:** [ChonSong/live2d-automation](https://github.com/ChonSong/live2d-automation)

## Metadata

- **Type:** cli
- **Status:** active
- **Language:** Python
- **Size:** 391 KB
- **Stars:** 0
- **Last Pushed:** 2026-08-03
- **License:** unknown
- **Tags:** ai, automation, cli, ide, mcp, python, solver

## README Excerpt

﻿# Live2D Automation MCP Server

Generate a mock intermediate Live2D package from a single character image.

## Features

- MCP tools for image analysis, face extraction, layer generation, rigging, physics, motions, and export
- Server-issued session IDs with TTL, concurrency limits, explicit close support, and status metrics
- Output directory confinement under `output/`
- Mock `.moc3` export contract validated before success is reported
- Explicit `detector_used`, `fallback_reason`, and `confidence_summary` metadata on analysis steps

## Installation

Minimal runtime:

```bash
pip install -e .
```

CPU-assisted vision stack:

```bash
pip install -e ".[vision-cpu]"
```

GPU-assisted vision stack:

```bash
pip install -e ".[vision-gpu]"
```

Development tools:

```bash
pip install -e ".[dev]"
```

## Usage

### Run the MCP server

```bash
python -m mcp_server.server
```

### Run the local CLI workflow

```bash
live2d-run run --image-path ATRI.png --output-dir output/ATRI --demo-adapter-mode full
```

Or without the console script:

```bash
python -m mcp_server.cli run --image-path ATRI.png --output-dir output/ATRI --demo-adapter-mode full
```

The CLI writes a `<model_name>_cli_report.json` file into the output directory.

If you already have a Cubism-ready PSD and only want to tune the Cubism automation half, use the
calibration command instead of re-running image analysis:

```bash
python -m mcp_server.cli calibrate-template --output-dir output/ATRI_real --model-name ATRI --psd-path output/ATRI_real/ATRI.psd --editor-path "C:\Program Files\Live2D\Cubism5\Cubism Editor 5\CubismEditor5.exe" --native-gui-controller-mode execute
```

If `--psd-path` is omitted, the CLI will look for `<output_dir>/<model_name>.psd`. This is the
fastest loop for calibrating `template_menu_sequence`, because it only rebuilds the Cubism plan,
dispatch bundle, execution report, and profile calibration report.

Add `--resume` when you want to continue from the latest compatible dispatch exe...
