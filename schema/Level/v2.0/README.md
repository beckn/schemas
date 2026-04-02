# Level — v2.0

A floor or vertical level within a multi-level transit station or facility, used to define internal navigation paths.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Level/attributes.yaml](https://schema.beckn.io/Level/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Level/v2.0/attributes.yaml](https://schema.beckn.io/Level/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Level/attributes.jsonschema.yaml](https://schema.beckn.io/Level/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Level/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Level/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Level/context.jsonld](https://schema.beckn.io/Level/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Level/v2.0/context.jsonld](https://schema.beckn.io/Level/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Level/vocab.jsonld](https://schema.beckn.io/Level/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Level/v2.0/vocab.jsonld](https://schema.beckn.io/Level/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `levelId` | no | string | Unique identifier for this level within the station |
| `levelName` | no | string | Human-readable name of the level (e.g. Ground Floor, Level 1) |
| `elevation` | no | number | Elevation of this level in metres above ground |
| `stationRef` | no | $ref: https://schema.beckn.io/Station/v2.0/attributes.yaml#/components/schemas/Station | Reference to the station this level belongs to |
| `id` | no | string | Unique identifier for the location |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the location |
| `gps` | no | string | GPS coordinates as a latitude,longitude string |
| `address` | no | $ref: https://schema.beckn.io/Address/v2.0/attributes.yaml#/components/schemas/Address | Physical address of the location |
| `city` | no | string | City name |
| `country` | no | string | ISO 3166-1 alpha-2 country code |
| `geojson` | no | $ref: https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml#/components/schemas/GeoJSONGeometry | GeoJSON geometry object representing this location |
