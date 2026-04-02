# StationInformation — v2.0

Static descriptive information about a shared mobility docking station, including its location, capacity, and features.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/StationInformation/attributes.yaml](https://schema.beckn.io/StationInformation/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/StationInformation/v2.0/attributes.yaml](https://schema.beckn.io/StationInformation/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/StationInformation/attributes.jsonschema.yaml](https://schema.beckn.io/StationInformation/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/StationInformation/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/StationInformation/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/StationInformation/context.jsonld](https://schema.beckn.io/StationInformation/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/StationInformation/v2.0/context.jsonld](https://schema.beckn.io/StationInformation/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/StationInformation/vocab.jsonld](https://schema.beckn.io/StationInformation/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/StationInformation/v2.0/vocab.jsonld](https://schema.beckn.io/StationInformation/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `stationId` | no | string | Unique identifier for the docking station |
| `shortName` | no | string | Shortened name of the station for display |
| `capacity` | no | number | Total number of docking points at this station |
| `hasKiosk` | no | boolean | Whether this station has a kiosk for key cards or passes |
| `rentalMethods` | no | string | Methods by which bikes can be rented (e.g. KEY, CREDITCARD, APP) |
| `regionId` | no | string | Identifier of the system region this station belongs to |
| `id` | no | string | Unique identifier for the location |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the location |
| `gps` | no | string | GPS coordinates as a latitude,longitude string |
| `address` | no | $ref: https://schema.beckn.io/Address/v2.0/attributes.yaml#/components/schemas/Address | Physical address of the location |
| `city` | no | string | City name |
| `country` | no | string | ISO 3166-1 alpha-2 country code |
| `geojson` | no | $ref: https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml#/components/schemas/GeoJSONGeometry | GeoJSON geometry object representing this location |
