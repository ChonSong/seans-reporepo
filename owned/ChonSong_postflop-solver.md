---
repo: 'ChonSong/postflop-solver'
url: 'https://github.com/ChonSong/postflop-solver'
description: '[Development suspended] An efficient open-source postflop solver library written in Rust'
type: library
status: suspended
language: Rust
size_kb: 547
stars: 0
last_pushed: '2024-07-09'
license: unknown
tags:
  - ai
  - gaming
  - go
  - ide
  - rust
  - solver
  - web-app
topics: []
refreshed_at: '2026-07-02 13:30 UTC'
---

# postflop-solver

> [Development suspended] An efficient open-source postflop solver library written in Rust

**URL:** [ChonSong/postflop-solver](https://github.com/ChonSong/postflop-solver)

## Metadata

- **Type:** library
- **Status:** suspended
- **Language:** Rust
- **Size:** 547 KB
- **Stars:** 0
- **Last Pushed:** 2024-07-09
- **License:** unknown
- **Tags:** ai, gaming, go, ide, rust, solver, web-app

## README Excerpt

# postflop-solver

> [!IMPORTANT]
> **As of October 2023, I have started developing a poker solver as a business and have decided to suspend development of this open-source project. See [this issue] for more information.**

[this issue]: https://github.com/b-inary/postflop-solver/issues/46

---

An open-source postflop solver library written in Rust

Documentation: https://b-inary.github.io/postflop_solver/postflop_solver/

**Related repositories**
- Web app (WASM Postflop): https://github.com/b-inary/wasm-postflop
- Desktop app (Desktop Postflop): https://github.com/b-inary/desktop-postflop

**Note:**
The primary purpose of this library is to serve as a backend engine for the GUI applications ([WASM Postflop] and [Desktop Postflop]).
The direct use of this library by the users/developers is not a critical purpose by design.
Therefore, breaking changes are often made without version changes.
See [CHANGES.md](CHANGES.md) for details about breaking changes.

[WASM Postflop]: https://github.com/b-inary/wasm-postflop
[Desktop Postflop]: https://github.com/b-inary/desktop-postflop

## Usage

- `Cargo.toml`

```toml
[dependencies]
postflop-solver = { git = "https://github.com/b-inary/postflop-solver" }
```

- Examples

You can find examples in the [examples](examples) directory.

If you have cloned this repository, you can run the example with the following command:

```sh
$ cargo run --release --example basic
```

## Implementation details

- **Algorithm**: The solver uses the state-of-the-art [Discounted CFR] algorithm.
  Currently, the value of γ is set to 3.0 instead of the 2.0 recommended in the original paper.
  Also, the solver resets the cumulative strategy when the number of iterations is a power of 4.
- **Performance**: The solver engine is highly optimized for performance with maintainable code.
  The engine supports multithreading by default, and it takes full advantage of unsafe Rust in hot spots.
  The developer reviews the assembly output from the compiler ...
