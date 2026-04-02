# InitAction — v2.0

Beckn /beckn/init message payload. Sent by a BAP to a BPP to initialise
a contract with consumer details (billing address, fulfillment preferences, etc.).
(Context wrapper stripped; only the message-content portion is inlined.)

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/InitAction/attributes.yaml](https://schema.beckn.io/InitAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/InitAction/v2.0/attributes.yaml](https://schema.beckn.io/InitAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/InitAction/attributes.jsonschema.yaml](https://schema.beckn.io/InitAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/InitAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/InitAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/InitAction/context.jsonld](https://schema.beckn.io/InitAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/InitAction/v2.0/context.jsonld](https://schema.beckn.io/InitAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/InitAction/vocab.jsonld](https://schema.beckn.io/InitAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/InitAction/v2.0/vocab.jsonld](https://schema.beckn.io/InitAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `contract` | yes | $ref: https://schema.beckn.io/Contract/v2.0/attributes.yaml#/components/schemas/Contract | - |
