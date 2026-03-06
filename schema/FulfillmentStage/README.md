# Fulfillment Stage

> **Canonical IRI:** [`https://schema.beckn.io/FulfillmentStage`](https://schema.beckn.io/FulfillmentStage)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for FulfillmentStage in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | CPD |
| `@type` | `string` | ✅ | — |
| `id` | `string` | ✅ | A unique identifier for this stage of fulfillment |
| `instructions` | any[] | — | A set of instructions to follow during this stage of fulfillment |
| `preferences` | any[] | — | A extensible set of attributes that describe the fulfillment preferences |
| `start` | object | — | An extensible set of attributes that describe the criteria required to start this stage of fulfillment |
| `end` | any | — | An extensible set of attributes that describe the criteria required to end this stage of fulfillment |
| `fulfillmentStageAttributes` | any | — | An extensible set of attributes that describe this stage of fulfillment |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/FulfillmentStage` |
| JSON Schema (latest) | `https://schema.beckn.io/FulfillmentStage/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/FulfillmentStage/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/FulfillmentStage/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
