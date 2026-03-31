# FulfillmentMode — v2.0

Describes the mode of fulfillment. This is an extensible container allowing domain-specific fulfillment modes to be expressed via attributes.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FulfillmentMode/attributes.yaml](https://schema.beckn.io/FulfillmentMode/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FulfillmentMode/v2.0/attributes.yaml](https://schema.beckn.io/FulfillmentMode/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FulfillmentMode/attributes.jsonschema.yaml](https://schema.beckn.io/FulfillmentMode/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FulfillmentMode/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FulfillmentMode/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FulfillmentMode/context.jsonld](https://schema.beckn.io/FulfillmentMode/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FulfillmentMode/v2.0/context.jsonld](https://schema.beckn.io/FulfillmentMode/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FulfillmentMode/vocab.jsonld](https://schema.beckn.io/FulfillmentMode/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FulfillmentMode/v2.0/vocab.jsonld](https://schema.beckn.io/FulfillmentMode/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | no | string | - |
| `@type` | no | string | - |
| `id` | no | string | - |
| `descriptor` | no | $ref: https://schema.beckn.io/Descriptor/attributes.yaml#/components/schemas/Descriptor | - |
| `modeAttributes` | no | $ref: https://schema.beckn.io/Attributes/attributes.yaml#/components/schemas/Attributes | Domain-specific fulfillment mode attributes (e.g., delivery, pickup, reservation, digital) |
