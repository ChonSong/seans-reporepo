---
repo: 'ChonSong/dev-loop'
url: 'https://github.com/ChonSong/dev-loop'
description: 'Autonomous coach/player development loop — AGENTS.md standard, checkpoint schema, cron config, scoring model, and project onboarding'
type: agent
status: active
language: Python
size_kb: 20354
stars: 0
last_pushed: '2026-06-30'
license: unknown
tags:
  - agent
  - ai
  - bot
  - hermes-agent
  - ide
  - rag
  - reliability
  - rust
topics: []
refreshed_at: '2026-07-05 23:53 UTC'
---

# dev-loop

> Autonomous coach/player development loop — AGENTS.md standard, checkpoint schema, cron config, scoring model, and project onboarding

**URL:** [ChonSong/dev-loop](https://github.com/ChonSong/dev-loop)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** Python
- **Size:** 20,354 KB
- **Stars:** 0
- **Last Pushed:** 2026-06-30
- **License:** unknown
- **Tags:** agent, ai, bot, hermes-agent, ide, rag, reliability, rust

## README Excerpt

# Dev Loop — Autonomous Development System

A multi-loop autonomous development system:
- **Grand SIE** (Strategic Intelligence Engine) — the top-layer brain. Scans the external world weekly (GitHub trending, arXiv, competitors, HN), decides what's worth building, and produces requirements specs. See [`docs/grand-sie-architecture.md`](docs/grand-sie-architecture.md).
- **Player** agents implement tasks from a backlog
- **Coach** agents adversarially review each commit, probe for gaps, and generate the next batch of tasks
- **Observation Memory** (`coach_memory.py`) — persistent, self-correcting behavioral knowledge store for the Coach. FTS5 query, trust-scored observations, circuit breaker for safety. Ported from agent-qa's A.U.D.N. curator pattern.
- **Self-Improvement Engine** (SIE) scans every 48h for coverage blind spots, processes learnings, and authors skills. Extended by Grand SIE for outward-facing strategic intelligence.

Inspired by g3's dialectical autocoding (Block AI Research, Dec 2025) and built by composing patterns from 10+ existing agent skills.

## Core Concept

Four autonomous loops with increasing cycle times:

```mermaid
flowchart TB
    subgraph GRAND_SIE["GRAND SIE — STRATEGIC INTELLIGENCE (weekly/biweekly)"]
        direction LR
        RADAR[Opportunity Radar] -->|external signals| SYNTH[Synthesis Engine]
        AUDIT[Self-Audit Engine] -->|internal waste| SYNTH
        SYNTH -->|strategic brief| REQ[Requirements Engine]
        REQ -->|specs + tasks| PLAYER_COACH
    end

    subgraph PLAYER_COACH["PLAYER/COACH LOOP (every 30m)"]
        AGENTS[AGENTS.md] -->|tasks + criteria| Player
        Player -->|implemented code| Checkpoint
        Checkpoint -->|review request| Coach
        Coach -->|reviews, approves, probes gaps| AGENTS
        Coach -->|generates tasks| AGENTS

        subgraph Memory["Observation Memory Layer (coach_memory.py)"]
            direction LR
            BRKR[Circuit Breaker] -->|if not tripped| INDEX[Memory Index]
...
