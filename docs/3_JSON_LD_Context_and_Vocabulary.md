# JSON-LD Context and Vocabulary

**Status:** Released  
**Author(s):** Ravi Prakash (FIDE / Beckn Foundation)  
**Created:** 2026-02-23  
**Updated:** 2026-02-23  
**Conformance impact:** Normative  
**Security/privacy implications:** No security or privacy implications identified.  
**Replaces / Relates to:** Normative companion to [20_JSONld_Context_and_Schema_Alignment.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/20_JSONld_Context_and_Schema_Alignment.md) in `protocol-specifications-v2`.

---

## Abstract

This document specifies how the Beckn Protocol Core Schema uses JSON-LD contexts and RDF vocabularies to provide machine-readable, globally unique semantics for every schema term. It describes the `beckn:` IRI namespace, the structure and purpose of `schema/context.jsonld` and `schema/vocab.jsonld`, the `@protected` context mechanism, and the rules for handling deprecated term aliases.

The key words MUST, SHOULD, and MAY in this document are used as defined in [2_Keyword_Definitions.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/2_Keyword_Definitions.md).

---

## 1. Context

The Beckn Protocol Core Schema defines approximately 90 schemas and hundreds of attribute terms. Without a formal semantic layer, these terms are ambiguous: the word `"address"` in one system might mean something different from `"address"` in another.

JSON-LD (JSON for Linking Data) resolves this ambiguity by mapping every term to a globally unique IRI (Internationalized Resource Identifier). A JSON document that references a JSON-LD context is simultaneously valid JSON and valid Linked Data — it can be processed as plain JSON by systems that do not use JSON-LD, and as RDF by systems that do.

---

## 2. The `beckn:` Namespace

All Beckn Protocol Core Schema terms are assigned IRIs within the `beckn:` namespace.

### 2.1 Namespace IRI

| Property | Value |
|---|---|
| **Prefix** | `beckn:` |
| **IRI** | `https://schema.beckn.io/core/v2.0/` |
| **Example term** | `beckn:Address` → `https://schema.beckn.io/core/v2.0/Address` |

### 2.2 Namespace Stability

The namespace IRI MUST NOT change for the lifetime of a Major version. When a Major version increment occurs (e.g., v3.0), a new namespace IRI is introduced (`https://schema.beckn.io/core/v3.0/`), and the v2.0 namespace is frozen.

Within the v2.0 namespace, IRIs assigned to deprecated terms MUST be retained indefinitely to ensure backward compatibility with existing Linked Data graphs.

---

## 3. `schema/context.jsonld` — The Root Context

### 3.1 Purpose

`schema/context.jsonld` is the root JSON-LD context for the entire Core Schema library. It is the single document that maps all core schema terms to their `beckn:` IRIs.

An implementor who references this document in a JSON-LD `@context` declaration gains access to the full Beckn core schema vocabulary:

```json
{
  "@context": "https://schema.beckn.io/core/v2.0/context.jsonld",
  "@type": "Catalog",
  "descriptor": {
    "name": "My Catalog"
  }
}
```

### 3.2 `@protected` Flag

The root context declares `"@protected": true` at the top level.

This means that no consuming document or domain pack MAY redefine any term declared in the root context. If a consuming document attempts to redefine a protected term, JSON-LD processors MUST raise an error.

This protection ensures that the semantic integrity of core terms cannot be accidentally overridden by domain-specific contexts.

**Normative rule:** Any domain schema pack that extends the core schema MUST NOT attempt to override or redefine any term in `schema/context.jsonld`.

### 3.3 Structure

```json
{
  "@context": {
    "@version": 1.1,
    "@protected": true,
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "beckn": "https://schema.beckn.io/core/v2.0/",
    "Address": "beckn:Address",
    "address": "beckn:address",
    ...
  }
}
```

### 3.4 Maintenance

The root context MUST be updated whenever:
- A new schema is added (its class term and all attribute terms MUST be added)
- An existing schema is modified with new attributes (the new terms MUST be added)
- A term is deprecated (the entry MUST be retained with an `@comment`)

---

## 4. `schema/vocab.jsonld` — The Root Vocabulary

### 4.1 Purpose

`schema/vocab.jsonld` is the RDF vocabulary document for the entire Core Schema library. It defines all schema classes and properties as RDF resources, enabling the schemas to be consumed by ontology tools, SPARQL queries, and Linked Data platforms.

### 4.2 Structure

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
      "@id": "beckn:Address",
      "@type": "rdfs:Class",
      "rdfs:label": "Address",
      "rdfs:comment": "A physical or postal address."
    },
    {
      "@id": "beckn:streetAddress",
      "@type": "rdf:Property",
      "rdfs:label": "streetAddress",
      "rdfs:domain": { "@id": "beckn:Address" },
      "rdfs:range": { "@id": "xsd:string" },
      "rdfs:comment": "The street address component."
    }
  ]
}
```

---

## 5. Per-Schema Contexts and Vocabularies

Each schema also has its own `context.jsonld` and `vocab.jsonld` files within its version directory. These per-schema files are subsets of the root aggregates.

They serve two purposes:
1. **Independent consumption** — a domain pack or tool that only uses one schema (e.g., `Address`) can reference just `schema/Address/v2.0/context.jsonld` without loading the full root context.
2. **Clarity** — the per-schema files make it easy to review all terms associated with a single schema in isolation.

The content of all per-schema context files MUST be consistent with the root `schema/context.jsonld`. If a discrepancy exists, the root context is authoritative.

---

## 6. Term Mapping Patterns

### 6.1 Simple Class Term

A schema class maps directly to a `beckn:` IRI:

```json
"Address": "beckn:Address"
```

### 6.2 Class Term with Nested Context

When attributes of a schema require disambiguation (e.g., `descriptor` is used in many schemas but each has a distinct IRI to enable separate SPARQL queries), a nested context is used:

```json
"Alert": {
  "@id": "beckn:Alert",
  "@context": {
    "descriptor": "beckn:alertDescriptor"
  }
}
```

### 6.3 Simple Property Term

```json
"address": "beckn:address"
```

### 6.4 Enumeration Property

When a property's value is drawn from a controlled vocabulary (an enum), the values MUST be mapped to IRIs:

```json
"paymentStatus": {
  "@id": "beckn:paymentStatus",
  "@type": "@id",
  "@context": {
    "PENDING": "beckn:PaymentPending",
    "COMPLETED": "beckn:PaymentCompleted",
    "FAILED": "beckn:PaymentFailed"
  }
}
```

This ensures that `"PENDING"` in a Beckn JSON document is unambiguously interpreted as `beckn:PaymentPending` — not as a plain string — when the document is processed as JSON-LD.

### 6.5 Deprecated Term Alias

When a term is deprecated and replaced by a new term, the original term entry MUST be retained in the context with:
- The `@id` pointing to the **new** (replacement) IRI (to preserve backward-compatible semantic equivalence)
- An `@comment` documenting the deprecation

```json
"Order": {
  "@id": "beckn:Contract",
  "@comment": "Deprecated. Use Contract instead. IRI preserved for backward compatibility."
},
"OrderItem": {
  "@id": "beckn:ContractItem",
  "@comment": "Deprecated. Use ContractItem instead. IRI preserved for backward compatibility."
}
```

This means that a legacy document using `"@type": "Order"` will be interpreted identically to a modern document using `"@type": "Contract"` when both reference the v2.0 context.

---

## 7. Using the Context in Practice

### 7.1 Referencing the Root Context (Recommended)

The simplest and most complete approach is to reference the root context by its canonical IRI:

```json
{
  "@context": "https://schema.beckn.io/core/v2.0/context.jsonld",
  "@type": "Contract",
  "contractNumber": "ORD-12345",
  "consumer": {
    "@type": "Consumer",
    "person": {
      "@type": "Person",
      "name": "Alice"
    }
  }
}
```

### 7.2 Referencing a Per-Schema Context

For lightweight use cases (e.g., validating only an `Address` object):

```json
{
  "@context": "https://raw.githubusercontent.com/beckn/common_schema/main/schema/Address/v2.0/context.jsonld",
  "@type": "Address",
  "streetAddress": "123 Main Street",
  "addressLocality": "Bengaluru",
  "postalCode": "560001"
}
```

### 7.3 Inline Context (Not Recommended)

Inline contexts are permitted by JSON-LD but SHOULD NOT be used in production Beckn implementations, as they cannot benefit from context caching and may conflict with the `@protected` declarations in the root context.

---

## 8. Conformance Requirements

| ID | Requirement | Level |
|---|---|---|
| JLD-01 | All core schema terms MUST be mapped to IRIs in the `beckn:` namespace | MUST |
| JLD-02 | The root `schema/context.jsonld` MUST declare `"@protected": true` | MUST |
| JLD-03 | Domain packs MUST NOT redefine any term declared in the root context | MUST |
| JLD-04 | Deprecated terms MUST retain their original context entry with an `@comment` | MUST |
| JLD-05 | Enum property values MUST be mapped to `beckn:` IRIs via `"@type": "@id"` | MUST |
| JLD-06 | Per-schema contexts MUST be consistent with the root context | MUST |
| JLD-07 | Inline contexts SHOULD NOT be used in production implementations | SHOULD NOT |

---

## 9. Security Considerations

The `@protected` flag in the root context prevents term hijacking by downstream consumers. Without it, a domain pack or consuming document could silently redefine a core term (e.g., redefine `"address"` to point to a different IRI), breaking semantic interoperability.

Implementors SHOULD use a controlled document loader that resolves `https://schema.beckn.io/core/v2.0/context.jsonld` to a trusted local copy or CDN-hosted version, to avoid runtime dependency on external HTTP resolution.

---

## 10. References

- [20_JSONld_Context_and_Schema_Alignment.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/20_JSONld_Context_and_Schema_Alignment.md)
- [2_Keyword_Definitions.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/2_Keyword_Definitions.md)
- [JSON-LD 1.1 — W3C Recommendation](https://www.w3.org/TR/json-ld11/)
- [JSON-LD 1.1 Processing Algorithms — W3C](https://www.w3.org/TR/json-ld11-api/)
- [RDF Schema 1.1 — W3C](https://www.w3.org/TR/rdf-schema/)
- [RFC 3987 — Internationalized Resource Identifiers](https://datatracker.ietf.org/doc/html/rfc3987)
- [2_Schema_Structure.md](./2_Schema_Structure.md)

---

## 11. Changelog

| Version | Date | Author | Summary |
|---|---|---|---|
| Draft-01 | 2026-02-23 | Ravi Prakash | Initial JSON-LD context and vocabulary specification |
