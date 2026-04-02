# Fare — v2.0

The monetary cost of travel for a specific journey or service, calculated based on applicable fare rules and passenger categories.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Fare/attributes.yaml](https://schema.beckn.io/Fare/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Fare/v2.0/attributes.yaml](https://schema.beckn.io/Fare/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Fare/attributes.jsonschema.yaml](https://schema.beckn.io/Fare/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Fare/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Fare/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Fare/context.jsonld](https://schema.beckn.io/Fare/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Fare/v2.0/context.jsonld](https://schema.beckn.io/Fare/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Fare/vocab.jsonld](https://schema.beckn.io/Fare/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Fare/v2.0/vocab.jsonld](https://schema.beckn.io/Fare/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `fareId` | no | string | Unique identifier for the fare |
| `amount` | no | number | Total fare amount |
| `currency` | no | string | ISO 4217 currency code |
| `fareAttributes` | no | string | Transfer permissions, agency, and transfer limit |
| `fareRules` | no | $ref: https://schema.beckn.io/FareLegRule/v2.0/attributes.yaml#/components/schemas/FareLegRule | Leg rules that determine when this fare applies |
| `id` | no | string | Unique identifier for the offer |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the offer |
| `price` | no | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | Price specification for this offer |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity period of the offer |
| `tags` | no | string | Tags or labels associated with the offer |
