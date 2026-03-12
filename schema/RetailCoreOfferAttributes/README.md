# RetailCoreOfferAttributes

> **Canonical IRI:** [`https://schema.beckn.io/RetailCoreOfferAttributes`](https://schema.beckn.io/RetailCoreOfferAttributes)
> **Tags:** `retail`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for RetailCoreOfferAttributes in the Beckn Protocol v2.0.1

Retail-specific offer attribute pack. Defines the constraints and eligibility
conditions under which an offer (coupon, discount, promotion) is applicable.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

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
| Canonical IRI | `https://schema.beckn.io/RetailCoreOfferAttributes` |
| JSON Schema (latest) | `https://schema.beckn.io/RetailCoreOfferAttributes/v2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/RetailCoreOfferAttributes/v2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/RetailCoreOfferAttributes/v2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
