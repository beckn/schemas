# ServerError — v2.0

Internal failure on the network participant's application; the request could not be processed. The response body MAY contain an `error` object with additional details.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/ServerError/attributes.yaml](https://schema.beckn.io/ServerError/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/ServerError/v2.0/attributes.yaml](https://schema.beckn.io/ServerError/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/ServerError/attributes.jsonschema.yaml](https://schema.beckn.io/ServerError/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/ServerError/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/ServerError/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/ServerError/context.jsonld](https://schema.beckn.io/ServerError/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/ServerError/v2.0/context.jsonld](https://schema.beckn.io/ServerError/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/ServerError/vocab.jsonld](https://schema.beckn.io/ServerError/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/ServerError/v2.0/vocab.jsonld](https://schema.beckn.io/ServerError/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `error` | no | $ref: https://schema.beckn.io/Error/v2.0/attributes.yaml#/components/schemas/Error | - |
