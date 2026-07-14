#!/home/sc/.hermes/venv/bin/python3
"""
skill-curation.py — Multi-source weekly skill curation pipeline.

Sources (Phase 0-1):
  1. skillsmp.com API       — star-sorted, >1000 threshold, no git needed
  2. VoltAgent/awesome-agent-skills       — 27.9K stars, 1000+ skills
  3. VoltAgent/awesome-openclaw-skills    — 5.2K skills (Hermes-compatible)
  4. sickn33/agentic-awesome-skills      — Agentic AI skills
  5. affaan-m/ECC                        — 228K stars, 278 skill dirs
  6. 0xNyk/awesome-hermes-agent          — Existing, kept

Phase 2 (Evaluate): mtime-based staleness for local skills.
Phase 3-4 (Delete + Judge): LLM-driven cron job.

Runs: weekly, Sunday 01:00 UTC.
"""

import json, shutil, subprocess, sys, time, re, urllib.request
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional

HERMES_HOME = Path.home() / ".hermes"
CACHE_DIR   = HERMES_HOME / "skill-selector-cache"
SKILLS_DIR  = HERMES_HOME / "skills"
STATE_DB    = HERMES_HOME / "state.db"
TMP_DIR     = Path("/tmp/skill-selector-swarm")
TMP_DIR.mkdir(exist_ok=True)

NOW    = datetime.now(timezone.utc)
NOW_TS = NOW.timestamp()


# ---------------------------------------------------------------------------
# Sources definition
# ---------------------------------------------------------------------------

REMOTES = [
    # (org, name, stars_threshold, priority)
    # priority: 1=premium (auto-candidate), 2=standard, 3=explore
    ("VoltAgent",        "awesome-agent-skills",      1000, 1),
    ("VoltAgent",        "awesome-openclaw-skills",   1000, 1),
    ("sickn33",          "agentic-awesome-skills",    1000, 1),
    ("affaan-m",         "ECC",                       1000, 1),
    ("0xNyk",            "awesome-hermes-agent",         0, 2),  # keep existing
]

# SkillsMP API — 50 req/day anonymous, 500/day with key
SKILLSMP_BASE = "https://skillsmp.com/api/v1/skills/search"
SKILLSMP_API_KEY = ""  # Optional: set in env SKILLSMP_API_KEY


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def run(cmd, **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True,
                          timeout=kw.pop("timeout", 90), **kw)


def load_metadata():
    fp = CACHE_DIR / "skill_metadata.json"
    return json.loads(fp.read_text()) if fp.exists() else []


def local_skill_names():
    meta = load_metadata()
    return {m["name"] for m in meta
            if m.get("path") and (Path(m["path"]) / "SKILL.md").exists()}



def http_get_raw(url: str, timeout: int = 20) -> Optional[str]:
    """Fetch raw text file content (SKILL.md) without JSON parsing."""
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout), url,
             "-H", "User-Agent: Mozilla/5.0"],
            capture_output=True, text=True, timeout=timeout + 5)
        if r.returncode == 0 and r.stdout:
            return r.stdout
    except Exception:
        pass
    return None

def http_get(url: str, timeout: int = 30) -> Optional[dict]:
    """
    Fetch JSON from URL using curl (known to work with skillsmp.com).
    Falls back to urllib.request if curl is unavailable.
    """
    try:
        cmd = ["curl", "-sL", url, "-H", "User-Agent: Mozilla/5.0"]
        if SKILLSMP_API_KEY:
            cmd += ["-H", f"Authorization: Bearer {SKILLSMP_API_KEY}"]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if r.returncode == 0 and r.stdout.strip():
            return json.loads(r.stdout)
    except Exception:
        pass
    # Fallback: urllib
    req = urllib.request.Request(url, headers={"User-Agent": "HermesAgent/1.0"})
    if SKILLSMP_API_KEY:
        req.add_header("Authorization", f"Bearer {SKILLSMP_API_KEY}")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"    HTTP error {url}: {e}")
        return None


# ---------------------------------------------------------------------------
# Phase 0: SkillsMP API discovery
# ---------------------------------------------------------------------------

def discover_via_skillsmp(min_stars: int = 1000, max_pages: int = 5, local_skills: set = None) -> list[dict]:
    """
    Fetch skills from skillsmp.com API sorted by stars.
    q='a' returns top ~1000 skills regardless of name content.
    q must be non-empty; sorting by stars overrides search relevance.
    Returns list of skill entries with name, description, stars, github_url.
    """
    print("\n=== Phase 0: SkillsMP API ===")
    all_skills = []
    per_page   = 100

    for page in range(1, max_pages + 1):
        # q='a' is a valid non-empty query; sortBy=stars returns the
        # same top-N regardless of the query letter's content
        url = (f"{SKILLSMP_BASE}"
               f"?q=a&sortBy=stars&page={page}&limit={per_page}")
        data = http_get(url)
        if not data:
            break

        skills = data.get("data", {}).get("skills", [])
        if not skills:
            break

        for s in skills:
            stars = s.get("stars", 0)
            if min_stars and stars < min_stars:
                # Results are sorted desc — once we hit below threshold, stop
                print(f"    Stopping at page {page}: stars={stars} < {min_stars}")
                return all_skills

            github_url = s.get("githubUrl", "")
            if not github_url or "github.com" not in github_url:
                continue

            all_skills.append({
                "name":        s.get("name", ""),
                "description": s.get("description", "")[:300],
                "stars":       stars,
                "github_url":  github_url,
                "source":      f"skillsmp/{s.get('author','')}",
                "has_local_file": False,
                "install_priority": 1 if stars >= 10000 else 2,
            })

        pagination = data.get("data", {}).get("pagination", {})
        total      = pagination.get("total", 0)
        has_next   = pagination.get("hasNext", False)
        print(f"    Page {page}/{max_pages}: +{len(skills)} skills "
              f"(total so far: {len(all_skills)}, has_next={has_next})")

        if not has_next:
            break

    local_lower = {n.lower() for n in (local_skills or set())}
    for s in all_skills:
        s["has_local_file"] = s.get("name", "").lower() in local_lower

    print(f"  SkillsMP: {len(all_skills)} candidates "
          f"(min_stars={min_stars}, max_pages={max_pages})")
    return all_skills


# ---------------------------------------------------------------------------
# Phase 1: Git-sync remote repos
# ---------------------------------------------------------------------------

def sync_remote_repos() -> list[Path]:
    """Clone or pull all REMOTES."""
    print("\n=== Phase 1: Git Sync ===")
    synced = []
    for org, name, threshold, priority in REMOTES:
        dest = TMP_DIR / name
        url  = f"https://github.com/{org}/{name}.git"
        print(f"  Syncing {org}/{name}...", end=" ", flush=True)
        if dest.exists():
            r = run(["git", "-C", str(dest), "pull", "--ff-only"], timeout=60)
            ok = r.returncode == 0
            msg = f"pulled (sha={run(['git','-C',str(dest),'log','-1','--format=%H'],timeout=10).stdout.strip()[:8]})" if ok else f"pull failed: {r.stderr[:80]}"
        else:
            r = run(["git", "clone", "--depth", "1", url, str(dest)], timeout=120)
            ok = r.returncode == 0
            msg = "cloned" if ok else f"clone failed: {r.stderr[:80]}"
        print(msg)
        if ok:
            synced.append(dest)
    print(f"  Synced {len(synced)}/{len(REMOTES)} repos")
    return synced


# ---------------------------------------------------------------------------
# Phase 1b: Extract candidates from synced repos
# ---------------------------------------------------------------------------

SKILL_NAME_RE = re.compile(r"\*\*\[([^\]]+)\]|\[([^\]]+)\]")


def extract_readme_skills(src_dir: Path, org: str, name: str, priority: int) -> list[dict]:
    """Parse README.md for skill list entries (VoltAgent/Awesome format)."""
    readme = src_dir / "README.md"
    if not readme.exists():
        return []

    text   = readme.read_text(errors="ignore")
    skills = []
    seen   = set()

    for line in text.split("\n"):
        line = line.strip()
        if not line.startswith("-"):
            continue

        # VoltAgent format: - **[name](url)** — description
        # Awesome format:   - [name](url) — description
        m = re.search(r"\[([^\]]+)\]\((https://github\.com/[^)]+)\)", line)
        if not m:
            continue
        raw_name = m.group(1).strip()
        url      = m.group(2).strip()

        # Strip maturity badges: **[beta]** [name](url)
        name_clean = re.sub(r"\*\*\[[^\]]+\]\([^)]+\)\s*", "", raw_name).strip()
        if not name_clean or name_clean.lower() in seen:
            continue
        seen.add(name_clean.lower())

        # Noise filter
        noise = {"contributing", "license", "discord", "community", "star",
                 "fork", "badge", "documentation", "guide", "readme"}
        if name_clean.lower() in noise:
            continue

        desc = ""
        for delim in (" — ", " - ", " —", " - "):
            if delim in line:
                parts = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1",
                               line.split(delim, 1)[1].strip())
                desc = parts[:280]
                break

        skills.append({
            "name":             name_clean,
            "description":      desc,
            "stars":            0,
            "github_url":       url,
            "source":           f"{org}/{name}",
            "has_local_file":   False,
            "install_priority":  priority,
        })

    return skills


def extract_skill_dirs(src_dir: Path, org: str, name: str, threshold: int, priority: int) -> list[dict]:
    """
    Walk subdirectories looking for SKILL.md files (ECC pattern).
    Returns candidates for each skill directory found.
    """
    skills = []
    seen   = set()
    skills_dir = src_dir / "skills"

    if not skills_dir.exists():
        return skills

    for sk_path in skills_dir.rglob("SKILL.md"):
        content = sk_path.read_text(errors="ignore")
        fm_name, fm_desc = "", ""

        if content.startswith("---"):
            end = content.find("---", 3)
            if end > 0:
                for line in content[3:end].strip().split("\n"):
                    if ":" in line:
                        k, v = line.split(":", 1)
                        k = k.strip()
                        v = v.strip().strip('"').strip("'")
                        if k == "name":
                            fm_name = v
                        elif k == "description":
                            fm_desc = v[:200]

        if not fm_name:
            fm_name = sk_path.parent.name.replace("-", " ").replace("_", " ").title()

        if fm_name.lower() in seen:
            continue
        seen.add(fm_name.lower())

        # Build GitHub URL from path
        rel   = sk_path.parent.relative_to(src_dir)
        gh_url = f"https://github.com/{org}/{name}/tree/main/{rel}"

        skills.append({
            "name":             fm_name,
            "description":      fm_desc or "",
            "stars":            0,
            "github_url":       gh_url,
            "source":           f"{org}/{name}/skills",
            "has_local_file":   True,
            "install_priority":  priority,
        })

    return skills


# ---------------------------------------------------------------------------
# Phase 1c: Manual install (GitHub URL → local SKILL.md)
# ---------------------------------------------------------------------------

def manual_install(github_url: str, skill_name: str) -> Optional[Path]:
    """
    Fetch a skill from GitHub and install to ~/.hermes/skills/.

    Strategy (3 tiers, cheapest first):
      1. Swarm cache  — copy from /tmp/skill-selector-swarm/ (zero API calls)
      2. Contents API  — download subdir files via GitHub REST API (60/hr limit)
      3. Git clone     — shallow clone standalone repo

    Returns Path to installed skill dir on success, None on failure.
    """
    safe = skill_name.lower().replace(" ", "-").replace("_", "-")
    dest_dir = SKILLS_DIR / safe
    if dest_dir.exists():
        return None

    tmp = TMP_DIR / f"install-{safe}"
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True)

    # --- Tier 1: Swarm cache (no API calls) ---
    SWARM_MAP = {
        "VoltAgent/awesome-agent-skills":   "awesome-agent-skills",
        "VoltAgent/awesome-openclaw-skills": "awesome-openclaw-skills",
        "sickn33/agentic-awesome-skills":  "agentic-awesome-skills",
        "affaan-m/ECC":                    "ECC",
        "0xNyk/awesome-hermes-agent":      "awesome-hermes-agent",
    }
    # Parse org_repo and subdir_path from github_url
    _, _, after_tree = github_url.rstrip("/").partition("/tree/")
    if after_tree:
        path_before_tree = github_url[:github_url.index("/tree/")]
        org_repo = "/".join(path_before_tree.rstrip("/").split("/")[-2:])
        parts = after_tree.split("/", 2)
        branch = parts[0]
        subdir_path = "/".join(parts[1:]) if len(parts) > 1 else ""
    else:
        org_repo = "/".join(github_url.rstrip("/").split("/")[-2:])
        subdir_path = ""

    swarm_key = SWARM_MAP.get(org_repo, "")
    if swarm_key and subdir_path:
        swarm_base = TMP_DIR.parent / "skill-selector-swarm" / swarm_key
        # Try original path and normalized (- instead of /) variant
        for candidate in [subdir_path, subdir_path.replace("/", "-")]:
            cached_skill = swarm_base / candidate / "SKILL.md"
            if cached_skill.exists():
                dest_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(cached_skill, dest_dir / "SKILL.md")
                refs_src = cached_skill.parent / "references"
                if refs_src.exists():
                    shutil.copytree(refs_src, dest_dir / "references", dirs_exist_ok=True)
                print(f"    {skill_name}: copied from swarm cache")
                return dest_dir

    # --- Parse for Tier 2/3 ---
    _, _, after_tree2 = github_url.rstrip("/").partition("/tree/")
    if not after_tree2:
        repo_url = github_url.rstrip("/")
        branch, subdir_path = "main", ""
    else:
        path_before_tree = github_url[:github_url.index("/tree/")]
        org_repo = "/".join(path_before_tree.rstrip("/").split("/")[-2:])
        parts = after_tree2.split("/", 2)
        branch = parts[0]
        subdir_path = "/".join(parts[1:]) if len(parts) > 1 else ""
        repo_url = f"https://github.com/{org_repo}"

    # --- Tier 2: Monorepo subdir -> Contents API ---
    if subdir_path:
        api_url = f"https://api.github.com/repos/{org_repo}/contents/{subdir_path}"
        data = http_get(api_url)
        if not data or not isinstance(data, list):
            return None

        files_to_fetch = {}
        for entry in data:
            name = entry.get("name", "")
            if name == "SKILL.md":
                files_to_fetch["SKILL.md"] = entry.get("download_url")
            elif name == "references":
                ref_api = f"https://api.github.com/repos/{org_repo}/contents/{subdir_path}/references"
                ref_data = http_get(ref_api)
                if ref_data and isinstance(ref_data, list):
                    for ref in ref_data:
                        if ref.get("type") == "file":
                            files_to_fetch[f"references/{ref['name']}"] = ref.get("download_url")

        if not files_to_fetch:
            return None

        dest_dir.mkdir(parents=True, exist_ok=True)
        for rel_path, raw_url in files_to_fetch.items():
            text = http_get_raw(raw_url)
            if text is not None:
                dest_path = dest_dir / rel_path
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                with open(dest_path, "w") as f:
                    f.write(text)
        return dest_dir

    # --- Tier 3: Standalone repo -> shallow git clone + rglob ---
    r = run(["git", "clone", "--depth=1", repo_url, str(tmp)], timeout=60)
    if r.returncode != 0:
        return None

    all_md = list(tmp.rglob("SKILL.md"))
    best = next((p for p in all_md
                 if p.parent.name.lower().replace("_","-") == safe), None)
    if not best:
        best = next((p for p in all_md
                     if safe in p.parent.name.lower().replace("_","-")), None)
    if best:
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(best, dest_dir / "SKILL.md")
        copy_refs(best.parent, dest_dir)
        return dest_dir

    return None





# ---------------------------------------------------------------------------
# Sources definition
# ---------------------------------------------------------------------------

REMOTES = [
    # (org, name, stars_threshold, priority)
    # priority: 1=premium (auto-candidate), 2=standard, 3=explore
    ("VoltAgent",        "awesome-agent-skills",      1000, 1),
    ("VoltAgent",        "awesome-openclaw-skills",   1000, 1),
    ("sickn33",          "agentic-awesome-skills",    1000, 1),
    ("affaan-m",         "ECC",                       1000, 1),
    ("0xNyk",            "awesome-hermes-agent",         0, 2),  # keep existing
]

# SkillsMP API — 50 req/day anonymous, 500/day with key
SKILLSMP_BASE = "https://skillsmp.com/api/v1/skills/search"
SKILLSMP_API_KEY = ""  # Optional: set in env SKILLSMP_API_KEY


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def run(cmd, **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True,
                          timeout=kw.pop("timeout", 90), **kw)


def load_metadata():
    fp = CACHE_DIR / "skill_metadata.json"
    return json.loads(fp.read_text()) if fp.exists() else []


def local_skill_names():
    meta = load_metadata()
    return {m["name"] for m in meta
            if m.get("path") and (Path(m["path"]) / "SKILL.md").exists()}



def http_get_raw(url: str, timeout: int = 20) -> Optional[str]:
    """Fetch raw text file content (SKILL.md) without JSON parsing."""
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout), url,
             "-H", "User-Agent: Mozilla/5.0"],
            capture_output=True, text=True, timeout=timeout + 5)
        if r.returncode == 0 and r.stdout:
            return r.stdout
    except Exception:
        pass
    return None

def http_get(url: str, timeout: int = 30) -> Optional[dict]:
    """
    Fetch JSON from URL using curl (known to work with skillsmp.com).
    Falls back to urllib.request if curl is unavailable.
    """
    try:
        cmd = ["curl", "-sL", url, "-H", "User-Agent: Mozilla/5.0"]
        if SKILLSMP_API_KEY:
            cmd += ["-H", f"Authorization: Bearer {SKILLSMP_API_KEY}"]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if r.returncode == 0 and r.stdout.strip():
            return json.loads(r.stdout)
    except Exception:
        pass
    # Fallback: urllib
    req = urllib.request.Request(url, headers={"User-Agent": "HermesAgent/1.0"})
    if SKILLSMP_API_KEY:
        req.add_header("Authorization", f"Bearer {SKILLSMP_API_KEY}")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"    HTTP error {url}: {e}")
        return None


# ---------------------------------------------------------------------------
# Phase 0: SkillsMP API discovery
# ---------------------------------------------------------------------------

def discover_via_skillsmp(min_stars: int = 1000, max_pages: int = 5, local_skills: set = None) -> list[dict]:
    """
    Fetch skills from skillsmp.com API sorted by stars.
    q='a' returns top ~1000 skills regardless of name content.
    q must be non-empty; sorting by stars overrides search relevance.
    Returns list of skill entries with name, description, stars, github_url.
    """
    print("\n=== Phase 0: SkillsMP API ===")
    all_skills = []
    per_page   = 100

    for page in range(1, max_pages + 1):
        # q='a' is a valid non-empty query; sortBy=stars returns the
        # same top-N regardless of the query letter's content
        url = (f"{SKILLSMP_BASE}"
               f"?q=a&sortBy=stars&page={page}&limit={per_page}")
        data = http_get(url)
        if not data:
            break

        skills = data.get("data", {}).get("skills", [])
        if not skills:
            break

        for s in skills:
            stars = s.get("stars", 0)
            if min_stars and stars < min_stars:
                # Results are sorted desc — once we hit below threshold, stop
                print(f"    Stopping at page {page}: stars={stars} < {min_stars}")
                return all_skills

            github_url = s.get("githubUrl", "")
            if not github_url or "github.com" not in github_url:
                continue

            all_skills.append({
                "name":        s.get("name", ""),
                "description": s.get("description", "")[:300],
                "stars":       stars,
                "github_url":  github_url,
                "source":      f"skillsmp/{s.get('author','')}",
                "has_local_file": False,
                "install_priority": 1 if stars >= 10000 else 2,
            })

        pagination = data.get("data", {}).get("pagination", {})
        total      = pagination.get("total", 0)
        has_next   = pagination.get("hasNext", False)
        print(f"    Page {page}/{max_pages}: +{len(skills)} skills "
              f"(total so far: {len(all_skills)}, has_next={has_next})")

        if not has_next:
            break

    local_lower = {n.lower() for n in (local_skills or set())}
    for s in all_skills:
        s["has_local_file"] = s.get("name", "").lower() in local_lower

    print(f"  SkillsMP: {len(all_skills)} candidates "
          f"(min_stars={min_stars}, max_pages={max_pages})")
    return all_skills


# ---------------------------------------------------------------------------
# Phase 1: Git-sync remote repos
# ---------------------------------------------------------------------------

def sync_remote_repos() -> list[Path]:
    """Clone or pull all REMOTES."""
    print("\n=== Phase 1: Git Sync ===")
    synced = []
    for org, name, threshold, priority in REMOTES:
        dest = TMP_DIR / name
        url  = f"https://github.com/{org}/{name}.git"
        print(f"  Syncing {org}/{name}...", end=" ", flush=True)
        if dest.exists():
            r = run(["git", "-C", str(dest), "pull", "--ff-only"], timeout=60)
            ok = r.returncode == 0
            msg = f"pulled (sha={run(['git','-C',str(dest),'log','-1','--format=%H'],timeout=10).stdout.strip()[:8]})" if ok else f"pull failed: {r.stderr[:80]}"
        else:
            r = run(["git", "clone", "--depth", "1", url, str(dest)], timeout=120)
            ok = r.returncode == 0
            msg = "cloned" if ok else f"clone failed: {r.stderr[:80]}"
        print(msg)
        if ok:
            synced.append(dest)
    print(f"  Synced {len(synced)}/{len(REMOTES)} repos")
    return synced


# ---------------------------------------------------------------------------
# Phase 1b: Extract candidates from synced repos
# ---------------------------------------------------------------------------

SKILL_NAME_RE = re.compile(r"\*\*\[([^\]]+)\]|\[([^\]]+)\]")


def extract_readme_skills(src_dir: Path, org: str, name: str, priority: int) -> list[dict]:
    """Parse README.md for skill list entries (VoltAgent/Awesome format)."""
    readme = src_dir / "README.md"
    if not readme.exists():
        return []

    text   = readme.read_text(errors="ignore")
    skills = []
    seen   = set()

    for line in text.split("\n"):
        line = line.strip()
        if not line.startswith("-"):
            continue

        # VoltAgent format: - **[name](url)** — description
        # Awesome format:   - [name](url) — description
        m = re.search(r"\[([^\]]+)\]\((https://github\.com/[^)]+)\)", line)
        if not m:
            continue
        raw_name = m.group(1).strip()
        url      = m.group(2).strip()

        # Strip maturity badges: **[beta]** [name](url)
        name_clean = re.sub(r"\*\*\[[^\]]+\]\([^)]+\)\s*", "", raw_name).strip()
        if not name_clean or name_clean.lower() in seen:
            continue
        seen.add(name_clean.lower())

        # Noise filter
        noise = {"contributing", "license", "discord", "community", "star",
                 "fork", "badge", "documentation", "guide", "readme"}
        if name_clean.lower() in noise:
            continue

        desc = ""
        for delim in (" — ", " - ", " —", " - "):
            if delim in line:
                parts = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1",
                               line.split(delim, 1)[1].strip())
                desc = parts[:280]
                break

        skills.append({
            "name":             name_clean,
            "description":      desc,
            "stars":            0,
            "github_url":       url,
            "source":           f"{org}/{name}",
            "has_local_file":   False,
            "install_priority":  priority,
        })

    return skills


def extract_skill_dirs(src_dir: Path, org: str, name: str, threshold: int, priority: int) -> list[dict]:
    """
    Walk subdirectories looking for SKILL.md files (ECC pattern).
    Returns candidates for each skill directory found.
    """
    skills = []
    seen   = set()
    skills_dir = src_dir / "skills"

    if not skills_dir.exists():
        return skills

    for sk_path in skills_dir.rglob("SKILL.md"):
        content = sk_path.read_text(errors="ignore")
        fm_name, fm_desc = "", ""

        if content.startswith("---"):
            end = content.find("---", 3)
            if end > 0:
                for line in content[3:end].strip().split("\n"):
                    if ":" in line:
                        k, v = line.split(":", 1)
                        k = k.strip()
                        v = v.strip().strip('"').strip("'")
                        if k == "name":
                            fm_name = v
                        elif k == "description":
                            fm_desc = v[:200]

        if not fm_name:
            fm_name = sk_path.parent.name.replace("-", " ").replace("_", " ").title()

        if fm_name.lower() in seen:
            continue
        seen.add(fm_name.lower())

        # Build GitHub URL from path
        rel   = sk_path.parent.relative_to(src_dir)
        gh_url = f"https://github.com/{org}/{name}/tree/main/{rel}"

        skills.append({
            "name":             fm_name,
            "description":      fm_desc or "",
            "stars":            0,
            "github_url":       gh_url,
            "source":           f"{org}/{name}/skills",
            "has_local_file":   True,
            "install_priority":  priority,
        })

    return skills


# ---------------------------------------------------------------------------
# Phase 1c: Manual install (GitHub URL → local SKILL.md)
# ---------------------------------------------------------------------------

def manual_install(github_url: str, skill_name: str) -> Optional[Path]:
    """
    Fetch a skill from GitHub and install to ~/.hermes/skills/.

    Strategy:
      - Subdir in monorepo  -> GitHub Contents API (no git clone needed)
      - Standalone repo     -> shallow git clone + rglob SKILL.md

    Returns Path to installed skill dir on success, None on failure.
    """
    safe = skill_name.lower().replace(" ", "-").replace("_", "-")
    dest_dir = SKILLS_DIR / safe
    if dest_dir.exists():
        return None

    tmp = TMP_DIR / f"install-{safe}"
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True)

    # Parse GitHub URL
    # Format: https://github.com/org/repo/tree/branch/path/to/dir
    #      or https://github.com/org/repo
    _, _, after_tree = github_url.rstrip("/").partition("/tree/")
    if not after_tree:
        # Plain repo URL
        repo_url = github_url.rstrip("/")
        branch, subdir_path = "main", ""
    else:
        # Extract org/repo from the full URL
        # github_url = https://github.com/org/repo/tree/branch/...
        # We need to strip the https://github.com/ prefix and split org/repo
        path_before_tree = github_url[:github_url.index("/tree/")]
        # path_before_tree = https://github.com/org/repo
        org_repo = "/".join(path_before_tree.rstrip("/").split("/")[-2:])
        # Now: org_repo = org/repo (e.g. openclaw/openclaw)
        parts = after_tree.split("/", 2)
        branch = parts[0]
        subdir_path = "/".join(parts[1:]) if len(parts) > 1 else ""
        repo_url = f"https://github.com/{org_repo}"

    # ------------------------------------------------------------------
    # Strategy 1: Monorepo subdir -> Contents API (fast, no full clone)
    # ------------------------------------------------------------------
    if subdir_path:
        api_url = f"https://api.github.com/repos/{org_repo}/contents/{subdir_path}"
        data = http_get(api_url)
        if not data or not isinstance(data, list):
            return None

        files_to_fetch = {}
        for entry in data:
            name = entry.get("name", "")
            if name == "SKILL.md":
                files_to_fetch["SKILL.md"] = entry.get("download_url")
            elif name == "references":
                # Recursively get references dir
                ref_api = f"https://api.github.com/repos/{org_repo}/contents/{subdir_path}/references"
                ref_data = http_get(ref_api)
                if ref_data and isinstance(ref_data, list):
                    for ref in ref_data:
                        if ref.get("type") == "file":
                            files_to_fetch[f"references/{ref['name']}"] = ref.get("download_url")

        if not files_to_fetch:
            return None

        dest_dir.mkdir(parents=True, exist_ok=True)
        for rel_path, raw_url in files_to_fetch.items():
            text = http_get_raw(raw_url)
            if text is not None:
                dest_path = dest_dir / rel_path
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                with open(dest_path, "w") as f:
                    f.write(text)
        return dest_dir

    # ------------------------------------------------------------------
    # Strategy 2: Standalone repo -> shallow git clone + rglob
    # ------------------------------------------------------------------
    r = run(["git", "clone", "--depth=1", repo_url, str(tmp)], timeout=60)
    if r.returncode != 0:
        return None

    all_md = list(tmp.rglob("SKILL.md"))
    best = next((p for p in all_md
                 if p.parent.name.lower().replace("_","-") == safe), None)
    if not best:
        best = next((p for p in all_md
                     if safe in p.parent.name.lower().replace("_","-")), None)
    if best:
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(best, dest_dir / "SKILL.md")
        copy_refs(best.parent, dest_dir)
        return dest_dir

    return None



# ---------------------------------------------------------------------------
# Phase 2: Evaluate local skills staleness
# ---------------------------------------------------------------------------

def evaluate_skills(cron_skills: set) -> list[dict]:
    meta = load_metadata()
    usage = []
    for m in meta:
        path = m.get("path", "")
        name = m.get("name", "")
        if not path:
            continue
        sk_md = Path(path) / "SKILL.md"
        if not sk_md.exists():
            continue
        mtime = sk_md.stat().st_mtime
        days  = int((NOW_TS - mtime) / 86400)
        usage.append({
            "name": name,
            "days_since_modified": days,
            "cron_protected": name in cron_skills,
            "stale": days > 60,
        })
    return usage


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()
    print(f"[skill-curation] {NOW.isoformat()}")
    print(f"  Sources: {[r[1] for r in REMOTES]}")
    print(f"  SkillsMP min_stars=1000, max_pages=5")

    cron_jobs  = json.loads((HERMES_HOME / "cron" / "jobs.json").read_text())
    cron_skills = {j for job in cron_jobs.get("jobs", [])
                   for j in job.get("skills", [])}

    local = local_skill_names()
    # Actual filesystem count (not metadata cache) for display
    fs_count = len({"-".join(f.parent.relative_to(SKILLS_DIR).parts).lower().replace(" ","-")
                   for f in SKILLS_DIR.rglob("SKILL.md")})
    print(f"  Local skills: {fs_count} (~{len(local)} metadata)")

    output = {
        "timestamp":         NOW.isoformat(),
        "skillsmp_candidates": [],
        "discovered":        [],
        "installed":         [],
        "delete_candidates": [],
        "stale_candidates":  [],
    }

    # --- Phase 0: SkillsMP API ---
    skillsmp_skills = discover_via_skillsmp(min_stars=1000, max_pages=5, local_skills=local)
    output["skillsmp_candidates"] = skillsmp_skills

    # --- Phase 1: Git sync ---
    synced = sync_remote_repos()

    # --- Phase 1b: Extract from synced repos ---
    all_candidates = []
    for repo_dir in synced:
        org     = repo_dir.name.split("_")[0]  # rough
        name    = repo_dir.name
        # find matching REMOTE entry
        matching = [r for r in REMOTES if name in r[1] or r[1] in name]
        if matching:
            _, _, threshold, priority = matching[0]
        else:
            threshold, priority = 0, 3

        # Try README extraction first
        skills_from_readme = extract_readme_skills(repo_dir, org, name, priority)
        print(f"  {repo_dir.name}: {len(skills_from_readme)} from README")

        # Try skill-dir extraction (ECC pattern)
        skills_from_dirs  = extract_skill_dirs(repo_dir, org, name, threshold, priority)
        if skills_from_dirs:
            print(f"  {repo_dir.name}: {len(skills_from_dirs)} from skills/ dirs")

        repo_candidates = skills_from_readme + skills_from_dirs

        new = [s for s in repo_candidates
               if s["name"].lower() not in {n.lower() for n in local}]
        print(f"    -> {len(new)} new (of {len(repo_candidates)} total)")
        all_candidates.extend(new)

    # Merge skillsmp results (dedupe by name)
    seen_names = {s["name"].lower() for s in all_candidates}
    for s in skillsmp_skills:
        if s["name"].lower() not in seen_names:
            all_candidates.append(s)
            seen_names.add(s["name"].lower())

    print(f"\n  Total candidates: {len(all_candidates)}")
    output["discovered"] = all_candidates[:100]  # cap for output

    # --- Phase 1d: Bulk copy from swarm cache (no API calls, no limit) ---
    print("\n=== Phase 1d: Bulk sync from swarm cache ===")
    # Swarm dirs already extracted (7,042 SKILL.md files across 5 repos)
    # Use org-prefixed names to avoid collisions — stores distinct skills
    # even when multiple repos have the same skill name (e.g. "code-review")
    SWARM_MAP = {
        "VoltAgent":            "awesome-agent-skills",
        "VoltAgent":            "awesome-openclaw-skills",  # noqa: E501
        "sickn33":              "agentic-awesome-skills",
        "affaan-m":             "ECC",
        "0xNyk":                "awesome-hermes-agent",
    }
    swarm_base = TMP_DIR.parent / "skill-selector-swarm"
    local_on_disk = {n.lower() for n in local}
    bulk_installed = []

    for org, swarm_subdir in SWARM_MAP.items():
        swarm_path = swarm_base / swarm_subdir
        if not swarm_path.exists():
            print(f"  [{org}] {swarm_subdir}: not found, skipping")
            continue
        count = 0
        for skill_md in swarm_path.rglob("SKILL.md"):
            skill_dir = skill_md.parent
            # Org-prefixed slug: "org-skillname" to avoid collision deduplication
            base_slug = skill_dir.name.lower().replace(" ", "-").replace("_", "-")
            safe = f"{org.lower()}-{base_slug}"
            if safe in local_on_disk:
                continue
            # Also skip if unprefixed name already on disk (don't double-store)
            if base_slug in local_on_disk:
                local_on_disk.add(safe)  # mark prefixed variant too
                continue
            dest = SKILLS_DIR / safe
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copy2(skill_md, dest / "SKILL.md")
            refs_src = skill_dir / "references"
            if refs_src.exists():
                shutil.copytree(refs_src, dest / "references", dirs_exist_ok=True)
            local_on_disk.add(safe)
            bulk_installed.append(safe)
            count += 1
        print(f"  [{org}/{swarm_subdir}] +{count} skills")

    total_on_disk = len({f.parent.name.lower() for f in SKILLS_DIR.rglob('SKILL.md')})
    print(f"  Bulk synced {len(bulk_installed)} skills from swarm cache")
    print(f"  Total on disk after sync: {total_on_disk}")

    # --- Phase 1c: API-based install for remaining candidates (SkillsMP + uncached git) ---
    print("\n=== Phase 1c: Install remaining via API (top priority) ===")
    # Combine: SkillsMP + Git candidates for install consideration
    install_pool = skillsmp_skills + all_candidates
    # Include bulk-installed skills in local set to avoid re-installing
    bulk_names_lower = {n.lower() for n in bulk_installed}
    local_lower = {n.lower() for n in local} | bulk_names_lower
    install_candidates = sorted(
        [s for s in install_pool
         if not s.get("has_local_file") and s.get("github_url")
         and s["name"].lower() not in local_lower],
        key=lambda x: (x.get("install_priority", 99), -(x.get("stars", 0)))
    )[:50]

    installed = []
    for skill in install_candidates:
        name, url = skill["name"], skill["github_url"]
        print(f"  {name} from {url}...", end=" ", flush=True)
        result = manual_install(url, name)
        if result:
            print(f"installed -> {result}")
            installed.append({"name": name, "path": str(result), "stars": skill.get("stars", 0)})
            local.add(name)
        else:
            print("failed/skipped")

    print(f"  Installed: {len(installed)}")
    output["installed"] = installed

    # --- Phase 2: Evaluate ---
    print("\n=== Phase 2: Evaluate ===")
    usage     = evaluate_skills(cron_skills)
    del_cand  = [u for u in usage if u["stale"] and not u["cron_protected"]]
    stale_prot = [u for u in usage if u["stale"] and u["cron_protected"]]
    print(f"  Evaluated {len(usage)} local skills")
    print(f"  Delete candidates: {len(del_cand)}")
    print(f"  Stale but protected: {len(stale_prot)}")
    output["delete_candidates"] = [
        {"name": d["name"], "reason": f"stale {d['days_since_modified']}d"}
        for d in del_cand]
    output["stale_candidates"] = [
        {"name": s["name"], "reason": f"stale {s['days_since_modified']}d"}
        for s in stale_prot]

    # Write full output
    out_fp = Path("/tmp/skill-curation-output.json")
    out_fp.write_text(json.dumps(output, indent=2))

    elapsed = time.time() - t0
    print(f"\n=== Summary ({elapsed:.1f}s) ===")
    print(f"  SkillsMP candidates: {len(skillsmp_skills)}")
    print(f"  Git candidates: {len(all_candidates) - len(skillsmp_skills)}")
    print(f"  Discovered total: {len(all_candidates)} | Installed: {len(installed)}")
    print(f"  Delete: {len(del_cand)} | Stale protected: {len(stale_prot)}")
    print(f"  Output: {out_fp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
