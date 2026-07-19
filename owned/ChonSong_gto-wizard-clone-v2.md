---
repo: 'ChonSong/gto-wizard-clone-v2'
url: 'https://github.com/ChonSong/gto-wizard-clone-v2'
description: 'GTO Wizard Clone v2 — rebuilt poker training platform with correct architecture: strategy browser, MCCFR solver, training quizzes, equity calculator, hand history analysis, ICM calculator'
type: monorepo
status: active
language: Python
size_kb: 1117
stars: 0
last_pushed: '2026-07-14'
license: unknown
tags:
  - ai
  - api
  - browser-automation
  - dashboard
  - database
  - docker
  - gaming
  - python
  - react
  - solver
  - training
  - typescript
  - web-app
topics: []
refreshed_at: '2026-07-19 23:34 UTC'
---

# gto-wizard-clone-v2

> GTO Wizard Clone v2 — rebuilt poker training platform with correct architecture: strategy browser, MCCFR solver, training quizzes, equity calculator, hand history analysis, ICM calculator

**URL:** [ChonSong/gto-wizard-clone-v2](https://github.com/ChonSong/gto-wizard-clone-v2)

## Metadata

- **Type:** monorepo
- **Status:** active
- **Language:** Python
- **Size:** 1,117 KB
- **Stars:** 0
- **Last Pushed:** 2026-07-14
- **License:** unknown
- **Tags:** ai, api, browser-automation, dashboard, database, docker, gaming, python, react, solver, training, typescript, web-app

## README Excerpt

# GTO Wizard Clone v2

Open-source GTO poker training platform — equity calculator, MCCFR solver, strategy browser, training quizzes, hand history analysis, ICM calculator.

**Live:** [wiz.codeovertcp.com](https://wiz.codeovertcp.com) (v1 deployment)

## Architecture

```
apps/web/         → Next.js 15 frontend (React 19, TypeScript, Tailwind v4)
apps/api/         → FastAPI backend (Python 3.12, Pydantic v2)
apps/solver/      → MCCFR engine (Python, Numba JIT)
packages/
  poker-core/     → Deck, hand eval, equity, range, all 7 game variants
  ui-components/  → Shared React components
  types/          → Shared TypeScript types
```

## Pages

| Route | Purpose |
|-------|---------|
| `/` | Dashboard |
| `/study` | Strategy browser — browse GTO ranges, traverse game tree |
| `/practice` | Training quizzes — test decisions against GTO |
| `/equity` | Equity calculator |
| `/icm` | ICM tournament calculator |
| `/analyze` | Hand history analysis |
| `/strategies` | Strategy lookup |
| `/courses` | Training courses |
| `/plo4` | PLO variants |

## Quick Start

```bash
# Backend
cd apps/api
pip install -r requirements.txt
PYTHONPATH=apps/api:. uvicorn apps.api.main:app --host 0.0.0.0 --port 8001

# Frontend
npm install
npm run dev  # → http://localhost:3000
```

## Docker

```bash
docker compose up -d
# → API on :8001, Web on :3000, PostgreSQL on :5432, Redis on :6379
```

## Tests

```bash
# Python
pip install -e packages/poker-core
python -m pytest packages/poker-core/tests/ -v

# Frontend
cd apps/web && npx vitest run

# E2E
cd apps/web && npx playwright test
```

## License

MIT
...
