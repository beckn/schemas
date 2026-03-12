# RetailCoreFulfillmentAttributes — v2.0

> **Canonical IRI:** [`https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0`](https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0)

Schema definition for RetailCoreFulfillmentAttributes v2.0.

## Properties

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
| JSON Schema | `https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0` |
| context.jsonld | `https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0/context.jsonld` |
| vocab.jsonld | `https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0/vocab.jsonld` |
