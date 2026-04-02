# LogisticsPlace — v2.0

A geographic location relevant to logistics such as origin, destination, hub, or waypoint. Includes structured address and GPS coordinates. Maps to beckn:Location and schema:Place.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/LogisticsPlace/attributes.yaml](https://schema.beckn.io/LogisticsPlace/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/LogisticsPlace/v2.0/attributes.yaml](https://schema.beckn.io/LogisticsPlace/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/LogisticsPlace/attributes.jsonschema.yaml](https://schema.beckn.io/LogisticsPlace/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/LogisticsPlace/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/LogisticsPlace/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/LogisticsPlace/context.jsonld](https://schema.beckn.io/LogisticsPlace/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/LogisticsPlace/v2.0/context.jsonld](https://schema.beckn.io/LogisticsPlace/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/LogisticsPlace/vocab.jsonld](https://schema.beckn.io/LogisticsPlace/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/LogisticsPlace/v2.0/vocab.jsonld](https://schema.beckn.io/LogisticsPlace/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | - |
| `name` | no | string | Name of the place |
| `type` | no | string | - |
| `address` | no | object | - |
| `gps` | no | object | - |
| `contact` | no | $ref: https://schema.beckn.io/Contact/v2.0/attributes.yaml#/components/schemas/Contact | - |
| `accessInstructions` | no | string | Instructions for courier to reach the place |
| `isVerified` | no | boolean | Whether the address has been geocode-verified |
