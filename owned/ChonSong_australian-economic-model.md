---
repo: 'ChonSong/australian-economic-model'
url: 'https://github.com/ChonSong/australian-economic-model'
description: 'Interactive Streamlit app modelling the Australian economy using Steve Keen's Minskyan debt-dynamics methodology — Keen-Goodwin-Minsky framework with housing, SFC, and resource submodels.'
type: library
status: active
language: Python
size_kb: 258810
stars: 0
last_pushed: '2026-07-02'
license: unknown
tags:
  - ai
  - api
  - browser-automation
  - energy
  - framework
  - go
  - python
  - solver
topics: []
refreshed_at: '2026-07-02 13:30 UTC'
---

# australian-economic-model

> Interactive Streamlit app modelling the Australian economy using Steve Keen's Minskyan debt-dynamics methodology — Keen-Goodwin-Minsky framework with housing, SFC, and resource submodels.

**URL:** [ChonSong/australian-economic-model](https://github.com/ChonSong/australian-economic-model)

## Metadata

- **Type:** library
- **Status:** active
- **Language:** Python
- **Size:** 258,810 KB
- **Stars:** 0
- **Last Pushed:** 2026-07-02
- **License:** unknown
- **Tags:** ai, api, browser-automation, energy, framework, go, python, solver

## README Excerpt

# Australia Economic Model — Keen Approach

An interactive Streamlit app that models the Australian economy following
**Professor Steve Keen's** methodology (Minskyan debt dynamics, stock-flow
consistent modelling).

## Quick Start

```bash
cd /home/sc/workspace/aus-econ-model
./run.sh
```

Opens at http://localhost:8501

## What It Does

| Page | Purpose |
|------|---------|
| **Model Simulator** | Interactively run the Keen-Goodwin-Minsky differential equations model. Adjust parameters for wage share, employment, private debt, interest rates, and investment. |
| **Data Explorer** | Pull and visualise actual Australian data from RBA and ABS APIs (private debt, CPI, housing finance, interest rates). |
| **Scenario Analysis** | Compare multiple scenarios: immigration caps, rate hikes, wage recovery, credit crunch, productivity boom. |
| **Living Standards** | Composite welfare index combining income, employment, debt burden, housing affordability, and growth. |
| **About** | Methodology, data sources, Steve Keen's framework, roadmap. |

## Architecture

```
aus_econ_model/
├── streamlit_app.py          # Entry point + home page
├── pages/
│   ├── 01_Model_Simulator.py # Interactive Keen model
│   ├── 02_Data_Explorer.py   # ABS/RBA data browser
│   ├── 03_Scenario_Analysis.py # What-if policy scenarios
│   ├── 04_Living_Standards.py # Composite welfare index
│   └── 05_About.py           # Methodology + sources
├── models/
│   ├── keen_model.py         # ODE model (Keen 1995 + housing extension)
│   └── data_manager.py       # RBA CSV + ABS SDMX data pull
├── components/
│   ├── charts.py             # Plotly visualisation components
│   └── explainers.py         # Educational text + parameter docs
└── data/
    └── cache/                # Cached API responses
```

## The Model

Implements the Keen (1995) three-equation system:

- **dω/dt** = (Φ(λ) − ω) × (g + α) — Wage share dynamics
- **dλ/dt** = (g − α − β) × λ — Employment dynamics  
- **dd/dt** = κ(π) − π — Priv...
