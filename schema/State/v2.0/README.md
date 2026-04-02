# State — v2.0

Schema definition for State in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/State/attributes.yaml](https://schema.beckn.io/State/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/State/v2.0/attributes.yaml](https://schema.beckn.io/State/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/State/attributes.jsonschema.yaml](https://schema.beckn.io/State/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/State/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/State/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/State/context.jsonld](https://schema.beckn.io/State/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/State/v2.0/context.jsonld](https://schema.beckn.io/State/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/State/vocab.jsonld](https://schema.beckn.io/State/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/State/v2.0/vocab.jsonld](https://schema.beckn.io/State/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | CPD |
| `@type` | yes | string | TPD |
| `descriptor` | yes | $ref: https://schema.beckn.io/Descriptor/v2.1/attributes.yaml#/components/schemas/Descriptor | - |
