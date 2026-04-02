# Alert — v2.0

Schema definition for Alert in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Alert/attributes.yaml](https://schema.beckn.io/Alert/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Alert/v2.0/attributes.yaml](https://schema.beckn.io/Alert/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Alert/attributes.jsonschema.yaml](https://schema.beckn.io/Alert/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Alert/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Alert/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Alert/context.jsonld](https://schema.beckn.io/Alert/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Alert/v2.0/context.jsonld](https://schema.beckn.io/Alert/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Alert/vocab.jsonld](https://schema.beckn.io/Alert/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Alert/v2.0/vocab.jsonld](https://schema.beckn.io/Alert/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `affectedEntities` | no | array | IDs of entities affected (route/order/fulfillment/etc.) |
| `descriptor` | yes | $ref: https://schema.beckn.io/Descriptor/v2.1/attributes.yaml#/components/schemas/Descriptor | - |
| `id` | yes | string | - |
| `severity` | no | string | - |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.1/attributes.yaml#/components/schemas/TimePeriod | - |
