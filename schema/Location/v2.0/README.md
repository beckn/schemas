# Location — v2.0

A **place** represented by **GeoJSON geometry** (Point/Polygon/Multi*) and optional human-readable `address`. This unifies all Beckn location fields into a single, widely-adopted representation (GeoJSON).

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Location/attributes.yaml](https://schema.beckn.io/Location/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Location/v2.0/attributes.yaml](https://schema.beckn.io/Location/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Location/attributes.jsonschema.yaml](https://schema.beckn.io/Location/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Location/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Location/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Location/context.jsonld](https://schema.beckn.io/Location/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Location/v2.0/context.jsonld](https://schema.beckn.io/Location/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Location/vocab.jsonld](https://schema.beckn.io/Location/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Location/v2.0/vocab.jsonld](https://schema.beckn.io/Location/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@type` | no | string | - |
| `address` | no | any | Optional human-readable address for the same place/area. |
| `geo` | yes | $ref: https://schema.beckn.io/GeoJSONGeometry/attributes.yaml#/components/schemas/GeoJSONGeometry | - |
