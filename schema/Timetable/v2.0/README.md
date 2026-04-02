# Timetable — v2.0

A structured schedule listing planned arrival and departure times for vehicles at each stop along a route.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Timetable/attributes.yaml](https://schema.beckn.io/Timetable/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Timetable/v2.0/attributes.yaml](https://schema.beckn.io/Timetable/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Timetable/attributes.jsonschema.yaml](https://schema.beckn.io/Timetable/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Timetable/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Timetable/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Timetable/context.jsonld](https://schema.beckn.io/Timetable/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Timetable/v2.0/context.jsonld](https://schema.beckn.io/Timetable/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Timetable/vocab.jsonld](https://schema.beckn.io/Timetable/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Timetable/v2.0/vocab.jsonld](https://schema.beckn.io/Timetable/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `routeRef` | no | $ref: https://schema.beckn.io/Route/v2.0/attributes.yaml#/components/schemas/Route | Reference to the route this timetable covers |
| `trips` | no | $ref: https://schema.beckn.io/VehicleJourney/v2.0/attributes.yaml#/components/schemas/VehicleJourney | Vehicle journeys (trips) in this timetable |
| `validFrom` | no | string | Date from which this timetable is valid |
| `validUntil` | no | string | Date until which this timetable is valid |
| `id` | no | string | Unique identifier for the catalog |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the catalog |
| `tags` | no | string | Tags associated with the catalog |
