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

Each schema folder containing `attributes.jsonschema.yaml` is tested across four layers. Two layouts are
supported: flat (`v2.1/SchemaName/attributes.jsonschema.yaml`) and versioned (`SchemaName/v2.1/attributes.jsonschema.yaml`).

| Layer | What it checks |
|-------|---------------|
| L1 OpenAPI | `attributes.jsonschema.yaml` has required top-level fields, all `$ref` chains resolve, `x-beckn-container` is declared with a valid v2.1 container name, `x-jsonld-id` annotations are present as flat properties (not nested under `x-jsonld`) |
| L2 JSON-LD | Schema-specific prefix is declared in `context.jsonld`, `@import` uses the generalised context URI, all `@id` values resolve via local prefixes, no orphan properties in example attribute blocks |
| L3 Consistency | Every non-keyword property in `attributes.jsonschema.yaml` has a mapping in `context.jsonld` (coverage — `@context` and `@type` are JSON-LD keywords and are automatically skipped), `x-jsonld-id` uses the correct schema-specific prefix (alignment), every class in `vocab.jsonld` is aliased as a **string** in `context.jsonld` (vocab coverage — dict-form `{"@id": "..."}` is NOT recognized) |
| L4 Examples | Each example JSON payload is extracted and validated against the combined core + extension schema using jsonschema, with cross-file `$ref` resolution and inheritance relaxation for `allOf` |

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
- **Schema root**: the domain folder containing either a `v2.1/` subfolder or per-schema versioned folders
- **Core directory**: the directory with `beckn.yaml` (or `attributes.jsonschema.yaml`) for core v2.1 schemas. The tester tries `attributes.jsonschema.yaml` first, then falls back to `beckn.yaml`. L4 is skipped if core is not present.

Two folder layouts are supported:

**Flat layout** (all schemas under a single `v2.1/` directory):
```
project/
├── core/                          ← core v2.1 schemas (needed for L4)
└── driver-network/
    └── v2.1/                      ← schema root
        ├── DriverJobResource/
        ├── DriverContract/
        ├── DriverPerformance/
        ├── driver-common/         ← shared types — NOT tested
        │   └── CodedValue/
        │       ├── attributes.jsonschema.yaml
        │       └── README.md
        └── ...
```

**Versioned layout** (each schema has its own version subfolder):
```
project/
├── core/                          ← core v2.1 schemas (needed for L4)
└── retail/
    ├── RetailResource/            ← schema root is the domain folder
    │   └── v2.1/
    │       ├── attributes.jsonschema.yaml
    │       ├── context.jsonld
    │       └── examples/
    ├── RetailOffer/
    │   └── v2.1/
    ├── RetailContract/
    │   └── v2.1/
    ├── retail-common/
    │   └── CodedValue/
    └── ...
```

**`{domain}-common/` folders are intentionally excluded from testing.** Auto-discovery scans
direct subdirectories of the schema root. For flat layout, it picks up folders that contain
`attributes.jsonschema.yaml` directly. For versioned layout, it detects `SchemaName/v2.1/attributes.jsonschema.yaml`
one level deeper. Shared type definitions in `{domain}-common/` are excluded either way.

If the user passes the domain root rather than the `v2.1/` subfolder, auto-detect the layout
and use the appropriate schema root.

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

**L1 — Nested `x-jsonld` instead of flat `x-jsonld-id`:** A property uses the nested form
`x-jsonld: { "@id": "prefix:prop" }` instead of the flat annotation `x-jsonld-id: "prefix:prop"`.
Fix: replace the nested `x-jsonld` with a flat `x-jsonld-id` property.

**L2 — Wrong `@import` value:** `context.jsonld` imports
`"https://schema.beckn.io/core/v2/context.jsonld"` (v2) instead of
`"https://schema.beckn.io/core/v2/context.jsonld#generalised"` (v2.1). Fix: update the
`@import` value in `context.jsonld`.

**L2 — Orphan properties in example:** An example payload's attribute block contains a
property that has no mapping in `context.jsonld`. Fix: either add the property to
`attributes.jsonschema.yaml` and `context.jsonld`, or remove it from the example.

**L3 A — False positives on `@context`/`@type`:** These are JSON-LD keywords, not domain
properties. The tester automatically skips any property starting with `@` during coverage
checks. If you see coverage failures for `@context` or `@type`, your tester scripts may
need updating — copy the latest scripts from this skill's `scripts/` directory.

**L3 B — Prefix alignment:** `x-jsonld-id` in `attributes.jsonschema.yaml` uses an undeclared or
wrong prefix. Fix: use the schema-specific prefix declared in `context.jsonld`.

**L3 C — Vocab coverage:** A class defined in `vocab.jsonld` has no type alias in
`context.jsonld`. Fix: add `"ClassName": "prefix:ClassName"` as a **string** value in
`context.jsonld`. The tester only recognizes string-form aliases like
`"ClassName": "prefix:ClassName"` — dict-form `"ClassName": {"@id": "prefix:ClassName"}`
will NOT pass.

**L4 — Block not found:** The test can't find the attribute block in the example payload.
The extractor tries both plain keys and `beckn:`-prefixed keys (since `beckn.yaml` uses
plain keys like `resources`, `offers`, `commitments` while examples may use either form).
For v2.1:
- `resourceAttributes` lives at `message.catalogs[].resources[].resourceAttributes` (or with `beckn:` prefix)
- `offerAttributes` lives at `message.catalogs[].offers[].offerAttributes`
- `contractAttributes` lives at `message.contract.contractAttributes`
- `commitmentAttributes` lives at `message.contract.commitments[].commitmentAttributes`
- `performanceAttributes` lives at `message.contract.performance[].performanceAttributes`
- `considerationAttributes` lives at `message.contract.consideration[].considerationAttributes`
- `settlementAttributes` lives at `message.contract.settlements[].settlementAttributes`
Also supports `message.catalog` (singular) as a flat catalog pattern for `resourceAttributes`.

**L4 — Cross-file `$ref` resolution failure:** A schema uses `allOf` with a `$ref` to
another schema's `attributes.jsonschema.yaml` (e.g., `../../RetailResource/v2.1/attributes.jsonschema.yaml#/...`).
The tester pre-loads these external references into its schema store. If the path is wrong
after a folder restructure, update the `$ref` paths in your `attributes.jsonschema.yaml`.

**L4 — `additionalProperties: false` blocking child properties:** When a child schema
extends a parent via `allOf`, the parent's `additionalProperties: false` blocks the child's
own properties during validation. The tester automatically relaxes this constraint, along
with `const` values (which conflict when child overrides `@context`/`@type`). If you still
see spurious failures, check that the parent schema reference resolves correctly.

**L4 — Schema validation failure:** An example attribute block doesn't match its schema.
Check required fields, property types, and enum values against `attributes.jsonschema.yaml`. Common
issues: `null` values where strings are expected (use `""` instead), wrong regex patterns
for time fields (use `^([01][0-9]|2[0-3]):[0-5][0-9]` for 24-hour time).

## Dependencies

- Python 3.8+
- `pyyaml` (`pip install pyyaml`)
- `jsonschema` (`pip install jsonschema`)
