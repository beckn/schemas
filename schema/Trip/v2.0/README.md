# Trip — v2.0

A confirmed and booked journey from an origin to a destination, representing a completed mobility service order.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Trip/attributes.yaml](https://schema.beckn.io/Trip/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Trip/v2.0/attributes.yaml](https://schema.beckn.io/Trip/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Trip/attributes.jsonschema.yaml](https://schema.beckn.io/Trip/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Trip/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Trip/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Trip/context.jsonld](https://schema.beckn.io/Trip/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Trip/v2.0/context.jsonld](https://schema.beckn.io/Trip/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Trip/vocab.jsonld](https://schema.beckn.io/Trip/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Trip/v2.0/vocab.jsonld](https://schema.beckn.io/Trip/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `tripId` | no | string | Unique identifier for the trip |
| `origin` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Pickup location |
| `destination` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Dropoff location |
| `startTime` | no | string | Actual start time of the trip |
| `endTime` | no | string | Actual end time of the trip |
| `distance` | no | number | Total distance of the trip in kilometres |
| `driverRef` | no | $ref: https://schema.beckn.io/Driver/v2.0/attributes.yaml#/components/schemas/Driver | Reference to the driver for this trip |
| `vehicleRef` | no | $ref: https://schema.beckn.io/Vehicle/v2.0/attributes.yaml#/components/schemas/Vehicle | Reference to the vehicle for this trip |
| `id` | no | string | Unique identifier for the contract |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the contract |
| `items` | no | $ref: https://schema.beckn.io/ContractItem/v2.0/attributes.yaml#/components/schemas/ContractItem | Line items within the contract |
| `fulfillments` | no | $ref: https://schema.beckn.io/Fulfillment/v2.1/attributes.yaml#/components/schemas/Fulfillment | Fulfillments associated with this contract |
| `state` | no | $ref: https://schema.beckn.io/State/v2.0/attributes.yaml#/components/schemas/State | Current state of the contract |
