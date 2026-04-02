# Waypoint — v2.0

A Waypoint is an intermediate stop or checkpoint on a logistics route, such as a sorting hub, relay station, or customs checkpoint. Maps to beckn:Stop.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Waypoint/attributes.yaml](https://schema.beckn.io/Waypoint/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Waypoint/v2.0/attributes.yaml](https://schema.beckn.io/Waypoint/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Waypoint/attributes.jsonschema.yaml](https://schema.beckn.io/Waypoint/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Waypoint/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Waypoint/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Waypoint/context.jsonld](https://schema.beckn.io/Waypoint/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Waypoint/v2.0/context.jsonld](https://schema.beckn.io/Waypoint/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Waypoint/vocab.jsonld](https://schema.beckn.io/Waypoint/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Waypoint/v2.0/vocab.jsonld](https://schema.beckn.io/Waypoint/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | - |
| `name` | no | string | - |
| `place` | yes | $ref: https://schema.beckn.io/Place/v2.0/attributes.yaml#/components/schemas/Place | - |
| `type` | no | string | - |
| `sequenceNumber` | no | integer | Order of this waypoint in the route |
| `scheduledArrival` | no | string | - |
| `scheduledDeparture` | no | string | - |
| `actualArrival` | no | string | - |
| `actualDeparture` | no | string | - |
| `dwellTimeMinutes` | no | integer | Expected dwell time at this waypoint in minutes |
| `handoverRequired` | no | boolean | Whether shipment changes carrier/vehicle at this point |
| `status` | no | string | - |
