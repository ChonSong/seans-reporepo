---
repo: 'ChonSong/intermediary-agent'
url: 'https://github.com/ChonSong/intermediary-agent'
description: 'A semantic supervisor that sits between you and Hermes — refining messy input, distilling verbose output, and steering the agent.'
type: agent
status: active
language: Python
size_kb: 299
stars: 1
last_pushed: '2026-07-19'
license: unknown
tags:
  - agent
  - ai
  - api
  - audio
  - bot
  - browser-automation
  - cli
  - go
  - hermes-agent
  - ide
  - llm
  - multi-agent
  - python
  - terminal
  - voice
  - web-app
topics: []
refreshed_at: '2026-07-19 23:34 UTC'
---

# intermediary-agent

> A semantic supervisor that sits between you and Hermes — refining messy input, distilling verbose output, and steering the agent.

**URL:** [ChonSong/intermediary-agent](https://github.com/ChonSong/intermediary-agent)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** Python
- **Size:** 299 KB
- **Stars:** 1
- **Last Pushed:** 2026-07-19
- **License:** unknown
- **Tags:** agent, ai, api, audio, bot, browser-automation, cli, go, hermes-agent, ide, llm, multi-agent, python, terminal, voice, web-app

## README Excerpt

# Intermediary Agent

> A self-hosted voice intermediary between you and Hermes. Refines messy input, distills verbose output, handles barge-in steering. Zero third-party API dependencies — runs entirely on your machine.

---

## Architecture

```
Browser (mic/speakers) ⟷ WebSocket ⟷ Voice Server (Python) ⟷ Hermes API
     getUserMedia()          PCM frames        STT → LLM → TTS
     WebRTC AEC                              (all local)
```

**All components run locally:**
- **STT**: faster-whisper (speech → text)
- **LLM**: Ollama qwen2.5:7b (intermediary: refine + distill + steer)
- **TTS**: Kokoro-82m (text → audio)
- **VAD**: silero-vad (speech/silence detection)
- **Hermes**: Your existing API (reasoning)

**No LiveKit. No Deepgram. No Cartesia. No OpenAI. No API keys.**

## Quick Start

### Prerequisites

```bash
# Install Ollama (https://ollama.com)
ollama pull qwen2.5:7b

# Install Kokoro TTS (https://github.com/hexgrad/kokoro)
pip install kokoro

# Install faster-whisper
pip install faster-whisper

# Install other deps
pip install -e ".[voice]"
```

### Run

```bash
# Terminal 1: Start voice server
cd /home/sc/intermediary-agent
python -m intermediary.voice.server

# Terminal 2: Start text server (optional, for text-only mode)
python -m uvicorn webui.text_server:app --host 0.0.0.0 --port 8080

# Browser: Open http://localhost:8080
# Click mic button → speak → hear response
```

## Current Status

| Phase | What | Status | Tests |
|-------|------|--------|-------|
| 0 | Docs, plan, skills loaded | ✅ Done | — |
| 1 | Text MVP (mock Hermes) | ✅ Done | 63 passing |
| 2 | Voice pipeline (local models) | 📋 Planned | — |
| 3 | Real Hermes integration | 📋 Planned | — |
| 4 | Discord bridge | 📋 Planned | — |
| 5 | WebUI extension | 📋 Planned | — |

## Documentation

| File | Purpose |
|------|---------|
| `README.md` | This file — overview, quick start |
| `PLAN.md` | Full implementation plan (architecture, components, integration) |
| `PLAN_PATH_C.md` | DeepThink an...
