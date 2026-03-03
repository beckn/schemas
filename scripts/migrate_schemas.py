#!/usr/bin/env python3
"""
migrate_schemas.py
──────────────────
Migrates domain schemas (mobility, logistics, local-retail) into core_schema/schema/
with flat structure, collision detection, interactive renaming, and x-tags injection.

Usage
─────
  # Scan only — detect collisions, write resolutions template (no changes made):
  python3 scripts/migrate_schemas.py --scan

  # Interactive — prompt for each collision, then execute:
  python3 scripts/migrate_schemas.py

  # Dry run — show full migration plan without making any changes:
  python3 scripts/migrate_schemas.py --dry-run [--resolutions FILE]

  # Non-interactive with pre-defined resolutions file:
  python3 scripts/migrate_schemas.py --resolutions scripts/migration-resolutions.json

All modes write a migration-log.json upon completion or scan.
"""

from __future__ import annotations
import argparse
import copy
import json
import os
import re
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


# ─── Source definitions ───────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).resolve().parent
CORE_SCHEMA_ROOT = SCRIPT_DIR.parent  # core_schema/
SCHEMA_DIR = CORE_SCHEMA_ROOT / "schema"

# Paths relative to spec_work/ — adapt if your workspace root differs
SPEC_WORK = CORE_SCHEMA_ROOT.parent

SOURCES = [
    {
        "id": "mobility",
        "path": SPEC_WORK / "mobility" / "schema",
        "tags": ["mobility"],
    },
    {
        "id": "logistics",
        "path": SPEC_WORK / "logistics" / "schema",
        "tags": ["logistics"],
    },
    {
        "id": "retail",
        "path": SPEC_WORK / "local-retail" / "schema",
        "tags": ["retail"],
    },
]

# Files/folders in schema directories that are NOT schema definitions
NON_SCHEMA_ITEMS = {"README.md", "context.jsonld", "vocab.jsonld", "README"}

BECKN_IO = "https://schema.beckn.io/"


# ─── Schema detection helpers ─────────────────────────────────────────────────

def is_schema_folder(path: Path) -> bool:
    """Return True if path is a schema folder (contains at least one v*/attributes.yaml)."""
    if not path.is_dir():
        return False
    for child in path.iterdir():
        if child.is_dir():
            attrs = child / "attributes.yaml"
            if attrs.exists():
                return True
    return False


def get_schema_versions(source_schema_path: Path) -> list[str]:
    """Return list of version folder names inside a schema folder."""
    return [
        d.name for d in sorted(source_schema_path.iterdir())
        if d.is_dir() and (d / "attributes.yaml").exists()
    ]


def discover_schemas(source_path: Path) -> list[str]:
    """Return sorted list of schema folder names in a source schema directory."""
    if not source_path.exists():
        print(f"  WARNING: source path does not exist: {source_path}", file=sys.stderr)
        return []
    return sorted(
        d.name for d in source_path.iterdir()
        if d.name not in NON_SCHEMA_ITEMS and is_schema_folder(source_path / d.name)
    )


# ─── $id and x-tags manipulation ─────────────────────────────────────────────

def load_yaml_file(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def dump_yaml_file(path: Path, doc: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(doc, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=100)


def update_attributes_yaml(
    attrs_path: Path,
    new_name: str,
    version: str,
    tags: list[str],
) -> None:
    """
    Update a copied attributes.yaml:
    - Set $id to https://schema.beckn.io/{new_name}/{version}
    - Add or merge x-tags
    """
    doc = load_yaml_file(attrs_path)

    # Update $id
    doc["$id"] = f"{BECKN_IO}{new_name}/{version}"

    # Update title if it matches the old folder name (best-effort)
    old_title = doc.get("title", "")
    if old_title and old_title != new_name:
        doc["title"] = new_name

    # Add/merge x-tags
    existing_tags = doc.get("x-tags", [])
    merged = list(dict.fromkeys(existing_tags + tags))  # deduplicated, order-preserving
    doc["x-tags"] = merged

    dump_yaml_file(attrs_path, doc)


# ─── Core schema list for collision detection ─────────────────────────────────

def get_existing_schema_names() -> set[str]:
    """Return set of all schema folder names currently in core_schema/schema/."""
    return {
        d.name for d in SCHEMA_DIR.iterdir()
        if d.name not in NON_SCHEMA_ITEMS and d.is_dir()
    }


# ─── Migration planning ───────────────────────────────────────────────────────

class MigrationPlan:
    """Accumulates planned copy operations, checking for collisions."""

    def __init__(self, existing: set[str]):
        self.existing = set(existing)  # all names taken (core + already planned)
        self.operations: list[dict] = []  # {source_id, from_name, to_name, from_path, tags, action}
        self.skipped: list[dict] = []

    def plan_copy(self, source_id: str, from_name: str, from_path: Path, tags: list[str], to_name: str) -> None:
        """Record a copy operation (from_name → to_name)."""
        self.operations.append({
            "source_id": source_id,
            "from_name": from_name,
            "to_name": to_name,
            "from_path": str(from_path),
            "tags": tags,
            "action": "copy" if from_name == to_name else "copy+rename",
        })
        self.existing.add(to_name)  # reserve the name

    def plan_skip(self, source_id: str, from_name: str, from_path: Path, reason: str) -> None:
        """Record a skip decision."""
        self.skipped.append({
            "source_id": source_id,
            "from_name": from_name,
            "from_path": str(from_path),
            "reason": reason,
        })

    def is_taken(self, name: str) -> bool:
        return name in self.existing


# ─── Resolution loading ───────────────────────────────────────────────────────

def load_resolutions(path: str) -> dict[str, dict]:
    """
    Load a resolutions JSON file.
    Returns a dict keyed by "{source_id}:{from_name}" → {"action": "rename"/"skip", "new_name": ...}
    """
    with open(path, "r") as f:
        data = json.load(f)
    result = {}
    for r in data.get("resolutions", []):
        key = f"{r['source']}:{r['folder']}"
        result[key] = r
    return result


# ─── Interactive prompt ───────────────────────────────────────────────────────

def prompt_collision(
    source_id: str,
    from_name: str,
    conflict_with: str,
    plan: MigrationPlan,
) -> tuple[str, str]:
    """
    Prompt the user for a collision resolution.
    Returns ("rename", new_name) or ("skip", "").
    """
    print(f"\n  ⚠️  COLLISION: '{from_name}' already exists (conflict with: {conflict_with})")
    print(f"     Source: {source_id}")
    print(f"     Options: enter a new name, 's' to skip")
    while True:
        try:
            answer = input(f"     New name for '{from_name}' [{source_id}] (or 's' to skip): ").strip()
        except EOFError:
            print("\n  (EOF — skipping)", file=sys.stderr)
            return "skip", ""
        if answer.lower() == "s":
            return "skip", ""
        if answer and re.match(r'^[A-Za-z][A-Za-z0-9_]*$', answer):
            if plan.is_taken(answer):
                print(f"     Name '{answer}' is also taken. Try another.")
                continue
            return "rename", answer
        print("     Invalid name. Use CamelCase or PascalCase, no spaces.")


# ─── Scan phase ───────────────────────────────────────────────────────────────

def scan_and_plan(resolutions: dict[str, dict] | None, interactive: bool) -> MigrationPlan:
    """
    Scan all sources, detect collisions, build a migration plan.
    If resolutions is provided: use it. If interactive: prompt. Else: abort on collision.
    """
    existing = get_existing_schema_names()
    plan = MigrationPlan(existing)

    for source in SOURCES:
        source_id = source["id"]
        source_path = source["path"]
        tags = source["tags"]

        schemas = discover_schemas(source_path)
        print(f"\n  Source: {source_id} ({source_path})")
        print(f"  Schemas found: {len(schemas)}")

        for name in schemas:
            from_path = source_path / name
            res_key = f"{source_id}:{name}"

            if not plan.is_taken(name):
                # No collision — plan a straight copy
                plan.plan_copy(source_id, name, from_path, tags, to_name=name)
            else:
                # Collision!
                conflict_desc = "core" if name in existing else "another source"

                if resolutions and res_key in resolutions:
                    res = resolutions[res_key]
                    action = res.get("action", "skip")
                    if action == "skip":
                        plan.plan_skip(source_id, name, from_path, reason="pre-defined skip")
                    elif action == "rename":
                        new_name = res.get("new_name", "")
                        if not new_name:
                            plan.plan_skip(source_id, name, from_path, reason="empty new_name in resolutions")
                        elif plan.is_taken(new_name):
                            print(f"  ERROR: Resolution new_name '{new_name}' is also taken for {res_key}", file=sys.stderr)
                            sys.exit(1)
                        else:
                            plan.plan_copy(source_id, name, from_path, tags, to_name=new_name)
                    elif action == "overwrite":
                        plan.plan_copy(source_id, name, from_path, tags, to_name=name)
                elif interactive:
                    action, new_name = prompt_collision(source_id, name, conflict_desc, plan)
                    if action == "skip":
                        plan.plan_skip(source_id, name, from_path, reason="user skip")
                    else:
                        plan.plan_copy(source_id, name, from_path, tags, to_name=new_name)
                else:
                    print(f"  COLLISION: {source_id}:{name} conflicts with {conflict_desc}. "
                          f"Use --resolutions or run interactively.", file=sys.stderr)
                    sys.exit(1)

    return plan


# ─── Execute phase ────────────────────────────────────────────────────────────

def execute_plan(plan: MigrationPlan, dry_run: bool) -> dict:
    """Execute the migration plan. Returns a migration log dict."""
    log = {
        "operations": [],
        "skipped": plan.skipped,
        "summary": {},
    }

    for op in plan.operations:
        from_path = Path(op["from_path"])
        to_name = op["to_name"]
        from_name = op["from_name"]
        source_id = op["source_id"]
        tags = op["tags"]
        target_path = SCHEMA_DIR / to_name

        versions = get_schema_versions(from_path)

        action_desc = f"{source_id}:{from_name}"
        if from_name != to_name:
            action_desc += f" → {to_name}"

        if dry_run:
            print(f"  [DRY] copy  {action_desc}  (versions: {', '.join(versions)})")
            log["operations"].append({**op, "status": "dry_run", "versions": versions})
            continue

        try:
            if target_path.exists():
                # Only overwrite if this was an explicit overwrite decision
                shutil.rmtree(target_path)

            shutil.copytree(str(from_path), str(target_path))

            # Update attributes.yaml in each version
            for version in versions:
                attrs = target_path / version / "attributes.yaml"
                if attrs.exists():
                    update_attributes_yaml(attrs, to_name, version, tags)

            print(f"  ✓  copied  {action_desc}  [{', '.join(tags)}]")
            log["operations"].append({**op, "status": "ok", "versions": versions})

        except Exception as exc:
            print(f"  ✗  FAILED  {action_desc}: {exc}", file=sys.stderr)
            log["operations"].append({**op, "status": "error", "error": str(exc)})

    # Add x-tags to existing CORE schemas too (tag them as 'common')
    if not dry_run:
        print("\n  Tagging existing core schemas with x-tags: [common] ...")
        tagged = 0
        for schema_dir in sorted(SCHEMA_DIR.iterdir()):
            if schema_dir.name in NON_SCHEMA_ITEMS or not schema_dir.is_dir():
                continue
            # Check if this schema was NOT just migrated
            migrated_names = {op["to_name"] for op in plan.operations}
            if schema_dir.name in migrated_names:
                continue  # Already got its domain tags
            # Apply 'common' tag
            for version_dir in schema_dir.iterdir():
                if version_dir.is_dir():
                    attrs = version_dir / "attributes.yaml"
                    if attrs.exists():
                        try:
                            doc = load_yaml_file(attrs)
                            existing_tags = doc.get("x-tags", [])
                            if "common" not in existing_tags:
                                doc["x-tags"] = ["common"] + existing_tags
                                dump_yaml_file(attrs, doc)
                                tagged += 1
                        except Exception as exc:
                            print(f"    WARNING: could not tag {attrs}: {exc}", file=sys.stderr)
        print(f"  ✓  Tagged {tagged} core schema files with x-tags: [common]")

    # Summary
    ok = sum(1 for op in log["operations"] if op.get("status") == "ok")
    skipped = len(plan.skipped)
    errors = sum(1 for op in log["operations"] if op.get("status") == "error")
    log["summary"] = {"copied": ok, "skipped": skipped, "errors": errors}

    return log


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Migrate domain schemas into core_schema with collision detection",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--scan", action="store_true",
                        help="Scan for collisions only; write resolutions template; no changes")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show migration plan without making any changes")
    parser.add_argument("--resolutions", metavar="FILE",
                        help="Path to resolutions JSON file (non-interactive mode)")
    args = parser.parse_args()

    print("Beckn Domain Schema Migration")
    print("=" * 50)
    print(f"  Target: {SCHEMA_DIR}")
    print()

    # Validate sources exist
    for s in SOURCES:
        if not s["path"].exists():
            print(f"  WARNING: Source not found: {s['path']}", file=sys.stderr)

    # Load resolutions if provided
    resolutions = None
    if args.resolutions:
        print(f"  Loading resolutions from: {args.resolutions}")
        resolutions = load_resolutions(args.resolutions)
        print(f"  {len(resolutions)} resolutions loaded")
        print()

    # ── SCAN mode ──────────────────────────────────────────────────────────────
    if args.scan:
        print("Scanning for collisions ...\n")

        # Build collision list and resolutions template without executing anything
        all_names = get_existing_schema_names()
        planned_names: set[str] = set(all_names)
        template: dict = {"resolutions": []}
        collisions = 0

        for source in SOURCES:
            source_schemas = discover_schemas(source["path"])
            print(f"  Source: {source['id']} — {len(source_schemas)} schemas")
            for name in source_schemas:
                if name in planned_names:
                    conflict = "core" if name in all_names else "another source"
                    suggested = f"{source['id'].capitalize()}{name}"
                    template["resolutions"].append({
                        "source": source["id"],
                        "folder": name,
                        "action": "rename",      # options: rename / skip / overwrite
                        "new_name": suggested,   # edit to your preferred name
                        "_conflict_with": conflict,
                        "_suggested": suggested,
                    })
                    print(f"    ⚠ COLLISION: {name} (vs {conflict}) → suggested: {suggested}")
                    collisions += 1
                else:
                    planned_names.add(name)

        out_path = CORE_SCHEMA_ROOT / "scripts" / "migration-resolutions.json"
        with open(out_path, "w") as f:
            json.dump(template, f, indent=2)
        print(f"\n✓ Resolutions template → {out_path}")
        print(f"  {collisions} collisions detected")
        print(f"\n  Edit the file to set preferred names, then run:")
        print(f"  python3 scripts/migrate_schemas.py --resolutions scripts/migration-resolutions.json")
        return

    # ── PLAN phase ─────────────────────────────────────────────────────────────
    interactive = (resolutions is None) and not args.dry_run
    if interactive:
        print("Running in INTERACTIVE mode. You will be prompted for each collision.\n")
    elif resolutions:
        print("Running in NON-INTERACTIVE mode using resolutions file.\n")

    print("Planning migration ...")
    plan = scan_and_plan(resolutions=resolutions, interactive=interactive)

    # Summary of plan
    print(f"\nMigration plan:")
    print(f"  To copy:  {len(plan.operations)}")
    print(f"  To skip:  {len(plan.skipped)}")
    for op in plan.operations:
        marker = "→" if op["from_name"] != op["to_name"] else " "
        print(f"    [{op['source_id']:10}] {op['from_name']:35} {marker} {op['to_name']}")
    if plan.skipped:
        print("  Skipped:")
        for sk in plan.skipped:
            print(f"    [{sk['source_id']:10}] {sk['from_name']} ({sk['reason']})")

    if args.dry_run:
        print(f"\n[DRY RUN] No files will be written.\n")
        execute_plan(plan, dry_run=True)
        return

    # ── Confirm ────────────────────────────────────────────────────────────────
    if interactive:
        print()
        try:
            confirm = input("Proceed with migration? [y/N] ").strip().lower()
        except EOFError:
            confirm = "y"
        if confirm != "y":
            print("Aborted.")
            return
    else:
        print("\nExecuting migration ...")

    # ── Execute ────────────────────────────────────────────────────────────────
    print()
    log = execute_plan(plan, dry_run=False)

    # Write log
    log_path = CORE_SCHEMA_ROOT / "scripts" / "migration-log.json"
    with open(log_path, "w") as f:
        json.dump(log, f, indent=2, default=str)

    s = log["summary"]
    print(f"\n{'='*50}")
    print(f"Migration complete: {s['copied']} copied, {s['skipped']} skipped, {s['errors']} errors")
    print(f"Log written to: {log_path}")
    print()
    print("Next steps:")
    print("  git add schema/ && git commit -m 'feat: migrate domain schemas (mobility, logistics, retail)'")
    print("  git push origin draft")


if __name__ == "__main__":
    main()
