#!/usr/bin/env python3
"""
validate_schemas.py
-------------------
Validates all attributes.yaml files in the schema/ directory against
the JSON Schema Draft 2020-12 formatting rules for this repository.

Checks performed:
  1. File is valid YAML
  2. $schema is declared and references JSON Schema Draft 2020-12
  3. $id is present and in versioned canonical form:
       https://schema.beckn.io/{SchemaName}/v{major}.{minor}
  4. All $ref values referencing schema.beckn.io are versioned canonical
       (no .yaml suffix, no bare unversioned URIs)
  5. No array items defined as bare type:object with no $ref or properties

Usage:
  pip install pyyaml
  python tools/validate_schemas.py

  # or target a single file:
  python tools/validate_schemas.py schema/Catalog/v2.0/attributes.yaml
"""

import os
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)

VERSIONED_URI = re.compile(
    r"^https://schema\.beckn\.io/[A-Za-z][A-Za-z0-9]*/v\d+\.\d+"
)
BECKN_IO_URI = re.compile(r"https://schema\.beckn\.io/")


def check_refs(obj, path="$"):
    """Recursively walk the schema object and collect $ref issues."""
    issues = []
    if isinstance(obj, dict):
        # Check $ref
        if "$ref" in obj:
            ref_val = str(obj["$ref"])
            base = ref_val.split("#")[0]
            if BECKN_IO_URI.search(base):
                if ".yaml" in base:
                    issues.append(
                        f"  [ref]  $ref has .yaml suffix at {path}: {ref_val}"
                    )
                elif not VERSIONED_URI.match(base):
                    issues.append(
                        f"  [ref]  $ref is not versioned at {path}: {ref_val}"
                    )

        # Check array items for bare type:object with no $ref
        if obj.get("type") == "array" and "items" in obj:
            items = obj["items"]
            if (
                isinstance(items, dict)
                and items.get("type") == "object"
                and "$ref" not in items
                and "properties" not in items
                and "oneOf" not in items
                and "anyOf" not in items
                and "allOf" not in items
            ):
                issues.append(
                    f"  [array] Array items is bare type:object with no $ref at {path}.items"
                )

        for key, value in obj.items():
            issues.extend(check_refs(value, f"{path}.{key}"))

    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            issues.extend(check_refs(item, f"{path}[{i}]"))

    return issues


def validate_file(filepath):
    """Validate a single attributes.yaml file. Returns list of issue strings."""
    issues = []

    with open(filepath, encoding="utf-8") as f:
        try:
            schema = yaml.safe_load(f)
        except yaml.YAMLError as e:
            return [f"  [yaml]  Parse error: {e}"]

    if not isinstance(schema, dict):
        return ["  [yaml]  File does not contain a YAML object"]

    # 1. $schema check
    if "$schema" not in schema:
        issues.append("  [meta]  Missing $schema declaration")
    elif "json-schema.org/draft/2020-12" not in schema.get("$schema", ""):
        issues.append(
            f"  [meta]  $schema is not Draft 2020-12: {schema.get('$schema')}"
        )

    # 2. $id check
    if "$id" not in schema:
        issues.append("  [meta]  Missing $id")
    else:
        id_val = schema["$id"]
        if not VERSIONED_URI.match(id_val):
            issues.append(
                f"  [meta]  $id not in versioned canonical form: {id_val}"
            )

    # 3 & 4. Recurse for $ref and array item issues
    issues.extend(check_refs(schema))

    return issues


def main():
    schema_dir = Path("schema")
    if not schema_dir.exists():
        print("Run this script from the repository root.")
        sys.exit(1)

    # Allow targeting a single file via CLI arg
    if len(sys.argv) > 1:
        files = [Path(arg) for arg in sys.argv[1:]]
    else:
        files = sorted(schema_dir.rglob("attributes.yaml"))

    total = len(files)
    passed = 0
    failed = 0
    fail_log = []

    for f in files:
        file_issues = validate_file(f)
        if file_issues:
            failed += 1
            fail_log.append((f, file_issues))
        else:
            passed += 1

    # Summary
    print(f"\nValidated {total} schema file(s)\n{'=' * 50}")
    if fail_log:
        for f, issues in fail_log:
            print(f"\nFAIL  {f}")
            for issue in issues:
                print(issue)
        print(f"\n{'=' * 50}")
        print(f"Result: {passed} passed, {failed} FAILED")
        sys.exit(1)
    else:
        print(f"Result: {passed} passed, 0 failed. All good.")
        sys.exit(0)


if __name__ == "__main__":
    main()
