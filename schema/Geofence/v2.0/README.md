# Geofence — v2.0

A virtual geographic boundary used to define service areas, restricted zones, or operational boundaries for mobility assets.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Geofence/attributes.yaml](https://schema.beckn.io/Geofence/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Geofence/v2.0/attributes.yaml](https://schema.beckn.io/Geofence/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Geofence/attributes.jsonschema.yaml](https://schema.beckn.io/Geofence/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Geofence/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Geofence/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Geofence/context.jsonld](https://schema.beckn.io/Geofence/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Geofence/v2.0/context.jsonld](https://schema.beckn.io/Geofence/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Geofence/vocab.jsonld](https://schema.beckn.io/Geofence/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Geofence/v2.0/vocab.jsonld](https://schema.beckn.io/Geofence/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `geofenceType` | no | string | Type of geofence (e.g. SERVICE_AREA, RESTRICTED, SPEED_LIMIT) |
| `geometry` | no | $ref: https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml#/components/schemas/GeoJSONGeometry | GeoJSON geometry defining the geofence boundary |
| `rules` | no | string | Operational rules applied within this geofence |
| `id` | no | string | Unique identifier for the location |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the location |
| `gps` | no | string | GPS coordinates as a latitude,longitude string |
| `address` | no | $ref: https://schema.beckn.io/Address/v2.0/attributes.yaml#/components/schemas/Address | Physical address of the location |
| `city` | no | string | City name |
| `country` | no | string | ISO 3166-1 alpha-2 country code |
| `geojson` | no | $ref: https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml#/components/schemas/GeoJSONGeometry | GeoJSON geometry object representing this location |
