#!/usr/bin/env python3
"""
validate_schema_compliance.py
Linked to: schemas#36 (S01-G / LR-5)

Validation guardrails for all schema files in the `schema/` directory.
Checks:
  1. Version folder compliance — folder name matches `v<major>.<minor>` pattern.
  2. $id compliance — must be `https://schema.beckn.io/<SchemaName>/v<major>.<minor>`.
  3. $schema compliance — must be JSON Schema 2020-12.
  4. Canonical @context — context.jsonld must reference the canonical base IRI.
  5. Canonical @vocab — vocab.jsonld must use `https://schema.beckn.io/` base.
  6. Per-schema JSON-LD presence — every v2.0 folder must have context.jsonld + vocab.jsonld.
  7. Required fields — attributes.yaml must have $id, $schema, title.

Usage:
    python3 scripts/validate_schema_compliance.py [--schema-dir <path>] [--fix-report]

Exit codes:
    0  All checks passed (or only warnings).
    1  One or more ERROR-level violations found.

Run in CI on every PR touching schema/.
"""

import sys
import argparse
import json
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


VERSION_PATTERN = re.compile(r"^v\d+\.\d+$")
ID_PATTERN = re.compile(
    r"^https://schema\.beckn\.io/(?P<name>[A-Za-z][A-Za-z0-9_]+)/(?P<ver>v\d+\.\d+)$"
)
CANONICAL_SCHEMA = "https://json-schema.org/draft/2020-12/schema"
CANONICAL_BASE = "https://schema.beckn.io/"


@dataclass
class Violation:
    level: str  # ERROR | WARN | INFO
    file: str
    rule: str
    message: str


def load_yaml_safe(path: Path) -> Optional[dict]:
    try:
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        return None


def load_json_safe(path: Path) -> Optional[dict]:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        return None


def check_attributes_yaml(
    schema_name: str, ver: str, attrs_path: Path, violations: list[Violation]
):
    data = load_yaml_safe(attrs_path)
    if data is None:
        violations.append(
            Violation("ERROR", str(attrs_path), "parse", "Failed to parse YAML")
        )
        return

    rel = str(attrs_path)

    # Rule 1: Must have $id
    schema_id = data.get("$id", "")
    if not schema_id:
        violations.append(
            Violation("ERROR", rel, "id-missing", "Missing $id field")
        )
    else:
        m = ID_PATTERN.match(schema_id)
        if not m:
            violations.append(
                Violation(
                    "ERROR",
                    rel,
                    "id-format",
                    f"$id '{schema_id}' does not match "
                    f"'https://schema.beckn.io/<Name>/v<major>.<minor>'",
                )
            )
        else:
            if m.group("name") != schema_name:
                violations.append(
                    Violation(
                        "ERROR",
                        rel,
                        "id-name-mismatch",
                        f"$id name '{m.group('name')}' does not match folder name '{schema_name}'",
                    )
                )
            if m.group("ver") != ver:
                violations.append(
                    Violation(
                        "ERROR",
                        rel,
                        "id-ver-mismatch",
                        f"$id version '{m.group('ver')}' does not match folder version '{ver}'",
                    )
                )

    # Rule 2: Must have $schema = 2020-12
    schema_decl = data.get("$schema", "")
    if not schema_decl:
        violations.append(
            Violation("WARN", rel, "schema-missing", "Missing $schema declaration")
        )
    elif schema_decl != CANONICAL_SCHEMA:
        violations.append(
            Violation(
                "ERROR",
                rel,
                "schema-wrong",
                f"$schema must be '{CANONICAL_SCHEMA}', got '{schema_decl}'",
            )
        )

    # Rule 3: Must have title
    if not data.get("title"):
        violations.append(
            Violation("WARN", rel, "title-missing", "Missing title field")
        )


def check_context_jsonld(
    schema_name: str, ver: str, ctx_path: Path, violations: list[Violation]
):
    data = load_json_safe(ctx_path)
    if data is None:
        violations.append(
            Violation("ERROR", str(ctx_path), "parse", "Failed to parse JSON")
        )
        return

    rel = str(ctx_path)
    context = data.get("@context", {})

    # Flatten if context is a list
    if isinstance(context, list):
        for item in context:
            if isinstance(item, dict):
                context = item
                break

    # Rule 4: @base or @vocab should point to canonical URL
    base = context.get("@base", "") or context.get("@vocab", "")
    if base and not base.startswith(CANONICAL_BASE):
        violations.append(
            Violation(
                "WARN",
                rel,
                "context-base-noncanonical",
                f"@base/@vocab '{base}' does not start with canonical '{CANONICAL_BASE}' — "
                f"verify this is intentional",
            )
        )


def check_vocab_jsonld(
    schema_name: str, ver: str, vocab_path: Path, violations: list[Violation]
):
    data = load_json_safe(vocab_path)
    if data is None:
        violations.append(
            Violation("ERROR", str(vocab_path), "parse", "Failed to parse JSON")
        )
        return

    rel = str(vocab_path)

    # Rule 5: vocab.jsonld must have @graph
    if "@graph" not in data:
        violations.append(
            Violation(
                "ERROR",
                rel,
                "vocab-no-graph",
                "vocab.jsonld missing @graph — per-schema vocab must have @graph array",
            )
        )

    # Rule 5b: @context should reference canonical base
    context = data.get("@context", {})
    if isinstance(context, list):
        for item in context:
            if isinstance(item, dict):
                context = item
                break
    vocab_base = context.get("@vocab", "") if isinstance(context, dict) else ""
    if vocab_base and not vocab_base.startswith(CANONICAL_BASE):
        violations.append(
            Violation(
                "WARN",
                rel,
                "vocab-base-noncanonical",
                f"@vocab '{vocab_base}' does not start with canonical '{CANONICAL_BASE}'",
            )
        )


def scan_schema_dir(schema_dir: Path) -> list[Violation]:
    violations: list[Violation] = []

    if not schema_dir.exists():
        violations.append(
            Violation("ERROR", str(schema_dir), "dir-missing", "Schema directory not found")
        )
        return violations

    for schema_folder in sorted(schema_dir.iterdir()):
        if not schema_folder.is_dir():
            continue
        schema_name = schema_folder.name
        if schema_name.startswith("."):
            continue

        for ver_folder in sorted(schema_folder.iterdir()):
            if not ver_folder.is_dir():
                continue
            ver = ver_folder.name

            # Rule: version folder must match vX.Y
            if not VERSION_PATTERN.match(ver):
                violations.append(
                    Violation(
                        "WARN",
                        str(ver_folder),
                        "ver-format",
                        f"Version folder '{ver}' does not match 'v<major>.<minor>' pattern",
                    )
                )
                continue

            attrs = ver_folder / "attributes.yaml"
            ctx = ver_folder / "context.jsonld"
            vocab = ver_folder / "vocab.jsonld"

            # Rule 6: All 3 files should exist
            for required_file in [attrs, ctx, vocab]:
                if not required_file.exists():
                    violations.append(
                        Violation(
                            "WARN",
                            str(ver_folder),
                            "file-missing",
                            f"Missing expected file: {required_file.name}",
                        )
                    )

            if attrs.exists():
                check_attributes_yaml(schema_name, ver, attrs, violations)
            if ctx.exists():
                check_context_jsonld(schema_name, ver, ctx, violations)
            if vocab.exists():
                check_vocab_jsonld(schema_name, ver, vocab, violations)

    return violations


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Beckn schema files for $id, $schema, canonical URL compliance."
    )
    parser.add_argument(
        "--schema-dir",
        default="schema",
        help="Root schema directory (default: schema)",
    )
    parser.add_argument(
        "--fix-report",
        action="store_true",
        help="Print a fix-oriented summary grouped by rule",
    )
    args = parser.parse_args()

    schema_dir = Path(args.schema_dir)
    print(f"Scanning: {schema_dir.resolve()}")

    violations = scan_schema_dir(schema_dir)

    errors = [v for v in violations if v.level == "ERROR"]
    warnings = [v for v in violations if v.level == "WARN"]
    infos = [v for v in violations if v.level == "INFO"]

    print(f"\nResults: {len(violations)} violation(s) — "
          f"{len(errors)} ERROR, {len(warnings)} WARN, {len(infos)} INFO\n")

    for v in violations:
        icon = "✗" if v.level == "ERROR" else ("⚠" if v.level == "WARN" else "·")
        print(f"  {icon} [{v.level}] [{v.rule}] {v.file}")
        print(f"       {v.message}")

    if args.fix_report and violations:
        print("\n--- Fix Report (grouped by rule) ---")
        by_rule: dict[str, list[Violation]] = {}
        for v in violations:
            by_rule.setdefault(v.rule, []).append(v)
        for rule, vs in sorted(by_rule.items()):
            print(f"\nRule: {rule} ({len(vs)} occurrence(s))")
            for v in vs:
                print(f"  {v.file}")

    if errors:
        print(f"\nFAIL: {len(errors)} ERROR(s) found — fix before merging.")
        return 1

    print("\nPASS: No ERROR-level violations found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
