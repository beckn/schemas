# CatalogProcessingResult — v2.0

Schema definition for CatalogProcessingResult in the Beckn Protocol v2.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CatalogProcessingResult/attributes.yaml](https://schema.beckn.io/CatalogProcessingResult/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CatalogProcessingResult/v2.0/attributes.yaml](https://schema.beckn.io/CatalogProcessingResult/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CatalogProcessingResult/attributes.jsonschema.yaml](https://schema.beckn.io/CatalogProcessingResult/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CatalogProcessingResult/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/CatalogProcessingResult/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CatalogProcessingResult/context.jsonld](https://schema.beckn.io/CatalogProcessingResult/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CatalogProcessingResult/v2.0/context.jsonld](https://schema.beckn.io/CatalogProcessingResult/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CatalogProcessingResult/vocab.jsonld](https://schema.beckn.io/CatalogProcessingResult/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CatalogProcessingResult/v2.0/vocab.jsonld](https://schema.beckn.io/CatalogProcessingResult/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `catalogId` | yes | string | The "id" of the submitted catalog |
| `status` | yes | string | Final processing outcome for this catalog |
| `itemCount` | no | integer | Number of items indexed (when accepted/partial) |
| `warnings` | no | array | Non-fatal issues encountered |
| `error` | no | $ref: https://schema.beckn.io/Error/attributes.yaml#/components/schemas/Error | - |
