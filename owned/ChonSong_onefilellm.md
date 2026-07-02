---
repo: ChonSong/onefilellm
url: 'https://github.com/ChonSong/onefilellm'
description: 'Specify a github or local repo, github pull request,  arXiv or Sci-Hub paper, Youtube transcript or documentation URL on the web and scrape into a text file and clipboard  for easier LLM ingestion'
type: agent
status: active
language: Python
size_kb: 1427
stars: 0
last_pushed: '2025-09-24'
license: unknown
tags:
  - agent
  - ai
  - api
  - awesome-list
  - bot
  - cli
  - llm
  - python
  - terminal
  - web-app
topics: []
refreshed_at: '2026-07-02 10:28 UTC'
---

# onefilellm

> Specify a github or local repo, github pull request,  arXiv or Sci-Hub paper, Youtube transcript or documentation URL on the web and scrape into a text file and clipboard  for easier LLM ingestion

**URL:** [ChonSong/onefilellm](https://github.com/ChonSong/onefilellm)

## Metadata

- **Type:** agent
- **Status:** active
- **Language:** Python
- **Size:** 1,427 KB
- **Stars:** 0
- **Last Pushed:** 2025-09-24
- **License:** unknown
- **Tags:** agent, ai, api, awesome-list, bot, cli, llm, python, terminal, web-app

## README Excerpt

# OneFileLLM

Content Aggregator for LLMs - Aggregate and structure multi-source data into a single XML file for LLM context.

## Description

OneFileLLM is a command-line tool that automates data aggregation from various sources (local files, GitHub repos, web pages, PDFs, YouTube transcripts, etc.) and combines them into a single, structured XML output that's automatically copied to your clipboard for use with Large Language Models.

## Installation

```bash
git clone https://github.com/jimmc414/onefilellm.git
cd onefilellm
pip install -r requirements.txt
```

### Pip install

OneFileLLM is also available as a pip package. You can install it directly and
use both the CLI and Python API without cloning the repository:

```bash
pip install onefilellm
```

## Command-Line Interface (CLI)

This project can also be installed as a command-line tool, which allows you to run `onefilellm` directly from your terminal.

### CLI Installation

To install the CLI, run the following command in the project's root directory:

```bash
pip install -e .
```

This will install the package in "editable" mode, meaning any changes you make to the source code will be immediately available to the command-line tool.

### CLI Usage

Once installed, you can use the `onefilellm` command instead of `python onefilellm.py`.

**Synopsis:**
`onefilellm [OPTIONS] [INPUT_SOURCES...]`

**Example:**
```bash
onefilellm ./docs/ https://github.com/user/project/issues/123
```

All other command-line arguments and options work the same as the script-based approach.

For GitHub API access (recommended):

```bash
export GITHUB_TOKEN="your_personal_access_token"
```

## Python API

After installing via pip, OneFileLLM can be invoked directly from Python code.

```python
from onefilellm import run

# Process inputs programmatically
run(["./docs/"])
```

## Command Help

```
usage: onefilellm.py [-h] [-c]
                     [-f {text,markdown,json,html,yaml,doculing,markitdown}]
                     [--alias-a...
