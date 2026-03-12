# RetailCoreFulfillmentAttributes

> **Canonical IRI:** [`https://schema.beckn.io/RetailCoreFulfillmentAttributes`](https://schema.beckn.io/RetailCoreFulfillmentAttributes)
> **Tags:** `retail`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for RetailCoreFulfillmentAttributes in the Beckn Protocol v2.0.1

Retail-specific fulfillment attribute pack. Describes how a seller fulfills
orders — the fulfillment types supported, delivery details, operating hours,
closures, SLA commitments, and special handling instructions.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI for the retail fulfillment schema. |
| `@type` | `string` | ✅ | Must be `beckn:RetailCoreFulfillmentAttributes`. |
| `supportedFulfillmentTypes` | `array` | — | Fulfillment types supported by the provider (e.g. HOME_DELIVERY, STORE_PICKUP). |
| `deliveryDetails` | `object` | — | Details about delivery logistics such as radius, charges, and partner. |
| `operatingHours` | `array` | — | Operating hours windows during which fulfillment is available. |
| `closures` | `array` | — | Scheduled closure dates or holidays. |
| `sla` | `object` | — | Service level agreement for fulfillment, including preparation and delivery time. |
| `handling` | `object` | — | Special handling instructions (e.g. fragile, temperature-controlled). |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/RetailCoreFulfillmentAttributes` |
| JSON Schema (latest) | `https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
