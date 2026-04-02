# TrackingRequest — v2.0

Schema definition for TrackingRequest in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/TrackingRequest/attributes.yaml](https://schema.beckn.io/TrackingRequest/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/TrackingRequest/v2.0/attributes.yaml](https://schema.beckn.io/TrackingRequest/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/TrackingRequest/attributes.jsonschema.yaml](https://schema.beckn.io/TrackingRequest/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/TrackingRequest/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/TrackingRequest/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/TrackingRequest/context.jsonld](https://schema.beckn.io/TrackingRequest/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/TrackingRequest/v2.0/context.jsonld](https://schema.beckn.io/TrackingRequest/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/TrackingRequest/vocab.jsonld](https://schema.beckn.io/TrackingRequest/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/TrackingRequest/v2.0/vocab.jsonld](https://schema.beckn.io/TrackingRequest/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | Tracking reference identifier |
| `callbackUrl` | no | string | Optional callback URL for streaming tracking coordinates/updates |
| `modeHint` | no | string | Optional delivery mode for the tracking handle. |
| `trackingDataSchema` | no | any | A JSON Schema (2020-12) that describes the structure of trackingData payloads. |
