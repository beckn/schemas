# Fulfillment

> **Canonical IRI:** [`https://schema.beckn.io/Fulfillment`](https://schema.beckn.io/Fulfillment)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for Fulfillment in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI |
| `@type` | `string` | ✅ | — |
| `agent` | any | — | The entity that directly performs the fulfillment |
| `fulfillmentAttributes` | any | — | Extensible set of domain-specific attributes describing the fulfillment |
| `id` | `string` | — | Fulfillment identifier |
| `instructions` | any[] | — | — |
| `mode` | any | ✅ | Extensible set of attributes describing the mode of fulfillment. Varies with Industry Use Case |
| `participants` | any[] | — | A list of participants who are entitled to receive the fulfillment of the order. By default, it is the consumer who placed the order |
| `state` | any | — | The current state of fulfillment |
| `stages` | any[] | — | The various stages of the fulfillment |
| `trackingEnabled` | `boolean` | — | Whether tracking is enabled / possible for this fulfillment |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Fulfillment` |
| JSON Schema (latest) | `https://schema.beckn.io/Fulfillment/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Fulfillment/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Fulfillment/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
