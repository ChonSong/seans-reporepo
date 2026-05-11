# Migration Candidates

Repos identified for extraction and migration into hermes-web-computer tiles.
Each candidate file contains: source analysis, extraction scope, transpile plan, effort estimate.

## Active Candidates

| Repo | Target Tile | Tier | Effort |
|------|------------|------|--------|
| [bytebot-ai/bytebot](bytebot-ai_bytebot.md) | Browser | T1 | 3-5 days |
| [trycua/cua](trycua_cua.md) | Sandbox | T1 | 3-4 days |
| [agent-os](ChonSong_agent-os.md) | Dashboard | T1 | 2-3 days |
| [sveltejs_ai-tools](sveltejs_ai-tools.md) | AI Components | T2 | 1-2 days |
| [upstash/context7](upstash_context7.md) | Research Data | T2 | 1 day |
| [sindresorhus/awesome](sindresorhus_awesome.md) | Resource Index | T2 | 0.5 days |

## Process

1. Review candidate profile
2. Run `repo-transmute v2 ingest <repo>` to get AST blueprint
3. Confirm extraction scope
4. Run `repo-transmute v2 migrate` with vision verification
5. Review PR, merge into hermes-web-computer
