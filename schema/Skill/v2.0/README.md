# Skill — v2.0

Schema definition for Skill in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Skill/attributes.yaml](https://schema.beckn.io/Skill/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Skill/v2.0/attributes.yaml](https://schema.beckn.io/Skill/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Skill/attributes.jsonschema.yaml](https://schema.beckn.io/Skill/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Skill/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Skill/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Skill/context.jsonld](https://schema.beckn.io/Skill/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Skill/v2.0/context.jsonld](https://schema.beckn.io/Skill/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Skill/vocab.jsonld](https://schema.beckn.io/Skill/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Skill/v2.0/vocab.jsonld](https://schema.beckn.io/Skill/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `category` | no | $ref: https://schema.beckn.io/CategoryCode/v2.1/attributes.yaml#/components/schemas/CategoryCode | - |
| `descriptor` | yes | $ref: https://schema.beckn.io/Descriptor/v2.1/attributes.yaml#/components/schemas/Descriptor | - |
| `id` | yes | string | - |
