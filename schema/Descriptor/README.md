# Descriptor

> **Canonical IRI:** [`https://schema.beckn.io/Descriptor`](https://schema.beckn.io/Descriptor)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for Descriptor in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | — | Use case specific JSON-LD context. This can change from use case to use case, even within a domain. |
| `@type` | `string` | ✅ | Type of the descriptor. The type can be overriden with a context-specific type |
| `longDesc` | `string` | — | Detailed description of the item |
| `shortDesc` | `string` | — | Short description of the item |
| `name` | `string` | — | Name of the entity being described |
| `thumbnailImage` | `string` (uri) | — | Name of the entity being described |
| `docs` | any[] | — | Links to downloadable documents |
| `mediaFile` | any[] | — | Links to multimedia files and images |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Descriptor` |
| JSON Schema (latest) | `https://schema.beckn.io/Descriptor/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Descriptor/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Descriptor/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
