# Schema Structure

**Status:** Released  
**Author(s):** Ravi Prakash (FIDE / Beckn Foundation)  
**Created:** 2026-02-23  
**Updated:** 2026-02-23  
**Conformance impact:** Normative  
**Security/privacy implications:** No security or privacy implications identified.  
**Replaces / Relates to:** Normative companion to [21_Schema_Pack_Contract.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/21_Schema_Pack_Contract.md). Aligned with [20_JSONld_Context_and_Schema_Alignment.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/20_JSONld_Context_and_Schema_Alignment.md).

---

## Abstract

This document specifies the normative directory layout, file naming conventions, and content requirements for every schema definition in the Beckn Protocol Core Schema repository. Conformance to this structure is REQUIRED for all schemas in this repository and RECOMMENDED for domain schema packs that reference it.

The key words MUST, SHOULD, and MAY in this document are used as defined in [2_Keyword_Definitions.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/2_Keyword_Definitions.md).

---

## 1. Context

The Beckn Protocol Core Schema library contains approximately 90 domain-agnostic schema definitions. Each schema needs to be independently discoverable, referenceable by URL, independently versionable, and semantically grounded in the `beckn:` JSON-LD namespace.

A consistent directory and file structure achieves all four goals simultaneously, without requiring a build toolchain or a registry service.

---

## 2. Directory Layout

### 2.1 Top-Level Structure

The repository MUST conform to the following top-level layout:

```
{repo-root}/
├── schema/
│   ├── context.jsonld      ← Root JSON-LD context (all schemas combined)
│   ├── vocab.jsonld        ← Root RDF vocabulary (all schemas combined)
│   ├── README.md           ← Index of all schemas
│   └── {SchemaName}/       ← One directory per schema (see § 2.2)
├── docs/                   ← RFC-style documentation
├── GOVERNANCE.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── LICENSE.md
└── README.md
```

### 2.2 Per-Schema Directory

Each schema MUST have its own directory under `schema/`, named using the schema's canonical PascalCase name.

Each schema directory MUST contain at least one version subdirectory.

```
schema/
└── {SchemaName}/
    └── v{MAJOR}.{MINOR}/
        ├── attributes.yaml    ← OpenAPI 3.1 component definition (REQUIRED)
        ├── context.jsonld     ← Per-schema JSON-LD context (REQUIRED)
        └── vocab.jsonld       ← Per-schema RDF vocabulary (REQUIRED)
```

**Example:**

```
schema/
└── Address/
    └── v2.0/
        ├── attributes.yaml
        ├── context.jsonld
        └── vocab.jsonld
```

---

## 3. Naming Conventions

### 3.1 Schema Directory Names

Schema directory names MUST:
- Use **PascalCase** (e.g., `FulfillmentStage`, not `fulfillment_stage` or `fulfillmentstage`)
- Match exactly the schema name used in `components.schemas.{SchemaName}` in `attributes.yaml`
- Match exactly the term used in `schema/context.jsonld`

### 3.2 Version Directory Names

Version directory names MUST follow the pattern `v{MAJOR}.{MINOR}`:
- `v2.0` — initial v2 release
- `v2.1` — minor addition (backward-compatible)
- `v3.0` — major/breaking change

A Patch-level change (documentation correction, no structural change) MUST NOT create a new version directory. The existing directory is updated in place.

### 3.3 File Names

The three files within each version directory MUST be named exactly:
- `attributes.yaml`
- `context.jsonld`
- `vocab.jsonld`

No other file names are permitted. Additional files (e.g., examples) MAY be placed in a subdirectory named `examples/`.

---

## 4. File: `attributes.yaml`

### 4.1 Purpose

`attributes.yaml` is the OpenAPI 3.1 component definition for the schema. It is the primary machine-readable source of truth for the schema's attribute structure, types, and constraints.

### 4.2 Required Structure

The file MUST conform to the following structure:

```yaml
openapi: 3.1.1
info:
  title: {SchemaName}
  description: |
    {Human-readable description of the schema.}
  version: {MAJOR}.{MINOR}.{PATCH}
  contact:
    name: Beckn Foundation
    url: https://beckn.org
  license:
    name: CC-BY-NC-SA-4.0
    url: https://creativecommons.org/licenses/by-nc-sa/4.0/

components:
  schemas:
    {SchemaName}:
      description: |
        {Full schema description.}
      type: object
      properties:
        ...
```

### 4.3 Constraints

- The `info.title` MUST match the schema directory name exactly.
- The `components.schemas` key MUST contain exactly one entry, named identically to the schema directory name.
- The `info.version` MUST use three-part semver (e.g., `2.0.0`).
- Required attributes MUST be listed in a `required:` array at the schema level.
- Deprecated attributes MUST be annotated with `deprecated: true` and a `description` citing the replacement.

### 4.4 `$ref` Usage

A schema MAY reference other core schemas via relative `$ref` paths:

```yaml
address:
  $ref: '../../Address/v2.0/attributes.yaml#/components/schemas/Address'
```

---

## 5. File: `context.jsonld`

### 5.1 Purpose

`context.jsonld` is the per-schema JSON-LD context. It maps the schema name and all its attribute names to IRIs in the `beckn:` namespace.

### 5.2 Required Structure

```json
{
  "@context": {
    "@version": 1.1,
    "beckn": "https://schema.beckn.io/core/v2.0/",
    "{SchemaName}": {
      "@id": "beckn:{SchemaName}"
    },
    "{attributeName}": "beckn:{attributeName}",
    ...
  }
}
```

### 5.3 Constraints

- The `beckn` prefix MUST resolve to `https://schema.beckn.io/core/v2.0/`.
- Every attribute defined in `attributes.yaml` MUST have a corresponding entry in `context.jsonld`.
- Attributes with `@type: @id` (i.e., enumeration values that are IRIs) MUST define their enumeration members in a nested `@context`.
- Deprecated term aliases MUST be preserved with an `@comment` noting the deprecation and the replacement IRI.

**Example — simple attribute:**
```json
"address": "beckn:address"
```

**Example — enumeration attribute:**
```json
"paymentStatus": {
  "@id": "beckn:paymentStatus",
  "@type": "@id",
  "@context": {
    "PENDING": "beckn:PaymentPending",
    "COMPLETED": "beckn:PaymentCompleted"
  }
}
```

**Example — deprecated alias:**
```json
"Order": {
  "@id": "beckn:Contract",
  "@comment": "Deprecated. Use Contract instead. IRI preserved for backward compatibility."
}
```

---

## 6. File: `vocab.jsonld`

### 6.1 Purpose

`vocab.jsonld` is the per-schema RDF vocabulary. It defines the RDF classes and properties for the schema, enabling the schema to be consumed as Linked Data.

### 6.2 Required Structure

```json
{
  "@context": {
    "beckn": "https://schema.beckn.io/core/v2.0/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "owl": "http://www.w3.org/2002/07/owl#"
  },
  "@graph": [
    {
      "@id": "beckn:{SchemaName}",
      "@type": "rdfs:Class",
      "rdfs:label": "{SchemaName}",
      "rdfs:comment": "{Description of the class.}"
    },
    {
      "@id": "beckn:{attributeName}",
      "@type": "rdf:Property",
      "rdfs:label": "{attributeName}",
      "rdfs:domain": { "@id": "beckn:{SchemaName}" },
      "rdfs:range": { "@id": "xsd:string" },
      "rdfs:comment": "{Description of the property.}"
    }
  ]
}
```

### 6.3 Constraints

- Every class defined in `attributes.yaml` MUST be declared as `rdfs:Class`.
- Every attribute defined in `attributes.yaml` MUST be declared as `rdf:Property` with an appropriate `rdfs:range`.
- Deprecated properties MUST be annotated with `owl:deprecated: true`.

---

## 7. Root Aggregates: `schema/context.jsonld` and `schema/vocab.jsonld`

In addition to the per-schema files, the repository maintains two root-level aggregates:

### 7.1 `schema/context.jsonld`

The root context is the union of all per-schema contexts. It MUST:
- Declare `"@protected": true` to prevent term redefinition by consuming documents
- Include every term defined across all per-schema `context.jsonld` files
- Declare the `beckn:` namespace prefix

The root context is the primary artifact used by implementors who want to reference all core schemas in a single JSON-LD `@context` declaration.

### 7.2 `schema/vocab.jsonld`

The root vocabulary is the union of all per-schema vocabularies. It MUST contain every class and property defined across all per-schema `vocab.jsonld` files.

---

## 8. Conformance Requirements

| ID | Requirement | Level |
|---|---|---|
| STR-01 | Each schema MUST have its own directory under `schema/` named in PascalCase | MUST |
| STR-02 | Each schema version MUST have a directory named `v{MAJOR}.{MINOR}` | MUST |
| STR-03 | Each version directory MUST contain `attributes.yaml`, `context.jsonld`, and `vocab.jsonld` | MUST |
| STR-04 | `attributes.yaml` MUST include a valid `openapi: 3.1.1` header | MUST |
| STR-05 | `attributes.yaml` MUST declare the schema under `components.schemas.{SchemaName}` | MUST |
| STR-06 | `context.jsonld` MUST map every attribute to a `beckn:` IRI | MUST |
| STR-07 | `vocab.jsonld` MUST declare the schema as `rdfs:Class` | MUST |
| STR-08 | The root `schema/context.jsonld` MUST be updated for any added or modified term | MUST |
| STR-09 | Deprecated terms MUST retain their `context.jsonld` entries with an `@comment` | MUST |
| STR-10 | Additional files MAY be placed in an `examples/` subdirectory | MAY |

---

## 9. Security Considerations

No security or privacy implications identified for the schema structure itself. See [GOVERNANCE.md](../GOVERNANCE.md) for access control and review requirements.

---

## 10. References

- [20_JSONld_Context_and_Schema_Alignment.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/20_JSONld_Context_and_Schema_Alignment.md)
- [21_Schema_Pack_Contract.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/21_Schema_Pack_Contract.md)
- [2_Keyword_Definitions.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/2_Keyword_Definitions.md)
- [OpenAPI Specification 3.1.1](https://spec.openapis.org/oas/v3.1.1)
- [JSON-LD 1.1 — W3C](https://www.w3.org/TR/json-ld11/)
- [RDF Schema 1.1 — W3C](https://www.w3.org/TR/rdf-schema/)
- [CONTRIBUTING.md](../CONTRIBUTING.md)

---

## 11. Changelog

| Version | Date | Author | Summary |
|---|---|---|---|
| Draft-01 | 2026-02-23 | Ravi Prakash | Initial normative schema structure specification |
