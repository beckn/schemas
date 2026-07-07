# Journey — v2.0

A complete travel itinerary from origin to destination, potentially comprising multiple legs using different transport modes.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Journey/attributes.yaml](https://schema.beckn.io/Journey/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Journey/v2.0/attributes.yaml](https://schema.beckn.io/Journey/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Journey/attributes.jsonschema.yaml](https://schema.beckn.io/Journey/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Journey/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Journey/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Journey/context.jsonld](https://schema.beckn.io/Journey/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Journey/v2.0/context.jsonld](https://schema.beckn.io/Journey/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Journey/vocab.jsonld](https://schema.beckn.io/Journey/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Journey/v2.0/vocab.jsonld](https://schema.beckn.io/Journey/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `origin` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Origin location of the journey |
| `destination` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Destination location of the journey |
| `departureTime` | no | string | Planned departure time |
| `arrivalTime` | no | string | Planned arrival time |
| `legs` | no | $ref: https://schema.beckn.io/Leg/v2.0/attributes.yaml#/components/schemas/Leg | Ordered list of legs comprising this journey |
| `id` | no | string | Unique identifier for the journey |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the journey |
