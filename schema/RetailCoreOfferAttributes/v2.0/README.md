# RetailCoreOfferAttributes — v2.0

Retail-specific offer attribute pack, used as the value of Offer.offerAttributes for retail domain offers. Covers return/cancellation/replacement policies, payment constraints, serviceability (distance + timing), daily time window, and holidays.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/RetailCoreOfferAttributes/attributes.yaml](https://schema.beckn.io/RetailCoreOfferAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/RetailCoreOfferAttributes/v2.0/attributes.yaml](https://schema.beckn.io/RetailCoreOfferAttributes/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/RetailCoreOfferAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/RetailCoreOfferAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/RetailCoreOfferAttributes/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/RetailCoreOfferAttributes/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/RetailCoreOfferAttributes/context.jsonld](https://schema.beckn.io/RetailCoreOfferAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/RetailCoreOfferAttributes/v2.0/context.jsonld](https://schema.beckn.io/RetailCoreOfferAttributes/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/RetailCoreOfferAttributes/vocab.jsonld](https://schema.beckn.io/RetailCoreOfferAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/RetailCoreOfferAttributes/v2.0/vocab.jsonld](https://schema.beckn.io/RetailCoreOfferAttributes/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | JSON-LD context URI for the retail offer schema. |
| `@type` | yes | string | JSON-LD type for this attribute pack. |
| `policies` | no | object | - |
| `paymentConstraints` | no | object | - |
| `serviceability` | no | object | Additional serviceability constraints beyond geographic eligibility (handled via core Offer.eligibleRegion).  |
| `timeRange` | no | object | Daily time window applicable on the specified days. |
| `holidays` | no | array | Specific dates excluded from this offer's availability. |
