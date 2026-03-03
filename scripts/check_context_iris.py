#!/usr/bin/env python3
"""
check_context_iris.py
---------------------
Checks that every beckn: IRI referenced in schema/context.jsonld is defined
somewhere in the schema/ directory tree — either as:

  1. A schema-class name      (directory name, or key under components.schemas
                               in an attributes.yaml)
  2. A property name          (key under components.schemas.{Name}.properties
                               in an attributes.yaml)
  3. An enumeration value     (string in any `enum:` list inside an
                               attributes.yaml)

IRIs that are missing from the attributes.yaml files are further classified
as either:

  • Legacy carry-overs — present in the upstream legacy context
    (protocol-specifications-v2) but not yet transcribed into a new
    attributes.yaml.  These are expected and informational.

  • Genuinely new / unresolved — present in the current context.jsonld but
    absent from both the attributes.yaml files AND the legacy context.
    These require explicit attention.

Usage:
    python3 scripts/check_context_iris.py [OPTIONS]

Options:
    --context PATH          Path to the root context file
                            (default: schema/context.jsonld)
    --schema-dir PATH       Schema directory to scan
                            (default: schema)
    --legacy-context URL    URL (or path) of the legacy context to use as an
                            allowlist for carry-overs
                            (default: https://raw.githubusercontent.com/
                             beckn/protocol-specifications-v2/refs/heads/
                             main/schema/core/v2/context.jsonld)
    --no-legacy             Skip the legacy-context fetch/load entirely
    --show-extras           Also print names defined in attributes.yaml
                            but not referenced as a beckn: IRI in context.jsonld

Exits with code 0 if there are no genuinely new/unresolved IRIs,
         code 1 if genuinely new/unresolved IRIs exist,
         code 2 on a file/dependency/network error.
"""

import json
import sys
import argparse
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "ERROR: PyYAML is required.  Install with:  pip install pyyaml",
        file=sys.stderr,
    )
    sys.exit(2)


BECKN_PREFIX = "beckn:"
DEFAULT_LEGACY_URL = (
    "https://raw.githubusercontent.com/beckn/protocol-specifications-v2"
    "/refs/heads/main/schema/core/v2/context.jsonld"
)


# ---------------------------------------------------------------------------
# JSON-LD helpers
# ---------------------------------------------------------------------------

def _walk_beckn(value: object, out: set[str]) -> None:
    """Recursively collect every beckn:* local-name from a JSON-LD value."""
    if isinstance(value, str):
        if value.startswith(BECKN_PREFIX):
            out.add(value[len(BECKN_PREFIX):])
    elif isinstance(value, dict):
        for v in value.values():
            _walk_beckn(v, out)
    elif isinstance(value, list):
        for item in value:
            _walk_beckn(item, out)


def collect_context_iris(data: dict) -> set[str]:
    """Return all beckn: local-names referenced anywhere in a context dict."""
    out: set[str] = set()
    ctx = data.get("@context", {})
    for key, value in ctx.items():
        if key.startswith("@"):
            continue
        _walk_beckn(value, out)
    return out


def load_json_from_path_or_url(source: str) -> dict:
    """Load a JSON file from a local path or an HTTP(S) URL."""
    if source.startswith("http://") or source.startswith("https://"):
        with urllib.request.urlopen(source, timeout=15) as resp:
            return json.loads(resp.read().decode())
    else:
        return json.loads(Path(source).read_text())


# ---------------------------------------------------------------------------
# attributes.yaml helpers
# ---------------------------------------------------------------------------

def _walk_enums(obj: object, out: set[str]) -> None:
    """Recursively collect all string values inside any `enum:` list."""
    if isinstance(obj, dict):
        if "enum" in obj and isinstance(obj["enum"], list):
            for v in obj["enum"]:
                if isinstance(v, str):
                    out.add(v)
        for v in obj.values():
            _walk_enums(v, out)
    elif isinstance(obj, list):
        for item in obj:
            _walk_enums(item, out)


def collect_schema_defined_names(
    schema_dir: Path,
) -> tuple[set[str], dict[str, list[str]]]:
    """
    Walk all schema/{Name}/v*/attributes.yaml files and collect:
      - Schema/class names  (PascalCase keys under components.schemas)
      - Property names      (keys under .properties in each schema object)
      - Enum values         (all strings in any `enum:` list, recursively)

    Returns (names_set, source_map) where source_map records which
    attributes.yaml file each name came from.
    """
    names: set[str] = set()
    sources: dict[str, list[str]] = {}

    def add(name: str, path: Path) -> None:
        names.add(name)
        sources.setdefault(name, []).append(str(path.relative_to(schema_dir.parent)))

    for attr_yaml in sorted(schema_dir.glob("*/v*/attributes.yaml")):
        try:
            with attr_yaml.open() as fh:
                doc = yaml.safe_load(fh)
        except Exception as exc:
            print(f"  WARNING: Could not parse {attr_yaml}: {exc}", file=sys.stderr)
            continue

        if not isinstance(doc, dict):
            continue

        schemas_block = doc.get("components", {}).get("schemas", {})
        if not isinstance(schemas_block, dict):
            continue

        for schema_name, schema_obj in schemas_block.items():
            add(schema_name, attr_yaml)

            if not isinstance(schema_obj, dict):
                continue

            # Property names
            props = schema_obj.get("properties", {})
            if isinstance(props, dict):
                for prop_name in props:
                    if prop_name.startswith("@"):
                        continue
                    add(prop_name, attr_yaml)

            # Enum values (recursive)
            enum_vals: set[str] = set()
            _walk_enums(schema_obj, enum_vals)
            for ev in enum_vals:
                add(ev, attr_yaml)

    return names, sources


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--context",
        default="schema/context.jsonld",
        help="Path to the root context file (default: schema/context.jsonld)",
    )
    parser.add_argument(
        "--schema-dir",
        default="schema",
        help="Schema directory to scan (default: schema)",
    )
    parser.add_argument(
        "--legacy-context",
        default=DEFAULT_LEGACY_URL,
        metavar="URL_OR_PATH",
        help=(
            "URL or path of the upstream legacy context used as an allowlist "
            "for carry-over IRIs (default: protocol-specifications-v2 on GitHub)"
        ),
    )
    parser.add_argument(
        "--no-legacy",
        action="store_true",
        help="Skip loading the legacy context; treat all missing IRIs as genuinely new.",
    )
    parser.add_argument(
        "--show-extras",
        action="store_true",
        help=(
            "Also list names defined in attributes.yaml files that are NOT "
            "referenced as a beckn: IRI in context.jsonld."
        ),
    )
    args = parser.parse_args()

    context_path = Path(args.context)
    schema_dir = Path(args.schema_dir)

    if not context_path.exists():
        print(f"ERROR: context file not found: {context_path}", file=sys.stderr)
        return 2
    if not schema_dir.is_dir():
        print(f"ERROR: schema directory not found: {schema_dir}", file=sys.stderr)
        return 2

    # ---- Load current context ----
    current_data = json.loads(context_path.read_text())
    context_iris = collect_context_iris(current_data)

    # ---- Load legacy context ----
    legacy_iris: set[str] = set()
    if not args.no_legacy:
        src = args.legacy_context
        print(f"Fetching legacy context from: {src}")
        try:
            legacy_data = load_json_from_path_or_url(src)
            legacy_iris = collect_context_iris(legacy_data)
            print(f"  → {len(legacy_iris)} beckn: IRIs found in legacy context")
        except Exception as exc:
            print(
                f"  WARNING: Could not load legacy context ({exc}). "
                "Treating all missing IRIs as genuinely new.",
                file=sys.stderr,
            )
    print()

    print(f"Context    : {context_path}")
    print(f"Schema dir : {schema_dir}/")
    print()

    # ---- Collect schema-defined names ----
    schema_names, sources = collect_schema_defined_names(schema_dir)

    print(f"beckn: IRIs in context.jsonld                          : {len(context_iris)}")
    print(f"Names defined across all schema/*/v*/attributes.yaml   : {len(schema_names)}")
    if legacy_iris:
        print(f"beckn: IRIs in legacy context (carry-over allowlist)    : {len(legacy_iris)}")
    print()

    # ---- Classify missing IRIs ----
    missing = context_iris - schema_names
    if not missing:
        print("✅  Every beckn: IRI in context.jsonld is defined in a schema attributes.yaml.")
        return 0

    legacy_carryover = sorted(missing & legacy_iris)   # in legacy → expected gap
    genuinely_new    = sorted(missing - legacy_iris)   # NOT in legacy → real gap

    exit_code = 0

    # --- Genuinely new/unresolved ---
    if genuinely_new:
        exit_code = 1
        print(
            f"❌  {len(genuinely_new)} beckn: IRI(s) in context.jsonld are NOT defined in any\n"
            f"    schema attributes.yaml AND were NOT present in the legacy context.\n"
            f"    These need explicit attention:\n"
        )
        for iri in genuinely_new:
            print(f"  beckn:{iri}")
        print()

    # --- Legacy carry-overs ---
    if legacy_carryover:
        print(
            f"⚠️   {len(legacy_carryover)} beckn: IRI(s) in context.jsonld are NOT yet defined in any\n"
            f"    schema attributes.yaml but WERE present in the legacy context.\n"
            f"    These are likely carry-overs that still need to be migrated:\n"
        )
        for iri in legacy_carryover:
            print(f"  beckn:{iri}")
        print()

    # --- Extra (in YAML but not in context) ---
    if args.show_extras:
        extra = sorted(schema_names - context_iris)
        if extra:
            print(
                f"ℹ️   {len(extra)} name(s) defined in schema attributes.yaml files\n"
                f"    but NOT referenced as a beckn: IRI in context.jsonld:\n"
            )
            for name in extra:
                src_list = sources.get(name, [])
                src_str = f"  ← {src_list[0]}" if src_list else ""
                print(f"  {name}{src_str}")
            print()

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
