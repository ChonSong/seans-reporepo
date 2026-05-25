---
repo: 'ChonSong/features-list'
url: 'https://github.com/ChonSong/features-list'
description: No description
type: monorepo
status: active
language: HTML
size_kb: 1706
stars: 0
last_pushed: '2026-05-12'
license: unknown
tags:
  - agent
  - ai
  - analytics
  - awesome-list
  - bot
  - dashboard
  - hermes-agent
  - ide
  - mcp
  - mobile
  - multi-agent
  - orchestration
  - react
  - transpilation
---

# features-list

> No description

**URL:** [ChonSong/features-list](https://github.com/ChonSong/features-list)

## Metadata

- **Type:** monorepo
- **Status:** active
- **Language:** HTML
- **Size:** 1,706 KB
- **Stars:** 0
- **Last Pushed:** 2026-05-12
- **License:** unknown
- **Tags:** agent, ai, analytics, awesome-list, bot, dashboard, hermes-agent, ide, mcp, mobile, multi-agent, orchestration, react, transpilation

## README Excerpt

# Hermes Workspace Features List

> Extracted from [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) via repo-transmute v2

## Overview

A comprehensive feature catalog of the hermes-workspace desktop application — a React + TanStack Start + Tailwind + Electron workspace for Hermes Agent with chat, orchestration, and multi-agent coding pipelines.

**Tech Stack:** React, TanStack Start, Tailwind CSS, Electron, @tanstack/react-query, @base-ui/react, @hugeicons/react

---

## Chat Features

| Component | Size | Description |
|-----------|------|-------------|
| `chat-screen` | 84K | Main chat interface with streaming, session management, history, model picker |
| `chat-composer` | 115K | Message input with model picker, file attachments, slash commands, workspace selection |
| `chat-message-list` | 72K | Message rendering with streaming animation, tool calls, research cards, search |
| `message-item` | 94K | Individual message display with markdown, code blocks, tool call rendering, status |
| `chat-sidebar` | 39K | Session list with search, rename, delete, recent sessions grouping |
| `chat-header` | 21K | Session header with model info, workspace context, mobile hamburger menu |
| `chat-empty-state` | 4.2K | Welcome screen when no messages |
| `context-bar` | 7.0K | Context indicator for file/memory attachments |
| `context-meter` | - | Context usage meter |
| `scroll-to-bottom-button` | 1.7K | Auto-scroll control |

### Chat Capabilities
- ✅ SSE streaming responses
- ✅ Optimistic message updates
- ✅ Tool call visualization
- ✅ Research card rendering
- ✅ Multi-session management
- ✅ Model switching per session
- ✅ File/memory context attachments
- ✅ Workspace selection
- ✅ Slash commands
- ✅ Connection status handling
- ✅ Message search
- ✅ Session rename/delete dialogs

---

## Dashboard Features

| Component | Size | Description |
|-----------|------|-------------|
| `dashboard-screen` | 39K | Main dashboard with KPI cards, analytics gr...
