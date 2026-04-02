# ExchangePoints — v2.0

Locations in a transport network where fixed-route and flexible services connect, enabling passenger interchange.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/ExchangePoints/attributes.yaml](https://schema.beckn.io/ExchangePoints/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/ExchangePoints/v2.0/attributes.yaml](https://schema.beckn.io/ExchangePoints/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/ExchangePoints/attributes.jsonschema.yaml](https://schema.beckn.io/ExchangePoints/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/ExchangePoints/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/ExchangePoints/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/ExchangePoints/context.jsonld](https://schema.beckn.io/ExchangePoints/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/ExchangePoints/v2.0/context.jsonld](https://schema.beckn.io/ExchangePoints/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/ExchangePoints/vocab.jsonld](https://schema.beckn.io/ExchangePoints/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/ExchangePoints/v2.0/vocab.jsonld](https://schema.beckn.io/ExchangePoints/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `exchangePointType` | no | string | Type of exchange point (e.g. FIXED_TO_FLEX, FLEX_TO_FLEX) |
| `connectingServices` | no | $ref: https://schema.beckn.io/VehicleJourney/v2.0/attributes.yaml#/components/schemas/VehicleJourney | Services that connect at this exchange point |
| `id` | no | string | Unique identifier for the fulfillment stop |
| `location` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Geographic location of the stop |
| `type` | no | string | Type of stop (start, end, intermediate) |
| `instructions` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Instructions for passengers at this stop |
| `time` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Expected time window at this stop |
