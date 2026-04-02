# Direction — v2.0

The direction of travel of a transport service along a route, typically expressed as inbound or outbound.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Direction/attributes.yaml](https://schema.beckn.io/Direction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Direction/v2.0/attributes.yaml](https://schema.beckn.io/Direction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Direction/attributes.jsonschema.yaml](https://schema.beckn.io/Direction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Direction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Direction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Direction/context.jsonld](https://schema.beckn.io/Direction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Direction/v2.0/context.jsonld](https://schema.beckn.io/Direction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Direction/vocab.jsonld](https://schema.beckn.io/Direction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Direction/v2.0/vocab.jsonld](https://schema.beckn.io/Direction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `directionId` | no | string | Binary direction identifier (0 for one direction, 1 for the other) |
| `directionCode` | no | string | Named direction code (e.g. INBOUND, OUTBOUND, CLOCKWISE) |
| `name` | no | string | Short display name of the entity |
| `short_desc` | no | string | Brief textual description |
| `long_desc` | no | string | Detailed or long-form description |
| `media` | no | string | Media resource URLs (images, audio, video) |
| `images` | no | string | Image URLs for visual display |
