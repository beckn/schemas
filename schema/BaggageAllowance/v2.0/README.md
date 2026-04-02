# BaggageAllowance — v2.0

The quantity and weight of baggage a passenger is permitted to carry or check in without incurring additional charges.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/BaggageAllowance/attributes.yaml](https://schema.beckn.io/BaggageAllowance/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/BaggageAllowance/v2.0/attributes.yaml](https://schema.beckn.io/BaggageAllowance/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/BaggageAllowance/attributes.jsonschema.yaml](https://schema.beckn.io/BaggageAllowance/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/BaggageAllowance/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/BaggageAllowance/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/BaggageAllowance/context.jsonld](https://schema.beckn.io/BaggageAllowance/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/BaggageAllowance/v2.0/context.jsonld](https://schema.beckn.io/BaggageAllowance/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/BaggageAllowance/vocab.jsonld](https://schema.beckn.io/BaggageAllowance/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/BaggageAllowance/v2.0/vocab.jsonld](https://schema.beckn.io/BaggageAllowance/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `cabinBaggageCount` | no | number | Maximum number of cabin (carry-on) bags allowed |
| `cabinBaggageWeight` | no | number | Maximum weight in kilograms for cabin baggage |
| `checkedBaggageCount` | no | number | Maximum number of checked bags allowed |
| `checkedBaggageWeight` | no | number | Maximum weight in kilograms per checked bag |
| `id` | no | string | Unique identifier for the constraint |
| `constraintType` | no | string | Type of constraint (extensible term) |
| `operator` | no | string | Comparator operator (e.g. <=, >=, =) |
| `value` | no | number | Numeric value of the constraint |
| `unitCode` | no | string | Unit of measure code (UN/ECE Rec 20) |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity window for this constraint |
