---
repo: 'ChonSong/minsky-circuit'
url: 'https://github.com/ChonSong/minsky-circuit'
description: 'A lightweight simulator modelling how credit expansion, leverage cycles, and asset price deflation interact across a simplified economy.'
type: infrastructure
status: active
language: Python
size_kb: 4
stars: 0
last_pushed: '2026-03-29'
license: unknown
tags:
  - ai
  - infrastructure
  - python
  - rag
topics: []
refreshed_at: '2026-05-11 09:24 UTC'
---

# minsky-circuit

> A lightweight simulator modelling how credit expansion, leverage cycles, and asset price deflation interact across a simplified economy.

**URL:** [ChonSong/minsky-circuit](https://github.com/ChonSong/minsky-circuit)

## Metadata

- **Type:** infrastructure
- **Status:** active
- **Language:** Python
- **Size:** 4 KB
- **Stars:** 0
- **Last Pushed:** 2026-03-29
- **License:** unknown
- **Tags:** ai, infrastructure, python, rag

## README Excerpt

# Minsky Circuit

Debt-driven systems develop endogenous instability — stability breeds recklessness, and mainstream economics consistently underestimates this. This insight applies to data infrastructure as much as to finance: the current AI infrastructure boom is financed by massive credit expansion.

Built a lightweight simulator modelling how credit expansion, leverage cycles, and asset price deflation interact across a simplified economy. Configured with real-world parameters — household debt ratios, corporate leverage, central bank balance sheets. Designed for exploring "what if" scenarios around interest rate shocks and credit crunches.

## Usage

```bash
pip install -e .
python -m minsky_circuit run --scenario scenarios/interest_rate_shock.yaml
```

## Scenarios

- `scenarios/interest_rate_shock.yaml` — 300bp rate hike on a leveraged economy
- `scenarios/credit_crunch.yaml` — credit contraction as banks tighten lending
- `scenarios/asset_deflation.yaml` — 25% asset price drop and balance sheet effects

## Tech Stack

- **Python 3.11+** — NumPy, Matplotlib, PyYAML, Structlog
...
