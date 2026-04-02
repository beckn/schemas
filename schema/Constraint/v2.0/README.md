# Constraint — v2.0

Schema definition for Constraint in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Constraint/attributes.yaml](https://schema.beckn.io/Constraint/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Constraint/v2.0/attributes.yaml](https://schema.beckn.io/Constraint/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Constraint/attributes.jsonschema.yaml](https://schema.beckn.io/Constraint/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Constraint/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Constraint/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Constraint/context.jsonld](https://schema.beckn.io/Constraint/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Constraint/v2.0/context.jsonld](https://schema.beckn.io/Constraint/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Constraint/vocab.jsonld](https://schema.beckn.io/Constraint/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Constraint/v2.0/vocab.jsonld](https://schema.beckn.io/Constraint/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | CPD |
| `@type` | yes | string | - |
| `constraintType` | no | string | Type of constraint (extensible term) |
| `id` | yes | string | Identifier for the constraint |
| `operator` | no | string | Comparator/operator (<=, >=, =, etc.) |
| `unitCode` | no | string | Unit code (e.g., km, min) |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.1/attributes.yaml#/components/schemas/TimePeriod | - |
| `value` | no | number | Constraint value |
