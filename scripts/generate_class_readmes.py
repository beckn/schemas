#!/usr/bin/env python3
"""
generate_class_readmes.py — Rich class-level README generator for Beckn core_schema.

Generates (or overwrites) schema/{ClassName}/README.md for every schema class.

Each README includes:
  - Canonical IRI badge block (https://schema.beckn.io/{ClassName})
  - Domain tags from x-tags in attributes.yaml
  - Description from attributes.yaml
  - Versions table with links to all 4 required artifacts per version
  - Properties table (latest version) with type, required flag, description
  - Linked Data table — all canonical API URLs (IRI, attributes, context, vocab)
  - Related Schemas — other beckn classes referenced via $ref in properties

By default this script OVERWRITES existing class-level README.md files so that
all 256 classes have consistent, rich documentation. Version-level README.md
files are NOT touched by this script.

Usage:
    cd /path/to/core_schema
    python3 scripts/generate_class_readmes.py [--dry-run] [--class ClassName]

Options:
    --dry-run          Print what would be generated without writing files.
    --class ClassName  Only process the named class (for testing).
    --verbose          Print per-file status.
"""

import argparse
import os
import re
import sys

import yaml  # pip install pyyaml


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
SCHEMA_DIR = os.path.join(REPO_ROOT, "schema")

NAMESPACE_BASE = "https://schema.beckn.io"


# ---------------------------------------------------------------------------
# Helpers — attributes.yaml loading + parsing
# ---------------------------------------------------------------------------

def load_yaml(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _clean_desc(text) -> str:
    """Collapse multi-line YAML block scalars to a single clean string."""
    if not text:
        return ""
    return " ".join(str(text).split())


def _infer_type(prop_def: dict) -> str:
    """Produce a human-readable type string from a JSON Schema property definition."""
    if not isinstance(prop_def, dict):
        return "any"

    ref = prop_def.get("$ref", "")
    if ref:
        name = ref.rstrip("/").split("/")[-1]
        # Skip version segments like "v2.0"
        if name and not re.match(r"^v\d+", name):
            return f"[{name}](../{name}/README.md)"
        return "object"

    t = prop_def.get("type", "")

    if t == "array":
        items = prop_def.get("items", {})
        if isinstance(items, dict):
            item_ref = items.get("$ref", "")
            if item_ref:
                name = item_ref.rstrip("/").split("/")[-1]
                if name and not re.match(r"^v\d+", name):
                    return f"[{name}](../{name}/README.md)[]"
            item_type = items.get("type", "any")
            return f"{item_type}[]"
        return "any[]"

    if t == "object":
        all_of = prop_def.get("allOf", [])
        for part in all_of:
            if isinstance(part, dict) and "$ref" in part:
                name = part["$ref"].rstrip("/").split("/")[-1]
                if name and not re.match(r"^v\d+", name):
                    return f"[{name}](../{name}/README.md)"
        return "object"

    if t:
        fmt = prop_def.get("format", "")
        return f"`{t}` ({fmt})" if fmt else f"`{t}`"

    # allOf / anyOf / oneOf
    for combiner in ("allOf", "anyOf", "oneOf"):
        parts = prop_def.get(combiner, [])
        if parts:
            names = []
            for part in parts:
                if isinstance(part, dict):
                    r = part.get("$ref", "")
                    if r:
                        n = r.rstrip("/").split("/")[-1]
                        if n and not re.match(r"^v\d+", n):
                            names.append(f"[{n}](../{n}/README.md)")
                    elif part.get("type"):
                        names.append(f"`{part['type']}`")
            if names:
                return " \\| ".join(names)

    return "any"


def _extract_refs(prop_def: dict) -> list:
    """Return all beckn class names referenced via $ref in a property definition."""
    refs = []

    def _from_ref(r: str):
        if not r:
            return
        name = r.rstrip("/").split("/")[-1]
        if name and not re.match(r"^v\d+", name) and name != "schema":
            # Heuristic: beckn schema names are PascalCase
            if re.match(r"^[A-Z][A-Za-z]+$", name):
                refs.append(name)

    if not isinstance(prop_def, dict):
        return refs

    _from_ref(prop_def.get("$ref", ""))

    items = prop_def.get("items", {})
    if isinstance(items, dict):
        _from_ref(items.get("$ref", ""))

    for combiner in ("allOf", "anyOf", "oneOf"):
        for part in (prop_def.get(combiner) or []):
            if isinstance(part, dict):
                _from_ref(part.get("$ref", ""))

    return refs


def extract_schema_info(attrs: dict, class_name: str) -> dict:
    """
    Extract class title, description, tags, and properties from attributes.yaml.

    Returns:
      {
        "title": str,
        "description": str,
        "tags": [str],
        "schema_id": str,   # from $id if present
        "properties": {
            "propName": {
                "description": str,
                "type": str,          # human-readable, with markdown links
                "required": bool,
                "refs": [str],        # referenced beckn class names
            }
        }
      }
    """
    result = {
        "title": class_name,
        "description": "",
        "tags": [],
        "schema_id": "",
        "properties": {},
    }

    # ── JSON Schema 2020-12 format ─────────────────────────────────────────
    if "$schema" in attrs or "$id" in attrs:
        result["title"] = attrs.get("title", class_name)
        result["description"] = _clean_desc(attrs.get("description", ""))
        result["tags"] = list(attrs.get("x-tags") or [])
        result["schema_id"] = attrs.get("$id", "")
        props = attrs.get("properties", {}) or {}
        required = set(attrs.get("required", []) or [])
        for prop_name, prop_def in props.items():
            if not isinstance(prop_def, dict):
                continue
            result["properties"][prop_name] = {
                "description": _clean_desc(prop_def.get("description", "")),
                "type": _infer_type(prop_def),
                "required": prop_name in required,
                "refs": _extract_refs(prop_def),
            }
        return result

    # ── OpenAPI 3.1 format ─────────────────────────────────────────────────
    components = attrs.get("components", {}) or {}
    schemas = components.get("schemas", {}) or {}
    schema_def = schemas.get(class_name) or (list(schemas.values())[0] if schemas else {})

    if not schema_def:
        return result

    if "allOf" in schema_def:
        merged = {}
        for part in (schema_def.get("allOf") or []):
            if isinstance(part, dict):
                merged.update(part)
        schema_def = {**schema_def, **merged}

    result["title"] = schema_def.get("title", class_name)
    result["description"] = _clean_desc(schema_def.get("description", ""))
    result["tags"] = list(schema_def.get("x-tags") or attrs.get("x-tags") or [])
    props = schema_def.get("properties", {}) or {}
    required = set(schema_def.get("required", []) or [])
    for prop_name, prop_def in props.items():
        if not isinstance(prop_def, dict):
            continue
        result["properties"][prop_name] = {
            "description": _clean_desc(prop_def.get("description", "")),
            "type": _infer_type(prop_def),
            "required": prop_name in required,
            "refs": _extract_refs(prop_def),
        }
    return result


# ---------------------------------------------------------------------------
# Human-readable helpers
# ---------------------------------------------------------------------------

def human_label(name: str) -> str:
    """Convert camelCase or PascalCase to Title Case with spaces."""
    spaced = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
    spaced = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", spaced)
    return spaced.strip()


def canonical_version(v: str) -> str:
    """Convert 'v2.0' → '2.0', 'v1.0.0' → '1.0.0'."""
    return v.lstrip("v")


# ---------------------------------------------------------------------------
# README generator
# ---------------------------------------------------------------------------

def generate_class_readme(class_name: str, info: dict, version_dirs: list) -> str:
    """
    Generate the rich class-level README.md content.

    Sections:
      1. H1 title + canonical IRI badge block
      2. Description paragraph
      3. Versions table (all artifact links per version)
      4. Properties table (from the latest version)
      5. Linked Data table (canonical API URLs)
      6. Related Schemas (if $ref entries exist)
    """
    title = human_label(info["title"] or class_name)
    desc = info["description"] or f"The `{class_name}` schema object."
    tags = info["tags"]
    canonical_iri = f"{NAMESPACE_BASE}/{class_name}"

    # Sort versions: latest last
    sorted_versions = sorted(version_dirs)
    latest_version = sorted_versions[-1] if sorted_versions else None
    latest_canon = canonical_version(latest_version) if latest_version else None

    lines = []

    # ── 1. Title + IRI badge block ─────────────────────────────────────────
    lines += [
        f"# {title}",
        "",
        f"> **Canonical IRI:** [`{canonical_iri}`]({canonical_iri})",
    ]
    if tags:
        tag_str = ", ".join(f"`{t}`" for t in tags)
        lines.append(f"> **Tags:** {tag_str}")
    lines += [
        "> **Namespace:** `https://schema.beckn.io/`",
        "> Part of the [Beckn Protocol Core Schema](../../README.md)",
        "",
        "---",
        "",
    ]

    # ── 2. Description ─────────────────────────────────────────────────────
    lines += [
        desc,
        "",
    ]

    # ── 3. Versions table ──────────────────────────────────────────────────
    lines += [
        "## Versions",
        "",
        "| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |",
        "|---------|----------------|----------------|--------------|--------|",
    ]
    for v in sorted_versions:
        cv = canonical_version(v)
        lines.append(
            f"| **{v}** "
            f"| [attributes.yaml](./{v}/attributes.yaml) "
            f"| [context.jsonld](./{v}/context.jsonld) "
            f"| [vocab.jsonld](./{v}/vocab.jsonld) "
            f"| [README](./{v}/README.md) |"
        )
    lines.append("")

    # ── 4. Properties table ────────────────────────────────────────────────
    props = info["properties"]
    if props:
        version_label = f" (latest: {latest_version})" if latest_version else ""
        lines += [
            f"## Properties{version_label}",
            "",
            "| Property | Type | Required | Description |",
            "|----------|------|:--------:|-------------|",
        ]
        for prop_name, prop_info in props.items():
            req = "✅" if prop_info["required"] else "—"
            desc_cell = prop_info["description"] or "—"
            # Truncate very long descriptions for table readability
            if len(desc_cell) > 150:
                desc_cell = desc_cell[:147] + "…"
            # Escape pipe characters in descriptions
            desc_cell = desc_cell.replace("|", "\\|")
            t = prop_info["type"] or "any"
            lines.append(f"| `{prop_name}` | {t} | {req} | {desc_cell} |")
        lines.append("")

    # ── 5. Linked Data table ───────────────────────────────────────────────
    lines += [
        "## Linked Data",
        "",
        "| Resource | URL |",
        "|----------|-----|",
        f"| Canonical IRI | `{canonical_iri}` |",
    ]
    if latest_canon and latest_version:
        lines += [
            f"| JSON Schema (latest) | `{NAMESPACE_BASE}/{class_name}/{latest_canon}` |",
            f"| context.jsonld (latest) | `{NAMESPACE_BASE}/{class_name}/{latest_canon}/context.jsonld` |",
            f"| vocab.jsonld (latest) | `{NAMESPACE_BASE}/{class_name}/{latest_canon}/vocab.jsonld` |",
        ]
        # Add all version rows if more than one version
        if len(sorted_versions) > 1:
            for v in sorted_versions:
                cv = canonical_version(v)
                lines.append(f"| JSON Schema ({v}) | `{NAMESPACE_BASE}/{class_name}/{cv}` |")
    lines += [
        f"| Root context.jsonld | `{NAMESPACE_BASE}/context.jsonld` |",
        f"| Root vocab.jsonld | `{NAMESPACE_BASE}/vocab.jsonld` |",
        "",
    ]

    # ── 6. Related Schemas ─────────────────────────────────────────────────
    # Collect all referenced class names from property $ref entries
    related: dict[str, list[str]] = {}  # ref_name → [prop_name, ...]
    for prop_name, prop_info in props.items():
        for ref_name in prop_info.get("refs", []):
            if ref_name != class_name:
                related.setdefault(ref_name, []).append(prop_name)

    if related:
        lines += [
            "## Related Schemas",
            "",
            "| Schema | Referenced via |",
            "|--------|----------------|",
        ]
        for ref_name in sorted(related):
            prop_list = ", ".join(f"`{p}`" for p in related[ref_name])
            lines.append(f"| [`{ref_name}`](../{ref_name}/README.md) | {prop_list} |")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Core processing
# ---------------------------------------------------------------------------

def process_class(class_name: str, class_dir: str, dry_run: bool, verbose: bool) -> dict:
    """Process a single class directory: generate/overwrite its root README.md."""
    stats = {"generated": 0, "errors": 0}

    # Find version subdirectories
    try:
        entries = os.listdir(class_dir)
    except OSError as e:
        print(f"  ERROR reading {class_dir}: {e}", file=sys.stderr)
        stats["errors"] += 1
        return stats

    version_dirs = sorted([
        e for e in entries
        if os.path.isdir(os.path.join(class_dir, e)) and re.match(r"^v\d+\.\d+", e)
    ])

    if not version_dirs:
        if verbose:
            print(f"  {class_name}/  — no version directories found, skipping")
        return stats

    # ── Load info from the latest version's attributes.yaml ───────────────
    info = {"title": class_name, "description": "", "tags": [], "schema_id": "", "properties": {}}
    for v in reversed(version_dirs):  # latest first
        attrs_path = os.path.join(class_dir, v, "attributes.yaml")
        if os.path.exists(attrs_path):
            try:
                attrs = load_yaml(attrs_path)
                info = extract_schema_info(attrs, class_name)
                break
            except Exception as e:
                print(f"  WARNING: Could not parse {attrs_path}: {e}", file=sys.stderr)

    # ── Generate / overwrite class-level README.md ─────────────────────────
    class_readme_path = os.path.join(class_dir, "README.md")
    content = generate_class_readme(class_name, info, version_dirs)

    existed = os.path.exists(class_readme_path)
    _write_file(class_readme_path, content, dry_run, verbose,
                f"  {class_name}/README.md" + (" [OVERWRITE]" if existed else " [NEW]"))
    stats["generated"] += 1

    return stats


def _write_file(path: str, content: str, dry_run: bool, verbose: bool, label: str):
    if dry_run:
        print(f"  [DRY-RUN] Would write: {label}")
    else:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        if verbose:
            print(f"  ✅ {label}")
        else:
            print(f"  ✅ {label}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Generate (or overwrite) schema/{ClassName}/README.md for all Beckn schema classes.\n"
            "Produces rich documentation with canonical IRIs, artifact links, "
            "properties table, linked data URLs, and related schema references."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would be generated without writing any files.",
    )
    parser.add_argument(
        "--class", dest="class_name", default=None,
        help="Only process the named class (for testing).",
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print per-file status.",
    )
    args = parser.parse_args()

    if not os.path.isdir(SCHEMA_DIR):
        print(f"ERROR: schema/ directory not found at {SCHEMA_DIR}", file=sys.stderr)
        sys.exit(1)

    # Collect class directories
    if args.class_name:
        class_dirs = [(args.class_name, os.path.join(SCHEMA_DIR, args.class_name))]
        if not os.path.isdir(class_dirs[0][1]):
            print(f"ERROR: Class directory not found: {class_dirs[0][1]}", file=sys.stderr)
            sys.exit(1)
    else:
        class_dirs = [
            (entry, os.path.join(SCHEMA_DIR, entry))
            for entry in sorted(os.listdir(SCHEMA_DIR))
            if os.path.isdir(os.path.join(SCHEMA_DIR, entry))
        ]

    total_generated = 0
    total_errors = 0

    mode_label = "[DRY-RUN] " if args.dry_run else ""
    print(f"\n{mode_label}Generating class READMEs for {len(class_dirs)} class(es) in {SCHEMA_DIR}\n")

    for class_name, class_dir in class_dirs:
        if args.verbose:
            print(f"{'─' * 60}")
            print(f"{class_name}/")
        stats = process_class(class_name, class_dir, args.dry_run, args.verbose)
        total_generated += stats["generated"]
        total_errors += stats["errors"]

    print(f"\n{'═' * 60}")
    print(f"{mode_label}Summary:")
    print(f"  Generated / updated : {total_generated} README.md file(s)")
    print(f"  Errors              : {total_errors}")
    print()

    if total_errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
