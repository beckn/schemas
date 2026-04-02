# VehicleStatus — v2.0

The real-time operational state of a vehicle or mobility asset, such as available, in use, reserved, or disabled.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/VehicleStatus/attributes.yaml](https://schema.beckn.io/VehicleStatus/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/VehicleStatus/v2.0/attributes.yaml](https://schema.beckn.io/VehicleStatus/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/VehicleStatus/attributes.jsonschema.yaml](https://schema.beckn.io/VehicleStatus/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/VehicleStatus/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/VehicleStatus/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/VehicleStatus/context.jsonld](https://schema.beckn.io/VehicleStatus/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/VehicleStatus/v2.0/context.jsonld](https://schema.beckn.io/VehicleStatus/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/VehicleStatus/vocab.jsonld](https://schema.beckn.io/VehicleStatus/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/VehicleStatus/v2.0/vocab.jsonld](https://schema.beckn.io/VehicleStatus/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `statusCode` | no | string | Operational status code (e.g. AVAILABLE, IN_USE, RESERVED, DISABLED, CHARGING) |
| `batteryLevel` | no | number | Current battery charge percentage |
| `rangeMeters` | no | number | Estimated remaining range in metres |
| `lastReportedAt` | no | string | Timestamp of the last status update |
| `id` | no | string | Unique identifier for the state |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the state |
| `updatedAt` | no | string | Timestamp when the state was last updated |
