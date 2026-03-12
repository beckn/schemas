# RetailCoreOrderAttributes — v2.0

> **Canonical IRI:** [`https://schema.beckn.io/RetailCoreOrderAttributes/v2.0`](https://schema.beckn.io/RetailCoreOrderAttributes/v2.0)

Schema definition for RetailCoreOrderAttributes v2.0.

## Properties

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
| JSON Schema | `https://schema.beckn.io/RetailCoreOrderAttributes/v2.0` |
| context.jsonld | `https://schema.beckn.io/RetailCoreOrderAttributes/v2.0/context.jsonld` |
| vocab.jsonld | `https://schema.beckn.io/RetailCoreOrderAttributes/v2.0/vocab.jsonld` |
