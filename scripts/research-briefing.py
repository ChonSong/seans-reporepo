#!/usr/bin/env python3
"""Generate a structured research briefing from repo tag queries.

Queries the seans-reporepo catalog by tag intersection, reads each matching
repo's full description, and produces a structured markdown briefing with:
  - Matched repos table
  - Capability cluster analysis
  - Integration opportunities
  - Next steps / suggested exploration

Usage:
  python3 scripts/research-briefing.py --tags agent,voice
  python3 scripts/research-briefing.py --tags agent,voice --any
  python3 scripts/research-briefing.py --tags llm --owned
  python3 scripts/research-briefing.py      # all repos
"""

import argparse
import sys
import textwrap
from pathlib import Path

# ── Import core functions from query.py ──────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
REPO_DIR = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

import query  # noqa: E402  (same-directory import)


def load_full_description(filepath: Path) -> str:
    """Read the full body of a repo .md file, stripping the YAML frontmatter."""
    content = filepath.read_text(encoding='utf-8', errors='replace')
    # Strip frontmatter
    if content.startswith('---'):
        try:
            fm_end = content.index('---', 3)
            body = content[fm_end + 3:].strip()
        except ValueError:
            body = content
    else:
        body = content
    return body


def read_repo_descriptions(entries: list[dict]) -> dict[str, str]:
    """Read the full description body for each matched repo.

    Returns {filename: full_body_text}.
    """
    descriptions = {}
    owned_dir = REPO_DIR / 'owned'
    starred_dir = REPO_DIR / 'starred'
    for e in entries:
        fname = e.get('_filename', '')
        source = e.get('_source', '')
        if source == 'owned':
            fp = owned_dir / fname
        elif source == 'starred':
            fp = starred_dir / fname
        else:
            continue
        if fp.exists():
            descriptions[fname] = load_full_description(fp)
    return descriptions


# ── Briefing section generators ──────────────────────────────────────────────

def generate_title(entries: list[dict], args_tags: list[str]) -> str:
    """Generate a descriptive title for the briefing."""
    if args_tags:
        tag_desc = ', '.join(args_tags[:5])
        if len(args_tags) > 5:
            tag_desc += f' +{len(args_tags) - 5} more'
        return f"# Research Briefing: Tags [{tag_desc}]\n"
    return "# Research Briefing: All Repos\n"


def generate_matched_repos_table(entries: list[dict]) -> str:
    """Generate the matched repos section with a table and summary counts."""
    if not entries:
        return "## Matched Repos\n\n*No matching repos found.*\n"

    owned_ct = sum(1 for e in entries if e.get('_source') == 'owned')
    starred_ct = sum(1 for e in entries if e.get('_source') == 'starred')

    lines = [
        "## Matched Repos\n",
        f"**{len(entries)} repos matched** ({owned_ct} owned, {starred_ct} starred).\n",
    ]

    # Reuse query.py's format_table
    lines.append(query.format_table(entries))
    lines.append("")

    # Breakdown by type
    type_counts: dict[str, int] = {}
    for e in entries:
        t = e.get('type', 'unknown') or 'unknown'
        type_counts[t] = type_counts.get(t, 0) + 1
    if type_counts:
        lines.append("**By type:** " + ", ".join(f"{k}={v}" for k, v in sorted(type_counts.items())))
        lines.append("")

    return '\n'.join(lines)


def generate_capability_summary(entries: list[dict], descriptions: dict[str, str]) -> str:
    """Analyze repo descriptions and produce a capability cluster map."""
    if not entries:
        return "## Capability Summary\n\n*No repos to analyze.*\n"

    lines = [
        "## Capability Summary\n",
    ]

    # Group repos by type for cluster analysis
    clusters: dict[str, list[dict]] = {}
    for e in entries:
        t = e.get('type', 'unknown') or 'unknown'
        clusters.setdefault(t, []).append(e)

    # Build capability descriptions per cluster
    cluster_capabilities = {
        'agent': 'Agent frameworks, CLI tools, and autonomous system orchestrators',
        'monorepo': 'Platform monorepos — multi-service deployments with integrated frontends/backends',
        'library': 'Reusable libraries and SDKs for composing into larger systems',
        'awesome-list': 'Curated resource collections for discovery and reference',
        'tool': 'Utility tools for automation, monitoring, and data processing',
        'web-app': 'Standalone web applications with specific user-facing functionality',
        'template': 'Project templates and starter kits',
        'unknown': 'Repos whose primary purpose is not yet classified',
    }

    for cluster_name, cluster_entries in sorted(clusters.items()):
        names = ', '.join(
            e.get('repo', '?').split('/')[-1] if '/' in e.get('repo', '')
            else e.get('repo', '?')
            for e in cluster_entries
        )
        cap = cluster_capabilities.get(cluster_name, '')
        lines.append(f"- **{cluster_name.title()}** ({len(cluster_entries)}): {cap}")
        lines.append(f"  - Repos: {names}")

    lines.append("")
    lines.append("### Key Themes\n")

    # Extract common tags across all matched repos
    tag_freq: dict[str, int] = {}
    for e in entries:
        for t in e.get('tags', []):
            tl = t.lower()
            tag_freq[tl] = tag_freq.get(tl, 0) + 1

    # Show top themes (tags appearing in >1 repo, sorted by frequency)
    themes = [(t, c) for t, c in sorted(tag_freq.items(), key=lambda x: -x[1]) if c > 1]
    if themes:
        for tag, count in themes[:10]:
            pct = round(count / len(entries) * 100)
            lines.append(f"- **{tag}** — appears in {count}/{len(entries)} repos ({pct}%)")
    else:
        lines.append("*No common themes identified.*")

    lines.append("")
    return '\n'.join(lines)


def generate_integration_opportunities(entries: list[dict]) -> str:
    """Suggest how the matched repos could work together."""
    if not entries:
        return "## Integration Opportunities\n\n*No repos to analyze.*\n"

    lines = [
        "## Integration Opportunities\n",
    ]

    # Look for complementary pairs
    types = [e.get('type', 'unknown') for e in entries]
    owners = [e.get('_source') for e in entries]

    has_owned = 'owned' in owners
    # Map names for cross-references
    names_short = [
        (e.get('repo', '?').split('/')[-1] if '/' in e.get('repo', '') else e.get('repo', '?'),
         e.get('repo', '?'),
         e.get('_source', ''))
        for e in entries
    ]

    # Identify integration vectors based on tags
    all_tags: set[str] = set()
    for e in entries:
        all_tags.update(t.lower() for t in e.get('tags', []))
    tag_list = sorted(all_tags)

    suggestions = []

    if has_owned and len(entries) >= 2:
        suggestions.append(
            f"- **Cross-repo pipeline**: You own {sum(1 for _ in owners if _ == 'owned')} of these "
            f"repos. Consider wiring them into a shared deployment or data pipeline."
        )

    # Suggest integration based on tool/agent mix
    if 'agent' in all_tags and 'api' in all_tags:
        suggestions.append(
            "- **Agent + API integration**: Combine agent repos with API-capable repos "
            "to create autonomous service orchestrators."
        )
    if 'docker' in all_tags and 'web-app' in all_tags:
        suggestions.append(
            "- **Containerized deployment**: Package web-app repos with Docker for consistent "
            "deployment alongside your existing stack."
        )
    if 'database' in all_tags and 'dashboard' in all_tags:
        suggestions.append(
            "- **Data pipeline**: Connect database-backed repos with dashboard repos "
            "for real-time monitoring and analytics."
        )
    if 'audio' in all_tags and 'voice' in all_tags:
        suggestions.append(
            "- **Voice pipeline**: Combine audio + voice repos into a speech-to-text "
            "or voice-command processing pipeline."
        )
    if 'llm' in all_tags or 'ai' in all_tags:
        suggestions.append(
            "- **LLM-backed automation**: Add LLM repos to agent pipelines for "
            "natural language task routing and decision making."
        )

    if not suggestions:
        suggestions.append("*No obvious integration patterns detected from available tags.*")

    lines.extend(suggestions)
    lines.append("")
    return '\n'.join(lines)


def generate_next_steps(entries: list[dict]) -> str:
    """Suggest concrete next actions based on the analysis."""
    if not entries:
        return "## Next Steps\n\n*No repos to act on.*\n"

    lines = ["## Next Steps\n"]

    # Recommend starred repos that could be adopted
    starred = [e for e in entries if e.get('_source') == 'starred']
    if starred:
        lines.append(
            f"1. **Review starred repos for adoption**: {len(starred)} starred repos matched. "
            "Consider forking or cloning the highest-value ones for deeper integration."
        )
        top_starred = sorted(starred, key=lambda e: -int(e.get('stars', 0)))[:3]
        for e in top_starred:
            name = e.get('repo', '?')
            stars = e.get('stars', 0)
            desc = e.get('description', '').strip() or 'No description'
            lines.append(f"   - [{name}]({e.get('url', '#')}) ({stars}★) — {desc}")

    # Recommend clustering owned repos
    owned = [e for e in entries if e.get('_source') == 'owned']
    if owned:
        lines.append(
            f"2. **Audit owned repos**: {len(owned)} owned repos matched. "
            "Check for stale or overlapping projects that could be consolidated."
        )

    # Suggest exploring further tag combinations
    tags_used: set[str] = set()
    for e in entries:
        tags_used.update(t.lower() for t in e.get('tags', []))
    tag_list = sorted(tags_used)
    if len(tag_list) >= 3:
        # Suggest a cross-section that wasn't queried
        lines.append(
            f"3. **Refine query**: Try a narrower combination like "
            f"`--tags {','.join(tag_list[:2])}` to focus on highest-density clusters."
        )

    lines.append("")
    lines.append("*Report generated by research-briefing.py*")
    lines.append("")
    return '\n'.join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Generate a structured research briefing from repo tag queries.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              python3 scripts/research-briefing.py --tags agent,voice
              python3 scripts/research-briefing.py --tags agent,voice --any
              python3 scripts/research-briefing.py --tags llm --owned
              python3 scripts/research-briefing.py  # all repos
        """),
    )
    parser.add_argument('--tags', type=str, default='',
                        help='Comma-separated tags to filter by')
    parser.add_argument('--any', action='store_true', dest='any_mode',
                        help='Match ANY listed tag instead of ALL (union vs intersection)')
    parser.add_argument('--owned', action='store_true',
                        help='Show only owned repos')
    parser.add_argument('--starred', action='store_true',
                        help='Show only starred repos')
    parser.add_argument('--all', action='store_true', dest='show_all',
                        help='Show all repos (default scope)')

    args = parser.parse_args()

    # Determine scope (same logic as query.py)
    scope = 'all'
    if args.owned and not args.starred:
        scope = 'owned'
    elif args.starred and not args.owned:
        scope = 'starred'
    elif args.owned and args.starred:
        scope = 'all'

    # Load entries
    entries = query.load_entries(scope)

    # Parse tags
    tags = [t.strip() for t in args.tags.split(',') if t.strip()] if args.tags else []
    mode = 'any' if args.any_mode else 'all'

    if tags:
        entries = [e for e in entries if query.match_tags(e, tags, mode)]

    # Sort by stars desc
    entries.sort(key=lambda e: -int(e.get('stars', 0)) if str(e.get('stars', '0')).isdigit() else 0)

    # Read full descriptions
    descriptions = read_repo_descriptions(entries)

    # Generate briefing
    sections = []
    sections.append(generate_title(entries, tags))
    sections.append(generate_matched_repos_table(entries))
    sections.append(generate_capability_summary(entries, descriptions))
    sections.append(generate_integration_opportunities(entries))
    sections.append(generate_next_steps(entries))

    result = '\n'.join(sections)
    print(result)
    sys.exit(0)


if __name__ == '__main__':
    main()
