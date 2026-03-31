# Tracking — v2.0

Non-streaming tracking handle per legacy semantics (url/transport/status).

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Tracking/attributes.yaml](https://schema.beckn.io/Tracking/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Tracking/v2.0/attributes.yaml](https://schema.beckn.io/Tracking/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Tracking/attributes.jsonschema.yaml](https://schema.beckn.io/Tracking/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Tracking/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Tracking/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Tracking/context.jsonld](https://schema.beckn.io/Tracking/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Tracking/v2.0/context.jsonld](https://schema.beckn.io/Tracking/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Tracking/vocab.jsonld](https://schema.beckn.io/Tracking/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Tracking/v2.0/vocab.jsonld](https://schema.beckn.io/Tracking/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `tl_method` | yes | string | Transport/method used to access the tracking handle. |
| `url` | yes | string | Link/handle to off-network tracking UI or endpoint. |
| `trackingStatus` | yes | string | - |
| `expires_at` | no | string | ISO 8601 expiry timestamp for the tracking handle. |
