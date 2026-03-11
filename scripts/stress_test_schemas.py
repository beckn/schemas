#!/usr/bin/env python3
"""
stress_test_schemas.py
Linked to: schemas#S03-A (stress testing framework)

Schema stress testing framework for all active Beckn domains.
Tests BecknAction against use-case payloads for:
  - retail (discover, on_discover, select, confirm, status, support, rate)
  - energy/EV (discover with spatial intent, confirm with contract)
  - open-extension principle (non-standard action: message is unconstrained)
  - negative tests (wrong message shape must fail)

Design notes:
  - BecknEndpoint.oneOf enumerates 20 standard endpoints (pattern also enforces format).
    Extension endpoints (e.g. beckn/igm/raise_grievance) satisfy the pattern but NOT the
    oneOf — they fail Context.action validation. The "open-extension" principle applies
    to BecknAction dispatch (no if/then match → message is unconstrained), but the Context
    action field still requires a known endpoint. This is a known design constraint.
  - All schemas reference https://schema.beckn.io/... which is resolved offline via the
    local registry built from schema/<Name>/v*/attributes.yaml.

Usage:
    python3 scripts/stress_test_schemas.py [--schema-dir <path>] [--domain <name>] [--verbose]

Exit codes:
    0  All stress tests passed.
    1  One or more stress tests failed.
"""

import sys
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, field
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

try:
    import jsonschema
    from jsonschema import validate, ValidationError
except ImportError:
    print("ERROR: jsonschema not installed. Run: pip install jsonschema>=4.0", file=sys.stderr)
    sys.exit(2)


# ─────────────────────────────────────────────────────────────────────────────
# Minimal valid sub-objects (reused across payloads)
# ─────────────────────────────────────────────────────────────────────────────

BECKN_CONTEXT_BASE = "https://schema.beckn.io/"


def _ctx(action: str, **extra) -> dict:
    """Build a minimal valid Context for a given action (BAP-only endpoints)."""
    return {
        "action": action,
        "bapId": "bap.example.com",
        "bapUri": "https://bap.example.com/",
        "messageId": "00000000-0000-0000-0000-000000000001",
        "transactionId": "00000000-0000-0000-0000-000000000002",
        "timestamp": "2026-03-11T10:00:00Z",
        "version": "2.0.0",
        **extra
    }


def _ctx_bpp(action: str, **extra) -> dict:
    """Build a minimal valid Context for an action that requires bppId/bppUri."""
    base = _ctx(action, **extra)
    base["bppId"] = "bpp.example.com"
    base["bppUri"] = "https://bpp.example.com/"
    return base


# ── Shared sub-objects ────────────────────────────────────────────────────────

# Minimal valid Participant (required: @context, @type, id, role)
# Note: Participant.@type has default="beckn:Participant" but no const — any string works
PARTICIPANT_BAP = {
    "@context": BECKN_CONTEXT_BASE,
    "@type": "beckn:Participant",
    "id": "bap.example.com",
    "role": "BAP"
}
PARTICIPANT_BPP = {
    "@context": BECKN_CONTEXT_BASE,
    "@type": "beckn:Participant",
    "id": "bpp.example.com",
    "role": "BPP"
}

# Minimal valid ContractItem (required: itemId)
CONTRACT_ITEM_GROCERY = {
    "itemId": "item-grocery-001"
}

# Minimal valid Contract (required: @type, participants, items)
# Contract.@type has pattern: ^beckn:[A-Za-z0-9._~-]+$  → must be "beckn:Contract"
CONTRACT_MINIMAL = {
    "@type": "beckn:Contract",
    "participants": [PARTICIPANT_BAP, PARTICIPANT_BPP],
    "items": [CONTRACT_ITEM_GROCERY]
}

# Minimal valid SupportRequest (required: @context, @type)
# SupportRequest.@type const = "Support" (no beckn: prefix — exact const value)
SUPPORT_REQUEST_OBJ = {
    "@context": BECKN_CONTEXT_BASE,
    "@type": "Support"
}

# Minimal valid RatingInput (required: @context, @type, target, range)
# RatingInput.@type default = "RatingForm" (no const constraint — any string works)
RATING_INPUT_OBJ = {
    "@context": BECKN_CONTEXT_BASE,
    "@type": "RatingForm",
    "target": {
        "@context": BECKN_CONTEXT_BASE,
        "@type": "RatingTarget",
        "id": "order-abc-001",
        "category": "Order"
    },
    "range": {
        "bestRating": 5,
        "worstRating": 1
    }
}

# Minimal valid Catalog entry (required: @context, @type, id, descriptor, bppId, bppUri, items)
# Catalog.@type const = "beckn:Catalog"
# Descriptor.required = [@type]; Descriptor.additionalProperties: false
CATALOG_ENTRY = {
    "@context": BECKN_CONTEXT_BASE,
    "@type": "beckn:Catalog",
    "id": "catalog-001",
    "descriptor": {
        "@type": "beckn:Descriptor",
        "name": "Example Store"
    },
    "bppId": "bpp.example.com",
    "bppUri": "https://bpp.example.com/",
    "items": []
}

# Minimal valid SpatialConstraint (required: op, targets)
# op is the CQL2-JSON operator; targets is an array of property/geometry paths
SPATIAL_CONSTRAINT_EV = {
    "op": "S_INTERSECTS",   # enum: S_WITHIN, S_CONTAINS, S_INTERSECTS, ... (uppercase)
    # targets: oneOf(string | array<string>) — JSONPath-like pointer to geometry field
    "targets": "$['availableAt'][*]['geo']",
    "geometry": {
        "type": "Point",
        "coordinates": [77.5946, 12.9716]
    }
}


# ─────────────────────────────────────────────────────────────────────────────
# Test case payloads
# ─────────────────────────────────────────────────────────────────────────────

# ── Retail flow ───────────────────────────────────────────────────────────────

# discover: message.intent is required; Intent has anyOf requiring at least one of
# textSearch, filters, spatial, or (filters+spatial). Use textSearch as the simplest.
DISCOVER_REQUEST = {
    "context": _ctx("beckn/discover"),
    "message": {
        "intent": {
            "textSearch": "grocery"
        }
    }
}

# on_discover: message.catalogs (array) required; each item must be a valid Catalog
ON_DISCOVER_CALLBACK = {
    "context": _ctx_bpp("beckn/on_discover"),
    "message": {
        "catalogs": [CATALOG_ENTRY]
    }
}

# select: message.contract required (Contract schema)
SELECT_REQUEST = {
    "context": _ctx_bpp("beckn/select"),
    "message": {
        "contract": CONTRACT_MINIMAL
    }
}

# confirm: message.contract required (Contract schema)
CONFIRM_REQUEST = {
    "context": _ctx_bpp("beckn/confirm"),
    "message": {
        "contract": CONTRACT_MINIMAL
    }
}

# status: message.order (object with required: id)
STATUS_REQUEST = {
    "context": _ctx_bpp("beckn/status"),
    "message": {
        "order": {
            "id": "order-abc-001"
        }
    }
}

# support: message.supportRequest (SupportRequest schema, required: @context, @type)
SUPPORT_REQUEST = {
    "context": _ctx_bpp("beckn/support"),
    "message": {
        "supportRequest": SUPPORT_REQUEST_OBJ
    }
}

# rate: message.ratingInputs (array of RatingInput, required: @context, @type, target, range)
RATE_REQUEST = {
    "context": _ctx_bpp("beckn/rate"),
    "message": {
        "ratingInputs": [RATING_INPUT_OBJ]
    }
}


# ── Extension endpoint (negative test or design-gap doc) ─────────────────────
# BecknEndpoint oneOf lists 20 consts. beckn/igm/raise_grievance matches the
# pattern but NOT the oneOf → Context.action validation FAILS.
# This is documented as EXPECTED_INVALID to confirm the design constraint is enforced.
EXTENSION_ENDPOINT_REQUEST = {
    "context": _ctx("beckn/igm/raise_grievance"),
    "message": {
        "grievance_type": "item_not_delivered"
    }
}


# ── EV / Energy domain ────────────────────────────────────────────────────────
# Context has no `domain` field (additionalProperties:false).
# Intent.additionalProperties:false, Intent.properties = textSearch/filters/spatial/media_search.
# A spatial EV search uses the `spatial` field.

EV_DISCOVER = {
    "context": _ctx("beckn/discover"),
    "message": {
        "intent": {
            # spatial must be an array of SpatialConstraint objects (required: op, targets)
            "spatial": [SPATIAL_CONSTRAINT_EV]
        }
    }
}

# EV confirm: same Contract structure, EV domain uses standard BecknAction Contract
EV_CONFIRM = {
    "context": _ctx_bpp("beckn/confirm"),
    "message": {
        "contract": {
            "@type": "beckn:Contract",   # pattern: ^beckn:[A-Za-z0-9._~-]+$
            "participants": [
                {
                    "@context": BECKN_CONTEXT_BASE,
                    "@type": "beckn:Participant",
                    "id": "ev-bap.example.com",
                    "role": "BAP"
                },
                {
                    "@context": BECKN_CONTEXT_BASE,
                    "@type": "beckn:Participant",
                    "id": "ev-bpp.example.com",
                    "role": "BPP"
                }
            ],
            "items": [
                {"itemId": "ev-charging-session-001"}
            ]
        }
    }
}

# ── Negative tests ────────────────────────────────────────────────────────────
# Wrong message shape for confirm: using old `order` key instead of `contract`
CONFIRM_WRONG_SHAPE = {
    "context": _ctx_bpp("beckn/confirm"),
    "message": {
        "order": {    # should be `contract` — this must FAIL
            "items": [{"id": "item-1"}]
        }
    }
}


# ─────────────────────────────────────────────────────────────────────────────
# Test runner
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class TestCase:
    name: str
    domain: str
    payload: dict
    expect_valid: bool = True   # False = expect validation error (negative test)
    description: str = ""


TEST_CASES = [
    TestCase("discover-retail", "retail", DISCOVER_REQUEST,
             description="Retail discover request (empty intent)"),
    TestCase("on_discover-retail", "retail", ON_DISCOVER_CALLBACK,
             description="Retail on_discover callback with Catalog"),
    TestCase("select-retail", "retail", SELECT_REQUEST,
             description="Retail select with minimal Contract"),
    TestCase("confirm-retail", "retail", CONFIRM_REQUEST,
             description="Retail confirm with minimal Contract"),
    TestCase("status-retail", "retail", STATUS_REQUEST,
             description="Status enquiry (order.id only)"),
    TestCase("support-retail", "retail", SUPPORT_REQUEST,
             description="Support request (minimal SupportRequest)"),
    TestCase("rate-retail", "retail", RATE_REQUEST,
             description="Rating request (RatingInput with target+range)"),
    # Extension: expect INVALID (beckn/igm/raise_grievance not in BecknEndpoint oneOf)
    TestCase("extension-endpoint-design-constraint", "core", EXTENSION_ENDPOINT_REQUEST,
             expect_valid=False,
             description="Extension endpoint fails Context.action validation (design constraint — known)"),
    TestCase("ev-discover", "deg:ev-charging", EV_DISCOVER,
             description="EV charging discover (spatial intent)"),
    TestCase("ev-confirm", "deg:ev-charging", EV_CONFIRM,
             description="EV charging confirm with Contract"),
    # Negative: wrong message key
    TestCase("confirm-wrong-shape", "retail", CONFIRM_WRONG_SHAPE,
             expect_valid=False,
             description="Confirm with `order` key (wrong) must fail → regression guard"),
]


def load_schema_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_local_registry(schema_dir: Path) -> dict:
    """
    Build a {uri: schema} registry by scanning schema/<Name>/v<X.Y>/attributes.yaml.
    Maps https://schema.beckn.io/<Name>/v<X.Y> → parsed schema dict.
    This allows offline validation without hitting the network.
    """
    registry = {}
    base = "https://schema.beckn.io"

    for name_dir in sorted(schema_dir.iterdir()):
        if not name_dir.is_dir() or name_dir.name.startswith("."):
            continue
        for ver_dir in sorted(name_dir.iterdir()):
            if not ver_dir.is_dir():
                continue
            attrs = ver_dir / "attributes.yaml"
            if not attrs.exists():
                continue
            try:
                data = load_schema_yaml(attrs)
                uri = f"{base}/{name_dir.name}/{ver_dir.name}"
                registry[uri] = data
            except Exception:
                pass

    return registry


def make_resolver(schema: dict, registry: dict):
    """
    Create a jsonschema RefResolver that resolves https://schema.beckn.io/... refs locally.
    """
    from jsonschema import RefResolver
    store = dict(registry)
    base_uri = schema.get("$id", "https://schema.beckn.io/BecknAction/v2.0")
    return RefResolver(base_uri=base_uri, referrer=schema, store=store)


def run_tests(schema_dir: Path, filter_domain: str | None, verbose: bool) -> int:
    beckn_action_path = schema_dir / "BecknAction" / "v2.0" / "attributes.yaml"

    if not beckn_action_path.exists():
        print(f"ERROR: BecknAction schema not found at {beckn_action_path}", file=sys.stderr)
        return 1

    schema = load_schema_yaml(beckn_action_path)
    registry = build_local_registry(schema_dir)
    resolver = make_resolver(schema, registry)

    print(f"BecknAction schema : {beckn_action_path}")
    print(f"Local registry     : {len(registry)} schemas indexed")
    print(f"Running            : {len(TEST_CASES)} test cases\n")

    passed = 0
    failed = 0
    skipped = 0

    for tc in TEST_CASES:
        if filter_domain and tc.domain != filter_domain:
            skipped += 1
            continue

        err_msg = ""
        try:
            from jsonschema import Draft202012Validator
            validator = Draft202012Validator(schema, resolver=resolver)
            errors_list = list(validator.iter_errors(tc.payload))
            valid = len(errors_list) == 0
            if not valid:
                err_msg = errors_list[0].message
        except Exception as e:
            valid = False
            err_msg = str(e)

        result_ok = (valid == tc.expect_valid)
        icon = "✓ PASS" if result_ok else "✗ FAIL"

        if result_ok:
            passed += 1
            outcome = "valid ✓" if valid else "invalid (expected) ✓"
            print(f"  {icon}  [{tc.domain}] {tc.name}")
            print(f"         {tc.description} → {outcome}")
        else:
            failed += 1
            if valid:
                print(f"  {icon}  [{tc.domain}] {tc.name}")
                print(f"         {tc.description}")
                print(f"         Expected INVALID but payload passed validation — fix test or schema")
            else:
                print(f"  {icon}  [{tc.domain}] {tc.name}")
                print(f"         {tc.description}")
                if verbose:
                    print(f"         Error: {err_msg}")
                else:
                    print(f"         Error (use --verbose for details): {err_msg[:120]}")

        print()

    print(f"{'─' * 62}")
    print(f"Results: {passed} passed, {failed} failed, {skipped} skipped")

    if failed:
        print("\nFAIL — Some stress tests did not pass. Review payloads and schemas above.")
        return 1

    print("\nPASS — All stress tests passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Schema stress testing framework for all active Beckn domains."
    )
    parser.add_argument(
        "--schema-dir", default="schema",
        help="Root schema directory (default: schema)"
    )
    parser.add_argument(
        "--domain", default=None,
        help="Filter tests by domain (retail, deg:ev-charging, core, etc.)"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Show full validation error messages on failure"
    )
    args = parser.parse_args()

    return run_tests(Path(args.schema_dir), args.domain, args.verbose)


if __name__ == "__main__":
    sys.exit(main())
