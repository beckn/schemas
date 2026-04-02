# VehiclePosition — v2.0

The current real-time geographic position, bearing, and speed of a vehicle operating a transport service.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/VehiclePosition/attributes.yaml](https://schema.beckn.io/VehiclePosition/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/VehiclePosition/v2.0/attributes.yaml](https://schema.beckn.io/VehiclePosition/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/VehiclePosition/attributes.jsonschema.yaml](https://schema.beckn.io/VehiclePosition/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/VehiclePosition/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/VehiclePosition/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/VehiclePosition/context.jsonld](https://schema.beckn.io/VehiclePosition/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/VehiclePosition/v2.0/context.jsonld](https://schema.beckn.io/VehiclePosition/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/VehiclePosition/vocab.jsonld](https://schema.beckn.io/VehiclePosition/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/VehiclePosition/v2.0/vocab.jsonld](https://schema.beckn.io/VehiclePosition/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `tripDescriptor` | no | $ref: https://schema.beckn.io/TripDescriptor/v2.0/attributes.yaml#/components/schemas/TripDescriptor | Identifies the trip this vehicle is operating |
| `vehicleDescriptor` | no | $ref: https://schema.beckn.io/VehicleDescriptor/v2.0/attributes.yaml#/components/schemas/VehicleDescriptor | Identifies the reporting vehicle |
| `latitude` | no | number | Current latitude in WGS-84 decimal degrees |
| `longitude` | no | number | Current longitude in WGS-84 decimal degrees |
| `bearing` | no | number | Current bearing in degrees (0=north, 90=east) |
| `speed` | no | number | Current speed in metres per second |
| `currentStopSequence` | no | number | Stop sequence index of the stop the vehicle is at or approaching |
| `currentStatus` | no | string | Vehicle status relative to the stop (INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO) |
| `timestamp` | no | string | Timestamp of this position report |
| `id` | no | string | Unique identifier for the tracking record |
| `url` | no | string | URL endpoint for real-time tracking information |
| `status` | no | $ref: https://schema.beckn.io/State/v2.0/attributes.yaml#/components/schemas/State | Current tracking status |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity period for this tracking record |
