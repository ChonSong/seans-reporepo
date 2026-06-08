---
repo: 'ChonSong/forrest-plan-and-track'
url: 'https://github.com/ChonSong/forrest-plan-and-track'
description: 'Two-week mission plan for Forrest internship — 14-day plan, scenario brief, experiment logs, diagrams'
type: agent
status: active
language: Python
size_kb: 84214
stars: 0
last_pushed: '2026-06-05'
license: unknown
tags:
  - agent
  - ai
  - api
  - go
  - ide
  - multi-agent
  - rag
---

# forrest-plan-and-track

> Two-week mission plan for Forrest internship — 14-day plan, scenario brief, experiment logs, diagrams

**URL:** [ChonSong/forrest-plan-and-track](https://github.com/ChonSong/forrest-plan-and-track)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** Python
- **Size:** 84,214 KB
- **Stars:** 0
- **Last Pushed:** 2026-06-05
- **License:** unknown
- **Tags:** agent, ai, api, go, ide, multi-agent, rag

## README Excerpt

# Forrest Plan & Track

> **Mission:** Prove that Forrest — an autonomous Monte Carlo optimization engine — can find non-obvious, actionable insights on a scenario nobody on the team has touched. Two weeks. 200 experiments. Three findings. One 15-minute share-out.

## The Promise

Your plan runs once. Forrest runs it 10,000 times.

## North Star

At the end of two weeks, a non-technical viewer should be able to read your three findings and say *"that's actually useful — I'd act on that."* Plain language beats clever modelling.

## Repo Structure

```
forrest-plan-and-track/
├── README.md              ← You are here
├── PLAN.md                ← Full 14-day plan with daily tasks
├── FORREST-MODEL.md       ← Mental model of the engine (read before coding)
├── SCENARIO.md            ← Demo scenario brief (project scheduling)
├── DEMO.md                ← Demo day presentation outline
├── PROGRESS.md            ← Running status board (update daily)
├── diagrams/
│   ├── engine-loop.html   ← Interactive engine loop visualization
│   ├── data-model.html    ← 4-entity data model
│   └── timeline.html      ← 14-day Gantt-style timeline
├── experiments/
│   ├── TEMPLATE.md        ← Copy for each run
│   ├── run-001-smoke.md   ← Day 2: 50-experiment smoke test
│   ├── run-002-tuning-1.md
│   ├── run-003-tuning-2.md
│   ├── run-004-tuning-3.md
│   ├── run-005-dress.md
│   ├── run-006-final-1.md ← Day 8: First 200-experiment run
│   └── run-007-final-2.md ← Day 10: Confidence check
├── daily-logs/
│   ├── TEMPLATE.md        ← Daily standup log template
│   ├── day-00.md
│   ├── day-01.md
│   └── ...
│   └── day-14.md
└── notes/
    ├── code-tour.md       ← Notes from reading the codebase
    ├── gotchas.md         ← Things that have bitten
    ├── tuning-log.md      ← What you changed and why
    └── three-things.md    ← Week 1 review prep (fragile things, unknowns, assumptions)
```

## Status

| Phase | Target | Status |
|-------|--------|--------|
| Day 0: Read & prep | Noteboo...
