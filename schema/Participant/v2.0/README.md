# Participant — v2.0

Schema definition for Participant in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Participant/attributes.yaml](https://schema.beckn.io/Participant/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Participant/v2.0/attributes.yaml](https://schema.beckn.io/Participant/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Participant/attributes.jsonschema.yaml](https://schema.beckn.io/Participant/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Participant/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Participant/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Participant/context.jsonld](https://schema.beckn.io/Participant/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Participant/v2.0/context.jsonld](https://schema.beckn.io/Participant/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Participant/vocab.jsonld](https://schema.beckn.io/Participant/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Participant/v2.0/vocab.jsonld](https://schema.beckn.io/Participant/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | any | One or more JSON-LD type IRIs for this participant. The first MUST be "beckn:Participant". Additional types (e.g. "beckn:Restaurant", "beckn:Consumer", "beckn:Rider") encode the domain role of the participant using sub-typing rather than a separate "role" field.  |
| `credentials` | no | array | - |
| `displayName` | no | string | - |
| `email` | no | string | - |
| `id` | yes | string | - |
| `rating` | no | $ref: https://schema.beckn.io/Rating/attributes.yaml#/components/schemas/Rating | - |
| `skills` | no | array | - |
| `telephone` | no | string | - |
