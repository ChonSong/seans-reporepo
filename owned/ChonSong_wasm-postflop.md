---
repo: 'ChonSong/wasm-postflop'
url: 'https://github.com/ChonSong/wasm-postflop'
description: '[Development suspended] Advanced open-source Texas Hold'em GTO solver with optimized performance (web browser version)'
type: webapp
status: suspended
language: Vue
size_kb: 4450
stars: 0
last_pushed: '2023-10-01'
license: unknown
tags:
  - ai
  - browser-automation
  - gaming
  - go
  - ide
  - solver
  - web-app
topics: []
refreshed_at: '2026-06-21 07:46 UTC'
---

# wasm-postflop

> [Development suspended] Advanced open-source Texas Hold'em GTO solver with optimized performance (web browser version)

**URL:** [ChonSong/wasm-postflop](https://github.com/ChonSong/wasm-postflop)

## Metadata

- **Type:** webapp
- **Status:** suspended
- **Language:** Vue
- **Size:** 4,450 KB
- **Stars:** 0
- **Last Pushed:** 2023-10-01
- **License:** unknown
- **Tags:** ai, browser-automation, gaming, go, ide, solver, web-app

## README Excerpt

# WASM Postflop

> [!IMPORTANT]
> **As of October 2023, I have started developing a poker solver as a business and have decided to suspend development of this open-source project. See [this issue] for more information.**

[this issue]: https://github.com/b-inary/postflop-solver/issues/46

---

**WASM Postflop** is a free, open-source GTO solver for Texas hold'em poker that works on web browsers.

Website: https://wasm-postflop.pages.dev/

**Related repositories**
- Desktop application: https://github.com/b-inary/desktop-postflop
- Solver engine: https://github.com/b-inary/postflop-solver

![Image](image.png)

## Why WASM Postflop?

The GTO (Game Theory Optimal) solver has become an indispensable tool for poker research.
However, unfortunately, there is a high barrier to trying out the GTO solver: the need to purchase expensive commercial software.
This project aims to overcome this situation by developing a free, open-source GTO solver.

Please note that this project does not intend to *replace* commercial GTO solvers.
They are great software, and it is not easy to create a new one that can compete with them.
This project intends to make the GTO solver more easily accessible to a broader audience.

### Features

- **Free to use**.
  The most important feature.
  Anyone can try out the solver for free!

- **Open source**.
  The implementation of the GTO solver is complex and is not easy to write down accurately.
  By making the program open source, we make it possible for anyone to examine the implementation.

- **Works on web browsers**.
  This feature brings several advantages.
  First, it allows for the solver to be easily accessible.
  Second, it naturally makes the solver a cross-platform application.
  Finally, it sandboxes the solver execution, so users do not have to worry about security.

- **Sufficiently fast**.
  Slow solvers are not wanted.
  By using WebAssembly, we have reduced the performance penalty of being a web application.
  We also supported mult...
