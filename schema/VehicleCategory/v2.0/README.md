# VehicleCategory — v2.0

A broad classification of vehicles by their physical type, such as two-wheeler, three-wheeler, four-wheeler, or bus.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/VehicleCategory/attributes.yaml](https://schema.beckn.io/VehicleCategory/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/VehicleCategory/v2.0/attributes.yaml](https://schema.beckn.io/VehicleCategory/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/VehicleCategory/attributes.jsonschema.yaml](https://schema.beckn.io/VehicleCategory/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/VehicleCategory/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/VehicleCategory/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/VehicleCategory/context.jsonld](https://schema.beckn.io/VehicleCategory/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/VehicleCategory/v2.0/context.jsonld](https://schema.beckn.io/VehicleCategory/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/VehicleCategory/vocab.jsonld](https://schema.beckn.io/VehicleCategory/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/VehicleCategory/v2.0/vocab.jsonld](https://schema.beckn.io/VehicleCategory/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `vehicleCategoryCode` | no | string | Code for the vehicle category (e.g. TWO_WHEELER, THREE_WHEELER, FOUR_WHEELER, BUS) |
| `maxPassengers` | no | number | Maximum number of passengers for vehicles in this category |
| `id` | no | string | Unique identifier for the category code |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable label for the category |
| `parentCategoryId` | no | string | Identifier of the parent category if hierarchical |
