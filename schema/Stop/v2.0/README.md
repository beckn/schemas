# Stop — v2.0

A designated location where vehicles stop to allow passengers to board or alight from a transport service.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Stop/attributes.yaml](https://schema.beckn.io/Stop/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Stop/v2.0/attributes.yaml](https://schema.beckn.io/Stop/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Stop/attributes.jsonschema.yaml](https://schema.beckn.io/Stop/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Stop/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Stop/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Stop/context.jsonld](https://schema.beckn.io/Stop/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Stop/v2.0/context.jsonld](https://schema.beckn.io/Stop/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Stop/vocab.jsonld](https://schema.beckn.io/Stop/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Stop/v2.0/vocab.jsonld](https://schema.beckn.io/Stop/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `stopId` | no | string | Unique identifier for the stop |
| `stopCode` | no | string | Short public-facing code for the stop |
| `stopName` | no | string | Human-readable name of the stop |
| `locationType` | no | string | Classification of location (0=stop, 1=station, 2=entrance, 3=generic_node, 4=boarding_area) |
| `parentStation` | no | $ref: https://schema.beckn.io/Station/v2.0/attributes.yaml#/components/schemas/Station | Reference to the parent station if this is a platform |
| `wheelchairBoarding` | no | string | Wheelchair accessibility (0=no info, 1=accessible, 2=not accessible) |
| `id` | no | string | Unique identifier for the fulfillment stop |
| `location` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Geographic location of the stop |
| `type` | no | string | Type of stop (start, end, intermediate) |
| `instructions` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Instructions for passengers at this stop |
| `time` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Expected time window at this stop |
