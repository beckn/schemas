---
name: beckn-v21-schema-tester
description: >
  Validates Beckn Protocol v2.1 generalised extension schema packs for correctness and
  consistency across four quality layers: OpenAPI structure, JSON-LD prefix resolution,
  cross-file consistency, and example payload validation. Use this skill whenever the user
  asks to test, validate, check, or verify their Beckn v2.1 generalised schemas — phrases
  like "run tests on my v2.1 schemas", "validate the generalised schema pack", "check if
  my resource schemas are correct", or "test the v2.1 contract schemas". Also use
  automatically at the end of any beckn-v21-schema generation workflow to confirm the
  generated pack is clean before publishing. For v2 schemas using Item/Order/Fulfillment
  semantics, use the beckn-schema-tester skill instead.
---

# Beckn v2.1 Schema Tester

This skill runs a four-layer automated test suite against any Beckn v2.1 generalised
extension schema pack. It validates that schemas targeting the `Resource → Offer → Contract`
model are structurally correct, JSON-LD consistent, and produce valid example payloads.

## What it checks

Each schema folder (any subdirectory of the `v2.1/` directory containing `attributes.yaml`)
is tested across four layers:

| Layer | What it checks |
|-------|---------------|
| L1 OpenAPI | `attributes.yaml` has required top-level fields, all `$ref` chains resolve, `x-beckn-container` is declared with a valid v2.1 container name, `x-jsonld-id` annotations are present |
| L2 JSON-LD | Schema-specific prefix is declared in `context.jsonld`, `@import` uses the generalised context URI, all `@id` values resolve via local prefixes, no orphan properties in example attribute blocks |
| L3 Consistency | Every property in `attributes.yaml` has a mapping in `context.jsonld` (coverage), `x-jsonld-id` uses the correct schema-specific prefix (alignment), every class in `vocab.jsonld` is aliased in `context.jsonld` (vocab coverage) |
| L4 Examples | Each example JSON payload is extracted and validated against the combined core + extension schema using jsonschema |

## Valid v2.1 Container Names

The following `x-beckn-container` values are valid for v2.1 generalised schemas:
- `resourceAttributes`
- `offerAttributes`
- `contractAttributes`
- `commitmentAttributes`
- `performanceAttributes`
- `considerationAttributes`
- `settlementAttributes`

## Step 1 — Identify paths

Ask the user (or infer from context):
- **Schema root**: the `v2.1/` directory (or its parent domain folder if `v2.1/` is a subfolder)
- **Core directory**: the directory with `beckn.yaml` and `attributes.yaml` for core v2.1 schemas. L4 is skipped if core is not present.

Typical structure:
```
project/
├── core/                          ← core v2.1 schemas (needed for L4)
└── driver-network/
    └── v2.1/                      ← schema root (contains schema folders)
        ├── DriverJobResourceAttributes/
        ├── DriverContractAttributes/
        ├── DriverPerformanceAttributes/
        ├── driver-common/         ← shared types — NOT tested as top-level schemas
        │   └── CodedValue/
        │       ├── attributes.yaml
        │       └── README.md
        └── ...
```

**`{domain}-common/` folders are intentionally excluded from testing.** Auto-discovery scans
only *direct* subdirectories of the schema root that contain an `attributes.yaml` at their
own level. Shared type definitions in `{domain}-common/{TypeName}/attributes.yaml` are one
level deeper and are never picked up as testable schemas.

If the user passes the domain root (`driver-network/`) rather than the `v2.1/` subfolder,
auto-detect the `v2.1/` subdirectory and use it as the schema root.

## Step 2 — Set up test scripts

Check whether a `tests/` directory already exists inside the schema root with the layer scripts.

If not present, copy them from this skill's `scripts/` directory:

```bash
mkdir -p "<schema-root>/tests"
cp "<skill-base-dir>/scripts/"*.py "<schema-root>/tests/"
```

The `<skill-base-dir>` is the directory containing this SKILL.md file.

## Step 3 — Run the tests

```bash
cd "<schema-root>"
python3 tests/run_tests.py
```

Or with explicit paths:
```bash
python3 tests/run_tests.py \
  --schema-root "<schema-root>/v2.1" \
  --core "<core-dir>"
```

## Step 4 — Report results

Summarize results clearly:
- State the total pass count (e.g., "72/72 checks passed — all green ✓")
- For any failures, explain *what* failed, *why* it matters, and give a concrete fix

## Common failures and fixes

**L1 — Invalid `x-beckn-container` value:** A schema declares `x-beckn-container: itemAttributes`
(v2 value) instead of a v2.1 value like `resourceAttributes`. Fix: update the container name.

**L1 — `x-beckn-container` missing on a shared type:** A shared type (e.g., `CodedValue`)
was placed directly in the schema root instead of inside `{domain}-common/`. Fix: move it
one level deeper into `{domain}-common/CodedValue/`.

**L2 — Wrong `@import` value:** `context.jsonld` imports
`"https://schema.beckn.io/core/v2/context.jsonld"` (v2) instead of
`"https://schema.beckn.io/core/v2/context.jsonld#generalised"` (v2.1). Fix: update the
`@import` value in `context.jsonld`.

**L2 — Orphan properties in example:** An example payload's attribute block contains a
property that has no mapping in `context.jsonld`. Fix: either add the property to
`attributes.yaml` and `context.jsonld`, or remove it from the example.

**L3 B — Prefix alignment:** `x-jsonld-id` in `attributes.yaml` uses an undeclared or
wrong prefix. Fix: use the schema-specific prefix declared in `context.jsonld`.

**L3 C — Vocab coverage:** A class defined in `vocab.jsonld` has no type alias in
`context.jsonld`. Fix: add `"ClassName": "prefix:ClassName"` to `context.jsonld`.

**L4 — Block not found:** The test can't find the attribute block in the example payload.
For v2.1:
- `resourceAttributes` lives at `message.catalogs[].beckn:resources[].beckn:resourceAttributes`
- `contractAttributes` lives at `message.contract.beckn:contractAttributes`
- `performanceAttributes` lives at `message.contract.beckn:performance[].beckn:performanceAttributes`
Check that your example uses the correct v2.1 payload structure.

**L4 — Schema validation failure:** An example attribute block doesn't match its schema.
Check required fields, property types, and enum values against `attributes.yaml`.

## Dependencies

- Python 3.8+
- `pyyaml` (`pip install pyyaml`)
- `jsonschema` (`pip install jsonschema`)
