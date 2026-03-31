# PriceSpecification — v2.1

Schema definition for PriceSpecification in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/PriceSpecification/attributes.yaml](https://schema.beckn.io/PriceSpecification/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml](https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/PriceSpecification/attributes.jsonschema.yaml](https://schema.beckn.io/PriceSpecification/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/PriceSpecification/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/PriceSpecification/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/PriceSpecification/context.jsonld](https://schema.beckn.io/PriceSpecification/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/PriceSpecification/v2.1/context.jsonld](https://schema.beckn.io/PriceSpecification/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/PriceSpecification/vocab.jsonld](https://schema.beckn.io/PriceSpecification/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/PriceSpecification/v2.1/vocab.jsonld](https://schema.beckn.io/PriceSpecification/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `currency` | no | string | ISO 4217 code |
| `value` | no | number | Total value for this price specification |
| `applicableQuantity` | no | $ref: https://schema.beckn.io/Quantity/attributes.yaml#/components/schemas/Quantity | - |
| `components` | no | array | Optional components (tax, shipping, discount, fee, surcharge) |
