# PlanningResult — v2.0

The output of a MaaS platform planning request, listing available transport options for a requested trip.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/PlanningResult/attributes.yaml](https://schema.beckn.io/PlanningResult/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/PlanningResult/v2.0/attributes.yaml](https://schema.beckn.io/PlanningResult/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/PlanningResult/attributes.jsonschema.yaml](https://schema.beckn.io/PlanningResult/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/PlanningResult/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/PlanningResult/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/PlanningResult/context.jsonld](https://schema.beckn.io/PlanningResult/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/PlanningResult/v2.0/context.jsonld](https://schema.beckn.io/PlanningResult/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/PlanningResult/vocab.jsonld](https://schema.beckn.io/PlanningResult/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/PlanningResult/v2.0/vocab.jsonld](https://schema.beckn.io/PlanningResult/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `origin` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Origin location for the planning query |
| `destination` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Destination location for the planning query |
| `options` | no | $ref: https://schema.beckn.io/RideOption/v2.0/attributes.yaml#/components/schemas/RideOption | Available transport options returned |
| `itineraries` | no | $ref: https://schema.beckn.io/Itinerary/v2.0/attributes.yaml#/components/schemas/Itinerary | Multi-modal itinerary options if applicable |
| `id` | no | string | Unique identifier for the catalog |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the catalog |
| `tags` | no | string | Tags associated with the catalog |
