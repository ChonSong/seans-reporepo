# Migration Candidates

Repos identified for extraction and migration into hermes-web-computer tiles.
Each candidate file contains: source analysis, extraction scope, transpile plan, effort estimate.

## Active Candidates

| Repo | Target Tile | Tier | Effort | Relevance |
|------|------------|------|--------|-----------|
| [bytebot-ai/bytebot](bytebot-ai_bytebot.md) | Browser | T1 | 3-5 days | 9/10 |
| [trycua/cua](trycua_cua.md) | Sandbox | T1 | 3-4 days | 8/10 |
| [ChonSong/agent-os](ChonSong_agent-os.md) | Dashboard | T1 | 2-3 days | 7/10 |
| [sveltejs/ai-tools](sveltejs_ai-tools.md) | AI Components | T2 | 1-2 days | 6/10 |
| [upstash/context7](upstash_context7.md) | Research Data | T2 | 1 day | 5/10 |
| [sindresorhus/awesome](sindresorhus_awesome.md) | Resource Index | T2 | 0.5 days | 4/10 |

## Process

1. Review candidate profile
2. Run `repo-transmute v2 ingest <repo>` to get AST blueprint
3. Confirm extraction scope
4. Run `repo-transmute v2 migrate` with vision verification
5. Review PR, merge into hermes-web-computer

## Reference Repos (Not Candidates)

These are tagged `reference` in the catalog — useful for design QA and inspiration but not migration targets:

- `thedaviddias/Front-End-Checklist` — Design QA checklist
- `bradtraversy/design-resources-for-developers` — Design inspiration
- `dypsilon/frontend-dev-bookmarks` — Developer resource collection
- `requestly/awesome-frontend-resources` — Frontend resource index
- `rtivital/omatsuri` — Frontend tool collection (design inspiration)
