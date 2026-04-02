# GeofencingZone — v2.0

A virtual geographic boundary used to define operational areas, speed limits, parking rules, or restrictions for shared mobility services.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/GeofencingZone/attributes.yaml](https://schema.beckn.io/GeofencingZone/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/GeofencingZone/v2.0/attributes.yaml](https://schema.beckn.io/GeofencingZone/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/GeofencingZone/attributes.jsonschema.yaml](https://schema.beckn.io/GeofencingZone/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/GeofencingZone/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/GeofencingZone/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/GeofencingZone/context.jsonld](https://schema.beckn.io/GeofencingZone/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/GeofencingZone/v2.0/context.jsonld](https://schema.beckn.io/GeofencingZone/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/GeofencingZone/vocab.jsonld](https://schema.beckn.io/GeofencingZone/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/GeofencingZone/v2.0/vocab.jsonld](https://schema.beckn.io/GeofencingZone/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `featureType` | no | string | Type of geofencing zone feature (e.g. parking, restricted, slow) |
| `geometry` | no | $ref: https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml#/components/schemas/GeoJSONGeometry | GeoJSON geometry defining the zone boundary |
| `rideAllowed` | no | boolean | Whether riding is permitted within this zone |
| `rideThroughAllowed` | no | boolean | Whether riding through without stopping is permitted |
| `stationParking` | no | boolean | Whether docking at a station is required to end a trip here |
| `id` | no | string | Unique identifier for the location |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the location |
| `gps` | no | string | GPS coordinates as a latitude,longitude string |
| `address` | no | $ref: https://schema.beckn.io/Address/v2.0/attributes.yaml#/components/schemas/Address | Physical address of the location |
| `city` | no | string | City name |
| `country` | no | string | ISO 3166-1 alpha-2 country code |
| `geojson` | no | $ref: https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml#/components/schemas/GeoJSONGeometry | GeoJSON geometry object representing this location |
