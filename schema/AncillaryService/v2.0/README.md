# AncillaryService — v2.0

An optional or additional service available for purchase alongside base transport, such as extra baggage or lounge access.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/AncillaryService/attributes.yaml](https://schema.beckn.io/AncillaryService/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/AncillaryService/v2.0/attributes.yaml](https://schema.beckn.io/AncillaryService/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/AncillaryService/attributes.jsonschema.yaml](https://schema.beckn.io/AncillaryService/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/AncillaryService/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/AncillaryService/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/AncillaryService/context.jsonld](https://schema.beckn.io/AncillaryService/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/AncillaryService/v2.0/context.jsonld](https://schema.beckn.io/AncillaryService/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/AncillaryService/vocab.jsonld](https://schema.beckn.io/AncillaryService/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/AncillaryService/v2.0/vocab.jsonld](https://schema.beckn.io/AncillaryService/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `serviceCode` | no | string | IATA service code (e.g. BG for extra baggage) |
| `serviceCategory` | no | string | Category of the ancillary service |
| `maxQuantity` | no | number | Maximum quantity of this service that can be purchased |
| `id` | no | string | Unique identifier for the offer |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the offer |
| `price` | no | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | Price specification for this offer |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity period of the offer |
| `tags` | no | string | Tags or labels associated with the offer |
