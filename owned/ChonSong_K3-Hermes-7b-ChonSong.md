---
repo: 'ChonSong/K3-Hermes-7b-ChonSong'
url: 'https://github.com/ChonSong/K3-Hermes-7b-ChonSong'
description: 'Hybrid K3/Hermes 7B Agent — serverless data pipeline, teacher distillation, fine-tuning, and deployment'
type: agent
status: active
language: Python
size_kb: 28
stars: 0
last_pushed: '2026-07-27'
license: unknown
tags:
  - agent
  - ai
  - api
  - benchmarking
  - cli
  - fine-tuning
  - go
  - hermes-agent
  - llm
  - testing
  - training
topics: []
refreshed_at: '2026-10-09 22:21 UTC'
---

# K3-Hermes-7b-ChonSong

> Hybrid K3/Hermes 7B Agent — serverless data pipeline, teacher distillation, fine-tuning, and deployment

**URL:** [ChonSong/K3-Hermes-7b-ChonSong](https://github.com/ChonSong/K3-Hermes-7b-ChonSong)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** Python
- **Size:** 28 KB
- **Stars:** 0
- **Last Pushed:** 2026-07-27
- **License:** unknown
- **Tags:** agent, ai, api, benchmarking, cli, fine-tuning, go, hermes-agent, llm, testing, training

## README Excerpt

# K3-Hermes-7b-ChonSong

**Hybrid K3/Hermes 7B Agent** — builds, trains, and hosts an open-source 7B reasoning + tool-calling model entirely through serverless APIs.

## Architecture

```
Phase 1: Data Gathering                    Phase 2: Teacher Distillation        Phase 3: Fine-Tune        Phase 4: Deploy
┌──────────────────────────────┐          ┌──────────────────────┐             ┌─────────────────┐       ┌────────────────┐
│ GitHub PRs (recent, vetted)  │  ──►     │ Moonshot K3 /        │  ──►        │ Fireworks.ai    │  ──►  │ Serverless      │
│ Release Notes (post-cutoff)  │          │ OpenRouter API       │             │ Together AI     │       │ Endpoint        │
│ Security Advisories (CVE)    │          │ ─ CoT Reasoning       │             │ Predibase       │       │ ─ OpenAI compat │
│ CLI Docs                     │          │ ─ K3 multi-step       │             │ ─ LoRA / QLoRA  │       │ ─ Pay-per-token │
│ Technical Wiki               │          │ ─ Hermes tool syntax  │             │ ─ Qwen 2.5 7B   │       │                 │
└──────────────────────────────┘          └──────────────────────┘             └─────────────────┘       └────────────────┘
         │                                │                                     │                        │
         ▼                                ▼                                     ▼                        ▼
   Raw markdown files              User/Assistant JSONL                  Adapter weights          Private API endpoint
```

## Phases

### Phase 1: Data Gathering
Collect domain-specific training data that the teacher model likely hasn't seen (post-cutoff):
- **GitHub PRs** — recent, merged PRs with meaningful discussion from active repos
- **Release Notes** — changelogs from popular tools published in the last 18 months
- **Security Advisories** — CVEs and vulnerability disclosures from NVD
- **CLI Docs** — scrape man pages, cheat sheets (tldr-pages), and documentation for popular tools
- **T...
