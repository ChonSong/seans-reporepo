# Cluster Mining Analysis: Voice/Media & Knowledge/Research

## 1. Cross-Reference: Starred vs. Owned — Abandoned or New Territory?

### Voice + Audio + Media Cluster

| Starred | Owned |
|---------|-------|
| FunAudioLLM/Fun-Audio-Chat (961★) — Large Audio Language Model | **hermes-web-computer** — already integrates Fun-Audio-Chat as voice agent |
| IAHispano/Applio (3,352★) — Voice conversion | **Codeovertcp** — voice-first web IDE concept |
| yt-dlp/yt-dlp (169K★) — Audio/video downloader | **seans-reporepo** — tags: audio, voice |
| | **hermes-agent** — tag: voice |

**Verdict: ACTIVE TERRITORY, NOT ABANDONED.**
- hermes-web-computer already has a working Fun-Audio-Chat integration with an audio bridge over WebSocket multiplexer (`{"protocol":"ui|agent|audio",...}`)
- Codeovertcp is a "voice-first agentic web IDE" — embryonic concept (153KB, last pushed Nov 2025)
- yt-dlp is starred but has zero owned counterparts doing media downloading
- Applio (voice conversion) has no owned counterpart at all — **untapped territory**

### Knowledge + Docs + Research Cluster

| Starred | Owned |
|---------|-------|
| karpathy/autoresearch (85.6K★) — Autonomous research agents | **seans-reporepo** itself — repo discovery catalog |
| Alibaba-NLP/DeepResearch (19.3K★) — Deep research agent | **onefilellm** — scrape repos/PRs/papers/YT → text for LLM |
| stitionai/devika (19.5K★) — AI software engineer | **forrest-plan-and-track** — tag: rag |
| Baiyuetribe/paper2gui (10.7K★) — AI papers → GUI | **circuit-breaker-framework** — tag: rag |
| comet-ml/opik (19.5K★) — LLM/RAG monitoring | **casaos-agent** — tag: rag |
| promptfoo/promptfoo (22K★) — Prompt/agent/RAG testing | **linux-web-serving-infrastructure** — tag: rag |
| upstash/context7 (57K★) — Code docs for LLMs | **hermes-knowledge-graph** — tag: hermes-agent |
| multica-ai/andrej-karpathy-skills (171K★) — LLM coding insights | |

**Verdict: GAP EXISTS — OWNED RAG TOOLS ARE BREADTH, NOT DEPTH.**
- The owned repos tagged `rag` are mostly infrastructure components (casaos-agent, minsky-circuit, clonezilla-backup) — not dedicated research/knowledge tools
- **onefilellm** is the closest owned repo to the research cluster: it already pulls GitHub repos, PRs, arxiv papers, Sci-Hub docs, YouTube transcripts
- No owned repo does autonomous research (unlike autoresearch/DeepResearch)
- No owned repo does LLM eval/RAG monitoring (unlike opik/promptfoo)
- **seans-reporepo itself is an untapped knowledge asset** — it's a structured catalog of 201 repos with 67 tags, perfect for RAG ingestion

---

## 2. Proposed New Applications (3 Concrete Ideas)

### Application A: Voice Research Pipeline
**Combines:** yt-dlp → Whisper (via onefilellm already has YT transcript) → LLM (Hermes) → TTS (Fun-Audio-Chat) → Discord/voice response

**How it works:**
1. Voice command "research topic X" via Fun-Audio-Chat (already integrated in hermes-web-computer)
2. yt-dlp fetches YouTube videos on topic X (starred, 169K★)
3. onefilellm extracts transcripts + arxiv papers + GitHub repos related to X
4. LLM synthesizes a briefing from the collected content
5. Fun-Audio-Chat reads the briefing back via TTS

**Buildable components:**
- Heresy-web-computer audio bridge (already exists) ← voice input/output
- onefilellm (owned fork) ← text extraction from YT/arXiv/GitHub
- yt-dlp (starred, pip installable) ← media download
- Hermes agent ← orchestration + LLM synthesis

**Effort:** Medium (3-5 days for a working prototype). The audio bridge and onefilellm already exist; the integration glue is the main work.

---

### Application B: Repo-Repo Research Agent
**Combines:** seans-reporepo (the tag-indexed catalog) → DeepResearch/autoresearch patterns → auto-briefing generator

**How it works:**
1. User asks "what's in the agent + voice intersection?"
2. Agent queries seans-reporepo's tag index → finds all repos tagged agent+voice → reads their READMEs
3. Agent searches for similar starred repos not yet cataloged
4. Generates a structured briefing: "Here are the 3 repos, what they do, and how they combine"
5. Optionally posts to a dashboard or Discord

**Buildable components:**
- seans-reporepo README (already exists with tag index + repo links) ← knowledge base
- Hermes agent (owned) ← orchestration + code reading
- onefilellm (owned fork) ← scrape related starred repos for deeper analysis
- Alibaba-NLP/DeepResearch (starred) ← deep research patterns to emulate

**Effort:** Low-Medium (1-2 days). The catalog is already structured. The main work is a Hermes skill/plugin that reads the tag index and walks repo READMEs.

**Quick-start:**
```bash
# A single Hermes prompt that already works:
"Read /home/sc/repos/seans-reporepo/README.md tag index, for each repo tagged voice+agent, read its md file, and summarize what they do together"
```

---

### Application C: Media-to-Knowledge Dashboard
**Combines:** yt-dlp → onefilellm → seans-reporepo → Discord/Web dashboard

**How it works:**
1. Cron job or webhook triggers: new starred repo added to seans-reporepo? Or new video from a monitored channel?
2. yt-dlp downloads video/audio
3. onefilellm extracts transcript/text
4. LLM summarizes and categorizes (tags it for seans-reporepo)
5. Posts summary to Discord + updates dashboard

**Buildable components:**
- yt-dlp (pip install yt-dlp) ← media ingestion
- onefilellm (owned fork) ← text extraction + summarization
- seans-reporepo (owned) ← catalog + tag data
- hermes-web-computer dashboard (owned) ← display
- hermes-telemetry (owned) ← event tracking

**Effort:** Medium (2-4 days). The pipeline components exist; needs scheduling, Discord webhook integration, and dashboard visualization.

---

## 3. Best Utility-to-Effort Ratio

| Application | Utility | Effort | Ratio |
|-------------|---------|--------|-------|
| **B: Repo-Repo Research Agent** | HIGH — turns seans-reporepo from passive catalog into active discovery engine | LOW (1-2 days) | ⭐⭐⭐⭐⭐ |
| A: Voice Research Pipeline | HIGH — novel voice→research→voice loop | MEDIUM (3-5 days) | ⭐⭐⭐⭐ |
| C: Media-to-Knowledge Dashboard | MEDIUM — good for content curation | MEDIUM (2-4 days) | ⭐⭐⭐ |

**Winner: Application B — Repo-Repo Research Agent.** 
- It has the best utility-to-effort ratio because:
  - The data is already structured (seans-reporepo README tag index)
  - No new dependencies needed — just a Hermes skill/plugin
  - It directly enhances the existing tool the user already maintains
  - It can be incrementally improved (start with tag queries, add web search later)

---

## 4. Quick Wins (Under 30 Minutes)

### Quick Win 1: Tag-Intersection Hermes Skill
Write a Hermes skill that reads seans-reporepo/tag_index and answers intersection queries like:
- "Which repos are tagged both 'voice' and 'agent'?"
- "Show me all 'video' tagged repos"
- "What tags overlap between owned and starred repos?"

**Time:** ~20 min. The tag index is already in the README as a markdown table. Just need a skill with a few regex queries.

### Quick Win 2: onefilellm + seans-reporepo = auto-catalog
onefilellm already accepts GitHub repo URLs. Create a script:
```bash
cd /path/to/seans-reporepo
python onefilellm.py --repo https://github.com/someuser/somerepo
# Output: structured markdown ready to drop into starred/
```
**Time:** ~15 min. onefilellm already does the scraping; just need to pipe output into the reporepo format.

### Quick Win 3: Voice Command → yt-dlp → Transcript
Using hermes-web-computer's existing audio bridge:
- Say "download and transcribe [YouTube URL]"
- Hermes runs `yt-dlp -x --audio-format mp3 [url]` then `whisper [file]`
- Paste transcript into conversation

**Time:** ~25 min. All tools exist; just wiring.

---

## Summary

| Aspect | Finding |
|--------|---------|
| Voice cluster | Active — hermes-web-computer already has Fun-Audio-Chat integration. Codeovertcp is embryonic. Applio (voice conversion) is untapped. yt-dlp is starred but unused. |
| Research cluster | Gap exists — no owned repo does autonomous research or LLM eval. onefilellm is closest (scrapes papers/transcripts). seans-reporepo itself is an untapped knowledge asset. |
| Best new app | **Repo-Repo Research Agent** — queries seans-reporepo tag index + walks repo READMEs to generate structured briefings. Low effort, high utility. |
| Quickest win | Write a tag-intersection query skill for Hermes that mines the existing 67-tag index. ~20 min. |

---

## Queue Status (June 16)

Queued at `/home/sc/repos/cluster-mine-queue/` for player-agent autonomous execution (priority 3):

| # | Task | Priority | Ready |
|---|------|----------|-------|
| 1 | build-tag-query-script — Python tag-intersection query for seans-reporepo | HIGH | ✅ Queued |
| 2 | integrate-query-into-reporepo — Wire into README + refresh.sh | HIGH | ✅ Queued |
| 3 | build-repo-research-briefing — Automated briefing from tag queries + repo reads | HIGH | ✅ Queued |
| 4 | create-research-cron — Weekly cron for auto-briefing | HIGH | ✅ Queued |
| 5 | build-autocatalog-script — Auto-import starred repos into catalog format | MEDIUM | ✅ Queued |
| 6 | wire-auto-catalog-weekly — Append to refresh.sh | MEDIUM | ✅ Queued |
| — | Voice pipeline + Research pipeline (App A, App C) | LOWER | 📋 Future tasks in AGENTS.md |
