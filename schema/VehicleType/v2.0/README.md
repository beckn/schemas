# VehicleType — v2.0

A class or category of vehicle defined by its mode of transport, capacity, propulsion type, and accessibility features.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/VehicleType/attributes.yaml](https://schema.beckn.io/VehicleType/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/VehicleType/v2.0/attributes.yaml](https://schema.beckn.io/VehicleType/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/VehicleType/attributes.jsonschema.yaml](https://schema.beckn.io/VehicleType/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/VehicleType/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/VehicleType/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/VehicleType/context.jsonld](https://schema.beckn.io/VehicleType/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/VehicleType/v2.0/context.jsonld](https://schema.beckn.io/VehicleType/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/VehicleType/vocab.jsonld](https://schema.beckn.io/VehicleType/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/VehicleType/v2.0/vocab.jsonld](https://schema.beckn.io/VehicleType/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `vehicleTypeCode` | no | string | Code identifying the vehicle type (e.g. BUS, TRAM, METRO, BICYCLE, SCOOTER) |
| `maxCapacity` | no | number | Maximum number of passengers the vehicle type can carry |
| `propulsionType` | no | string | Propulsion type (e.g. ELECTRIC, COMBUSTION, HUMAN, HYBRID) |
| `wheelchairAccessible` | no | boolean | Whether vehicles of this type are wheelchair accessible |
| `id` | no | string | Unique identifier for the category code |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable label for the category |
| `parentCategoryId` | no | string | Identifier of the parent category if hierarchical |
