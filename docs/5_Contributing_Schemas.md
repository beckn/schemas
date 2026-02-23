# Contributing Schemas

**Status:** Released  
**Author(s):** Ravi Prakash (FIDE / Beckn Foundation)  
**Created:** 2026-02-23  
**Updated:** 2026-02-23  
**Conformance impact:** Informative  
**Security/privacy implications:** No security or privacy implications identified.  
**Replaces / Relates to:** Companion to [CONTRIBUTING.md](../CONTRIBUTING.md) and [GOVERNANCE.md](../GOVERNANCE.md).

---

## Abstract

This document is a practical guide for contributors who wish to propose and author a new core schema, or modify an existing one, for the Beckn Protocol Core Schema library. It walks through the full lifecycle from initial proposal to merged PR, providing templates, decision criteria, and worked examples.

---

## 1. Introduction

The core schema library is intentionally minimal — it contains only schemas that are genuinely domain-agnostic and required for interoperability across the Beckn ecosystem. Before investing time in authoring a schema, contributors should verify that the proposed schema is an appropriate addition to the core library.

This document assumes familiarity with:
- The three-tier schema model ([1_Introduction.md](./1_Introduction.md))
- The schema directory and file structure ([2_Schema_Structure.md](./2_Schema_Structure.md))
- The JSON-LD context requirements ([3_JSON_LD_Context_and_Vocabulary.md](./3_JSON_LD_Context_and_Vocabulary.md))
- The versioning and deprecation policy ([4_Versioning_and_Deprecation.md](./4_Versioning_and_Deprecation.md))

---

## 2. Is This Schema Right for the Core Library?

Before proposing a new schema, ask the following questions:

| Question | If YES → | If NO → |
|---|---|---|
| Is this schema used across multiple industry domains? | Likely belongs in core | Likely belongs in a domain pack |
| Does this schema contain any domain-specific attributes (e.g., `vehicleType`, `prescriptionRequired`)? | Does NOT belong in core | May belong in core |
| Does an existing core schema already cover this concept? | Extend the existing schema | Propose a new schema |
| Is this schema a subset or specialisation of an existing core schema? | Extend via domain pack | Propose a new schema |
| Is this schema referenced by multiple other core schemas? | Likely belongs in core | Consider a domain pack |

If in doubt, open an issue with the label `schema-proposal` and discuss with the maintainers before investing in authoring.

---

## 3. Proposal Phase

### 3.1 Raise a GitHub Issue

Open a GitHub issue with the following information:

**Title:** `[Proposal] {SchemaName} — {one-line description}`

**Body:**
```
## Proposed Schema
Name: {SchemaName}

## Problem / Motivation
{Describe the gap in the current schema library. What use case does this schema enable that is not currently possible?}

## Domain Applicability
{List at least two industry domains where this schema would be used.}

## Proposed Attributes (draft)
{List the key attributes you anticipate. Exact naming can be refined later.}

## Existing Alternatives Considered
{List any existing schemas you considered reusing or extending, and why they are insufficient.}

## Change Classification
{Patch | Minor | Major}
```

### 3.2 Community Discussion

Allow at least **7 calendar days** for maintainer and community feedback before proceeding to implementation. For Minor changes, this is a courtesy. For Major changes, this wait is required by [GOVERNANCE.md](../GOVERNANCE.md).

---

## 4. Implementation Phase

### 4.1 Create the Directory

Create the schema directory at:

```
schema/{SchemaName}/v2.0/
```

Use the exact PascalCase name from your approved proposal.

### 4.2 Author `attributes.yaml`

Copy the template from [CONTRIBUTING.md § 4.1](../CONTRIBUTING.md) and fill in:

- `info.title` — exact PascalCase schema name
- `info.description` — one or two sentences describing what this schema represents and in what context it is used
- `info.version` — `2.0.0` for a new schema in the current release
- `components.schemas.{SchemaName}` — the full schema definition

**Attribute authoring guidelines:**

- Attribute names MUST use **camelCase** (e.g., `streetAddress`, not `street_address`)
- `type` MUST be declared for every property
- `description` MUST be provided for every property, in complete sentences
- Optional attributes MUST NOT appear in the `required` array
- Cross-references to other core schemas MUST use relative `$ref` paths

**Example — a new `SupportRequest` schema:**

```yaml
openapi: 3.1.1
info:
  title: SupportRequest
  description: |
    A request for support raised by a consumer or provider during a transaction.
  version: 2.0.0
  contact:
    name: Beckn Foundation
    url: https://beckn.org
  license:
    name: CC-BY-NC-SA-4.0
    url: https://creativecommons.org/licenses/by-nc-sa/4.0/

components:
  schemas:
    SupportRequest:
      description: |
        Represents a support request raised by a participant in a transaction.
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the support request.
        refId:
          type: string
          description: Reference to the transaction or contract to which this request relates.
        message:
          type: string
          description: The human-readable message describing the support issue.
      required:
        - id
```

### 4.3 Author `context.jsonld`

Map every attribute from `attributes.yaml` to a `beckn:` IRI.

For a new schema, all IRIs will be new — they are minted by placing the attribute name after the `beckn:` prefix.

```json
{
  "@context": {
    "@version": 1.1,
    "beckn": "https://schema.beckn.io/core/v2.0/",
    "SupportRequest": {
      "@id": "beckn:SupportRequest"
    },
    "refId": "beckn:refId",
    "message": "beckn:message"
  }
}
```

Note: `id` is already declared in the root context as `"id": "beckn:id"` and does not need to be re-declared in per-schema contexts.

### 4.4 Author `vocab.jsonld`

Declare the schema class and all properties as RDF resources.

```json
{
  "@context": {
    "beckn": "https://schema.beckn.io/core/v2.0/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@graph": [
    {
      "@id": "beckn:SupportRequest",
      "@type": "rdfs:Class",
      "rdfs:label": "SupportRequest",
      "rdfs:comment": "A support request raised by a participant in a transaction."
    },
    {
      "@id": "beckn:refId",
      "@type": "rdf:Property",
      "rdfs:label": "refId",
      "rdfs:domain": { "@id": "beckn:SupportRequest" },
      "rdfs:range": { "@id": "xsd:string" },
      "rdfs:comment": "Reference to the transaction or contract."
    },
    {
      "@id": "beckn:message",
      "@type": "rdf:Property",
      "rdfs:label": "message",
      "rdfs:domain": { "@id": "beckn:SupportRequest" },
      "rdfs:range": { "@id": "xsd:string" },
      "rdfs:comment": "Human-readable description of the support issue."
    }
  ]
}
```

### 4.5 Update `schema/context.jsonld`

Add the new class and attribute terms to the root context. Terms that are already present (e.g., `id`, `message`) MUST NOT be duplicated.

```json
"SupportRequest": "beckn:SupportRequest",
"refId": "beckn:refId"
```

### 4.6 Update `schema/README.md`

Add the new schema to the alphabetically ordered schema list in `schema/README.md`.

### 4.7 Update `CHANGELOG.md`

Add a line under `### Added` in the current version entry:

```
- `SupportRequest` — A support request raised by a participant in a transaction
```

---

## 5. Modifying an Existing Schema

To add an optional attribute to an existing schema:

1. Add the attribute to `attributes.yaml` (do NOT add it to `required`)
2. Add the term to the per-schema `context.jsonld`
3. Add the property declaration to the per-schema `vocab.jsonld`
4. Add the term to the root `schema/context.jsonld`
5. Update `CHANGELOG.md`
6. If this is the first change to the schema since it was released, classify as **Minor** and refer to [4_Versioning_and_Deprecation.md](./4_Versioning_and_Deprecation.md) for whether a new version directory is needed

---

## 6. Pull Request

When all files are in place and validated:

1. Open a pull request against the `main` branch
2. Reference the issue number in the PR description
3. Complete the checklist in [CONTRIBUTING.md § 7](../CONTRIBUTING.md)
4. Request review from a Maintainer

---

## 7. References

- [1_Introduction.md](./1_Introduction.md)
- [2_Schema_Structure.md](./2_Schema_Structure.md)
- [3_JSON_LD_Context_and_Vocabulary.md](./3_JSON_LD_Context_and_Vocabulary.md)
- [4_Versioning_and_Deprecation.md](./4_Versioning_and_Deprecation.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
- [GOVERNANCE.md](../GOVERNANCE.md)
- [21_Schema_Pack_Contract.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/21_Schema_Pack_Contract.md)

---

## 8. Changelog

| Version | Date | Author | Summary |
|---|---|---|---|
| Draft-01 | 2026-02-23 | Ravi Prakash | Initial contributing schemas guide |
