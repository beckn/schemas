# RetailCoreFulfillmentAttributes — v2.0

Retail-specific fulfillment attribute pack extending Beckn core Fulfillment. Used as the value of Fulfillment.fulfillmentAttributes for retail domain fulfillments. Covers supported fulfillment types, delivery endpoint, operating schedule, SLA semantics, and handling constraints.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/RetailCoreFulfillmentAttributes/attributes.yaml](https://schema.beckn.io/RetailCoreFulfillmentAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0/attributes.yaml](https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/RetailCoreFulfillmentAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/RetailCoreFulfillmentAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/RetailCoreFulfillmentAttributes/context.jsonld](https://schema.beckn.io/RetailCoreFulfillmentAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0/context.jsonld](https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/RetailCoreFulfillmentAttributes/vocab.jsonld](https://schema.beckn.io/RetailCoreFulfillmentAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0/vocab.jsonld](https://schema.beckn.io/RetailCoreFulfillmentAttributes/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | JSON-LD context URI for the retail fulfillment schema. |
| `@type` | yes | string | JSON-LD type for this attribute pack. |
| `supportedFulfillmentTypes` | no | array | Fulfillment modes supported by this provider for this offer. |
| `deliveryDetails` | no | object | Delivery endpoint details for DELIVERY fulfillment type. |
| `operatingHours` | no | array | Recurring store operating schedule. |
| `closures` | no | array | Explicit closure periods overriding operatingHours. |
| `sla` | no | object | Service level agreement for fulfillment. Indicates expected time bounds from the defined lifecycle event.  |
| `handling` | no | array | Special handling requirements for this fulfillment. |
