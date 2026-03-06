# Retail Core Order

> **Canonical IRI:** [`https://schema.beckn.io/RetailCoreOrder`](https://schema.beckn.io/RetailCoreOrder)
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Retail-specific order-level attributes that extend core Beckn Order. These attributes capture transaction-instance metadata relevant to retail domains without duplicating core Order semantics.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `buyerInstructions` | `string` | — | Special instructions provided by buyer for this order. |
| `deliveryPreferences` | object | — | Buyer-specified delivery handling preferences during negotiation. Final confirmed schedule should be reflected in core Fulfillment.start/end. |
| `gift` | object | — | — |
| `invoicePreferences` | object | — | Buyer-provided invoicing details/preferences (if applicable). |
| `loyalty` | object | — | Loyalty / rewards program details. |
| `source` | object | — | Attribution / source metadata for the order (channel/campaign). |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/RetailCoreOrder` |
| JSON Schema (latest) | `https://schema.beckn.io/RetailCoreOrder/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/RetailCoreOrder/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/RetailCoreOrder/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
