# CatalogProcessingResult — v2.0

Processing result for a single catalog submission.

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
| `catalogId` | yes | string | Identifier of the submitted catalog |
| `status` | yes | string | Processing outcome. Using oneOf [string, object] to allow domain-specific status objects (e.g. beckn:CatalogAccepted) alongside standard string codes. |
| `errors` | no | array | Per-item or per-catalog errors (present when REJECTED or PARTIAL) |
| `stats` | no | object | Optional statistics about the processed catalog |
