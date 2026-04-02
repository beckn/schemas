# SurgeMultiplier — v2.0

A dynamic pricing factor applied during periods of high demand that increases base fares proportionally to balance supply and demand.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/SurgeMultiplier/attributes.yaml](https://schema.beckn.io/SurgeMultiplier/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/SurgeMultiplier/v2.0/attributes.yaml](https://schema.beckn.io/SurgeMultiplier/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/SurgeMultiplier/attributes.jsonschema.yaml](https://schema.beckn.io/SurgeMultiplier/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/SurgeMultiplier/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/SurgeMultiplier/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/SurgeMultiplier/context.jsonld](https://schema.beckn.io/SurgeMultiplier/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/SurgeMultiplier/v2.0/context.jsonld](https://schema.beckn.io/SurgeMultiplier/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/SurgeMultiplier/vocab.jsonld](https://schema.beckn.io/SurgeMultiplier/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/SurgeMultiplier/v2.0/vocab.jsonld](https://schema.beckn.io/SurgeMultiplier/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `multiplierValue` | no | number | The surge multiplier value (e.g. 1.5 for 1.5x surge) |
| `validUntil` | no | string | Timestamp until which the surge multiplier is active |
| `reason` | no | string | Reason for the surge (e.g. HIGH_DEMAND, SPECIAL_EVENT) |
| `geofenceRef` | no | $ref: https://schema.beckn.io/Geofence/v2.0/attributes.yaml#/components/schemas/Geofence | Geographic area where the surge pricing applies |
| `title` | no | string | Title or label of this price component |
| `price` | no | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | Monetary value of this component |
| `tags` | no | string | Tags associated with this price component |
