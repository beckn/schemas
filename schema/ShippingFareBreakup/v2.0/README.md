# ShippingFareBreakup — v2.0

A single line item in the fare breakup for a logistics service.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/ShippingFareBreakup/attributes.yaml](https://schema.beckn.io/ShippingFareBreakup/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/ShippingFareBreakup/v2.0/attributes.yaml](https://schema.beckn.io/ShippingFareBreakup/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/ShippingFareBreakup/attributes.jsonschema.yaml](https://schema.beckn.io/ShippingFareBreakup/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/ShippingFareBreakup/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/ShippingFareBreakup/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/ShippingFareBreakup/context.jsonld](https://schema.beckn.io/ShippingFareBreakup/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/ShippingFareBreakup/v2.0/context.jsonld](https://schema.beckn.io/ShippingFareBreakup/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/ShippingFareBreakup/vocab.jsonld](https://schema.beckn.io/ShippingFareBreakup/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/ShippingFareBreakup/v2.0/vocab.jsonld](https://schema.beckn.io/ShippingFareBreakup/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `title` | yes | string | Name of the fare component |
| `amount` | yes | number | - |
| `currency` | no | string | - |
| `type` | no | string | - |
| `taxBreakup` | no | array | Tax sub-components if applicable |
| `waived` | no | boolean | Whether this component was waived |
