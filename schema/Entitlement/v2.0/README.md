# Entitlement — v2.0

A contractually granted, policy-governed right that allows a specific party to access, use, or claim a defined economic resource within stated scope and validity constraints. It represents the enforceable permission created by an order, independent of the credential used to exercise it.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Entitlement/attributes.yaml](https://schema.beckn.io/Entitlement/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Entitlement/v2.0/attributes.yaml](https://schema.beckn.io/Entitlement/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Entitlement/attributes.jsonschema.yaml](https://schema.beckn.io/Entitlement/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Entitlement/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Entitlement/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Entitlement/context.jsonld](https://schema.beckn.io/Entitlement/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Entitlement/v2.0/context.jsonld](https://schema.beckn.io/Entitlement/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Entitlement/vocab.jsonld](https://schema.beckn.io/Entitlement/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Entitlement/v2.0/vocab.jsonld](https://schema.beckn.io/Entitlement/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | CPD |
| `@type` | yes | string | The domain-specific type of entitlement that allows domains to extend this schema |
| `id` | yes | string | A unique identifier for this entitlement within the entitlement provider's namespace |
| `resource` | no | $ref: https://schema.beckn.io/ContractItem/attributes.yaml#/components/schemas/ContractItem | The resource being availed or accessed against this entitlement |
| `descriptor` | yes | $ref: https://schema.beckn.io/Descriptor/attributes.yaml#/components/schemas/Descriptor | Human-readable information regarding the entitlement like QR-code images, attached documents containing terms and conditions, video or audio files instructing the user on how to use the entitlement |
| `credentials` | no | array | - |
