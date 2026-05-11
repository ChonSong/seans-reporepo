#!/usr/bin/env python3
"""Generate the repo catalog for seans-reporepo.

Usage: python3 generate-catalog.py /path/to/repo
"""
import base64
import json
import os
import subprocess
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path


# ── Tag normalization from GitHub topics ──────────────────────────────
# Shared between owned and starred. Maps GitHub topic keywords to our
# canonical tag names. Broad enough to catch common ecosystem topics.
TOPIC_TAG_MAP = {
    # Core tech
    "ai": "ai", "machine-learning": "ai", "artificial-intelligence": "ai",
    "deep-learning": "ai", "generative-ai": "ai",
    "llm": "llm", "large-language-model": "llm", "language-model": "llm",
    "agent": "agent", "agents": "agent", "autonomous-agent": "agent",
    "multi-agent": "multi-agent", "multiagent": "multi-agent",
    "mcp": "mcp", "model-context-protocol": "mcp",
    "cli": "cli", "command-line": "cli", "terminal": "terminal",
    "tui": "tui", "terminal-ui": "tui",
    "api": "api", "rest-api": "api", "graphql": "api",
    "web-app": "web-app", "webapp": "web-app", "web-application": "web-app",
    "frontend": "web-app", "frontend-dev": "web-app",
    "backend": "infrastructure", "backend-dev": "infrastructure",
    "bot": "bot", "chatbot": "bot",
    "docker": "docker", "container": "docker", "containers": "docker",
    "kubernetes": "docker", "k8s": "docker",
    "infrastructure": "infrastructure", "infra": "infrastructure",
    "server": "infrastructure", "serverless": "infrastructure",
    "cloud": "infrastructure", "aws": "infrastructure", "gcp": "infrastructure",
    "monitoring": "monitoring", "observability": "observability",
    "telemetry": "telemetry", "logging": "logging", "analytics": "analytics",
    "dashboard": "dashboard", "admin-panel": "dashboard",
    # Languages
    "typescript": "typescript", "javascript": "javascript", "python": "python",
    "go": "go", "golang": "go", "rust": "rust",
    "svelte": "svelte", "react": "react", "vue": "vue",
    # Patterns
    "framework": "framework", "library": "library", "sdk": "library",
    "plugin": "plugin", "extension": "plugin",
    "testing": "testing", "test-framework": "testing",
    "benchmark": "benchmarking", "benchmarking": "benchmarking",
    "automation": "automation", "ci-cd": "automation",
    "workflow": "workflow-engine", "workflow-engine": "workflow-engine",
    "orchestration": "orchestration", "orchestrator": "orchestration",
    # Domains
    "gaming": "gaming", "game": "gaming",
    "dotfiles": "dotfiles", "dev-environment": "dotfiles",
    "backup": "backup", "sync": "sync", "synchronization": "sync",
    "security": "security", "auth": "security", "authentication": "security",
    "database": "database", "db": "database",
    "vector-db": "vector-db", "vector-database": "vector-db",
    "vector-search": "vector-search", "embeddings": "embeddings",
    "rag": "rag", "retrieval-augmented-generation": "rag",
    "fine-tuning": "fine-tuning", "finetuning": "fine-tuning",
    "training": "training",
    "browser-automation": "browser-automation", "browser": "browser-automation",
    "scraping": "browser-automation", "scraper": "browser-automation",
    "voice": "voice", "audio": "audio", "video": "video",
    "music": "audio", "text-to-speech": "voice",
    "mobile": "mobile", "ios": "mobile", "android": "mobile",
    "research": "research", "paper": "research",
    "education": "education", "learning": "education",
    # Ecosystem-specific
    "openclaw": "openclaw", "hermes": "hermes-agent",
    "nanobot": "agent",
    "coding-agent": "coding-agent", "code-generation": "coding-agent",
    "code-packing": "code-packing", "code-ingestion": "code-ingestion",
    "awesome": "awesome-list", "awesome-list": "awesome-list",
    "resources": "awesome-list", "collection": "awesome-list",
    "image-gen": "image-gen", "image-generation": "image-gen",
    "comfyui": "image-gen", "stable-diffusion": "image-gen",
    "proxy": "proxy", "reverse-proxy": "reverse-proxy",
    "nginx": "nginx", "vpn": "vpn", "wireguard": "vpn",
    "paas": "paas", "platform": "paas",
    "chat-ui": "chat-ui", "chat": "chat-ui",
    "sustainability": "sustainability", "green-computing": "sustainability",
    "energy": "energy", "energy-efficiency": "energy",
    "reliability": "reliability", "circuit-breaker": "reliability",
    "transpilation": "transpilation", "transpiler": "transpilation",
    "ide": "ide", "code-editor": "ide",
    "remote-dev": "remote-dev", "remote-development": "remote-dev",
    "solver": "solver", "poker": "gaming",
    "express": "express", "postgresql": "database",
    "aie": "aie", "harness": "harness",
    "design-system": "design-system", "ui": "ui", "ux": "ui",
    "web-design": "design-system", "css": "css",
    "roadmap": "education", "developer-roadmap": "education",
}

# Keyword map for description/README text scanning (fallback when no topics).
TEXT_KEYWORD_MAP = {
    "dashboard": "dashboard",
    "agent": "agent", "nanobot": "agent",
    "ai": "ai",
    "llm": "llm",
    "cli": "cli",
    "web": "web-app",
    "api": "api",
    "bot": "bot",
    "monitor": "monitoring",
    "backup": "backup",
    "sync": "sync",
    "docker": "docker",
    "infrastructure": "infrastructure",
    "transmut": "transpilation",
    "circuit breaker": "reliability",
    "energy": "energy",
    "carbon": "sustainability",
    "benchmark": "benchmarking",
    "poker": "gaming",
    "starcraft": "gaming",
    "dotfiles": "dotfiles",
    "landing": "website",
    "mobile": "mobile",
    "voice": "voice",
    "audio": "audio",
    "video": "video",
    "terminal": "terminal",
    "tui": "tui",
    "game": "gaming",
    "sol": "solver",
    "code-server": "remote-dev",
    "ide": "ide",
    "openclaw": "openclaw",
    "hermes": "hermes-agent",
    "aie": "aie",
    "harness": "harness",
    "orchestrat": "orchestration",
    "react": "react",
    "express": "express",
    "postgresql": "database",
    "go": "go",
    "python": "python",
    "typescript": "typescript",
    "rust": "rust",
    "nginx": "nginx",
    "proxy": "proxy",
    "telemetry": "telemetry",
    "logging": "logging",
    "analytics": "analytics",
    "mcp": "mcp",
    "plugin": "plugin",
    "framework": "framework",
    "testing": "testing",
    "automation": "automation",
    "repomix": "code-packing",
    "gitingest": "code-ingestion",
    "openhands": "coding-agent",
    "opencode": "coding-agent",
    "comfyui": "image-gen",
    "stable": "image-gen",
    "langfuse": "observability",
    "opik": "observability",
    "milvus": "vector-db",
    "txtai": "vector-search",
    "temporal": "workflow-engine",
    "dokku": "paas",
    "headscale": "vpn",
    "wireguard": "vpn",
    "netdata": "monitoring",
    "swag": "reverse-proxy",
    "open-webui": "chat-ui",
    "karpathy": "research",
    "deepresearch": "research",
    "autoresearch": "research",
    "awesome": "awesome-list",
    "list": "awesome-list",
    "agent-browser": "browser-automation",
    "browser": "browser-automation",
    "vector": "vector-db",
    "embedding": "embeddings",
    "fine-tun": "fine-tuning",
    "training": "training",
    "rag": "rag",
    "retrieval": "rag",
    "multi-agent": "multi-agent",
    "team": "multi-agent",
    "svelte": "svelte",
}


def gh(cmd: str) -> str:
    """Run a gh command and return stdout."""
    result = subprocess.run(
        f"gh {cmd}",
        shell=True,
        capture_output=True,
        text=True,
        timeout=120,
    )
    if result.returncode != 0:
        print(f"gh error: {result.stderr[:200]}", file=sys.stderr)
        return ""
    return result.stdout


def merge_tags(text_tags: list, topics: list) -> list:
    """Merge keyword-extracted tags with GitHub topics."""
    tags = set(text_tags)
    for t in topics:
        t_lower = t.lower().replace("_", "-")
        # Direct match
        if t_lower in TOPIC_TAG_MAP:
            tags.add(TOPIC_TAG_MAP[t_lower])
        # Partial match: check if any key is a substring of the topic
        for key, tag in TOPIC_TAG_MAP.items():
            if key in t_lower or t_lower in key:
                tags.add(tag)
    return sorted(tags)


def extract_tags(desc: str, readme: str = "") -> list:
    """Extract utility tags from description and README text."""
    text = (desc or "") + " " + (readme or "")
    tags = set()
    for kw, tag in TEXT_KEYWORD_MAP.items():
        if kw.lower() in text.lower():
            tags.add(tag)
    return sorted(tags)


def detect_type(desc: str, fork: bool, readme: str = "") -> str:
    desc_lower = (desc or "").lower()
    readme_lower = (readme or "").lower()
    combined = desc_lower + " " + readme_lower

    if "monorepo" in combined or "dashboard" in combined:
        return "monorepo"
    if "framework" in combined or "library" in combined:
        return "library"
    if "awesome" in combined or "list of" in combined:
        return "awesome-list"
    if "agent" in combined or "bot" in combined or "assistant" in combined:
        return "agent"
    if "cli" in combined or "command line" in combined:
        return "cli"
    if "web app" in combined or "web-based" in combined:
        return "webapp"
    if "docker" in combined or "infrastructure" in combined or "server" in combined:
        return "infrastructure"
    if "backup" in combined or "sync" in combined:
        return "utility"
    if fork:
        return "fork"
    return "unknown"


def detect_status(desc: str, archived: bool, fork: bool, has_readme: bool) -> str:
    desc_lower = (desc or "").lower()
    if archived:
        return "archived"
    if "scaffolded" in desc_lower or "awaiting" in desc_lower:
        return "scaffolded"
    if "suspended" in desc_lower:
        return "suspended"
    if fork and not has_readme:
        return "fork"
    return "active"


def format_frontmatter(data: dict) -> str:
    """Format YAML frontmatter manually to avoid PyYAML dependency."""
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            if not value:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                for item in value:
                    lines.append(f"  - {item}")
        elif isinstance(value, bool):
            lines.append(f"{key}: {str(value).lower()}")
        else:
            s = str(value) if value is not None else ""
            if any(c in s for c in [":", "#", "{", "}", "[", "]", ",", "&", "*", "?", "|", "-", "<", ">", "=", "!", "%", "@", "`"]):
                s = f"'{s}'"
            elif s == "":
                s = '""'
            lines.append(f"{key}: {s}")
    lines.append("---")
    return "\n".join(lines)


def generate_repo_markdown(entry: dict, readme_text: str = "") -> str:
    """Generate markdown file content for a repo."""
    fm_data = {
        "repo": entry["name"],
        "url": entry["url"],
        "description": entry["description"],
        "type": entry["type"],
        "status": entry["status"],
        "language": entry.get("language", "other"),
        "size_kb": entry["size_kb"],
        "stars": entry.get("stars", 0),
        "last_pushed": entry.get("last_pushed", ""),
        "license": entry.get("license", "unknown"),
        "tags": entry.get("tags", []),
        "topics": entry.get("topics", []),
        "refreshed_at": entry.get("refreshed_at", ""),
    }
    if entry.get("fork_of"):
        fm_data["fork_of"] = entry["fork_of"]

    content = format_frontmatter(fm_data)
    content += f"\n\n# {entry['name'].split('/')[-1]}\n\n"
    content += f"> {entry['description']}\n\n"
    content += f"**URL:** [{entry['name']}]({entry['url']})\n"
    if entry.get("fork_of"):
        content += f"**Fork of:** [{entry['fork_of']}](https://github.com/{entry['fork_of']})\n"

    content += f"\n## Metadata\n\n"
    content += f"- **Type:** {entry['type']}\n"
    content += f"- **Status:** {entry['status']}\n"
    content += f"- **Language:** {entry.get('language', 'N/A')}\n"
    content += f"- **Size:** {entry['size_kb']:,} KB\n"
    if not entry.get("fork_of"):
        content += f"- **Stars:** {entry.get('stars', 0):,}\n"
    content += f"- **Last Pushed:** {entry.get('last_pushed', 'N/A')}\n"
    content += f"- **License:** {entry.get('license', 'unknown')}\n"
    if entry.get("tags"):
        content += f"- **Tags:** {', '.join(entry['tags'])}\n"

    if readme_text:
        content += f"\n## README Excerpt\n\n{readme_text[:2000]}...\n"

    return content


def generate_readme(owned: list, starred: list, refreshed_at: str) -> str:
    """Generate the main README.md."""
    total_kb = sum(e.get("size_kb", 0) for e in owned + starred)

    # Build tag index
    tag_index = {}
    for e in owned + starred:
        for tag in e.get("tags", []):
            if tag not in tag_index:
                tag_index[tag] = {"owned": [], "starred": []}
            bucket = "owned" if e["name"].startswith("ChonSong/") else "starred"
            tag_index[tag][bucket].append(e["name"])

    # Language stats
    lang_stats = {}
    for e in owned + starred:
        lang = e.get("language", "other")
        if lang not in lang_stats:
            lang_stats[lang] = {"count": 0, "total_kb": 0}
        lang_stats[lang]["count"] += 1
        lang_stats[lang]["total_kb"] += e.get("size_kb", 0)

    readme = textwrap.dedent(f"""\
    # sean's-reporepo

    > Personal code catalog — owned and starred repositories indexed for ideation, discovery, and combinatorial application design.
    >
    > **Last refreshed:** {refreshed_at}

    ## Quick Stats

    | | Owned | Starred | Total |
    |---|---|---|---|
    | Repos | {len(owned)} | {len(starred)} | {len(owned) + len(starred)} |
    | Total Size | {sum(e.get('size_kb', 0) for e in owned):,} KB | {sum(e.get('size_kb', 0) for e in starred):,} KB | {total_kb:,} KB ({total_kb//1024:,} MB) |
    | Languages | {len(set(e.get('language') for e in owned))} | {len(set(e.get('language') for e in starred))} | {len(set(e.get('language') for e in owned + starred))} |
    | Tags | — | — | {len(tag_index)} |

    ## Structure

    ```
    ├── owned/           # My repositories ({len(owned)})
    │   ├── agent-os.md
    │   ├── repo-transmute.md
    │   └── ...
    ├── starred/         # Repos I've starred ({len(starred)})
    │   ├── yamadashy_repomix.md
    │   ├── e2b-dev_awesome-ai-agents.md
    │   └── ...
    ├── scripts/         # Utility scripts for catalog management
    ├── COMBINATORIAL.md # Cross-repo tag overlap analysis
    └── README.md        # This file
    ```

    ## Owned Repositories

    """)

    # Group owned by type
    type_groups = {}
    for e in owned:
        t = e.get("type", "unknown")
        if t not in type_groups:
            type_groups[t] = []
        type_groups[t].append(e)

    for t in sorted(type_groups.keys()):
        repos = type_groups[t]
        readme += f"### {t.replace('-', ' ').title()} ({len(repos)})\n\n"
        readme += "| Repo | Language | Size | Stars | Tags |\n"
        readme += "|---|---|---|---|---|\n"
        for e in sorted(repos, key=lambda x: x.get("size_kb", 0), reverse=True):
            tags = ", ".join(e.get("tags", [])[:3])
            link = f"[{e['short_name']}](owned/{e['name'].replace('/', '_')}.md)"
            readme += f"| {link} | {e.get('language', '-')} | {e.get('size_kb', 0):,} KB | {e.get('stars', 0):,} | {tags} |\n"
        readme += "\n"

    # Top starred
    top_starred = sorted(starred, key=lambda x: x.get("stars", 0), reverse=True)[:20]
    readme += "## Starred Repositories (Top 20 by Stars)\n\n"
    readme += "| Repo | Type | Language | Stars | Tags |\n"
    readme += "|---|---|---|---|---|\n"
    for e in top_starred:
        tags = ", ".join(e.get("tags", [])[:3])
        link = f"[{e['short_name']}](starred/{e['name'].replace('/', '_')}.md)"
        readme += f"| {link} | {e.get('type', '-')} | {e.get('language', '-')} | {e.get('stars', 0):,} | {tags} |\n"
    readme += f"\n*...and {len(starred) - 20} more in `starred/`*\n\n"

    # Tag index
    readme += "## Tag Index\n\n"
    readme += "| Tag | Count | Repos |\n"
    readme += "|---|---|---|\n"
    for tag in sorted(tag_index.keys()):
        info = tag_index[tag]
        total = len(info["owned"]) + len(info["starred"])
        sample = (info["owned"] + info["starred"])[:3]
        sample_str = ", ".join(s.split("/")[-1] for s in sample)
        if total > 3:
            sample_str += f" +{total-3} more"
        readme += f"| `{tag}` | {total} | {sample_str} |\n"

    # Language breakdown
    readme += "\n## Language Breakdown\n\n"
    readme += "| Language | Count | Total Size |\n"
    readme += "|---|---|---|\n"
    for lang in sorted(lang_stats.keys(), key=lambda x: lang_stats[x]["count"], reverse=True):
        info = lang_stats[lang]
        readme += f"| {lang} | {info['count']} | {info['total_kb']:,} KB |\n"

    # Combinatorial link
    readme += "\n## Combinatorial Potential\n\n"
    combo_tags = {k: v for k, v in tag_index.items() if v["owned"] and v["starred"]}
    readme += f"{len(combo_tags)} tags bridge owned and starred repos. See [COMBINATORIAL.md](COMBINATORIAL.md) for full analysis.\n"

    return readme


def generate_combinatorial(owned: list, starred: list) -> str:
    """Generate COMBINATORIAL.md with full tag overlap analysis."""
    tag_index = {}
    for e in owned + starred:
        for tag in e.get("tags", []):
            if tag not in tag_index:
                tag_index[tag] = {"owned": [], "starred": []}
            bucket = "owned" if e["name"].startswith("ChonSong/") else "starred"
            tag_index[tag][bucket].append(e)

    combo_tags = {k: v for k, v in tag_index.items() if v["owned"] and v["starred"]}

    lines = [
        "# Combinatorial Potential",
        "",
        "Repos that share tags are candidates for combination.",
        f"{len(combo_tags)} tags bridge owned and starred repos.",
        "",
    ]

    # Sort by total count descending (highest overlap first)
    for tag in sorted(combo_tags.keys(), key=lambda t: len(combo_tags[t]["owned"]) + len(combo_tags[t]["starred"]), reverse=True):
        info = combo_tags[tag]
        total = len(info["owned"]) + len(info["starred"])
        lines.append(f"### `{tag}` ({total} repos)")
        lines.append("")
        lines.append("Owned:")
        for e in sorted(info["owned"], key=lambda x: x.get("size_kb", 0), reverse=True):
            lines.append(f"- [{e['short_name']}]({e['url']}) — {e.get('description', '')[:80]}")
        lines.append("")
        lines.append("Starred:")
        for e in sorted(info["starred"], key=lambda x: x.get("stars", 0), reverse=True):
            lines.append(f"- [{e['short_name']}]({e['url']}) ⭐{e.get('stars', 0):,} — {e.get('description', '')[:80]}")
        lines.append("")

    # Star-only clusters (interesting starred repos that share tags)
    star_only = {k: v for k, v in tag_index.items() if not v["owned"] and len(v["starred"]) >= 3}
    if star_only:
        lines.append("## Starred-Only Clusters")
        lines.append("")
        lines.append("Tags that appear in starred repos but not owned — potential areas to explore.")
        lines.append("")
        for tag in sorted(star_only.keys(), key=lambda t: len(star_only[t]["starred"]), reverse=True)[:10]:
            repos = star_only[tag]["starred"]
            lines.append(f"### `{tag}` ({len(repos)} repos)")
            lines.append("")
            for e in sorted(repos, key=lambda x: x.get("stars", 0), reverse=True):
                lines.append(f"- [{e['short_name']}]({e['url']}) ⭐{e.get('stars', 0):,}")
            lines.append("")

    return "\n".join(lines)


def generate_changelog(old_names: set, new_entries: list, old_stars: dict) -> list:
    """Compare old vs new catalog, return list of change descriptions."""
    changes = []
    new_names = {e["name"] for e in new_entries}

    added = new_names - old_names
    removed = old_names - new_names

    if added:
        for name in sorted(added):
            e = next(x for x in new_entries if x["name"] == name)
            stars = e.get("stars", 0)
            star_str = f" ⭐{stars:,}" if stars > 0 else ""
            changes.append(f"+ {name}{star_str}")

    if removed:
        for name in sorted(removed):
            changes.append(f"- {name}")

    # Star count changes (starred only)
    star_changes = []
    for e in new_entries:
        if e["name"] in old_stars:
            old = old_stars[e["name"]]
            new = e.get("stars", 0)
            if old != new and new > 0:
                diff = new - old
                sign = "+" if diff > 0 else ""
                star_changes.append((e["name"], diff))

    if star_changes:
        star_changes.sort(key=lambda x: abs(x[1]), reverse=True)
        for name, diff in star_changes[:20]:  # Top 20 changes
            sign = "+" if diff > 0 else ""
            changes.append(f"  {name} {sign}{diff} stars")

    return changes


def safe_name(name: str) -> str:
    return name.replace("/", "_").replace(" ", "-")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate-catalog.py <repo-dir>")
        sys.exit(1)

    repo_dir = Path(sys.argv[1])
    print(f"Generating catalog in {repo_dir}")

    # Load old state for changelog
    old_names = set()
    old_stars = {}
    for d in ["owned", "starred"]:
        dir_path = repo_dir / d
        if dir_path.exists():
            for f in dir_path.glob("*.md"):
                old_names.add(f.name.replace(".md", "").replace("_", "/"))
                # Parse stars from frontmatter
                try:
                    content = f.read_text()
                    if "---" in content:
                        for line in content.split("---")[1].split("---")[0].split("\n"):
                            if line.startswith("stars:"):
                                old_stars[f.name.replace(".md", "").replace("_", "/")] = int(line.split(":")[1].strip().replace(",", ""))
                                break
                except Exception:
                    pass

    # Create directories
    (repo_dir / "owned").mkdir(exist_ok=True)
    (repo_dir / "starred").mkdir(exist_ok=True)

    refreshed_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Fetch owned repos
    print("Fetching owned repos...")
    owned_json = gh(
        'repo list ChonSong --limit 100 --json nameWithOwner,description,primaryLanguage,stargazerCount,forkCount,diskUsage,pushedAt,isFork,parent,licenseInfo,repositoryTopics'
    )
    if not owned_json:
        print("ERROR: Could not fetch owned repos")
        sys.exit(1)

    owned_data = json.loads(owned_json)
    print(f"  Found {len(owned_data)} owned repos")

    # Fetch starred repos
    print("Fetching starred repos...")
    starred_raw = gh("api user/starred --paginate")
    if not starred_raw:
        print("ERROR: Could not fetch starred repos")
        sys.exit(1)

    starred_raw_data = json.loads(starred_raw)
    # Filter: skip forks whose parent is already in owned
    owned_names_set = set(r["nameWithOwner"] for r in owned_data)
    starred_filtered = []
    for r in starred_raw_data:
        parent = r.get("parent", {}).get("full_name", "") if r.get("parent") else ""
        if parent not in owned_names_set:
            starred_filtered.append(r)

    print(f"  Found {len(starred_filtered)} starred repos (after filtering)")

    # Process owned
    readme_404_count = 0
    owned_entries = []
    for r in owned_data:
        name = r["nameWithOwner"]
        desc = r.get("description") or ""
        lang = r.get("primaryLanguage", {}).get("name") if r.get("primaryLanguage") else None
        size = r.get("diskUsage", 0)
        stars = r.get("stargazerCount", 0)
        pushed = (r.get("pushedAt") or "")[:10]
        fork = r.get("isFork", False)
        parent = r.get("parent", {}).get("nameWithOwner", "") if r.get("parent") else ""
        license_info = r.get("licenseInfo", {}).get("spdxId") if r.get("licenseInfo") else None
        topics = [t["name"] for t in (r.get("repositoryTopics") or [])]

        # Try to get README — handle 404s gracefully
        readme_text = ""
        try:
            readme_out = gh(f'api "repos/{name}/readme" --jq ".content"')
            if readme_out:
                readme_text = base64.b64decode(readme_out.strip()).decode("utf-8", errors="ignore")[:3000]
        except Exception:
            pass
        # If gh returned empty (404/private), it's already silent from gh()

        text_tags = extract_tags(desc, readme_text)
        tags = merge_tags(text_tags, topics)
        type_ = detect_type(desc, fork, readme_text)
        status = detect_status(desc, False, fork, bool(readme_text))

        entry = {
            "name": name,
            "short_name": name.split("/")[-1],
            "url": f"https://github.com/{name}",
            "description": desc or "No description",
            "type": type_,
            "status": status,
            "language": lang or "other",
            "size_kb": size,
            "stars": stars,
            "last_pushed": pushed,
            "license": license_info or "unknown",
            "tags": tags,
            "fork_of": parent if fork else None,
            "topics": topics,
            "refreshed_at": refreshed_at,
        }

        md_content = generate_repo_markdown(entry, readme_text[:2000] if readme_text else "")
        fn = safe_name(name)
        (repo_dir / "owned" / f"{fn}.md").write_text(md_content)
        owned_entries.append(entry)

    print(f"  Created {len(owned_entries)} owned files")

    # Process starred
    starred_entries = []
    for r in starred_filtered:
        name = r["full_name"]
        desc = r.get("description") or ""
        lang = r.get("language") or "other"
        size = r.get("size", 0)
        stars = r.get("stargazers_count", 0)
        pushed = (r.get("pushed_at") or "")[:10]
        fork = r.get("is_fork", False)
        parent = r.get("parent", {}).get("full_name", "") if r.get("parent") else ""
        license_info = r.get("license", {}).get("spdx_id") if r.get("license") else None
        topics = r.get("topics", [])
        archived = r.get("archived", False)

        text_tags = extract_tags(desc)
        tags = merge_tags(text_tags, topics)
        type_ = detect_type(desc, fork)
        status = "archived" if archived else "active"

        entry = {
            "name": name,
            "short_name": name.split("/")[-1],
            "url": f"https://github.com/{name}",
            "description": desc or "No description",
            "type": type_,
            "status": status,
            "language": lang,
            "size_kb": size,
            "stars": stars,
            "last_pushed": pushed,
            "license": license_info or "unknown",
            "tags": tags,
            "fork_of": parent if fork else None,
            "topics": topics,
            "refreshed_at": refreshed_at,
        }

        md_content = generate_repo_markdown(entry)
        fn = safe_name(name)
        (repo_dir / "starred" / f"{fn}.md").write_text(md_content)
        starred_entries.append(entry)

    print(f"  Created {len(starred_entries)} starred files")

    # Generate README
    readme = generate_readme(owned_entries, starred_entries, refreshed_at)
    (repo_dir / "README.md").write_text(readme)
    print(f"  Generated README.md (refreshed: {refreshed_at})")

    # Generate COMBINATORIAL.md
    combinatorial = generate_combinatorial(owned_entries, starred_entries)
    (repo_dir / "COMBINATORIAL.md").write_text(combinatorial)
    print("  Generated COMBINATORIAL.md")

    # Remove stale files
    for d in ["owned", "starred"]:
        expected_names = {safe_name(e["name"]) + ".md" for e in (owned_entries if d == "owned" else starred_entries)}
        for f in (repo_dir / d).glob("*.md"):
            if f.name not in expected_names:
                f.unlink()
                print(f"  Removed stale: {d}/{f.name}")

    # Print changelog
    changes = generate_changelog(old_names, owned_entries + starred_entries, old_stars)
    if changes:
        print("\n  ── Changelog ──")
        for c in changes:
            print(f"    {c}")
    else:
        print("\n  No changes detected.")

    print(f"\nCatalog generation complete. {refreshed_at}")


if __name__ == "__main__":
    main()
