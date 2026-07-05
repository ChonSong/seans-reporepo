---
repo: 'ChonSong/llm-benchmark-platform'
url: 'https://github.com/ChonSong/llm-benchmark-platform'
description: 'Web-based LLM benchmarking platform for comparing coding models across adherence, refactoring, and extension tasks'
type: monorepo
status: active
language: Python
size_kb: 96
stars: 0
last_pushed: '2026-06-14'
license: unknown
tags:
  - ai
  - api
  - awesome-list
  - benchmarking
  - cli
  - dashboard
  - docker
  - go
  - ide
  - llm
  - python
  - typescript
  - web-app
topics: []
refreshed_at: '2026-07-05 03:43 UTC'
---

# llm-benchmark-platform

> Web-based LLM benchmarking platform for comparing coding models across adherence, refactoring, and extension tasks

**URL:** [ChonSong/llm-benchmark-platform](https://github.com/ChonSong/llm-benchmark-platform)

## Metadata

- **Type:** monorepo
- **Status:** active
- **Language:** Python
- **Size:** 96 KB
- **Stars:** 0
- **Last Pushed:** 2026-06-14
- **License:** unknown
- **Tags:** ai, api, awesome-list, benchmarking, cli, dashboard, docker, go, ide, llm, python, typescript, web-app

## README Excerpt

# LLM Benchmark Platform

A web-based, Dockerized platform for benchmarking LLM coding capabilities across three evaluation dimensions: Prompt Adherence, Refactoring, and System Extension.

## Features

- **Three Evaluation Tasks:**
  - **Task A: Strict Adherence** - Python Rate Limiter with 10 rigid rules
  - **Task B: Legacy Refactoring** - TypeScript API Handler with security issues
  - **Task C: System Extension** - Notification System with pattern recognition

- **Comprehensive Metrics:**
  - Cost analysis per run
  - Speed/latency measurement
  - Verbosity (Lines of Code) comparison
  - Qualitative radar chart (Completeness, Defensiveness, Precision)

- **Interactive Dashboard:**
  - Results comparison with charts
  - Code diff viewer
  - Model configuration management
  - Custom test case creation

## Quick Start

### Using Docker Compose (Recommended)

1. Clone the repository and navigate to the project directory

2. Copy the environment file and add your API keys:
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

3. Start the application:
   ```bash
   docker-compose up --build
   ```

4. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Manual Setup

#### Backend

```bash
cd backend
pip install poetry
poetry install
poetry run uvicorn app.main:app --reload
```

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Configuration

### API Keys

Configure your LLM provider API keys in the `.env` file:

```
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
GOOGLE_API_KEY=your-google-key
```

### Model Configuration

Models can be configured through the UI or by calling the API:

- **GPT-4o** (OpenAI)
- **Claude Sonnet 4** (Anthropic)
- **Gemini 2.0 Flash** (Google)

## Usage

1. **Seed Default Data**: Click "Seed Defaults" on the Models and Test Cases pages to populate with pre-configured options.

2. **...
