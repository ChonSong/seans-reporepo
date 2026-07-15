---
repo: 'ChonSong/forrest-plan-and-track'
url: 'https://github.com/ChonSong/forrest-plan-and-track'
description: 'Two-week mission plan for Forrest internship — 14-day plan, scenario brief, experiment logs, diagrams'
type: monorepo
status: active
language: Python
size_kb: 84300
stars: 0
last_pushed: '2026-06-10'
license: unknown
tags:
  - ai
  - api
  - cli
  - dashboard
  - go
  - python
topics: []
refreshed_at: '2026-07-15 00:23 UTC'
---

# forrest-plan-and-track

> Two-week mission plan for Forrest internship — 14-day plan, scenario brief, experiment logs, diagrams

**URL:** [ChonSong/forrest-plan-and-track](https://github.com/ChonSong/forrest-plan-and-track)

## Metadata

- **Type:** monorepo
- **Status:** active
- **Language:** Python
- **Size:** 84,300 KB
- **Stars:** 0
- **Last Pushed:** 2026-06-10
- **License:** unknown
- **Tags:** ai, api, cli, dashboard, go, python

## README Excerpt

# Forrest Plan & Track

> **Mission:** Transform Forrest from a Claude-driven simulation concept into a working data analysis engine over the OneTag HMAS database. No API keys. No external services. Just structured analysis over real industrial data.

## The Promise

Your schema loads once. Forrest runs it in 0.1 seconds. Three findings emerge.

## North Star

A non-technical viewer should be able to read the three findings and say *"that's actually useful — I'd act on that."* Plain language beats clever modelling.

## Repo Structure

```
forrest-plan-and-track/
├── README.md              ← You are here
├── PLAN.md                ← Full plan (updated for data analysis)
├── FORREST-MODEL.md       ← Engine: Query→Analyze→Rank loop
├── SCENARIO.md            ← OneTag HMAS domain description
├── DEMO.md                ← Demo day presentation outline
├── PROGRESS.md            ← Running status board
├── data/
│   └── onetag.db          ← SQLite database (seeded sample data)
├── engine/
│   ├── runner.py          ← Main entry point
│   ├── findings.py        ← Finding data model
│   ├── scoring.py         ← Finding scoring
│   └── passes/
│       ├── anomalies.py   ← Data integrity checks
│       ├── patterns.py    ← Usage pattern recognition
│       ├── relations.py   ← Cross-entity correlations
│       └── stats.py       ← Statistical distributions
├── streamlit_onetag/
│   └── app.py             ← Dashboard with "🚀 Forrest Findings" page
├── prisma/
│   ├── schema.prisma      ← Full OneTag data model
│   └── schema.sqlite.sql  ← SQLite CREATE TABLE statements
├── scripts/
│   └── seed_data.py       ← Database seed script
├── diagrams/              ← Mermaid + HTML visualizations
├── experiments/           ← Experiment log templates
├── daily-logs/            ← Daily standup templates
└── notes/                 ← Analysis notes and gotchas
```

## Status

| Phase | Status |
|-------|--------|
| Foundation (schema + seed data) | ✅ Complete |
| Engine concept rewrite | ✅ ...
