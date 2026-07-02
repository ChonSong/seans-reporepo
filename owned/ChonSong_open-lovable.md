---
repo: 'ChonSong/open-lovable'
url: 'https://github.com/ChonSong/open-lovable'
description: 'Self-contained site cloner — extract any URL into a full React/Next.js codebase'
type: monorepo
status: active
language: TypeScript
size_kb: 1334
stars: 0
last_pushed: '2026-06-11'
license: unknown
tags:
  - ai
  - api
  - dashboard
  - go
  - ide
  - llm
  - multi-agent
  - react
  - solver
topics: []
refreshed_at: '2026-07-02 10:28 UTC'
---

# open-lovable

> Self-contained site cloner — extract any URL into a full React/Next.js codebase

**URL:** [ChonSong/open-lovable](https://github.com/ChonSong/open-lovable)

## Metadata

- **Type:** monorepo
- **Status:** active
- **Language:** TypeScript
- **Size:** 1,334 KB
- **Stars:** 0
- **Last Pushed:** 2026-06-11
- **License:** unknown
- **Tags:** ai, api, dashboard, go, ide, llm, multi-agent, react, solver

## README Excerpt

# Open Lovable

Chat with AI to build React apps instantly. An example app made by the [Firecrawl](https://firecrawl.dev/?ref=open-lovable-github) team. For a complete cloud solution, check out [Lovable.dev](https://lovable.dev/) ❤️.

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZtaHFleGRsMTNlaWNydGdianI4NGQ4dHhyZjB0d2VkcjRyeXBucCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZFVLWMa6dVskQX0qu1/giphy.gif" alt="Open Lovable Demo" width="100%"/>

## Setup

1. **Clone & Install**
```bash
git clone https://github.com/firecrawl/open-lovable.git
cd open-lovable
pnpm install  # or npm install / yarn install
```

2. **Add `.env.local`**

```env
# =================================================================
# REQUIRED
# =================================================================
FIRECRAWL_API_KEY=your_firecrawl_api_key    # https://firecrawl.dev

# =================================================================
# AI PROVIDER - Choose your LLM
# =================================================================
GEMINI_API_KEY=your_gemini_api_key        # https://aistudio.google.com/app/apikey
ANTHROPIC_API_KEY=your_anthropic_api_key  # https://console.anthropic.com
OPENAI_API_KEY=your_openai_api_key        # https://platform.openai.com
GROQ_API_KEY=your_groq_api_key            # https://console.groq.com

# =================================================================
# FAST APPLY (Optional - for faster edits)
# =================================================================
MORPH_API_KEY=your_morphllm_api_key    # https://morphllm.com/dashboard

# =================================================================
# SANDBOX PROVIDER - Choose ONE: Vercel (default) or E2B
# =================================================================
SANDBOX_PROVIDER=vercel  # or 'e2b'

# Option 1: Vercel Sandbox (default)
# Choose one authentication method:

# Method A: OIDC Token (recommended for development)
# Run `vercel link` then `vercel env pull` to get VE...
