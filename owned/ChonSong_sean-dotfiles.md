---
repo: 'ChonSong/sean-dotfiles'
url: 'https://github.com/ChonSong/sean-dotfiles'
description: My Arch Linux Hyprland dotfiles with StarCraft mode configuration
type: unknown
status: active
language: QML
size_kb: 998
stars: 0
last_pushed: '2025-12-26'
license: unknown
tags:
  - ai
  - dotfiles
  - gaming
  - go
  - terminal
---

# sean-dotfiles

> My Arch Linux Hyprland dotfiles with StarCraft mode configuration

**URL:** [ChonSong/sean-dotfiles](https://github.com/ChonSong/sean-dotfiles)

## Metadata

- **Type:** unknown
- **Status:** active
- **Language:** QML
- **Size:** 998 KB
- **Stars:** 0
- **Last Pushed:** 2025-12-26
- **License:** unknown
- **Tags:** ai, dotfiles, gaming, go, terminal

## README Excerpt

# Dotfiles

This repository contains my personal Linux dotfiles for my Arch/Hyprland setup.

## Features

- **StarCraft Mode**: Press `Super+Alt+S` to enable StarCraft controls where `Ctrl+WASD` acts as arrow keys
- **Hyprland**: Wayland compositor configuration with extensive keybindings
- **QuickShell**: Custom shell integration with panels and widgets
- **Fish**: Modern shell configuration with custom functions
- **Kitty**: Terminal emulator configuration
- **Themes**: Custom color schemes and wallpapers

## StarCraft Mode

The StarCraft mode is a special keybinding submap that allows gaming-style controls:

- **Activate**: `Super+Alt+S`
- **Controls**: 
  - `Ctrl+W` → `Ctrl+Up`
  - `Ctrl+A` → `Ctrl+Left` 
  - `Ctrl+S` → `Ctrl+Down`
  - `Ctrl+D` → `Ctrl+Right`
- **Deactivate**: `Super+Alt+S` (same as activate)

This is particularly useful for applications that use Ctrl+arrow keys for navigation but you prefer WASD controls.

## Installation

Clone this repository and symlink the configuration files:

```bash
git clone https://github.com/YOUR_USERNAME/dotfiles.git
cd dotfiles
./install.sh
```

## Structure

```
dotfiles/
├── .config/
│   ├── hypr/          # Hyprland configuration
│   ├── quickshell/    # QuickShell setup
│   ├── fish/          # Fish shell config
│   ├── kitty/         # Terminal config
│   ├── fuzzel/        # Application launcher
│   └── wlogout/       # Logout menu
├── .bashrc           # Bash configuration
└── .starship.toml    # Shell prompt config
```

## Credits

Built on Arch Linux with Hyprland Wayland compositor....
