# LogisticsRoute — v2.0

A Route is the planned path for a shipment from origin to destination, potentially passing through multiple hubs and waypoints. Maps to beckn:Journey.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/LogisticsRoute/attributes.yaml](https://schema.beckn.io/LogisticsRoute/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/LogisticsRoute/v2.0/attributes.yaml](https://schema.beckn.io/LogisticsRoute/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/LogisticsRoute/attributes.jsonschema.yaml](https://schema.beckn.io/LogisticsRoute/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/LogisticsRoute/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/LogisticsRoute/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/LogisticsRoute/context.jsonld](https://schema.beckn.io/LogisticsRoute/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/LogisticsRoute/v2.0/context.jsonld](https://schema.beckn.io/LogisticsRoute/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/LogisticsRoute/vocab.jsonld](https://schema.beckn.io/LogisticsRoute/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/LogisticsRoute/v2.0/vocab.jsonld](https://schema.beckn.io/LogisticsRoute/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | Unique route identifier |
| `name` | no | string | Human-readable route name |
| `origin` | yes | $ref: https://schema.beckn.io/Place/attributes.yaml#/components/schemas/Place | - |
| `destination` | yes | $ref: https://schema.beckn.io/Place/attributes.yaml#/components/schemas/Place | - |
| `waypoints` | no | array | Intermediate waypoints/hubs on the route |
| `totalDistance` | no | object | - |
| `estimatedDuration` | no | object | - |
| `transportMode` | no | string | - |
| `routeType` | no | string | Classification of route |
| `geometry` | no | object | GeoJSON LineString of route geometry |
| `tollCost` | no | number | Estimated toll charges in INR |
| `restrictions` | no | array | Route restrictions (e.g. night driving ban) |
