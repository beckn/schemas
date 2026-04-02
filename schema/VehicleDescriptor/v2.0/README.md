# VehicleDescriptor — v2.0

An identifier that uniquely references a specific vehicle in a real-time transit feed.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/VehicleDescriptor/attributes.yaml](https://schema.beckn.io/VehicleDescriptor/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/VehicleDescriptor/v2.0/attributes.yaml](https://schema.beckn.io/VehicleDescriptor/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/VehicleDescriptor/attributes.jsonschema.yaml](https://schema.beckn.io/VehicleDescriptor/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/VehicleDescriptor/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/VehicleDescriptor/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/VehicleDescriptor/context.jsonld](https://schema.beckn.io/VehicleDescriptor/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/VehicleDescriptor/v2.0/context.jsonld](https://schema.beckn.io/VehicleDescriptor/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/VehicleDescriptor/vocab.jsonld](https://schema.beckn.io/VehicleDescriptor/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/VehicleDescriptor/v2.0/vocab.jsonld](https://schema.beckn.io/VehicleDescriptor/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `vehicleId` | no | string | Internal system identifier for the vehicle |
| `label` | no | string | User-visible label or number for the vehicle |
| `licensePlate` | no | string | Vehicle license plate number |
| `name` | no | string | Short display name of the entity |
| `short_desc` | no | string | Brief textual description |
| `long_desc` | no | string | Detailed or long-form description |
| `media` | no | string | Media resource URLs (images, audio, video) |
| `images` | no | string | Image URLs for visual display |
