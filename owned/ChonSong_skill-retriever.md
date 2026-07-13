---
repo: 'ChonSong/skill-retriever'
url: 'https://github.com/ChonSong/skill-retriever'
description: 'AgentSkillOS-powered semantic skill retrieval for Hermes Agent.'
type: 'awesome-list'
status: active
language: HTML
size_kb: 34462
stars: 6
last_pushed: '2026-07-12'
license: unknown
tags:
  - agent
  - ai
  - awesome-list
  - docker
  - embeddings
  - go
  - hermes-agent
  - ide
  - llm
  - plugin
  - python
  - rag
  - solver
topics:
  - hermes-agent
  - skills
refreshed_at: '2026-07-13 03:44 UTC'
---

# skill-retriever

> AgentSkillOS-powered semantic skill retrieval for Hermes Agent.

**URL:** [ChonSong/skill-retriever](https://github.com/ChonSong/skill-retriever)

## Metadata

- **Type:** awesome-list
- **Status:** active
- **Language:** HTML
- **Size:** 34,462 KB
- **Stars:** 6
- **Last Pushed:** 2026-07-12
- **License:** unknown
- **Tags:** agent, ai, awesome-list, docker, embeddings, go, hermes-agent, ide, llm, plugin, python, rag, solver

## README Excerpt

<p align="center">
  <img src="logo.png" alt="Skill Retriever" height="130">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
  <a href="https://github.com/ynulihao/AgentSkillOS"><img src="https://img.shields.io/badge/Built%20on-AgentSkillOS-purple" alt="Built on AgentSkillOS"></a>
</p>

# Skill Retriever

> **AgentSkillOS-powered semantic skill retrieval for Hermes Agent.**

Pre-filters **2,000+ skills** (622 community + 179 Hermes + 1,860 indexed from AAS) organized in a **10,000-category capability taxonomy** to the top-5 most relevant per query. The corpus was expanded on 2026-07-10 with 392 permissively-licensed skills from [Agentic Awesome Skills](https://github.com/sickn33/agentic-awesome-skills) v14.1.0 (1,860 total AAS skills indexed, 392 shipped).

## Why a Skill Tree?

Pure semantic retrieval prioritizes textual similarity and misses skills that look unrelated in embedding space but are crucial for solving the task. Our LLM + Skill Tree navigates the capability hierarchy to surface non-obvious but functionally relevant skills.

<p align="center">
  <img src="skill_retrieval_academic_comparison.png" alt="Skill Retrieval: Semantic vs Tree" style="max-width: 760px;">
</p>
<sub><i>Left: Pure semantic retrieval is narrow and myopic. Right: Skill Tree navigation surfaces functionally relevant skills the embedding space hides.</i></sub>

## The Capability Tree

Skills are organized into a coarse-to-fine capability hierarchy. At scale, this is the difference between finding the right skill and drowning in an invisible pile.

<p align="center">
  <img src="tree_10000_expand.gif" alt="10K Skill Tree Explored" height="360">
</p>
<sub><i>The 10,000-category capability tree — the structure our 800+ ship-safe skills are mapped into.</i></sub>

## How It Works

```                     
User Query
    │
    ▼
┌───────────────────...
