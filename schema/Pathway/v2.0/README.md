# Pathway — v2.0

A connection between two points within a transit station (e.g., stairway, elevator, walkway) used for indoor navigation and accessibility routing.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Pathway/attributes.yaml](https://schema.beckn.io/Pathway/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Pathway/v2.0/attributes.yaml](https://schema.beckn.io/Pathway/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Pathway/attributes.jsonschema.yaml](https://schema.beckn.io/Pathway/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Pathway/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Pathway/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Pathway/context.jsonld](https://schema.beckn.io/Pathway/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Pathway/v2.0/context.jsonld](https://schema.beckn.io/Pathway/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Pathway/vocab.jsonld](https://schema.beckn.io/Pathway/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Pathway/v2.0/vocab.jsonld](https://schema.beckn.io/Pathway/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `pathwayId` | no | string | Unique identifier for the pathway |
| `fromStopId` | no | $ref: https://schema.beckn.io/Stop/v2.0/attributes.yaml#/components/schemas/Stop | Stop at the start of the pathway |
| `toStopId` | no | $ref: https://schema.beckn.io/Stop/v2.0/attributes.yaml#/components/schemas/Stop | Stop at the end of the pathway |
| `pathwayMode` | no | string | Type of pathway (1=walkway, 2=stairs, 3=moving_sidewalk, 4=escalator, 5=elevator, 6=fare_gate, 7=exit_gate) |
| `isBidirectional` | no | boolean | Whether the pathway can be traversed in both directions |
| `length` | no | number | Length of the pathway in metres |
| `traversalTime` | no | number | Time in seconds to traverse the pathway |
| `id` | no | string | Unique identifier for the location |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the location |
| `gps` | no | string | GPS coordinates as a latitude,longitude string |
| `address` | no | $ref: https://schema.beckn.io/Address/v2.0/attributes.yaml#/components/schemas/Address | Physical address of the location |
| `city` | no | string | City name |
| `country` | no | string | ISO 3166-1 alpha-2 country code |
| `geojson` | no | $ref: https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml#/components/schemas/GeoJSONGeometry | GeoJSON geometry object representing this location |
