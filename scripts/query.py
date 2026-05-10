#!/usr/bin/env python3
"""Query the repo catalog by tags, types, languages, or free text."""
import json, os, sys, glob
from pathlib import Path

CATALOG_DIR = Path(__file__).parent.parent

def load_entries():
    entries = []
    for d in ['owned', 'starred']:
        for f in Path(f'{CATALOG_DIR}/{d}').glob('*.md'):
            content = f.read_text()
            # Parse frontmatter
            if content.startswith('---'):
                fm_end = content.index('---', 3)
                fm_text = content[3:fm_end]
                entry = {}
                for line in fm_text.split('\n'):
                    if ':' in line:
                        key, val = line.split(':', 1)
                        val = val.strip().strip("'\"")
                        if val.startswith('['):
                            val = [v.strip().strip("'\"") for v in val[1:-1].split(',') if v.strip().strip("'\"")]
                        entry[key.strip()] = val
                entries.append(entry)
    return entries

def search(entries, query=None, tag=None, type_=None, language=None, min_stars=None, min_size=None):
    results = entries
    if query:
        results = [e for e in results if query.lower() in json.dumps(e).lower()]
    if tag:
        results = [e for e in results if tag in e.get('tags', [])]
    if type_:
        results = [e for e in results if e.get('type') == type_]
    if language:
        results = [e for e in results if e.get('language', '').lower() == language.lower()]
    if min_stars is not None:
        results = [e for e in results if int(e.get('stars', 0)) >= min_stars]
    if min_size is not None:
        results = [e for e in results if int(e.get('size_kb', 0)) >= min_size]
    return results

def main():
    entries = load_entries()
    
    if len(sys.argv) < 2:
        print("Usage: query.py [tag|type|language|search] <value>")
        print("       query.py --all")
        print("       query.py --stats")
        return
    
    cmd = sys.argv[1]
    if cmd == '--all':
        for e in entries:
            print(f"{e.get('repo', '?')} | {e.get('type', '-')} | {e.get('language', '-')} | {e.get('stars', 0):,}★")
    elif cmd == '--stats':
        types = {}
        langs = {}
        tags = {}
        for e in entries:
            t = e.get('type', 'unknown')
            types[t] = types.get(t, 0) + 1
            l = e.get('language', 'unknown')
            langs[l] = langs.get(l, 0) + 1
            for tag in e.get('tags', []):
                tags[tag] = tags.get(tag, 0) + 1
        print(f"Total repos: {len(entries)}")
        print(f"\nTypes: {dict(sorted(types.items(), key=lambda x: -x[1]))}")
        print(f"\nLanguages: {dict(sorted(langs.items(), key=lambda x: -x[1]))}")
        print(f"\nTop tags: {dict(sorted(tags.items(), key=lambda x: -x[1])[:20])}")
    elif cmd in ['tag', 'type', 'language', 'search']:
        value = sys.argv[2] if len(sys.argv) > 2 else ''
        if cmd == 'tag':
            results = search(entries, tag=value)
        elif cmd == 'type':
            results = search(entries, type_=value)
        elif cmd == 'language':
            results = search(entries, language=value)
        elif cmd == 'search':
            results = search(entries, query=value)
        for e in results:
            print(f"{e.get('repo', '?')} | {e.get('type', '-')} | {e.get('language', '-')} | {e.get('stars', 0):,}★ | {e.get('tags', [])}")
    else:
        print(f"Unknown command: {cmd}")

if __name__ == '__main__':
    main()
