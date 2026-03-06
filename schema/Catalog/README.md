# Catalog

> **Canonical IRI:** [`https://schema.beckn.io/Catalog`](https://schema.beckn.io/Catalog)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Catalog schema for Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI for the core Catalog schema |
| `@type` | `string` | ✅ | Type of the catalog |
| `bppId` | `string` | ✅ | BPP (Beckn Protocol Provider) identifier that publishes this catalog |
| `bppUri` | `string` (uri) | ✅ | BPP (Beckn Protocol Provider) URI endpoint |
| `descriptor` | any | ✅ | A verbal summary of the catalog for humans, AI agents, etc to read and understand the context. |
| `id` | `string` | ✅ | Unique identifier for the catalog |
| `isActive` | `boolean` | — | Whether the catalog is active |
| `items` | any[] | ✅ | Array of beckn core Item entities in this catalog |
| `offers` | any[] | — | — |
| `providerId` | `string` | — | Reference to the provider that owns this catalog |
| `validity` | any | — | The time period during which this catalog is valid |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Catalog` |
| JSON Schema (latest) | `https://schema.beckn.io/Catalog/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Catalog/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Catalog/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
