#!/usr/bin/env python3
"""Query the repo catalog by tags, scope, and overlap analysis.

Usage:
  python3 query.py --tags agent,voice          # repos with ALL listed tags (intersection)
  python3 query.py --tags agent,voice --any    # repos with ANY listed tag (union)
  python3 query.py --owned                     # owned repos only
  python3 query.py --starred                   # starred repos only
  python3 query.py --overlap                   # tags appearing in both owned and starred
  python3 query.py --tags agent --owned        # combine filters
  python3 query.py --all                       # show everything (default scope)
"""

import argparse, sys, os
from pathlib import Path

REPO_DIR = Path(__file__).parent.parent
OWNED_DIR = REPO_DIR / 'owned'
STARRED_DIR = REPO_DIR / 'starred'


def parse_frontmatter(content: str) -> dict:
    """Parse YAML-like frontmatter from a .md file. Returns dict of metadata."""
    entry = {}
    if not content.startswith('---'):
        return entry
    try:
        fm_end = content.index('---', 3)
    except ValueError:
        return entry
    fm_text = content[3:fm_end]
    current_list_key = None
    for line in fm_text.split('\n'):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith('- '):
            if current_list_key:
                if current_list_key not in entry:
                    entry[current_list_key] = []
                val = stripped[2:].strip().strip("'\"")
                if val:
                    entry[current_list_key].append(val)
            continue
        current_list_key = None
        if ':' not in stripped:
            continue
        key, val = stripped.split(':', 1)
        key = key.strip()
        val = val.strip()
        if not val:
            current_list_key = key
        elif val.startswith('['):
            items = [v.strip().strip("'\"") for v in val[1:-1].split(',') if v.strip().strip("'\"")]
            entry[key] = items
        else:
            entry[key] = val.strip("'\"")
    return entry


def load_entries(scope: str = 'all') -> list[dict]:
    """Load all repo entries, optionally filtering by scope."""
    entries = []
    for dirname in ['owned', 'starred']:
        if scope == 'owned' and dirname != 'owned':
            continue
        if scope == 'starred' and dirname != 'starred':
            continue
        dir_path = OWNED_DIR if dirname == 'owned' else STARRED_DIR
        if not dir_path.exists():
            continue
        for f in sorted(dir_path.glob('*.md')):
            content = f.read_text(encoding='utf-8', errors='replace')
            entry = parse_frontmatter(content)
            entry['_source'] = dirname
            entry['_filename'] = f.name
            if 'repo' not in entry:
                entry['repo'] = f.stem
            entries.append(entry)
    return entries


def match_tags(entry: dict, tags: list[str], mode: str = 'all') -> bool:
    """Check if entry matches tag filter. mode='all' for AND, mode='any' for OR."""
    entry_tags = [t.lower() for t in entry.get('tags', [])]
    query_tags = [t.strip().lower() for t in tags if t.strip()]
    if not query_tags:
        return True
    if mode == 'any':
        return any(qt in entry_tags for qt in query_tags)
    else:
        return all(qt in entry_tags for qt in query_tags)


def format_table(entries: list[dict]) -> str:
    """Format entries as a markdown table."""
    if not entries:
        return "*No matching repos found.*\n"
    lines = []
    lines.append("| Repo | Type | Language | Stars | Tags | Description |")
    lines.append("|------|------|----------|-------|------|-------------|")
    for e in entries:
        repo = e.get('repo', '?')
        url = e.get('url', '')
        if url:
            repo_link = f"[{repo}]({url})"
        else:
            repo_link = repo
        rtype = e.get('type', '-')
        lang = e.get('language', '-')
        try:
            stars = int(e.get('stars', 0))
            stars_str = f"{stars:,}★"
        except (ValueError, TypeError):
            stars_str = '0★'
        tags = ', '.join(e.get('tags', [])[:5])
        desc = e.get('description', '').strip() or '-'
        if len(desc) > 80:
            desc = desc[:77] + '...'
        lines.append(f"| {repo_link} | {rtype} | {lang} | {stars_str} | {tags} | {desc} |")
    lines.append(f"\n*{len(entries)} repos shown.*")
    return '\n'.join(lines)


def cmd_overlap(entries: list[dict]) -> str:
    """Show tags that appear in both owned and starred repos."""
    owned_tags: dict[str, int] = {}
    starred_tags: dict[str, int] = {}
    for e in entries:
        for t in e.get('tags', []):
            tl = t.lower()
            if e.get('_source') == 'owned':
                owned_tags[tl] = owned_tags.get(tl, 0) + 1
            else:
                starred_tags[tl] = starred_tags.get(tl, 0) + 1

    shared = sorted(set(owned_tags.keys()) & set(starred_tags.keys()))

    lines = []
    lines.append("# Overlapping Tags (Owned ∩ Starred)\n")
    if not shared:
        lines.append("*No shared tags found.*\n")
        return '\n'.join(lines)
    lines.append("| Tag | Owned Count | Starred Count | Total |")
    lines.append("|-----|-------------|---------------|-------|")
    for tag in shared:
        oc = owned_tags.get(tag, 0)
        sc = starred_tags.get(tag, 0)
        lines.append(f"| {tag} | {oc} | {sc} | {oc + sc} |")
    lines.append(f"\n*{len(shared)} overlapping tags.*")
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Query the seans-reporepo catalog by tags, scope, and overlap.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 query.py --tags agent,voice
  python3 query.py --tags agent,voice --any
  python3 query.py --tags llm --owned
  python3 query.py --overlap
  python3 query.py --all
        """
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
    parser.add_argument('--overlap', action='store_true',
                        help='Show tags appearing in both owned and starred')

    args = parser.parse_args()

    # Determine scope
    scope = 'all'
    if args.owned and not args.starred:
        scope = 'owned'
    elif args.starred and not args.owned:
        scope = 'starred'
    elif args.owned and args.starred:
        scope = 'all'

    # Load
    entries = load_entries(scope)

    # Overlap mode
    if args.overlap:
        print(cmd_overlap(entries))
        sys.exit(0)

    # Tag filter
    tags = [t.strip() for t in args.tags.split(',') if t.strip()] if args.tags else []
    mode = 'any' if args.any_mode else 'all'

    if tags:
        entries = [e for e in entries if match_tags(e, tags, mode)]

    # Sort by stars desc, then repo name
    def sort_key(e):
        try:
            return -int(e.get('stars', 0))
        except (ValueError, TypeError):
            return 0
    entries.sort(key=sort_key)

    print(format_table(entries))
    sys.exit(0)


if __name__ == '__main__':
    main()
