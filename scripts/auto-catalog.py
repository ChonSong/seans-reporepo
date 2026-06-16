#!/usr/bin/env python3
"""Auto-catalog a GitHub repo into the seans-reporepo catalog.

Ingests a GitHub repo URL (or onefilellm output via stdin) and produces
a structured markdown file matching the seans-reporepo format.

Usage:
  python3 scripts/auto-catalog.py --url https://github.com/user/repo
  python3 scripts/auto-catalog.py --stdin < onefilellm-output.txt
  python3 scripts/auto-catalog.py --url https://github.com/user/repo --owned
"""
import argparse
import json
import os
import re
import sys
import textwrap
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_DIR = Path(__file__).parent.parent
OWNED_DIR = REPO_DIR / 'owned'
STARRED_DIR = REPO_DIR / 'starred'

# ── Tag normalization ──────────────────────────────────────────────
# Mirrors the mapping in generate-catalog.py
TOPIC_TAG_MAP = {
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
    "typescript": "typescript", "javascript": "javascript", "python": "python",
    "go": "go", "golang": "go", "rust": "rust",
    "svelte": "svelte", "react": "react", "vue": "vue",
    "framework": "framework", "library": "library", "sdk": "library",
    "plugin": "plugin", "extension": "plugin",
    "testing": "testing", "test-framework": "testing",
    "benchmark": "benchmarking", "benchmarking": "benchmarking",
    "automation": "automation", "ci-cd": "automation",
    "workflow": "workflow-engine", "workflow-engine": "workflow-engine",
    "orchestration": "orchestration", "orchestrator": "orchestration",
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

TEXT_KEYWORD_MAP = {
    "dashboard": "dashboard", "agent": "agent", "nanobot": "agent",
    "ai": "ai", "llm": "llm", "cli": "cli", "web": "web-app",
    "api": "api", "bot": "bot", "monitor": "monitoring",
    "backup": "backup", "sync": "sync", "docker": "docker",
    "infrastructure": "infrastructure", "transmut": "transpilation",
    "circuit breaker": "reliability", "energy": "energy",
    "carbon": "sustainability", "benchmark": "benchmarking",
    "poker": "gaming", "starcraft": "gaming", "dotfiles": "dotfiles",
    "mobile": "mobile", "voice": "voice", "audio": "audio",
    "video": "video", "terminal": "terminal", "tui": "tui",
    "game": "gaming", "sol": "solver", "code-server": "remote-dev",
    "ide": "ide", "openclaw": "openclaw", "hermes": "hermes-agent",
    "aie": "aie", "harness": "harness", "orchestrat": "orchestration",
    "react": "react", "express": "express", "postgresql": "database",
    "go": "go", "python": "python", "typescript": "typescript",
    "rust": "rust", "nginx": "nginx", "proxy": "proxy",
    "telemetry": "telemetry", "logging": "logging", "analytics": "analytics",
    "mcp": "mcp", "plugin": "plugin", "framework": "framework",
    "testing": "testing", "automation": "automation",
    "repomix": "code-packing", "gitingest": "code-ingestion",
    "openhands": "coding-agent", "opencode": "coding-agent",
    "comfyui": "image-gen", "stable": "image-gen",
    "langfuse": "observability", "opik": "observability",
    "milvus": "vector-db", "txtai": "vector-search",
    "temporal": "workflow-engine", "dokku": "paas",
    "headscale": "vpn", "wireguard": "vpn", "netdata": "monitoring",
    "swag": "reverse-proxy", "open-webui": "chat-ui",
    "karpathy": "research", "deepresearch": "research",
    "autoresearch": "research", "awesome": "awesome-list",
    "list": "awesome-list", "agent-browser": "browser-automation",
    "browser": "browser-automation", "vector": "vector-db",
    "embedding": "embeddings", "fine-tun": "fine-tuning",
    "training": "training", "rag": "rag", "retrieval": "rag",
    "multi-agent": "multi-agent", "team": "multi-agent", "svelte": "svelte",
}


def extract_tags(text: str) -> list:
    """Extract tags from description/README text."""
    tags = set()
    for kw, tag in TEXT_KEYWORD_MAP.items():
        if kw.lower() in text.lower():
            tags.add(tag)
    return sorted(tags)


def merge_tags(text_tags: list, topics: list) -> list:
    """Merge keyword-extracted tags with GitHub topics."""
    tags = set(text_tags)
    for t in topics:
        t_lower = t.lower().replace("_", "-")
        if t_lower in TOPIC_TAG_MAP:
            tags.add(TOPIC_TAG_MAP[t_lower])
        for key, tag in TOPIC_TAG_MAP.items():
            if key in t_lower or t_lower in key:
                tags.add(tag)
    return sorted(tags)


def detect_type(desc: str, fork: bool) -> str:
    """Detect repo type from description."""
    dl = (desc or "").lower()
    if "monorepo" in dl or "dashboard" in dl:
        return "monorepo"
    if "framework" in dl or "library" in dl:
        return "library"
    if "awesome" in dl or "list of" in dl:
        return "awesome-list"
    if "agent" in dl or "bot" in dl or "assistant" in dl:
        return "agent"
    if "cli" in dl or "command line" in dl:
        return "cli"
    if "web app" in dl or "web-based" in dl:
        return "webapp"
    if "docker" in dl or "infrastructure" in dl or "server" in dl:
        return "infrastructure"
    if "backup" in dl or "sync" in dl:
        return "utility"
    if fork:
        return "fork"
    return "unknown"


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


def generate_repo_markdown(data: dict) -> str:
    """Generate the full .md file content for a repo entry."""
    name = data["repo"]
    short_name = name.split("/")[-1]
    url = data["url"]
    description = data.get("description", "")
    rtype = data.get("type", "unknown")
    status = data.get("status", "active")
    language = data.get("language", "other")
    size_kb = data.get("size_kb", 0)
    stars = data.get("stars", 0)
    last_pushed = data.get("last_pushed", "")
    license_val = data.get("license", "unknown")
    tags = data.get("tags", [])

    fm_data = {
        "repo": name,
        "url": url,
        "description": description,
        "type": rtype,
        "status": status,
        "language": language if language else "other",
        "size_kb": size_kb,
        "stars": stars,
        "last_pushed": last_pushed,
        "license": license_val,
        "tags": tags,
    }

    content = format_frontmatter(fm_data)
    content += f"\n\n# {short_name}\n\n"
    content += f"> {description}\n\n"
    content += f"**URL:** [{name}]({url})\n"
    content += f"\n## Metadata\n\n"
    content += f"- **Type:** {rtype}\n"
    content += f"- **Status:** {status}\n"
    content += f"- **Language:** {language if language else 'N/A'}\n"
    content += f"- **Size:** {size_kb:,} KB\n"
    content += f"- **Stars:** {stars:,}\n"
    content += f"- **Last Pushed:** {last_pushed}\n"
    content += f"- **License:** {license_val}\n"
    if tags:
        content += f"- **Tags:** {', '.join(tags)}\n"

    return content


def parse_github_url(url: str) -> tuple[str, str]:
    """Parse a GitHub URL into (owner, repo)."""
    # Strip trailing .git, trailing slashes
    url = url.rstrip("/")
    if url.endswith(".git"):
        url = url[:-4]
    # Match patterns: https://github.com/owner/repo, git@github.com:owner/repo
    m = re.search(r"github\.com[/:]([^/]+)/([^/]+)", url)
    if not m:
        raise ValueError(f"Not a valid GitHub URL: {url}")
    return m.group(1), m.group(2)


def fetch_github_api(owner: str, repo: str) -> dict:
    """Fetch repo metadata from GitHub API."""
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(api_url)
    req.add_header("Accept", "application/vnd.github.v3+json")
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code == 403:
            raise RuntimeError(
                f"GitHub API rate limited (403). Set GITHUB_TOKEN env var or try later."
            ) from e
        elif e.code == 404:
            raise RuntimeError(f"Repo {owner}/{repo} not found (404).") from e
        else:
            raise RuntimeError(f"GitHub API error {e.code}: {e.reason}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error fetching GitHub API: {e.reason}") from e

    description = data.get("description") or ""
    topics = data.get("topics", []) or []
    language = data.get("language") or "other"
    size_kb = data.get("size", 0)
    stars = data.get("stargazers_count", 0) or 0
    forks = data.get("forks_count", 0) or 0
    fork = data.get("fork", False)
    license_info = data.get("license")
    license_val = license_info.get("spdx_id", "unknown") if license_info else "unknown"
    pushed_at = data.get("pushed_at", "")
    if pushed_at:
        pushed_at = pushed_at[:10]  # YYYY-MM-DD
    archived = data.get("archived", False)

    # Derive tags
    text_tags = extract_tags(description)
    tags = merge_tags(text_tags, topics)

    # Detect type
    rtype = detect_type(description, fork)

    # Status
    status = "active"
    if archived:
        status = "archived"

    return {
        "repo": f"{owner}/{repo}",
        "url": f"https://github.com/{owner}/{repo}",
        "description": description,
        "type": rtype,
        "status": status,
        "language": language,
        "size_kb": size_kb,
        "stars": stars,
        "forks": forks,
        "last_pushed": pushed_at,
        "license": license_val,
        "topics": topics,
        "tags": tags,
        "archived": archived,
        "fork": fork,
        "refreshed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def check_duplicate(data: dict) -> str | None:
    """Check if a repo already exists in the catalog. Returns the existing file path or None."""
    full_name = data["repo"]
    filename = full_name.replace("/", "_") + ".md"
    # Check owned
    owned_path = OWNED_DIR / filename
    if owned_path.exists():
        return str(owned_path)
    # Check starred
    starred_path = STARRED_DIR / filename
    if starred_path.exists():
        return str(starred_path)
    return None


def write_catalog_entry(data: dict, scope: str | None = None) -> str:
    """Write the catalog entry to the appropriate directory. Returns the output path."""
    full_name = data["repo"]
    owner = full_name.split("/")[0]
    filename = full_name.replace("/", "_") + ".md"

    # Determine scope
    if scope == "owned" or (scope is None and owner.lower() == "chonsong"):
        out_dir = OWNED_DIR
    else:
        out_dir = STARRED_DIR

    out_dir.mkdir(parents=True, exist_ok=True)
    output_path = out_dir / filename
    content = generate_repo_markdown(data)
    output_path.write_text(content, encoding="utf-8")
    return str(output_path)


def cmd_url(url: str, scope: str | None = None, force: bool = False):
    """Handle --url mode: fetch from GitHub API and catalog."""
    owner, repo_name = parse_github_url(url)
    print(f"Fetching {owner}/{repo_name} from GitHub API...", file=sys.stderr)
    data = fetch_github_api(owner, repo_name)

    existing = check_duplicate(data)
    if existing and not force:
        print(f"Already cataloged at {existing}. Use --force to overwrite.", file=sys.stderr)
        sys.exit(0)

    out_path = write_catalog_entry(data, scope)
    print(f"Cataloged: {out_path}")
    print(f"  Repo: {data['repo']}")
    print(f"  Type: {data['type']}")
    print(f"  Tags: {', '.join(data['tags'])}")


def cmd_stdin(scope: str | None = None, force: bool = False):
    """Handle --stdin mode: parse input and catalog."""
    input_data = sys.stdin.read().strip()
    if not input_data:
        print("Error: no input on stdin", file=sys.stderr)
        sys.exit(1)

    # Try JSON
    try:
        data = json.loads(input_data)
    except json.JSONDecodeError:
        # Try markdown frontmatter
        data = parse_frontmatter(input_data)

    if not data or "repo" not in data:
        print("Error: could not parse repo info from stdin (expected JSON or markdown with frontmatter)", file=sys.stderr)
        sys.exit(1)

    # Normalize fields
    if "url" not in data and "repo" in data:
        data["url"] = f"https://github.com/{data['repo']}"

    existing = check_duplicate(data)
    if existing and not force:
        print(f"Already cataloged at {existing}. Use --force to overwrite.", file=sys.stderr)
        sys.exit(0)

    out_path = write_catalog_entry(data, scope)
    print(f"Cataloged: {out_path}")


def parse_frontmatter(content: str) -> dict:
    """Parse simple YAML-like frontmatter from a .md file."""
    entry = {}
    if not content.startswith("---"):
        return entry
    try:
        fm_end = content.index("---", 3)
    except ValueError:
        return entry
    fm_text = content[3:fm_end]
    current_list_key = None
    for line in fm_text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- "):
            if current_list_key:
                if current_list_key not in entry:
                    entry[current_list_key] = []
                val = stripped[2:].strip().strip("'\"")
                if val:
                    entry[current_list_key].append(val)
            continue
        current_list_key = None
        if ":" not in stripped:
            continue
        key, val = stripped.split(":", 1)
        key = key.strip()
        val = val.strip()
        if not val:
            current_list_key = key
        elif val.startswith("["):
            items = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip().strip("'\"")]
            entry[key] = items
        else:
            entry[key] = val.strip("'\"")
    return entry


def main():
    parser = argparse.ArgumentParser(
        description="Auto-catalog a GitHub repo into the seans-reporepo catalog.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              python3 scripts/auto-catalog.py --url https://github.com/yt-dlp/yt-dlp
              python3 scripts/auto-catalog.py --url https://github.com/user/repo --owned
              python3 scripts/auto-catalog.py --stdin < /path/to/repo.md
              python3 scripts/auto-catalog.py --url https://github.com/user/repo --force
        """),
    )
    parser.add_argument("--url", type=str, default="", help="GitHub repo URL to catalog")
    parser.add_argument("--stdin", action="store_true", help="Read repo info from stdin (JSON or markdown frontmatter)")
    parser.add_argument("--owned", action="store_true", help="Mark as owned repo (default: auto-detect based on owner)")
    parser.add_argument("--starred", action="store_true", help="Mark as starred repo (default: auto-detect)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing entry if present")
    args = parser.parse_args()

    # Determine scope
    scope = None
    if args.owned and not args.starred:
        scope = "owned"
    elif args.starred and not args.owned:
        scope = "starred"

    if args.url:
        cmd_url(args.url, scope, args.force)
    elif args.stdin:
        cmd_stdin(scope, args.force)
    else:
        parser.print_help()
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
