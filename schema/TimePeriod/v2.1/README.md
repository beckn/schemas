# TimePeriod — v2.1

Time window with date-time precision for availability/validity

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/TimePeriod/attributes.yaml](https://schema.beckn.io/TimePeriod/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/TimePeriod/v2.1/attributes.yaml](https://schema.beckn.io/TimePeriod/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/TimePeriod/attributes.jsonschema.yaml](https://schema.beckn.io/TimePeriod/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/TimePeriod/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/TimePeriod/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/TimePeriod/context.jsonld](https://schema.beckn.io/TimePeriod/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/TimePeriod/v2.1/context.jsonld](https://schema.beckn.io/TimePeriod/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/TimePeriod/vocab.jsonld](https://schema.beckn.io/TimePeriod/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/TimePeriod/v2.1/vocab.jsonld](https://schema.beckn.io/TimePeriod/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `startDate` | no | string | Start instant (inclusive) |
| `endDate` | no | string | End instant (exclusive or inclusive per domain semantics) |
| `startTime` | no | string | Start time of the time period |
| `endTime` | no | string | End time of the time period |
