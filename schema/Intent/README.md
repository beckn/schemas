# Intent

> **Canonical IRI:** [`https://schema.beckn.io/Intent`](https://schema.beckn.io/Intent)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

A declaration of an intent to discover catalogs.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `textSearch` | `string` | — | Free text search query for items |
| `filters` | object | — | Filter criteria for items |
| `spatial` | any[] | — | Optional array of spatial constraints (CQL2-JSON semantics). |
| `media_search` | object | — | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Intent` |
| JSON Schema (latest) | `https://schema.beckn.io/Intent/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Intent/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Intent/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
