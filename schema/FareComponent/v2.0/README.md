# FareComponent — v2.0

A component of an air travel fare that applies to a specific flight segment or leg, used in aviation pricing.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FareComponent/attributes.yaml](https://schema.beckn.io/FareComponent/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FareComponent/v2.0/attributes.yaml](https://schema.beckn.io/FareComponent/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FareComponent/attributes.jsonschema.yaml](https://schema.beckn.io/FareComponent/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FareComponent/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FareComponent/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FareComponent/context.jsonld](https://schema.beckn.io/FareComponent/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FareComponent/v2.0/context.jsonld](https://schema.beckn.io/FareComponent/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FareComponent/vocab.jsonld](https://schema.beckn.io/FareComponent/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FareComponent/v2.0/vocab.jsonld](https://schema.beckn.io/FareComponent/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `fareBasisCode` | no | string | IATA fare basis code identifying the fare type |
| `cabin` | no | string | Cabin class (ECONOMY, BUSINESS, FIRST) |
| `bookingCode` | no | string | Booking class code (e.g. Y, M, K) |
| `amount` | no | number | Fare amount for this component |
| `currency` | no | string | ISO 4217 currency code |
| `segmentRef` | no | $ref: https://schema.beckn.io/FlightSegment/v2.0/attributes.yaml#/components/schemas/FlightSegment | Flight segment this fare component applies to |
| `title` | no | string | Title or label of this price component |
| `price` | no | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | Monetary value of this component |
| `tags` | no | string | Tags associated with this price component |
