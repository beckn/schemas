# Fulfillment Mode

> **Canonical IRI:** [`https://schema.beckn.io/FulfillmentMode`](https://schema.beckn.io/FulfillmentMode)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Describes the mode of fulfillment. This is an extensible container allowing domain-specific fulfillment modes to be expressed via attributes.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | — | — |
| `@type` | `string` | — | — |
| `id` | `string` | — | — |
| `descriptor` | object | — | — |
| `modeAttributes` | any | — | Domain-specific fulfillment mode attributes (e.g., delivery, pickup, reservation, digital) |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/FulfillmentMode` |
| JSON Schema (latest) | `https://schema.beckn.io/FulfillmentMode/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/FulfillmentMode/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/FulfillmentMode/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
