# LocationGroup — v2.0

A set of geographic locations (stops or areas) that can collectively serve as an origin or destination for flexible transit services.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/LocationGroup/attributes.yaml](https://schema.beckn.io/LocationGroup/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/LocationGroup/v2.0/attributes.yaml](https://schema.beckn.io/LocationGroup/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/LocationGroup/attributes.jsonschema.yaml](https://schema.beckn.io/LocationGroup/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/LocationGroup/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/LocationGroup/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/LocationGroup/context.jsonld](https://schema.beckn.io/LocationGroup/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/LocationGroup/v2.0/context.jsonld](https://schema.beckn.io/LocationGroup/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/LocationGroup/vocab.jsonld](https://schema.beckn.io/LocationGroup/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/LocationGroup/v2.0/vocab.jsonld](https://schema.beckn.io/LocationGroup/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `locationGroupId` | no | string | Unique identifier for the location group |
| `locationGroupName` | no | string | Human-readable name for the location group |
| `stops` | no | $ref: https://schema.beckn.io/Stop/v2.0/attributes.yaml#/components/schemas/Stop | Stops included in this location group |
| `id` | no | string | Unique identifier for the location |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the location |
| `gps` | no | string | GPS coordinates as a latitude,longitude string |
| `address` | no | $ref: https://schema.beckn.io/Address/v2.0/attributes.yaml#/components/schemas/Address | Physical address of the location |
| `city` | no | string | City name |
| `country` | no | string | ISO 3166-1 alpha-2 country code |
| `geojson` | no | $ref: https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml#/components/schemas/GeoJSONGeometry | GeoJSON geometry object representing this location |
