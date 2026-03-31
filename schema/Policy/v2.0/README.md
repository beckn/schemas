# Policy — v2.0

Schema definition for Policy in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Policy/attributes.yaml](https://schema.beckn.io/Policy/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Policy/v2.0/attributes.yaml](https://schema.beckn.io/Policy/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Policy/attributes.jsonschema.yaml](https://schema.beckn.io/Policy/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Policy/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Policy/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Policy/context.jsonld](https://schema.beckn.io/Policy/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Policy/v2.0/context.jsonld](https://schema.beckn.io/Policy/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Policy/vocab.jsonld](https://schema.beckn.io/Policy/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Policy/v2.0/vocab.jsonld](https://schema.beckn.io/Policy/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `descriptor` | yes | $ref: https://schema.beckn.io/Descriptor/attributes.yaml#/components/schemas/Descriptor | Validity window for this policy version |
| `id` | yes | string | Identifier for the policy |
| `policyType` | no | string | Type/kind of policy (extensible term) |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/attributes.yaml#/components/schemas/TimePeriod | Validity window for this policy version |
| `policyAttributes` | no | $ref: https://schema.beckn.io/Attributes/attributes.yaml#/components/schemas/Attributes | - |
