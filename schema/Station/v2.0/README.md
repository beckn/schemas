# Station — v2.0

A major transit facility serving as a hub for one or more transport modes, typically offering waiting areas, ticketing, and interchange facilities.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Station/attributes.yaml](https://schema.beckn.io/Station/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Station/v2.0/attributes.yaml](https://schema.beckn.io/Station/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Station/attributes.jsonschema.yaml](https://schema.beckn.io/Station/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Station/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Station/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Station/context.jsonld](https://schema.beckn.io/Station/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Station/v2.0/context.jsonld](https://schema.beckn.io/Station/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Station/vocab.jsonld](https://schema.beckn.io/Station/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Station/v2.0/vocab.jsonld](https://schema.beckn.io/Station/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `stationId` | no | string | Unique identifier for the station |
| `stationName` | no | string | Human-readable name of the station |
| `stationType` | no | string | Primary transport mode served (e.g. RAIL, BUS, METRO, FERRY) |
| `platforms` | no | $ref: https://schema.beckn.io/Quay/v2.0/attributes.yaml#/components/schemas/Quay | Platforms or quays within this station |
| `levels` | no | $ref: https://schema.beckn.io/Level/v2.0/attributes.yaml#/components/schemas/Level | Levels or floors within the station |
| `pathways` | no | $ref: https://schema.beckn.io/Pathway/v2.0/attributes.yaml#/components/schemas/Pathway | Internal navigation pathways within the station |
| `id` | no | string | Unique identifier for the location |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the location |
| `gps` | no | string | GPS coordinates as a latitude,longitude string |
| `address` | no | $ref: https://schema.beckn.io/Address/v2.0/attributes.yaml#/components/schemas/Address | Physical address of the location |
| `city` | no | string | City name |
| `country` | no | string | ISO 3166-1 alpha-2 country code |
| `geojson` | no | $ref: https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml#/components/schemas/GeoJSONGeometry | GeoJSON geometry object representing this location |
