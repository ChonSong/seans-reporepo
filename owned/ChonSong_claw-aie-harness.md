---
repo: 'ChonSong/claw-aie-harness'
url: 'https://github.com/ChonSong/claw-aie-harness'
description: '"OpenHarness: Open Agent Harness with a Built-in Personal Agent--Ohmo!"'
type: agent
status: active
language: Python
size_kb: 10759
stars: 0
last_pushed: '2026-04-14'
license: unknown
tags:
  - agent
  - ai
  - aie
  - awesome-list
  - go
  - harness
  - python
  - vector-search
topics: []
refreshed_at: '2026-07-02 10:28 UTC'
---

# claw-aie-harness

> "OpenHarness: Open Agent Harness with a Built-in Personal Agent--Ohmo!"

**URL:** [ChonSong/claw-aie-harness](https://github.com/ChonSong/claw-aie-harness)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** Python
- **Size:** 10,759 KB
- **Stars:** 0
- **Last Pushed:** 2026-04-14
- **License:** unknown
- **Tags:** agent, ai, aie, awesome-list, go, harness, python, vector-search

## README Excerpt

<h1 align="center">
  <code>claw-aie-harness</code>
  <br>
  <sub>OpenHarness + AIE Observability</sub>
</h1>

<p align="center">
  <a href="https://github.com/HKUDS/OpenHarness"><img src="https://img.shields.io/badge/Fork_of-OpenHarness-blue?style=for-the-badge" alt="OpenHarness Fork"></a>
  <a href="#aie-integration"><img src="https://img.shields.io/badge/AIE-Observability-ff69b4?style=for-the-badge" alt="AIE Integration"></a>
  <a href="#quick-start"><img src="https://img.shields.io/badge/Quick_Start-2_min-blue?style=for-the-badge" alt="Quick Start"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-≥3.10-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Tools-43+-green?style=for-the-badge" alt="43+ Tools">
  <img src="https://img.shields.io/badge/AIE_Events-7_types-purple?style=for-the-badge" alt="7 AIE Event Types">
  <img src="https://img.shields.io/badge/Tests-142_Passing-brightgreen" alt="142 Tests">
</p>

**claw-aie-harness** is a fork of [OpenHarness](https://github.com/HKUDS/OpenHarness) with built-in AIE (Agent Interaction Evaluator) observability. Every tool call, delegation, and session event is captured, sanitized, and logged — so you can audit, replay, and evaluate what your agents actually did.

It inherits everything from OpenHarness: 43+ tools, swarm coordination, skills, hooks, memory, and multi-platform chat. Then it adds a zero-config observability layer on top.

---

## Quick Start

### Install

```bash
git clone https://github.com/ChonSong/claw-aie-harness.git
cd claw-aie-harness
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

### Start the AIE Receiver

```bash
oh aie serve
# Listening on http://0.0.0.0:8901
```

### Configure Hooks

Copy the default hook config into your project:

```bash
mkdir -p .openharness
cp .openharness/aie...
