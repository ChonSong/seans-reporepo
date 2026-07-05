---
repo: 'ChonSong/starcraft-battlenet-web'
url: 'https://github.com/ChonSong/starcraft-battlenet-web'
description: 'StarCraft Battle.net Web Gaming Platform - Complete Docker infrastructure for serving Battle.net games over the web with VNC, Nginx, Redis, and enterprise-grade security'
type: cli
status: active
language: HTML
size_kb: 7
stars: 0
last_pushed: '2025-12-29'
license: unknown
tags:
  - ai
  - api
  - browser-automation
  - cli
  - docker
  - gaming
  - infrastructure
  - monitoring
  - nginx
  - proxy
  - solver
  - web-app
topics: []
refreshed_at: '2026-07-05 03:43 UTC'
---

# starcraft-battlenet-web

> StarCraft Battle.net Web Gaming Platform - Complete Docker infrastructure for serving Battle.net games over the web with VNC, Nginx, Redis, and enterprise-grade security

**URL:** [ChonSong/starcraft-battlenet-web](https://github.com/ChonSong/starcraft-battlenet-web)

## Metadata

- **Type:** cli
- **Status:** active
- **Language:** HTML
- **Size:** 7 KB
- **Stars:** 0
- **Last Pushed:** 2025-12-29
- **License:** unknown
- **Tags:** ai, api, browser-automation, cli, docker, gaming, infrastructure, monitoring, nginx, proxy, solver, web-app

## README Excerpt

# StarCraft Battle.net Web Gaming Platform

Complete infrastructure for serving Battle.net and StarCraft games over the web.

## 🚀 Quick Start

```bash
docker-compose up -d
```

## 🌐 Access Information

- **Web Portal:** `http://localhost:6080/vnc.html`
- **VNC Password:** `battlenet123`
- **VNC Port:** 5902 (for VNC clients)

## 📋 Services

| Service | Description | Port |
|---------|-------------|------|
| VNC Server | Battle.net gaming desktop | 6080 (web) / 5902 (direct) |
| Nginx | Web interface & SSL termination | 80 |
| Redis | Session caching | 6379 |

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Browser   │───▶│     Nginx      │───▶│     VNC         │
│                 │    │ (Reverse Proxy) │    │   Container     │
│  Gaming Portal  │    │  • SSL/HTTPS    │    │  • Ubuntu + XFCE │
│  • Web Interface│    │  • Load Balance│    │  • Battle.net   │
│  • Auto-connect │    │  • Rate Limit   │    │  • StarCraft    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🔧 Management

### Status Monitoring
```bash
./show-status.sh
```

### View Logs
```bash
docker logs -f starcraft-vnc
docker logs -f starcraft-nginx
```

### Restart Services
```bash
docker-compose restart
```

## 🔒 Security Features

- **SSL/TLS Encryption** with automatic certificate management
- **Rate Limiting** for API endpoints
- **Security Headers** (HSTS, CSP, XSS protection)
- **Container Isolation** for secure gaming environment
- **Access Control** with VNC password protection

## 📊 Performance

- **Real-time Gaming** with low-latency VNC streaming
- **Resource Optimization** with efficient container management
- **Auto-scaling** support through Docker Compose
- **Session Persistence** via Redis caching

## 🎮 Gaming Features

- **Full Desktop Access** to Ubuntu gaming environment
- **Battle.net Auto-install** with Wine compatibility
- **StarCraft Support** with optimal graphics settings
- **Browser-based Access** fr...
