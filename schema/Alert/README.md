# Alert

> **Canonical IRI:** [`https://schema.beckn.io/Alert`](https://schema.beckn.io/Alert)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for Alert in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | — |
| `@type` | `string` | ✅ | — |
| `affectedEntities` | string[] | — | IDs of entities affected (route/order/fulfillment/etc.) |
| `descriptor` | object | ✅ | — |
| `id` | `string` | ✅ | — |
| `severity` | `string` | — | — |
| `validity` | object | — | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Alert` |
| JSON Schema (latest) | `https://schema.beckn.io/Alert/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Alert/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Alert/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
