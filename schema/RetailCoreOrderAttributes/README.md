# RetailCoreOrderAttributes

> **Canonical IRI:** [`https://schema.beckn.io/RetailCoreOrderAttributes`](https://schema.beckn.io/RetailCoreOrderAttributes)
> **Tags:** `retail`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for RetailCoreOrderAttributes in the Beckn Protocol v2.0.1

Retail-specific order attribute pack. Captures buyer preferences and
supplementary information attached at the order level, such as delivery
preferences, gifting, invoicing, and loyalty programme details.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI for the retail order schema. |
| `@type` | `string` | ✅ | Must be `beckn:RetailCoreOrderAttributes`. |
| `buyerInstructions` | `string` | — | Free-text instructions from the buyer to the seller. |
| `deliveryPreferences` | `object` | — | Preferences relating to delivery time, instructions, or contactless options. |
| `gift` | `object` | — | Gifting metadata such as message and wrapping preference. |
| `invoicePreferences` | `object` | — | Invoicing preferences including GST number or billing address. |
| `loyalty` | `object` | — | Loyalty programme details for earning or redeeming points. |
| `source` | `object` | — | Order source attribution details. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/RetailCoreOrderAttributes` |
| JSON Schema (latest) | `https://schema.beckn.io/RetailCoreOrderAttributes/v2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/RetailCoreOrderAttributes/v2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/RetailCoreOrderAttributes/v2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
