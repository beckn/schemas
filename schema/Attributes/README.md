# Attributes

> **Canonical IRI:** [`https://schema.beckn.io/Attributes`](https://schema.beckn.io/Attributes)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

JSON-LD aware container for domain-specific attributes of an Item. MUST include @context (URI) and @type (compact or full IRI). Any additional properties are allowed and interpreted per the provided JSON-LD context.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | Use case specific JSON-LD context URI |
| `@type` | `string` | ✅ | JSON-LD type defined within the context |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Attributes` |
| JSON Schema (latest) | `https://schema.beckn.io/Attributes/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Attributes/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Attributes/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
