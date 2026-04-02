# RideRequest — v2.0

A passenger's request for an on-demand transport service between two points, specifying origin, destination, and travel preferences.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/RideRequest/attributes.yaml](https://schema.beckn.io/RideRequest/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/RideRequest/v2.0/attributes.yaml](https://schema.beckn.io/RideRequest/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/RideRequest/attributes.jsonschema.yaml](https://schema.beckn.io/RideRequest/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/RideRequest/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/RideRequest/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/RideRequest/context.jsonld](https://schema.beckn.io/RideRequest/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/RideRequest/v2.0/context.jsonld](https://schema.beckn.io/RideRequest/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/RideRequest/vocab.jsonld](https://schema.beckn.io/RideRequest/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/RideRequest/v2.0/vocab.jsonld](https://schema.beckn.io/RideRequest/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `origin` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Pickup location for the ride |
| `destination` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Dropoff location for the ride |
| `requestedTime` | no | string | Requested pickup time |
| `passengerCount` | no | number | Number of passengers |
| `vehiclePreference` | no | $ref: https://schema.beckn.io/VehicleCategory/v2.0/attributes.yaml#/components/schemas/VehicleCategory | Preferred vehicle category |
| `textSearch` | no | string | Free-text search query expressing what the traveler is looking for |
| `filters` | no | string | JSONPath filter criteria applied to the search results |
| `spatial` | no | $ref: https://schema.beckn.io/SpatialConstraint/v2.0/attributes.yaml#/components/schemas/SpatialConstraint | Geographic constraints on the search area |
| `provider` | no | string | Identifier of a specific provider to search within |
