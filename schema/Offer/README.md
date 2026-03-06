# Offer

> **Canonical IRI:** [`https://schema.beckn.io/Offer`](https://schema.beckn.io/Offer)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for Offer in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI for the core offer schema |
| `@type` | `string` | ✅ | TPD |
| `acceptedPaymentMethod` | object | — | — |
| `addOnItems` | [id](../id/README.md)[] | — | Optional extras modeled as items (e.g., toppings, accessories) |
| `addOns` | [id](../id/README.md)[] | — | Optional extra Offers that can be attached (e.g., warranty, gift wrap) |
| `constraints` | any[] | — | — |
| `descriptor` | object | ✅ | — |
| `eligibleRegion` | any[] | — | Regions where the offer is eligible |
| `id` | `string` | ✅ | Unique id for this offer |
| `isActive` | `boolean` | — | Whether the offer is active |
| `items` | [id](../id/README.md)[] | ✅ | Base item(s) the offer applies to (single or bundle) |
| `offerAttributes` | any | — | Attribute Pack attachment (pricing models, discounts, rail terms, etc.) |
| `policies` | any[] | — | — |
| `price` | any | — | Price snapshot; detailed models can live in offerAttributes |
| `provider` | [id](../id/README.md) | ✅ | Seller / provider of this offer |
| `validity` | any | — | Offer validity window |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Offer` |
| JSON Schema (latest) | `https://schema.beckn.io/Offer/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Offer/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Offer/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
