#!/usr/bin/env python3
"""
generate_missing_files.py — Phase 1 generator for Beckn core_schema.

For every schema/{ClassName}/{version}/ folder that is missing any of the
four required files, generates:
  - context.jsonld    (JSON-LD term mapping for this class)
  - vocab.jsonld      (RDF vocabulary for this class and its properties)
  - README.md         (version-level, with properties table)

Also generates schema/{ClassName}/README.md (class-level) if missing.

Rules:
  - NEVER overwrites existing files.
  - All properties are initially mapped to beckn:{propertyName}.
    Phases 2-4 (deduplicate_iris.py, align_schema_org.py, consolidate_vocab.py)
    will refine these mappings.
  - Handles both JSON Schema 2020-12 ($schema/$id/properties) and
    OpenAPI 3.1 (openapi/components/schemas) attribute formats.

Usage:
    cd /path/to/core_schema
    python3 scripts/generate_missing_files.py [--dry-run] [--class ClassName]

Options:
    --dry-run          Print what would be generated without writing files.
    --class ClassName  Only process the named class (for testing).
    --verbose          Print per-file status for all classes.
"""

import argparse
import json
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


# ---------------------------------------------------------------------------
# Helpers — attributes.yaml parsing
# ---------------------------------------------------------------------------

def load_yaml(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def extract_schema_info(attrs: dict, class_name: str) -> dict:
    """
    Extract class description and properties from attributes.yaml.

    Returns a dict:
      {
        "description": str,
        "properties": {
            "propName": {"description": str, "type": str, "required": bool}
        }
      }

    Handles two formats:
      - JSON Schema 2020-12: top-level $schema, description, properties, required
      - OpenAPI 3.1:         openapi, components.schemas.{ClassName}.*
    """
    result = {"description": "", "properties": {}}

    # ── JSON Schema 2020-12 format ─────────────────────────────────────────
    if "$schema" in attrs or "$id" in attrs:
        result["description"] = _clean_desc(attrs.get("description", ""))
        props = attrs.get("properties", {}) or {}
        required = set(attrs.get("required", []) or [])
        for prop_name, prop_def in props.items():
            if not isinstance(prop_def, dict):
                continue
            result["properties"][prop_name] = {
                "description": _clean_desc(prop_def.get("description", "")),
                "type": _infer_type(prop_def),
                "required": prop_name in required,
            }
        return result

    # ── OpenAPI 3.1 format ─────────────────────────────────────────────────
    components = attrs.get("components", {}) or {}
    schemas = components.get("schemas", {}) or {}

    # Try exact class name first, then first schema entry
    schema_def = schemas.get(class_name) or (list(schemas.values())[0] if schemas else {})

    if not schema_def:
        return result

    # Flatten allOf if present
    if "allOf" in schema_def:
        merged = {}
        for part in (schema_def.get("allOf") or []):
            if isinstance(part, dict):
                merged.update(part)
        schema_def = {**schema_def, **merged}

    result["description"] = _clean_desc(schema_def.get("description", ""))
    props = schema_def.get("properties", {}) or {}
    required = set(schema_def.get("required", []) or [])
    for prop_name, prop_def in props.items():
        if not isinstance(prop_def, dict):
            continue
        result["properties"][prop_name] = {
            "description": _clean_desc(prop_def.get("description", "")),
            "type": _infer_type(prop_def),
            "required": prop_name in required,
        }
    return result


def _clean_desc(text) -> str:
    """Collapse multi-line YAML block scalars to a single clean string."""
    if not text:
        return ""
    return " ".join(str(text).split())


def _infer_type(prop_def: dict) -> str:
    """Produce a human-readable type string from a JSON Schema property definition."""
    if not isinstance(prop_def, dict):
        return "any"

    # $ref → extract the referenced class name
    ref = prop_def.get("$ref", "")
    if ref:
        # https://schema.beckn.io/Foo/v2.0  or  #/components/schemas/Foo
        name = ref.rstrip("/").split("/")[-1]
        if name and name not in ("v2.0", "schema"):
            return name
        return "object"

    t = prop_def.get("type", "")

    if t == "array":
        items = prop_def.get("items", {})
        item_ref = items.get("$ref", "") if isinstance(items, dict) else ""
        if item_ref:
            name = item_ref.rstrip("/").split("/")[-1]
            if name and name not in ("v2.0", "schema"):
                return f"[{name}]"
        item_type = items.get("type", "any") if isinstance(items, dict) else "any"
        return f"[{item_type}]"

    if t == "object":
        # Check allOf for a $ref
        all_of = prop_def.get("allOf", [])
        for part in all_of:
            if isinstance(part, dict) and "$ref" in part:
                name = part["$ref"].rstrip("/").split("/")[-1]
                if name and name not in ("v2.0", "schema"):
                    return name
        return "object"

    if t:
        fmt = prop_def.get("format", "")
        return f"{t} ({fmt})" if fmt else t

    # allOf / anyOf / oneOf with a $ref
    for combiner in ("allOf", "anyOf", "oneOf"):
        parts = prop_def.get(combiner, [])
        if parts:
            names = []
            for part in parts:
                if isinstance(part, dict) and "$ref" in part:
                    name = part["$ref"].rstrip("/").split("/")[-1]
                    if name and name not in ("v2.0", "schema"):
                        names.append(name)
            if names:
                return " | ".join(names)

    return "any"


# ---------------------------------------------------------------------------
# Helpers — human-readable label from camelCase
# ---------------------------------------------------------------------------

def human_label(name: str) -> str:
    """Convert camelCase or PascalCase to Title Case with spaces."""
    # Insert space before uppercase letters that follow lowercase
    spaced = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
    # Insert space before sequences like 'ID', 'URI' etc.
    spaced = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", spaced)
    return spaced.strip()


# ---------------------------------------------------------------------------
# File generators
# ---------------------------------------------------------------------------

def generate_context_jsonld(class_name: str, info: dict) -> str:
    """Generate context.jsonld content for a class."""
    context = {
        "@version": 1.1,
        "@protected": True,
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "beckn": "https://schema.beckn.io/",
        class_name: f"beckn:{class_name}",
    }
    for prop_name in info["properties"]:
        context[prop_name] = f"beckn:{prop_name}"

    return json.dumps({"@context": context}, indent=2, ensure_ascii=False) + "\n"


def generate_vocab_jsonld(class_name: str, info: dict) -> str:
    """Generate vocab.jsonld content for a class."""
    std_context = {
        "@version": 1.1,
        "beckn": "https://schema.beckn.io/",
        "owl": "http://www.w3.org/2002/07/owl#",
        "schema": "https://schema.org/",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
    }

    graph = [
        {
            "@id": f"beckn:{class_name}",
            "@type": "rdfs:Class",
            "rdfs:label": human_label(class_name),
            "rdfs:comment": info["description"] or f"TODO: Description Needed - {class_name}",
        }
    ]

    for prop_name, prop_info in info["properties"].items():
        graph.append({
            "@id": f"beckn:{prop_name}",
            "@type": "rdf:Property",
            "rdfs:label": human_label(prop_name),
            "rdfs:comment": prop_info["description"] or f"TODO: Description Needed - {prop_name}",
        })

    doc = {"@context": std_context, "@graph": graph}
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def generate_version_readme(class_name: str, version: str, info: dict) -> str:
    """Generate version-level README.md content."""
    desc = info["description"] or f"The `{class_name}` schema object."
    props = info["properties"]

    lines = [
        f"# {human_label(class_name)} — {version}",
        "",
        desc,
        "",
        f"Part of the [Beckn Protocol Core Schema](../../../README.md) · [{class_name}](../README.md)",
        "",
        "## Files",
        "",
        "| File | Description |",
        "|------|-------------|",
        f"| [attributes.yaml](./attributes.yaml) | JSON Schema 2020-12 definition for `{class_name}` |",
        f"| [context.jsonld](./context.jsonld) | JSON-LD context for `{class_name}` {version} |",
        f"| [vocab.jsonld](./vocab.jsonld) | RDF vocabulary for `{class_name}` {version} |",
    ]

    if props:
        lines += [
            "",
            "## Properties",
            "",
            "| Property | Type | Required | Description |",
            "|----------|------|----------|-------------|",
        ]
        for prop_name, prop_info in props.items():
            required_mark = "✅" if prop_info["required"] else "—"
            desc_cell = prop_info["description"] or "—"
            # Truncate very long descriptions for table readability
            if len(desc_cell) > 120:
                desc_cell = desc_cell[:117] + "…"
            t = prop_info["type"] or "any"
            lines.append(f"| `{prop_name}` | {t} | {required_mark} | {desc_cell} |")

    lines.append("")
    return "\n".join(lines)


def generate_class_readme(class_name: str, info: dict, versions: list) -> str:
    """Generate class-level README.md content."""
    desc = info["description"] or f"The `{class_name}` schema object."

    lines = [
        f"# {human_label(class_name)}",
        "",
        desc,
        "",
        "Part of the [Beckn Protocol Core Schema](../../README.md)",
        "",
        "## Versions",
        "",
        "| Version | Status |",
        "|---------|--------|",
    ]
    for v in sorted(versions):
        lines.append(f"| [{v}](./{v}/README.md) | Current |")

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Core processing
# ---------------------------------------------------------------------------

def process_class(class_name: str, class_dir: str, dry_run: bool, verbose: bool) -> dict:
    """
    Process a single class directory.
    Returns a stats dict with counts of generated files.
    """
    stats = {"generated": 0, "skipped": 0, "errors": 0}

    # Find version subdirectories
    try:
        entries = os.listdir(class_dir)
    except OSError as e:
        print(f"  ERROR reading {class_dir}: {e}", file=sys.stderr)
        stats["errors"] += 1
        return stats

    version_dirs = [
        e for e in entries
        if os.path.isdir(os.path.join(class_dir, e)) and re.match(r"^v\d+\.\d+", e)
    ]

    if not version_dirs:
        if verbose:
            print(f"  {class_name}/  — no version directories found, skipping")
        return stats

    # ── Class-level README.md ──────────────────────────────────────────────
    class_readme_path = os.path.join(class_dir, "README.md")
    if not os.path.exists(class_readme_path):
        # Try to get description from the first available attributes.yaml
        info_for_class = {"description": "", "properties": {}}
        for v in sorted(version_dirs):
            attrs_path = os.path.join(class_dir, v, "attributes.yaml")
            if os.path.exists(attrs_path):
                try:
                    attrs = load_yaml(attrs_path)
                    info_for_class = extract_schema_info(attrs, class_name)
                except Exception:
                    pass
                break

        content = generate_class_readme(class_name, info_for_class, version_dirs)
        _write_file(class_readme_path, content, dry_run, verbose, f"  {class_name}/README.md")
        stats["generated"] += 1
    else:
        if verbose:
            print(f"  {class_name}/README.md  — exists, skipping")
        stats["skipped"] += 1

    # ── Version directories ────────────────────────────────────────────────
    for version in version_dirs:
        version_dir = os.path.join(class_dir, version)
        attrs_path = os.path.join(version_dir, "attributes.yaml")

        if not os.path.exists(attrs_path):
            if verbose:
                print(f"  {class_name}/{version}/  — no attributes.yaml, skipping")
            continue

        # Load attributes.yaml
        try:
            attrs = load_yaml(attrs_path)
            info = extract_schema_info(attrs, class_name)
        except Exception as e:
            print(f"  ERROR parsing {attrs_path}: {e}", file=sys.stderr)
            stats["errors"] += 1
            continue

        # Generate context.jsonld
        ctx_path = os.path.join(version_dir, "context.jsonld")
        if not os.path.exists(ctx_path):
            content = generate_context_jsonld(class_name, info)
            _write_file(ctx_path, content, dry_run, verbose, f"  {class_name}/{version}/context.jsonld")
            stats["generated"] += 1
        else:
            if verbose:
                print(f"  {class_name}/{version}/context.jsonld  — exists, skipping")
            stats["skipped"] += 1

        # Generate vocab.jsonld
        vocab_path = os.path.join(version_dir, "vocab.jsonld")
        if not os.path.exists(vocab_path):
            content = generate_vocab_jsonld(class_name, info)
            _write_file(vocab_path, content, dry_run, verbose, f"  {class_name}/{version}/vocab.jsonld")
            stats["generated"] += 1
        else:
            if verbose:
                print(f"  {class_name}/{version}/vocab.jsonld  — exists, skipping")
            stats["skipped"] += 1

        # Generate README.md (version-level)
        readme_path = os.path.join(version_dir, "README.md")
        if not os.path.exists(readme_path):
            content = generate_version_readme(class_name, version, info)
            _write_file(readme_path, content, dry_run, verbose, f"  {class_name}/{version}/README.md")
            stats["generated"] += 1
        else:
            if verbose:
                print(f"  {class_name}/{version}/README.md  — exists, skipping")
            stats["skipped"] += 1

    return stats


def _write_file(path: str, content: str, dry_run: bool, verbose: bool, label: str):
    if dry_run:
        print(f"  [DRY-RUN] Would write: {label}")
    else:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        if verbose:
            print(f"  ✅ Generated: {label}")
        else:
            print(f"  ✅ {label}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate missing context.jsonld, vocab.jsonld, and README.md files for Beckn schema classes."
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would be generated without writing any files."
    )
    parser.add_argument(
        "--class", dest="class_name", default=None,
        help="Only process the named class (for testing)."
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print per-file status for all classes including skipped files."
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
    total_skipped = 0
    total_errors = 0

    mode_label = "[DRY-RUN] " if args.dry_run else ""
    print(f"\n{mode_label}Processing {len(class_dirs)} class(es) in {SCHEMA_DIR}\n")

    for class_name, class_dir in class_dirs:
        print(f"{'─' * 60}")
        print(f"{class_name}/")
        stats = process_class(class_name, class_dir, args.dry_run, args.verbose)
        total_generated += stats["generated"]
        total_skipped += stats["skipped"]
        total_errors += stats["errors"]

    print(f"\n{'═' * 60}")
    print(f"{mode_label}Summary:")
    print(f"  Generated : {total_generated} file(s)")
    print(f"  Skipped   : {total_skipped} file(s) (already exist)")
    print(f"  Errors    : {total_errors} file(s)")
    print()

    if total_errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
