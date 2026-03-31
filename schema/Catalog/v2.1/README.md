# Catalog — v2.1

Catalog schema for Beckn Protocol v2.0.0

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Catalog/attributes.yaml](https://schema.beckn.io/Catalog/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Catalog/v2.1/attributes.yaml](https://schema.beckn.io/Catalog/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Catalog/attributes.jsonschema.yaml](https://schema.beckn.io/Catalog/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Catalog/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/Catalog/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Catalog/context.jsonld](https://schema.beckn.io/Catalog/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Catalog/v2.1/context.jsonld](https://schema.beckn.io/Catalog/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Catalog/vocab.jsonld](https://schema.beckn.io/Catalog/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Catalog/v2.1/vocab.jsonld](https://schema.beckn.io/Catalog/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `bppId` | no | string | BPP (Beckn Protocol Provider) identifier that publishes this catalog |
| `bppUri` | no | string | Beckn Protocol API base URL of the BPP |
| `publishDirectives` | no | object | Directives controlling publish behavior for master/regular catalog flow. Deprecated and planned for removal in a future release. |
| `descriptor` | yes | allOf | Human / Agent-readable description of this catalog |
| `id` | yes | string | Unique identifier for the catalog |
| `isActive` | no | boolean | Whether the catalog is active |
| `offers` | no | array | Array of offers optionally linked to resources |
| `resources` | no | array | Array of generalized Resource entities in this catalog (new model) |
| `provider` | yes | $ref: https://schema.beckn.io/Provider/attributes.yaml#/components/schemas/Provider | - |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/attributes.yaml#/components/schemas/TimePeriod | The time period during which this catalog is valid |
