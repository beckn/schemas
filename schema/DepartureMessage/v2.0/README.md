# DepartureMessage — v2.0

A real-time message containing predicted departure times for vehicles at a stop, as used in VDV real-time standards.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/DepartureMessage/attributes.yaml](https://schema.beckn.io/DepartureMessage/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/DepartureMessage/v2.0/attributes.yaml](https://schema.beckn.io/DepartureMessage/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/DepartureMessage/attributes.jsonschema.yaml](https://schema.beckn.io/DepartureMessage/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/DepartureMessage/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/DepartureMessage/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/DepartureMessage/context.jsonld](https://schema.beckn.io/DepartureMessage/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/DepartureMessage/v2.0/context.jsonld](https://schema.beckn.io/DepartureMessage/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/DepartureMessage/vocab.jsonld](https://schema.beckn.io/DepartureMessage/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/DepartureMessage/v2.0/vocab.jsonld](https://schema.beckn.io/DepartureMessage/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `stopRef` | no | $ref: https://schema.beckn.io/Stop/v2.0/attributes.yaml#/components/schemas/Stop | Reference to the stop for which departures are reported |
| `lineRef` | no | $ref: https://schema.beckn.io/Line/v2.0/attributes.yaml#/components/schemas/Line | Reference to the line departing from this stop |
| `vehicleRef` | no | $ref: https://schema.beckn.io/VehicleDescriptor/v2.0/attributes.yaml#/components/schemas/VehicleDescriptor | Reference to the departing vehicle |
| `expectedDeparture` | no | string | Predicted departure time |
| `delaySeconds` | no | number | Delay in seconds relative to scheduled departure |
| `id` | no | string | Unique identifier for the alert |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the alert |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Time period during which the alert is active |
| `status` | no | $ref: https://schema.beckn.io/State/v2.0/attributes.yaml#/components/schemas/State | Current status of the alert |
