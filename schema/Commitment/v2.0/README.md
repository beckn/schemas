# Commitment — v2.0

Container schemas fetched from beckn.yaml. This cannot be extended as it is a reserved schema in beckn protocol. Any additional properties added to this schema can only be made using its *Attributes property

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Commitment/attributes.yaml](https://schema.beckn.io/Commitment/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Commitment/v2.0/attributes.yaml](https://schema.beckn.io/Commitment/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Commitment/attributes.jsonschema.yaml](https://schema.beckn.io/Commitment/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Commitment/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Commitment/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Commitment/context.jsonld](https://schema.beckn.io/Commitment/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Commitment/v2.0/context.jsonld](https://schema.beckn.io/Commitment/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Commitment/vocab.jsonld](https://schema.beckn.io/Commitment/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Commitment/v2.0/vocab.jsonld](https://schema.beckn.io/Commitment/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | no | string | - |
| `status` | yes | object | - |
| `resources` | yes | array | - |
| `offer` | yes | $ref: https://schema.beckn.io/Offer/v2.1/attributes.yaml#/components/schemas/Offer | - |
| `commitmentAttributes` | no | allOf | Domain-specific extension attributes for this commitment. |
