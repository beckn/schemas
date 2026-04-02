# RiderCategory — v2.0

A classification of passenger type (e.g., adult, child, senior, student) used to determine applicable fare entitlements.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/RiderCategory/attributes.yaml](https://schema.beckn.io/RiderCategory/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/RiderCategory/v2.0/attributes.yaml](https://schema.beckn.io/RiderCategory/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/RiderCategory/attributes.jsonschema.yaml](https://schema.beckn.io/RiderCategory/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/RiderCategory/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/RiderCategory/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/RiderCategory/context.jsonld](https://schema.beckn.io/RiderCategory/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/RiderCategory/v2.0/context.jsonld](https://schema.beckn.io/RiderCategory/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/RiderCategory/vocab.jsonld](https://schema.beckn.io/RiderCategory/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/RiderCategory/v2.0/vocab.jsonld](https://schema.beckn.io/RiderCategory/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `riderCategoryId` | no | string | Unique identifier for the rider category |
| `eligibilityRules` | no | string | Rules defining who qualifies for this rider category |
| `proofRequired` | no | string | Type of proof required to qualify (e.g. student ID, senior card) |
| `id` | no | string | Unique identifier for the category code |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable label for the category |
| `parentCategoryId` | no | string | Identifier of the parent category if hierarchical |
