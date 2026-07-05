---
repo: 'ChonSong/claw-aie'
url: 'https://github.com/ChonSong/claw-aie'
description: 'AIE-compatible harness with working hooks and tool execution'
type: agent
status: active
language: Python
size_kb: 126
stars: 0
last_pushed: '2026-04-17'
license: unknown
tags:
  - agent
  - ai
  - aie
  - cli
  - harness
  - python
  - sync
topics: []
refreshed_at: '2026-07-05 03:43 UTC'
---

# claw-aie

> AIE-compatible harness with working hooks and tool execution

**URL:** [ChonSong/claw-aie](https://github.com/ChonSong/claw-aie)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** Python
- **Size:** 126 KB
- **Stars:** 0
- **Last Pushed:** 2026-04-17
- **License:** unknown
- **Tags:** agent, ai, aie, cli, harness, python, sync

## README Excerpt

# claw-aie — AIE-Compatible Agent Harness

> Instrumented agent harness with async tool execution, PreToolUse/PostToolUse hooks, and AIE event emission.
> Part of the [ChonSong Ecosystem](https://github.com/ChonSong/ecosystem).

---

## What It Does

claw-aie is the **canonical execution layer** for the Agent Interaction Evaluator (AIE) ecosystem. Every consequential action passes through a hook pipeline, and every hook can emit structured events to AIE for indexing, drift detection, and audit trail generation.

```
Agent request
    ↓
ToolExecutor.execute(tool, input)
    ↓ HookRunner.run_pre_tool_use() ← permission, rate limit, AIE emit
    ↓ (denied? → return blocked)
    ↓ _dispatch(tool, input) → actual execution
    ↓ HookRunner.run_post_tool_use() ← AIE emit with outcome
    ↓
ToolResult
    ↓ event emitted to AIE logger via /tmp/ailogger.sock
```

## Architecture

```
claw-aie/
├── src/                          # claw-code Python routing layer (upstream, as-is)
├── aie_integration/              # Our additions
│   ├── tool_executor.py          # Async tool executor (bash, file_read, file_write, glob, grep)
│   ├── sanitiser.py              # Secret stripping for event payloads
│   ├── hooks/
│   │   ├── base.py               # ToolHook ABC
│   │   ├── runner.py             # HookRunner — PreToolUse / PostToolUse pipeline
│   │   ├── permission_hook.py    # Block destructive tools (rm -rf, system paths)
│   │   ├── rate_limit_hook.py    # Per-tool token bucket rate limiting
│   │   └── aie_emitter.py        # Emit structured events to AIE logger
│   ├── config.py                 # hooks.yaml loader
│   └── cli.py                    # CLI entry point (Phase D)
├── SPEC.md                       # Full specification
└── tests/
```

## Quick Start

```bash
# Install dependencies
pip install -e .

# Run a tool directly (Phase A — working)
PYTHONPATH=src:. python3 -c "
import asyncio
from aie_integration.tool_executor import ToolExecutor

async def main():
    exec...
