# RetailCoreOrderAttributes — v2.0

Retail-specific order-level attributes that extend core Beckn Order. Used as the value of Order.orderAttributes for retail domain orders. Captures transaction-instance metadata relevant to retail domains without duplicating core Order semantics.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/RetailCoreOrderAttributes/attributes.yaml](https://schema.beckn.io/RetailCoreOrderAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/RetailCoreOrderAttributes/v2.0/attributes.yaml](https://schema.beckn.io/RetailCoreOrderAttributes/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/RetailCoreOrderAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/RetailCoreOrderAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/RetailCoreOrderAttributes/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/RetailCoreOrderAttributes/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/RetailCoreOrderAttributes/context.jsonld](https://schema.beckn.io/RetailCoreOrderAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/RetailCoreOrderAttributes/v2.0/context.jsonld](https://schema.beckn.io/RetailCoreOrderAttributes/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/RetailCoreOrderAttributes/vocab.jsonld](https://schema.beckn.io/RetailCoreOrderAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/RetailCoreOrderAttributes/v2.0/vocab.jsonld](https://schema.beckn.io/RetailCoreOrderAttributes/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | JSON-LD context URI for the retail order schema. |
| `@type` | yes | string | JSON-LD type for this attribute pack. |
| `buyerInstructions` | no | string | Special instructions provided by buyer for this order. |
| `deliveryPreferences` | no | object | Buyer-specified delivery handling preferences during negotiation. Final confirmed schedule should be reflected in core Fulfillment.start/end.  |
| `gift` | no | object | - |
| `invoicePreferences` | no | object | Buyer-provided invoicing details/preferences (if applicable). |
| `loyalty` | no | object | Loyalty / rewards program details. |
| `source` | no | object | Attribution / source metadata for the order (channel/campaign). |
