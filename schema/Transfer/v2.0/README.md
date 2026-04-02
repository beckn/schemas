# Transfer — v2.0

A defined connection rule between two routes or services at a common stop, specifying minimum transfer time or transfer type.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Transfer/attributes.yaml](https://schema.beckn.io/Transfer/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Transfer/v2.0/attributes.yaml](https://schema.beckn.io/Transfer/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Transfer/attributes.jsonschema.yaml](https://schema.beckn.io/Transfer/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Transfer/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Transfer/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Transfer/context.jsonld](https://schema.beckn.io/Transfer/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Transfer/v2.0/context.jsonld](https://schema.beckn.io/Transfer/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Transfer/vocab.jsonld](https://schema.beckn.io/Transfer/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Transfer/v2.0/vocab.jsonld](https://schema.beckn.io/Transfer/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `fromStopId` | no | $ref: https://schema.beckn.io/Stop/v2.0/attributes.yaml#/components/schemas/Stop | Stop passengers transfer from |
| `toStopId` | no | $ref: https://schema.beckn.io/Stop/v2.0/attributes.yaml#/components/schemas/Stop | Stop passengers transfer to |
| `fromRouteId` | no | $ref: https://schema.beckn.io/Route/v2.0/attributes.yaml#/components/schemas/Route | Route passengers transfer from |
| `toRouteId` | no | $ref: https://schema.beckn.io/Route/v2.0/attributes.yaml#/components/schemas/Route | Route passengers transfer to |
| `transferType` | no | string | Type of transfer (0=recommended, 1=timed, 2=min_time, 3=not_possible) |
| `minTransferTime` | no | number | Minimum transfer time in seconds |
| `id` | no | string | Unique identifier for the fulfillment stop |
| `location` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Geographic location of the stop |
| `type` | no | string | Type of stop (start, end, intermediate) |
| `instructions` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Instructions for passengers at this stop |
| `time` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Expected time window at this stop |
