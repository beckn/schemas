# Time — v2.0

Represents a moment or duration in time. Can express a timestamp, a duration, or a time range.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Time/attributes.yaml](https://schema.beckn.io/Time/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Time/v2.0/attributes.yaml](https://schema.beckn.io/Time/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Time/attributes.jsonschema.yaml](https://schema.beckn.io/Time/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Time/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Time/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Time/context.jsonld](https://schema.beckn.io/Time/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Time/v2.0/context.jsonld](https://schema.beckn.io/Time/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Time/vocab.jsonld](https://schema.beckn.io/Time/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Time/v2.0/vocab.jsonld](https://schema.beckn.io/Time/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | no | string | - |
| `@type` | no | string | - |
| `timestamp` | no | string | A specific instant in time (ISO 8601) |
| `duration` | no | string | ISO 8601 duration (e.g., PT30M for 30 minutes) |
| `range` | no | $ref: https://schema.beckn.io/TimePeriod/v2.1/attributes.yaml#/components/schemas/TimePeriod | A time range with start and end |
| `label` | no | string | Human-readable label for this time |
