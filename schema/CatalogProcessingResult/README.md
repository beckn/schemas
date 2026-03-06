# Catalog Processing Result

> **Canonical IRI:** [`https://schema.beckn.io/CatalogProcessingResult`](https://schema.beckn.io/CatalogProcessingResult)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for CatalogProcessingResult in the Beckn Protocol v2.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `catalogId` | `string` | ✅ | The "id" of the submitted catalog |
| `status` | `string` | ✅ | Final processing outcome for this catalog |
| `itemCount` | `integer` | — | Number of items indexed (when accepted/partial) |
| `warnings` | any[] | — | Non-fatal issues encountered |
| `error` | object | — | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/CatalogProcessingResult` |
| JSON Schema (latest) | `https://schema.beckn.io/CatalogProcessingResult/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/CatalogProcessingResult/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/CatalogProcessingResult/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
