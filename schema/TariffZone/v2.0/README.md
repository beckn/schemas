# TariffZone — v2.0

A geographic zone used to define and apply fare structures, within which a single fare or set of rules applies.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/TariffZone/attributes.yaml](https://schema.beckn.io/TariffZone/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/TariffZone/v2.0/attributes.yaml](https://schema.beckn.io/TariffZone/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/TariffZone/attributes.jsonschema.yaml](https://schema.beckn.io/TariffZone/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/TariffZone/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/TariffZone/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/TariffZone/context.jsonld](https://schema.beckn.io/TariffZone/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/TariffZone/v2.0/context.jsonld](https://schema.beckn.io/TariffZone/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/TariffZone/vocab.jsonld](https://schema.beckn.io/TariffZone/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/TariffZone/v2.0/vocab.jsonld](https://schema.beckn.io/TariffZone/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `zoneId` | no | string | Unique identifier for the tariff zone |
| `zoneName` | no | string | Human-readable name of the tariff zone |
| `geometry` | no | $ref: https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml#/components/schemas/GeoJSONGeometry | GeoJSON geometry defining the zone boundary |
| `id` | no | string | Unique identifier for the location |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the location |
| `gps` | no | string | GPS coordinates as a latitude,longitude string |
| `address` | no | $ref: https://schema.beckn.io/Address/v2.0/attributes.yaml#/components/schemas/Address | Physical address of the location |
| `city` | no | string | City name |
| `country` | no | string | ISO 3166-1 alpha-2 country code |
| `geojson` | no | $ref: https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml#/components/schemas/GeoJSONGeometry | GeoJSON geometry object representing this location |
