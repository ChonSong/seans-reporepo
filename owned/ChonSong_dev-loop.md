---
repo: 'ChonSong/dev-loop'
url: 'https://github.com/ChonSong/dev-loop'
description: 'Autonomous coach/player development loop — AGENTS.md standard, checkpoint schema, cron config, scoring model, and project onboarding'
type: agent
status: active
language: other
size_kb: 19
stars: 0
last_pushed: '2026-06-17'
license: unknown
tags:
  - agent
  - ai
  - awesome-list
  - bot
  - browser-automation
  - hermes-agent
  - ide
  - rust
topics: []
refreshed_at: '2026-06-21 07:46 UTC'
---

# dev-loop

> Autonomous coach/player development loop — AGENTS.md standard, checkpoint schema, cron config, scoring model, and project onboarding

**URL:** [ChonSong/dev-loop](https://github.com/ChonSong/dev-loop)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** other
- **Size:** 19 KB
- **Stars:** 0
- **Last Pushed:** 2026-06-17
- **License:** unknown
- **Tags:** agent, ai, awesome-list, bot, browser-automation, hermes-agent, ide, rust

## README Excerpt

# Dev Loop — Autonomous Coach/Player Development System

A structured autonomous development loop where **Player** agents implement tasks from a backlog and **Coach** agents adversarially review each commit. Inspired by g3's dialectical autocoding (Block AI Research, Dec 2025) and built by composing patterns from 10+ existing agent skills.

## Core Concept

```
AGENTS.md (tasks + criteria)  ──→  Player (implements, tests, commits)
         ↑                              │
         │                              ▼
    Coach (reviews, approves,       Checkpoint.json
    generates next tasks)         (state tracking)
```

Each repo describes itself via `AGENTS.md` + `.checkpoint.json`. The loop discovers repos by scanning for these files.

## How the Agents Were Designed

Both the Player and Coach agents were designed by studying ~12 existing skills in the Hermes ecosystem and extracting their most effective patterns. Here's what inspired each design decision:

### Coach-Agent Inspirations

| Skill | Pattern Borrowed | How It's Used |
|-------|-----------------|---------------|
| **self-improvement-engine** | Weighted scoring formula (`priority × area × recency`) | Adapted to `blocking_weight × confidence` for ranking what task gaps to address first when backlog runs out |
| **parallel-investigation** | Spawn 2-3 subagents, each probing an independent dimension | Used when the Coach needs to check 3+ endpoints/services simultaneously to find what's broken before generating tasks |
| **writing-plans** | 2-5 minute task granularity, exact file paths, verification steps | Each generated task must fit one tick — prevents oversized tasks like "seed strategies" that should be 3-5 smaller ones |
| **planning/blueprint** | "Brainstorm before investigating" — name 2-3 candidates before running probes | Prevents aimless investigation: the Coach already has context from the review and should hypothesize before curling endpoints |
| **planning/product-lens** | ICE scoring (Impact ...
