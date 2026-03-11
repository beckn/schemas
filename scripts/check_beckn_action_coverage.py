#!/usr/bin/env python3
"""
check_beckn_action_coverage.py
Linked to: schemas#43 (S02-I)

CI check: Every endpoint listed in BecknEndpoint/v2.0/attributes.yaml `oneOf[].const`
must have a corresponding `if/then` block in BecknAction/v2.0/attributes.yaml.

Usage:
    python3 scripts/check_beckn_action_coverage.py [--schema-dir <path>]

Exit codes:
    0  All BecknEndpoint examples covered in BecknAction if/then blocks.
    1  One or more endpoints missing from BecknAction — CI should fail.

Run in CI on every PR touching BecknEndpoint/ or BecknAction/.
"""

import sys
import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def extract_beckn_endpoint_consts(beckn_endpoint: dict) -> list[str]:
    """
    Extract all `const` values from the top-level `oneOf` list in
    BecknEndpoint/v2.0/attributes.yaml.
    Returns a sorted list of endpoint strings like ['beckn/cancel', 'beckn/confirm', ...].
    """
    one_of = beckn_endpoint.get("oneOf", [])
    consts = []
    for entry in one_of:
        if isinstance(entry, dict) and "const" in entry:
            consts.append(entry["const"])
    return sorted(consts)


def extract_beckn_action_covered(beckn_action: dict) -> list[str]:
    """
    Extract all `context.action.const` values from `allOf[].if.properties.context
    .properties.action.const` in BecknAction/v2.0/attributes.yaml.
    Returns a sorted list of covered endpoint strings.
    """
    all_of = beckn_action.get("allOf", [])
    covered = []
    for block in all_of:
        if not isinstance(block, dict):
            continue
        if_block = block.get("if", {})
        try:
            action_const = (
                if_block["properties"]["context"]["properties"]["action"]["const"]
            )
            covered.append(action_const)
        except (KeyError, TypeError):
            pass
    return sorted(covered)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check BecknAction if/then coverage matches BecknEndpoint oneOf consts."
    )
    parser.add_argument(
        "--schema-dir",
        default="schema",
        help="Root schema directory (default: schema)",
    )
    args = parser.parse_args()

    schema_dir = Path(args.schema_dir)
    endpoint_yaml = schema_dir / "BecknEndpoint" / "v2.0" / "attributes.yaml"
    action_yaml = schema_dir / "BecknAction" / "v2.0" / "attributes.yaml"

    # --- Validate paths ---
    for p in [endpoint_yaml, action_yaml]:
        if not p.exists():
            print(f"ERROR: File not found: {p}", file=sys.stderr)
            return 1

    # --- Load schemas ---
    beckn_endpoint = load_yaml(endpoint_yaml)
    beckn_action = load_yaml(action_yaml)

    # --- Extract values ---
    endpoints = extract_beckn_endpoint_consts(beckn_endpoint)
    covered = set(extract_beckn_action_covered(beckn_action))

    if not endpoints:
        print("WARNING: No `const` values found in BecknEndpoint oneOf. "
              "Is the schema empty?", file=sys.stderr)
        return 0

    # --- Check coverage ---
    missing = [ep for ep in endpoints if ep not in covered]
    extra = sorted(covered - set(endpoints))

    print(f"BecknEndpoint endpoints : {len(endpoints)}")
    print(f"BecknAction if/then blocks : {len(covered)}")

    if extra:
        print(f"\nINFO: BecknAction has {len(extra)} if/then block(s) for endpoints "
              f"not listed in BecknEndpoint.oneOf (extension endpoints — OK):")
        for ep in extra:
            print(f"  + {ep}")

    if missing:
        print(f"\nFAIL: {len(missing)} endpoint(s) in BecknEndpoint.oneOf have NO "
              f"corresponding if/then block in BecknAction:")
        for ep in missing:
            print(f"  ✗ {ep}")
        print(
            "\nFix: Add an if/then block to schema/BecknAction/v2.0/attributes.yaml "
            "for each missing endpoint listed above."
        )
        return 1

    print("\nPASS: All BecknEndpoint endpoints are covered in BecknAction if/then blocks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
