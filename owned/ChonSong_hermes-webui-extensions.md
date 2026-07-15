---
repo: 'ChonSong/hermes-webui-extensions'
url: 'https://github.com/ChonSong/hermes-webui-extensions'
description: 'Extensions library for Hermes WebUI! Marketplace of ways to enhance your experience!'
type: library
status: active
language: JavaScript
size_kb: 8546
stars: 0
last_pushed: '2026-07-14'
license: unknown
tags:
  - ai
  - api
  - cli
  - go
  - hermes-agent
  - ide
  - rust
  - testing
  - web-app
topics: []
refreshed_at: '2026-07-15 00:23 UTC'
---

# hermes-webui-extensions

> Extensions library for Hermes WebUI! Marketplace of ways to enhance your experience!

**URL:** [ChonSong/hermes-webui-extensions](https://github.com/ChonSong/hermes-webui-extensions)

## Metadata

- **Type:** library
- **Status:** active
- **Language:** JavaScript
- **Size:** 8,546 KB
- **Stars:** 0
- **Last Pushed:** 2026-07-14
- **License:** unknown
- **Tags:** ai, api, cli, go, hermes-agent, ide, rust, testing, web-app

## README Excerpt

# Hermes WebUI Extensions

[![CI](https://github.com/hermes-webui/hermes-webui-extensions/actions/workflows/extensions.yml/badge.svg)](https://github.com/hermes-webui/hermes-webui-extensions/actions/workflows/extensions.yml)
[![Pages](https://img.shields.io/github/deployments/hermes-webui/hermes-webui-extensions/github-pages?label=pages)](https://hermes-webui.github.io/hermes-webui-extensions/)

This repository is the community extension library for Hermes WebUI.

The goal is to give trusted local extensions a shared place to document,
package, review, and iterate without turning every optional workflow into
Hermes WebUI core code.

## Status

This repository is young but the core loop is live: the registry, CI safety
gates, and the one-click install/uninstall UI in WebUI (Settings → Extensions)
have all shipped. The WebUI extension APIs are still growing, so the conventions
here are a maintained foundation rather than a locked marketplace contract.

For the current WebUI-side loading contract, see
[`docs/EXTENSIONS.md`](https://github.com/nesquena/hermes-webui/blob/main/docs/EXTENSIONS.md)
in the main Hermes WebUI repository. For authoring an entry in this repo, see
[`docs/extension-entry.md`](docs/extension-entry.md).

## What Belongs Here

- Optional local workflows that should not be core WebUI features.
- UI panels, tools, diagnostics, or workspace helpers that run as trusted
  same-origin extension assets.
- Local sidecar integrations, such as native desktop helpers, when their trust
  model and installation steps are explicit.
- Native-host resource bundles that belong to a sidecar extension, as long as
  the entry makes clear that those assets are for the native host and are not
  WebUI core UI.
- Examples that help extension authors follow the current WebUI contract.

## What Does Not Belong Here

- Core bug fixes or required WebUI behavior.
- Remote third-party script loaders.
- Secrets, tokens, credentials, or machine-specific configuration.
- Unreviewed ...
