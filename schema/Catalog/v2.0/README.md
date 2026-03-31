# Catalog — v2.0

Schema definition for Catalog in the Beckn Protocol

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Catalog/attributes.yaml](https://schema.beckn.io/Catalog/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Catalog/v2.0/attributes.yaml](https://schema.beckn.io/Catalog/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Catalog/attributes.jsonschema.yaml](https://schema.beckn.io/Catalog/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Catalog/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Catalog/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Catalog/context.jsonld](https://schema.beckn.io/Catalog/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Catalog/v2.0/context.jsonld](https://schema.beckn.io/Catalog/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Catalog/vocab.jsonld](https://schema.beckn.io/Catalog/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Catalog/v2.0/vocab.jsonld](https://schema.beckn.io/Catalog/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | JSON-LD context URI for the core Catalog schema |
| `@type` | yes | string | Type of the catalog |
| `beckn:id` | yes | string | Unique identifier for the catalog |
| `beckn:descriptor` | yes | $ref: https://schema.beckn.io/Descriptor/attributes.yaml#/components/schemas/Descriptor | - |
| `beckn:providerId` | no | string | Reference to the provider that owns this catalog |
| `beckn:bppId` | yes | string | BPP (Beckn Protocol Provider) identifier that publishes this catalog |
| `beckn:bppUri` | yes | string | BPP (Beckn Protocol Provider) URI endpoint |
| `beckn:validity` | no | $ref: https://schema.beckn.io/TimePeriod/attributes.yaml#/components/schemas/TimePeriod | - |
| `beckn:isActive` | no | boolean | Whether the catalog is active |
| `beckn:items` | yes | array | Array of beckn core Item entities in this catalog, returned directly without ItemResult wrapper for improved performance and simplified response structure  |
| `beckn:offers` | no | array | - |
