# FareBreakup — v2.0

A detailed breakdown of the total fare into its constituent components, including base fare, taxes, surcharges, and discounts.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FareBreakup/attributes.yaml](https://schema.beckn.io/FareBreakup/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FareBreakup/v2.0/attributes.yaml](https://schema.beckn.io/FareBreakup/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FareBreakup/attributes.jsonschema.yaml](https://schema.beckn.io/FareBreakup/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FareBreakup/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FareBreakup/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FareBreakup/context.jsonld](https://schema.beckn.io/FareBreakup/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FareBreakup/v2.0/context.jsonld](https://schema.beckn.io/FareBreakup/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FareBreakup/vocab.jsonld](https://schema.beckn.io/FareBreakup/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FareBreakup/v2.0/vocab.jsonld](https://schema.beckn.io/FareBreakup/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `componentTitle` | no | string | Human-readable title for this fare component |
| `amount` | no | number | Monetary amount for this fare component |
| `currency` | no | string | ISO 4217 currency code for this component |
| `taxAmount` | no | number | Tax amount included in this component |
| `taxRate` | no | number | Tax rate percentage applied |
| `title` | no | string | Title or label of this price component |
| `price` | no | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | Monetary value of this component |
| `tags` | no | string | Tags associated with this price component |
