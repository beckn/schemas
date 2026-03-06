# Rating

> **Canonical IRI:** [`https://schema.beckn.io/Rating`](https://schema.beckn.io/Rating)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Aggregated rating information for an entity. Aligns with schema.org/AggregateRating semantics.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | — | — |
| `@type` | `string` | — | — |
| `ratingValue` | `number` | — | Rating value (typically 0-5) |
| `ratingCount` | `integer` | — | Number of ratings |
| `reviewText` | `string` | — | Optional textual review or comment |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Rating` |
| JSON Schema (latest) | `https://schema.beckn.io/Rating/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Rating/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Rating/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
