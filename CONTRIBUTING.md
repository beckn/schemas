# Contributing to Beckn Protocol Core Schema

**Status:** Released  
**Author(s):** Ravi Prakash (FIDE / Beckn Foundation)  
**Created:** 2026-02-23  
**Updated:** 2026-02-23  
**Conformance impact:** Informative  
**Security/privacy implications:** No security or privacy implications identified.  
**Replaces / Relates to:** Companion to [GOVERNANCE.md](./GOVERNANCE.md).

---

## Abstract

This document describes how to contribute to the Beckn Protocol Core Schema repository — from reporting issues to authoring new schemas and submitting pull requests.

---

## 1. Introduction

Contributions are welcome from all participants in the Beckn ecosystem. Before contributing, please read both this document and the [GOVERNANCE.md](./GOVERNANCE.md), which defines the change classification system (Patch / Minor / Major / Informative) and the decision-making process.

All contributors MUST abide by the [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

The key words MUST, SHOULD, and MAY in this document are used as defined in [2_Keyword_Definitions.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/2_Keyword_Definitions.md).

---

## 2. Ways to Contribute

| Contribution type | How to start |
|---|---|
| Report a schema error | Open a GitHub issue using the **Schema Bug** template |
| Propose a new schema | Open a GitHub issue using the **Schema Proposal** template |
| Propose a change to an existing schema | Open a GitHub issue describing the change and its impact |
| Fix documentation | Open a PR directly; no issue required for Informative changes |
| Request a deprecation | Open a GitHub issue with the label `deprecation` |

---

## 3. Setting Up Locally

No build toolchain is required. The repository contains plain YAML, JSON-LD, and Markdown files.

```bash
git clone git@github.com:beckn/common_schema.git
cd common_schema
```

A YAML linter and a JSON-LD validator are recommended before submitting a PR:

```bash
# YAML lint (requires yamllint)
yamllint schema/

# JSON-LD validation (requires jsonld-cli or similar)
jsonld validate schema/context.jsonld
```

---

## 4. Authoring a New Schema

A new core schema MUST satisfy all of the following before being accepted:

1. **Domain-agnostic** — it MUST NOT contain any industry-specific or domain-specific attributes. Those belong in domain schema packs.
2. **Minimal** — it SHOULD contain only attributes required for interoperability. Avoid speculative attributes.
3. **Named in PascalCase** — e.g., `FulfillmentStage`, not `fulfillment_stage` or `fulfillmentstage`.
4. **Placed in the correct directory** — `schema/{SchemaName}/v2.0/`
5. **Three files provided** — `attributes.jsonschema.yaml`, `context.jsonld`, and `vocab.jsonld` (see [`docs/2_Schema_Structure.md`](./docs/2_Schema_Structure.md))
6. **JSON-LD context updated** — the new schema's term MUST be added to `schema/context.jsonld`
7. **`schema/README.md` updated** — the schema list MUST include the new schema

### 4.1 `attributes.jsonschema.yaml` Template

```yaml
openapi: 3.1.1
info:
  title: {SchemaName}
  description: |
    {Description of what this schema represents.}
  version: 2.0.0
  contact:
    name: Beckn Foundation
    url: https://beckn.org
  license:
    name: CC-BY-NC-SA 4.0 International
    url: https://creativecommons.org/licenses/by-nc-sa/4.0/

components:
  schemas:
    {SchemaName}:
      description: |
        {Full schema description.}
      type: object
      properties:
        id:
          type: string
          description: Unique identifier.
```

### 4.2 `context.jsonld` Template

```json
{
  "@context": {
    "@version": 1.1,
    "beckn": "https://schema.beckn.io/core/v2.0/",
    "{SchemaName}": {
      "@id": "beckn:{SchemaName}"
    }
  }
}
```

### 4.3 `vocab.jsonld` Template

```json
{
  "@context": {
    "beckn": "https://schema.beckn.io/core/v2.0/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@graph": [
    {
      "@id": "beckn:{SchemaName}",
      "@type": "rdfs:Class",
      "rdfs:label": "{SchemaName}",
      "rdfs:comment": "{Description.}"
    }
  ]
}
```

---

## 5. Modifying an Existing Schema

Before modifying an existing schema, classify your change using the table in [GOVERNANCE.md § 5.1](./GOVERNANCE.md).

- **Patch** changes (e.g., correcting a `description` field) MAY be submitted as a direct PR.
- **Minor** changes (e.g., adding an optional attribute) MUST update all three files (`attributes.jsonschema.yaml`, `context.jsonld`, `vocab.jsonld`) and the root `schema/context.jsonld`.
- **Major** changes (e.g., renaming a term or removing a required attribute) MUST follow the deprecation process in [GOVERNANCE.md § 6.1](./GOVERNANCE.md) and MUST include a migration guide.

---

## 6. Deprecating a Schema or Attribute

To deprecate a schema or attribute:

1. Add `deprecated: true` to the relevant property or schema in `attributes.jsonschema.yaml`, with a `description` noting the replacement.
2. Add an `@comment` in the relevant entry in `schema/context.jsonld` noting the deprecated status and the replacement IRI.
3. Retain the per-schema `context.jsonld` and `vocab.jsonld` files unchanged (for backward compatibility).
4. Add a deprecation entry to `CHANGELOG.md`.
5. Open a PR with the label `deprecation`.

Deprecated schemas MUST NOT be removed until a subsequent Major version release.

---

## 7. Pull Request Checklist

Before requesting review, verify that your PR satisfies all of the following:

- [ ] Schema directory structure follows [`docs/2_Schema_Structure.md`](./docs/2_Schema_Structure.md)
- [ ] All three schema files are present and consistent (`attributes.jsonschema.yaml`, `context.jsonld`, `vocab.jsonld`)
- [ ] `schema/context.jsonld` has been updated for any added, renamed, or deprecated terms
- [ ] `schema/README.md` schema list has been updated
- [ ] `CHANGELOG.md` has been updated with the appropriate entry
- [ ] Change is classified correctly (Patch / Minor / Major / Informative)
- [ ] For Major changes: deprecation notices are present and a migration guide is included
- [ ] YAML is valid (run `yamllint schema/`)
- [ ] JSON-LD is valid (run `jsonld validate schema/context.jsonld`)

---

## 8. Commit Message Format

Use the following format for commit messages:

```
<type>(<scope>): <short description>

[optional body]

[optional footer: Closes #<issue>]
```

Where `<type>` is one of:
- `feat` — new schema or attribute
- `fix` — schema correction
- `deprecate` — deprecation of a schema or attribute
- `docs` — documentation-only change
- `chore` — housekeeping (`.gitignore`, tooling, etc.)

**Examples:**
```
feat(FulfillmentStage): add optional `authorization` attribute
fix(Address): correct postalCode description
deprecate(Order): alias maintained; replaced by Contract
docs(2_Schema_Structure): clarify vocab.jsonld requirements
```

---

## 9. References

- [GOVERNANCE.md](./GOVERNANCE.md)
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
- [docs/2_Schema_Structure.md](./docs/2_Schema_Structure.md)
- [docs/3_JSON_LD_Context_and_Vocabulary.md](./docs/3_JSON_LD_Context_and_Vocabulary.md)
- [2_Keyword_Definitions.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/2_Keyword_Definitions.md)

---

## 10. Changelog

| Version | Date | Author | Summary |
|---|---|---|---|
| Draft-01 | 2026-02-23 | Ravi Prakash | Initial contributing guide |
