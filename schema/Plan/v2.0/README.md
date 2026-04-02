# Plan — v2.0

A journey planning response containing one or more itinerary options for a given trip request.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Plan/attributes.yaml](https://schema.beckn.io/Plan/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Plan/v2.0/attributes.yaml](https://schema.beckn.io/Plan/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Plan/attributes.jsonschema.yaml](https://schema.beckn.io/Plan/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Plan/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Plan/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Plan/context.jsonld](https://schema.beckn.io/Plan/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Plan/v2.0/context.jsonld](https://schema.beckn.io/Plan/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Plan/vocab.jsonld](https://schema.beckn.io/Plan/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Plan/v2.0/vocab.jsonld](https://schema.beckn.io/Plan/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `requestedTime` | no | string | The departure or arrival time that was requested |
| `itineraries` | no | $ref: https://schema.beckn.io/Itinerary/v2.0/attributes.yaml#/components/schemas/Itinerary | List of itinerary options returned in the plan |
| `from` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Origin location for this plan |
| `to` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Destination location for this plan |
| `id` | no | string | Unique identifier for the catalog |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the catalog |
| `tags` | no | string | Tags associated with the catalog |
