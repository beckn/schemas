# FareResult — v2.0

The calculated fare for a requested trip, returned as part of a trip planning or fare enquiry response.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FareResult/attributes.yaml](https://schema.beckn.io/FareResult/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FareResult/v2.0/attributes.yaml](https://schema.beckn.io/FareResult/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FareResult/attributes.jsonschema.yaml](https://schema.beckn.io/FareResult/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FareResult/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FareResult/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FareResult/context.jsonld](https://schema.beckn.io/FareResult/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FareResult/v2.0/context.jsonld](https://schema.beckn.io/FareResult/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FareResult/vocab.jsonld](https://schema.beckn.io/FareResult/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FareResult/v2.0/vocab.jsonld](https://schema.beckn.io/FareResult/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `totalAmount` | no | number | Total calculated fare amount |
| `currency` | no | string | ISO 4217 currency code |
| `fareProducts` | no | $ref: https://schema.beckn.io/FareProduct/v2.0/attributes.yaml#/components/schemas/FareProduct | Fare products applicable to the result |
| `fareBreakup` | no | $ref: https://schema.beckn.io/FareBreakup/v2.0/attributes.yaml#/components/schemas/FareBreakup | Itemised breakdown of the calculated fare |
| `id` | no | string | Unique identifier for the offer |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the offer |
| `price` | no | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | Price specification for this offer |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity period of the offer |
| `tags` | no | string | Tags or labels associated with the offer |
