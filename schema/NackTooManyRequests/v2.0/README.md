# NackTooManyRequests — v2.0

The synchronous rejection body returned when the responding NP has exceeded a request rate limit (AUT_RATE_LIMITED) or a policy-governed engagement capacity limit (POL_NP_CAPACITY_EXCEEDED). The caller MUST apply back-off before retrying. Implementations SHOULD include a Retry-After header on 429 responses.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/NackTooManyRequests/attributes.yaml](https://schema.beckn.io/NackTooManyRequests/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/NackTooManyRequests/v2.0/attributes.yaml](https://schema.beckn.io/NackTooManyRequests/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/NackTooManyRequests/attributes.jsonschema.yaml](https://schema.beckn.io/NackTooManyRequests/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/NackTooManyRequests/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/NackTooManyRequests/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/NackTooManyRequests/context.jsonld](https://schema.beckn.io/NackTooManyRequests/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/NackTooManyRequests/v2.0/context.jsonld](https://schema.beckn.io/NackTooManyRequests/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/NackTooManyRequests/vocab.jsonld](https://schema.beckn.io/NackTooManyRequests/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/NackTooManyRequests/v2.0/vocab.jsonld](https://schema.beckn.io/NackTooManyRequests/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `message` | yes | object | - |
