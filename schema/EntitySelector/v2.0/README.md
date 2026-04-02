# EntitySelector — v2.0

A selector that identifies which transport entities (routes, trips, stops, or agencies) are affected by a given alert.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/EntitySelector/attributes.yaml](https://schema.beckn.io/EntitySelector/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/EntitySelector/v2.0/attributes.yaml](https://schema.beckn.io/EntitySelector/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/EntitySelector/attributes.jsonschema.yaml](https://schema.beckn.io/EntitySelector/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/EntitySelector/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/EntitySelector/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/EntitySelector/context.jsonld](https://schema.beckn.io/EntitySelector/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/EntitySelector/v2.0/context.jsonld](https://schema.beckn.io/EntitySelector/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/EntitySelector/vocab.jsonld](https://schema.beckn.io/EntitySelector/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/EntitySelector/v2.0/vocab.jsonld](https://schema.beckn.io/EntitySelector/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `agencyId` | no | string | Identifier of the affected agency |
| `routeId` | no | string | Identifier of the affected route |
| `routeType` | no | string | Type of the affected route (e.g. BUS, RAIL) |
| `tripDescriptor` | no | $ref: https://schema.beckn.io/TripDescriptor/v2.0/attributes.yaml#/components/schemas/TripDescriptor | Descriptor identifying the affected trip |
| `stopId` | no | string | Identifier of the affected stop |
| `id` | no | string | Unique identifier for the alert |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the alert |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Time period during which the alert is active |
| `status` | no | $ref: https://schema.beckn.io/State/v2.0/attributes.yaml#/components/schemas/State | Current status of the alert |
