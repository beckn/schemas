# TimePeriod — v2.0

Time window with date-time precision for availability/validity

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/TimePeriod/attributes.yaml](https://schema.beckn.io/TimePeriod/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml](https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/TimePeriod/attributes.jsonschema.yaml](https://schema.beckn.io/TimePeriod/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/TimePeriod/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/TimePeriod/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/TimePeriod/context.jsonld](https://schema.beckn.io/TimePeriod/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/TimePeriod/v2.0/context.jsonld](https://schema.beckn.io/TimePeriod/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/TimePeriod/vocab.jsonld](https://schema.beckn.io/TimePeriod/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/TimePeriod/v2.0/vocab.jsonld](https://schema.beckn.io/TimePeriod/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@type` | yes | string | JSON-LD type for a date-time period |
| `schema:startDate` | no | string | Start instant (inclusive) |
| `schema:endDate` | no | string | End instant (exclusive or inclusive per domain semantics) |
| `schema:startTime` | no | string | Start time of the time period |
| `schema:endTime` | no | string | End time of the time period |
