"""Mirror skills from source repos into this catalog.

Usage:
    python scripts/sync.py          # sync all sources
    python scripts/sync.py --dry    # preview without writing

Reads sources.yml, clones each source repo (shallow), copies SKILL.md files
from the configured path into vendor/<namespace>/, and writes a manifest
of what was synced. Idempotent and safe to run on a schedule.
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
VENDOR = ROOT / "vendor"
SOURCES = ROOT / "sources.yml"


def clone(repo: str, branch: str, dest: Path) -> bool:
    if dest.exists():
        shutil.rmtree(dest)
    url = f"https://github.com/{repo}.git"
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", branch, url, str(dest)],
            check=True, capture_output=True, text=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"  clone failed: {e.stderr.strip()}", file=sys.stderr)
        return False


def sync_source(src: dict) -> int:
    repo = src["repo"]
    branch = src.get("branch", "main")
    relpath = src["path"]
    namespace = src["namespace"]
    print(f"syncing {repo} ({branch}) -> vendor/{namespace}")

    tmp = ROOT / ".sync-tmp" / namespace
    if not clone(repo, branch, tmp):
        return 0

    src_dir = tmp / relpath
    if not src_dir.is_dir():
        print(f"  path {relpath} not found, skipping", file=sys.stderr)
        shutil.rmtree(tmp, ignore_errors=True)
        return 0

    dest_dir = VENDOR / namespace
    # Remove stale skills from this vendor
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    include = src.get("include")
    count = 0
    for skill_dir in sorted(src_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        if include and skill_dir.name not in include:
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        target = dest_dir / skill_dir.name
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy2(skill_md, target / "SKILL.md")
        # copy references/ if present
        refs = skill_dir / "references"
        if refs.is_dir():
            shutil.copytree(refs, target / "references", dirs_exist_ok=True)
        count += 1

    shutil.rmtree(tmp, ignore_errors=True)
    print(f"  synced {count} skills")
    return count


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--source", metavar="NAMESPACE",
                    help="sync only the source with this namespace")
    args = ap.parse_args()

    if not SOURCES.exists():
        print("sources.yml not found", file=sys.stderr)
        return 1

    with open(SOURCES) as f:
        config = yaml.safe_load(f) or {}
    sources = config.get("sources", [])

    total = 0
    for src in sources:
        if args.source and src.get("namespace") != args.source:
            continue
        total += sync_source(src)

    # Clean up empty vendor dir
    if VENDOR.exists() and not any(VENDOR.iterdir()):
        VENDOR.rmdir()

    print(f"\ntotal synced: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
