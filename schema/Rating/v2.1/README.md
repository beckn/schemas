# Rating — v2.1

Aggregated rating information for an entity. Aligns with schema.org/AggregateRating semantics.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Rating/attributes.yaml](https://schema.beckn.io/Rating/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Rating/v2.1/attributes.yaml](https://schema.beckn.io/Rating/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Rating/attributes.jsonschema.yaml](https://schema.beckn.io/Rating/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Rating/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/Rating/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Rating/context.jsonld](https://schema.beckn.io/Rating/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Rating/v2.1/context.jsonld](https://schema.beckn.io/Rating/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Rating/vocab.jsonld](https://schema.beckn.io/Rating/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Rating/v2.1/vocab.jsonld](https://schema.beckn.io/Rating/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | no | string | - |
| `@type` | no | string | - |
| `ratingValue` | no | number | Rating value (typically 0-5) |
| `ratingCount` | no | integer | Number of ratings |
| `reviewText` | no | string | Optional textual review or comment |
