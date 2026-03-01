# Introduction to the Beckn Protocol Core Schema

**Status:** Released  
**Author(s):** Ravi Prakash (Beckn Labs)  
**Created:** 2026-02-23  
**Updated:** 2026-03-01  
**Conformance impact:** Informative  
**Security/privacy implications:** No security or privacy implications identified.  
**Replaces / Relates to:** Companion to [6_Schema_Distribution_Model.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/6_Schema_Distribution_Model.md) in `protocol-specifications-v2`.

---

## Abstract

This document introduces the Beckn Protocol Core Schema library. It describes what the library contains, why it exists as a separate repository, how it fits into the three-tier Beckn schema model, and how it relates to the broader `protocol-specifications-v2` specification.

---

## 1. Context

The Beckn Protocol v2 is an open interoperability protocol that enables value exchange across any industry domain — mobility, food delivery, healthcare, education, and beyond. At its heart, the protocol defines a set of standardised data structures (schemas) that all participants — buyers, sellers, platforms, and infrastructure services — use to exchange value.

In Beckn Protocol v1.x, all schema definitions lived inside a single monolithic YAML file. This created versioning friction: a change to one schema forced a version bump on all schemas, and domain-specific implementations had difficulty extending the schema without forking the whole specification.

Beckn Protocol v2 solves this with a **three-tier schema model**. The core schema library — this repository — is the second tier.

---

## 2. The Three-Tier Schema Model

The Beckn Protocol v2 schema model is organised into three tiers, each with a distinct scope and lifecycle:

```
┌─────────────────────────────────────────────────────────────────┐
│  Tier 1 — Transport Envelope                                    │
│  Repository: beckn/protocol-specifications-v2                   │
│  Contains: API request/response envelope, Context object,       │
│            RequestContainer, CallbackContainer, AckResponse     │
│  Namespace: defined per-release in protocol-specifications-v2   │
└────────────────────────┬────────────────────────────────────────┘
                         │ depends on
┌────────────────────────▼────────────────────────────────────────┐
│  Tier 2 — Core Schema  ◄  THIS REPOSITORY                       │
│  Repository: beckn/common_schema                                │
│  Contains: Domain-agnostic schemas (Address, Catalog, Item,     │
│            Fulfillment, Contract, Payment, etc.)                │
│  Namespace: https://schema.beckn.io/core/v2.0/                  │
└────────────────────────┬────────────────────────────────────────┘
                         │ extended by
┌────────────────────────▼────────────────────────────────────────┐
│  Tier 3 — Domain Schema Packs                                   │
│  Repository: one per industry vertical (e.g., beckn/mobility)   │
│  Contains: Domain-specific schemas that extend Tier 2 schemas   │
│  Namespace: defined per domain pack                             │
└─────────────────────────────────────────────────────────────────┘
```

### 2.1 Tier 1 — Transport Envelope

The transport envelope is the outermost layer of every Beckn API message. It defines the `Context` object (carrying transaction metadata such as `bapId`, `bppId`, `transactionId`, `messageId`, and the API action), the `RequestContainer` that wraps every outgoing message, and the `CallbackContainer` that wraps every callback response.

The transport envelope is defined in `beckn/protocol-specifications-v2`. It references Tier 2 schemas for the payload body.

### 2.2 Tier 2 — Core Schema (This Repository)

The core schema library contains all domain-agnostic schemas — the reusable building blocks that are meaningful across any industry. Examples:

- `Address` — a physical or postal address (used in mobility, commerce, healthcare, etc.)
- `Catalog` — a collection of items offered by a provider
- `Contract` — a formalised agreement between consumer and provider
- `Fulfillment` — a record of how an item or service will be delivered

Every schema in this tier is:
- **Domain-agnostic** — contains no industry-specific attributes
- **Versioned independently** — each schema has its own `v2.0/` directory
- **Semantically grounded** — every term maps to an IRI in the `beckn:` namespace via JSON-LD
- **OpenAPI 3.1 compatible** — available as `$ref`-able components

### 2.3 Tier 3 — Domain Schema Packs

Domain schema packs extend the core schemas for a specific industry vertical. A mobility domain pack might extend `Fulfillment` with `vehicleType` and `driverDetails`. A healthcare pack might extend `Item` with `dosage` and `prescriptionRequired`.

Domain packs live in separate repositories and reference this repository via `$ref` or JSON-LD `@import`. They do not modify the core schemas — they extend them.

---

## 3. What This Repository Contains

This repository (`beckn/common_schema`) contains:

| Path | Description |
|---|---|
| `schema/context.jsonld` | The unified JSON-LD context mapping all core schema terms to `beckn:` IRIs |
| `schema/vocab.jsonld` | The RDF vocabulary defining all classes and properties |
| `schema/{SchemaName}/v2.0/attributes.yaml` | OpenAPI 3.1 component definition for the schema |
| `schema/{SchemaName}/v2.0/context.jsonld` | Per-schema JSON-LD context |
| `schema/{SchemaName}/v2.0/vocab.jsonld` | Per-schema RDF vocabulary |
| `docs/` | This documentation |
| `GOVERNANCE.md` | Governance model |
| `CONTRIBUTING.md` | Contribution guidelines |
| `CHANGELOG.md` | Version history |

The current release is **v2.0**, corresponding to the Beckn Protocol v2.0 specification.

---

## 4. Why JSON-LD?

JSON-LD (JSON for Linking Data) allows the schemas in this library to be used in two ways simultaneously:

1. **As plain JSON** — any JSON document that conforms to the OpenAPI attribute definitions is valid. JSON-LD awareness is not required for basic protocol use.
2. **As Linked Data** — when a JSON-LD context is referenced, every term in the document maps to a globally unique IRI. This enables semantic interoperability, RDF graph construction, and ontology alignment.

The `beckn:` namespace (`https://schema.beckn.io/core/v2.0/`) is the canonical IRI base for all Beckn core schema terms.

---

## 5. Relationship to `protocol-specifications-v2`

The `protocol-specifications-v2` repository contains:
- The full protocol specification (25 RFC documents)
- The transport envelope schema (Tier 1)
- The governance model for the protocol as a whole

This repository (`common_schema`) contains only the Tier 2 core schema definitions. It has its own versioning lifecycle and governance model, aligned with but independent of the full protocol specification.

The most relevant cross-references in `protocol-specifications-v2` are:

| Document | What it covers |
|---|---|
| [6_Schema_Distribution_Model.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/6_Schema_Distribution_Model.md) | The three-tier model in full detail |
| [20_JSONld_Context_and_Schema_Alignment.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/20_JSONld_Context_and_Schema_Alignment.md) | JSON-LD context design rules that this repo follows |
| [21_Schema_Pack_Contract.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/21_Schema_Pack_Contract.md) | How domain packs extend the core schema |

---

## 6. Where to Go Next

| Goal | Document |
|---|---|
| Understand the schema directory layout | [2_Schema_Structure.md](./2_Schema_Structure.md) |
| Understand JSON-LD contexts and vocabularies | [3_JSON_LD_Context_and_Vocabulary.md](./3_JSON_LD_Context_and_Vocabulary.md) |
| Understand versioning and deprecation | [4_Versioning_and_Deprecation.md](./4_Versioning_and_Deprecation.md) |
| Contribute a new schema | [5_Contributing_Schemas.md](./5_Contributing_Schemas.md) |

---

## 7. References

- [6_Schema_Distribution_Model.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/6_Schema_Distribution_Model.md)
- [20_JSONld_Context_and_Schema_Alignment.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/20_JSONld_Context_and_Schema_Alignment.md)
- [21_Schema_Pack_Contract.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/21_Schema_Pack_Contract.md)
- [beckn/common_schema — GitHub](https://github.com/beckn/common_schema)
- [JSON-LD 1.1 Specification — W3C](https://www.w3.org/TR/json-ld11/)
- [OpenAPI Specification 3.1.1](https://spec.openapis.org/oas/v3.1.1)

---

## 8. Changelog

| Version | Date | Author | Summary |
|---|---|---|---|
| Draft-01 | 2026-02-23 | Ravi Prakash | Initial introduction document |
