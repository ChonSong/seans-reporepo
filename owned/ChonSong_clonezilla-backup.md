---
repo: 'ChonSong/clonezilla-backup'
url: 'https://github.com/ChonSong/clonezilla-backup'
description: Clonezilla backup
type: cli
status: active
language: other
size_kb: 2
stars: 0
last_pushed: '2025-12-02'
license: unknown
tags:
  - ai
  - backup
  - cli
  - ide
  - rag
topics: []
refreshed_at: '2026-05-11 09:24 UTC'
---

# clonezilla-backup

> Clonezilla backup

**URL:** [ChonSong/clonezilla-backup](https://github.com/ChonSong/clonezilla-backup)

## Metadata

- **Type:** cli
- **Status:** active
- **Language:** other
- **Size:** 2 KB
- **Stars:** 0
- **Last Pushed:** 2025-12-02
- **License:** unknown
- **Tags:** ai, backup, cli, ide, rag

## README Excerpt

# Clonezilla Automated Backup to GitHub

This repository contains a Bash script (`backup.sh`) to automate the process of creating a disk or partition image using Clonezilla, uploading it to a private GitHub repository, and then deleting the local backup files.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Important Considerations](#important-considerations)

## Features
- **Automated Backup:** Creates a Clonezilla image of a specified disk or partition.
- **Private GitHub Storage:** Pushes the generated backup image to a dedicated private GitHub repository.
- **Local Cleanup:** Automatically deletes the local backup files after successful upload to save disk space.

## Prerequisites
Before running the script, ensure you have the following:
1.  **Clonezilla:** Installed on your system. The script assumes `/usr/sbin/clonezilla` is available.
    If not installed, run: `sudo apt install clonezilla` (for Debian/Ubuntu-based systems).
2.  **GitHub CLI (`gh`):** Installed and authenticated with a Personal Access Token (PAT) that has `repo` scope.
    -   **Installation:** Follow instructions for your OS from [GitHub CLI documentation](https://cli.github.com/manual/installation).
    -   **Authentication:** `gh auth login` (or populate `config.sh` and the script will handle it).
3.  **Git:** Installed on your system.
    -   `sudo apt install git` (for Debian/Ubuntu-based systems).

## Setup
1.  **Clone this repository:**
    ```bash
    git clone https://github.com/gutgyv/clonezilla-backup.git
    cd clonezilla-backup
    ```
2.  **Configure `config.sh`:**
    Edit the `config.sh` file with your specific details. This file is sourced by `backup.sh`.
    ```bash
    nano config.sh
    ```
    Fill in the following variables:
    -   `GITHUB_USERNAME`: Your GitHub username.
    -   `GITHUB_TOKEN`: Your GitHub Personal Access Token (PAT) with `repo` scope. [Generate one here](https://github.com/settings...
