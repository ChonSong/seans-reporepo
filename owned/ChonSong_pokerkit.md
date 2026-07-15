---
repo: ChonSong/pokerkit
url: 'https://github.com/ChonSong/pokerkit'
description: 'An open-source Python library for poker game simulations, hand evaluations, and statistical analysis'
type: library
status: active
language: Python
size_kb: 6067
stars: 0
last_pushed: '2025-05-08'
license: unknown
tags:
  - ai
  - api
  - automation
  - gaming
  - ide
  - llm
  - python
  - rag
  - tui
topics: []
refreshed_at: '2026-07-15 00:23 UTC'
---

# pokerkit

> An open-source Python library for poker game simulations, hand evaluations, and statistical analysis

**URL:** [ChonSong/pokerkit](https://github.com/ChonSong/pokerkit)

## Metadata

- **Type:** library
- **Status:** active
- **Language:** Python
- **Size:** 6,067 KB
- **Stars:** 0
- **Last Pushed:** 2025-05-08
- **License:** unknown
- **Tags:** ai, api, automation, gaming, ide, llm, python, rag, tui

## README Excerpt

========
PokerKit
========

PokerKit is an open-source software library, written in pure Python, for simulating games, evaluating hands, and facilitating statistical analysis, developed by the Universal, Open, Free, and Transparent Computer Poker Research Group. PokerKit supports an extensive array of poker variants and it provides a flexible architecture for users to define their custom games. These facilities are exposed via an intuitive unified high-level programmatic API. The library can be used in a variety of use cases, from poker AI development, and tool creation, to online poker casino implementation. PokerKit's reliability has been established through static type checking, extensive doctests, and unit tests, achieving 99% code coverage.

Features
--------

* Extensive poker game logic for major and minor poker variants.
* High-speed hand evaluations.
* Customizable game states and parameters.
* Robust implementation with static type checking and extensive unit tests and doctests.

Installation
------------

The PokerKit library requires Python Version 3.11 or above and can be installed using pip:

.. code-block:: bash

   pip install pokerkit

Usages
------

Example usages of PokerKit is shown below.

Multi-Runout in an All-In Situation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below shows the 4-runout hand between Phil Hellmuth and the Loose Cannon Ernest Wiggins.

Link: https://youtu.be/cnjJv7x0HMY?si=4l05Ez7lQVczt8DI&t=638

Note that the starting stacks for some players are set to be ``math.inf`` as they are not mentioned.

.. code-block:: python

   from math import inf

   from pokerkit import Automation, Mode, NoLimitTexasHoldem

   state = NoLimitTexasHoldem.create_state(
       # Automations
       (
           Automation.ANTE_POSTING,
           Automation.BET_COLLECTION,
           Automation.BLIND_OR_STRADDLE_POSTING,
           Automation.HOLE_CARDS_SHOWING_OR_MUCKING,
           Automation.HAND_KILLING,
           Automation.CHIPS_PUSHING,
         ...
