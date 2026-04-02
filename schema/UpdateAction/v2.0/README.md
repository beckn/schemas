# UpdateAction — v2.0

Beckn /beckn/update message payload. Sent by a BAP to a BPP to request
changes to an active contract (e.g., update fulfillment address, add items,
change quantities). The context.try flag must be true during negotiation.
(Context wrapper stripped; only the message-content portion is inlined.)

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/UpdateAction/attributes.yaml](https://schema.beckn.io/UpdateAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/UpdateAction/v2.0/attributes.yaml](https://schema.beckn.io/UpdateAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/UpdateAction/attributes.jsonschema.yaml](https://schema.beckn.io/UpdateAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/UpdateAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/UpdateAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/UpdateAction/context.jsonld](https://schema.beckn.io/UpdateAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/UpdateAction/v2.0/context.jsonld](https://schema.beckn.io/UpdateAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/UpdateAction/vocab.jsonld](https://schema.beckn.io/UpdateAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/UpdateAction/v2.0/vocab.jsonld](https://schema.beckn.io/UpdateAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `contract` | yes | $ref: https://schema.beckn.io/Contract/v2.0/attributes.yaml#/components/schemas/Contract | - |
