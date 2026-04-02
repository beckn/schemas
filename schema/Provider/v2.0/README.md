# Provider — v2.0

Schema definition for Provider in the Beckn Protocol

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Provider/attributes.yaml](https://schema.beckn.io/Provider/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Provider/v2.0/attributes.yaml](https://schema.beckn.io/Provider/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Provider/attributes.jsonschema.yaml](https://schema.beckn.io/Provider/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Provider/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Provider/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Provider/context.jsonld](https://schema.beckn.io/Provider/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Provider/v2.0/context.jsonld](https://schema.beckn.io/Provider/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Provider/vocab.jsonld](https://schema.beckn.io/Provider/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Provider/v2.0/vocab.jsonld](https://schema.beckn.io/Provider/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `beckn:id` | yes | string | Unique identifier for the provider |
| `beckn:descriptor` | yes | $ref: https://schema.beckn.io/Descriptor/v2.1/attributes.yaml#/components/schemas/Descriptor | - |
| `beckn:validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.1/attributes.yaml#/components/schemas/TimePeriod | - |
| `beckn:locations` | no | array | Physical locations where the provider operates |
| `beckn:rateable` | no | boolean | Whether the provider can be rated by customers |
| `beckn:rating` | no | $ref: https://schema.beckn.io/Rating/v2.1/attributes.yaml#/components/schemas/Rating | - |
| `beckn:providerAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | - |
