---
repo: 'ChonSong/gto-wizard-clone'
url: 'https://github.com/ChonSong/gto-wizard-clone'
description: 'Open-source GTO poker training platform — equity calculator, CFR solver, training modes, hand history analysis, ICM calculator'
type: monorepo
status: active
language: TypeScript
size_kb: 120127
stars: 2
last_pushed: '2026-07-11'
license: unknown
tags:
  - ai
  - api
  - database
  - docker
  - gaming
  - python
  - react
  - solver
  - testing
  - training
  - transpilation
  - typescript
  - web-app
topics:
  - wip
refreshed_at: '2026-07-19 23:34 UTC'
---

# gto-wizard-clone

> Open-source GTO poker training platform — equity calculator, CFR solver, training modes, hand history analysis, ICM calculator

**URL:** [ChonSong/gto-wizard-clone](https://github.com/ChonSong/gto-wizard-clone)

## Metadata

- **Type:** monorepo
- **Status:** active
- **Language:** TypeScript
- **Size:** 120,127 KB
- **Stars:** 2
- **Last Pushed:** 2026-07-11
- **License:** unknown
- **Tags:** ai, api, database, docker, gaming, python, react, solver, testing, training, transpilation, typescript, web-app

## README Excerpt

# GTO Wizard Clone - WIP

**Open-source GTO poker training platform** — equity calculator, CFR solver, PLO4 tools, double board / bomb pot solver, training modes, hand history analysis, ICM calculator, push/fold charts, training courses, and community spots.

## Supported Game Variants

| Variant | Status | Notes |
|---------|--------|-------|
| No-Limit Hold'em (NLH) | ✅ Built | OMPEval (C++) |
| Pot-Limit Omaha 4 (PLO4) | ✅ Built | PokerHandEvaluator (C++/Python) |
| PLO5 (5-card Omaha) | ✅ Built | 4-card from 5 eval |
| Omaha Hi/Lo (8-or-better) | ✅ Built | Split pot, 8-qualifier |
| Shortdeck (6+ Hold'em) | ✅ Built | Flush > full house |
| **Double Board PLO** | ✅ Built (novel) | Two boards, scoop/chop scoring |
| **Bomb Pot** | ✅ Built (novel) | Action-first betting, straddle games |

## Key Libraries

| Library | Stars | Use |
|---------|-------|-----|
| [HenryRLee/PokerHandEvaluator](https://github.com/HenryRLee/PokerHandEvaluator) | 501 | PLO4/PLO5/Hi-Lo hand evaluation |
| [zekyll/OMPEval](https://github.com/zekyll/OMPEval) | 224 | NLH hand evaluator (C++) |
| [siavashg87/poker-odds-calc](https://github.com/siavashg87/poker-odds-calc) | 99 | Multi-variant equity (Hold'em, Omaha, Shortdeck) |
| [ksoeze/OmahaRangeExplorer](https://github.com/ksoeze/OmahaRangeExplorer) | 4 | Python PLO4 range builder |

## Architecture

```
apps/web/        Next.js 15 frontend
apps/api/        FastAPI backend
apps/solver/     Python MCCFR engine (gRPC)
packages/
  poker-core/    Shared poker math (Python + TypeScript)
  types/         Shared TypeScript types
  ui-components/ React component library
```

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 15, React 19, TypeScript, Tailwind v4 |
| Backend | FastAPI, Pydantic v2, WebSockets, Celery |
| Solver | Python 3.12, NumPy, Numba, MCCFR |
| PLO4/Omaha | PokerHandEvaluator (C++/Python) |
| Database | PostgreSQL (Neon serverless) |
| Cache | Redis |

## Quick Start

```bash
git clone https://git...
