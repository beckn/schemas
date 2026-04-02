# Intent — v2.0

A declaration of an intent to transact

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Intent/attributes.yaml](https://schema.beckn.io/Intent/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Intent/v2.0/attributes.yaml](https://schema.beckn.io/Intent/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Intent/attributes.jsonschema.yaml](https://schema.beckn.io/Intent/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Intent/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Intent/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Intent/context.jsonld](https://schema.beckn.io/Intent/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Intent/v2.0/context.jsonld](https://schema.beckn.io/Intent/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Intent/vocab.jsonld](https://schema.beckn.io/Intent/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Intent/v2.0/vocab.jsonld](https://schema.beckn.io/Intent/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `textSearch` | no | string | Free text search query for items |
| `filters` | no | object | Filter criteria for items |
| `spatial` | no | array | Optional array of spatial constraints (CQL2-JSON semantics). |
| `mediaSearch` | no | $ref: https://schema.beckn.io/MediaSearch/v2.0/attributes.yaml#/components/schemas/MediaSearch | - |
