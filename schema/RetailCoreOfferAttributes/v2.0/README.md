# RetailCoreOfferAttributes — v2.0

> **Canonical IRI:** [`https://schema.beckn.io/RetailCoreOfferAttributes/v2.0`](https://schema.beckn.io/RetailCoreOfferAttributes/v2.0)

Schema definition for RetailCoreOfferAttributes v2.0.

## Properties

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI for the retail offer schema. |
| `@type` | `string` | ✅ | Must be `beckn:RetailCoreOfferAttributes`. |
| `policies` | `object` | — | Coupon-level policies such as single-use, stacking, and minimum order value. |
| `paymentConstraints` | `object` | — | Eligible payment methods and instruments for this offer. |
| `serviceability` | `object` | — | Geographic or delivery-mode serviceability constraints for the offer. |
| `timeRange` | `object` | — | Validity window for the offer. |
| `holidays` | `array` | — | Dates on which the offer is not valid. |

## Linked Data

| Resource | URL |
|----------|-----|
| JSON Schema | `https://schema.beckn.io/RetailCoreOfferAttributes/v2.0` |
| context.jsonld | `https://schema.beckn.io/RetailCoreOfferAttributes/v2.0/context.jsonld` |
| vocab.jsonld | `https://schema.beckn.io/RetailCoreOfferAttributes/v2.0/vocab.jsonld` |
