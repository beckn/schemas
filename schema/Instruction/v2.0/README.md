# Instruction — v2.0

Schema definition for Instruction in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Instruction/attributes.yaml](https://schema.beckn.io/Instruction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Instruction/v2.0/attributes.yaml](https://schema.beckn.io/Instruction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Instruction/attributes.jsonschema.yaml](https://schema.beckn.io/Instruction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Instruction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Instruction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Instruction/context.jsonld](https://schema.beckn.io/Instruction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Instruction/v2.0/context.jsonld](https://schema.beckn.io/Instruction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Instruction/vocab.jsonld](https://schema.beckn.io/Instruction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Instruction/v2.0/vocab.jsonld](https://schema.beckn.io/Instruction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `descriptor` | yes | $ref: https://schema.beckn.io/Descriptor/attributes.yaml#/components/schemas/Descriptor | - |
| `id` | yes | string | - |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/attributes.yaml#/components/schemas/TimePeriod | - |
