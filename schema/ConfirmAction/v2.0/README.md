# ConfirmAction — v2.0

Beckn /beckn/confirm message payload. Sent by a BAP to a BPP to confirm
a contract, finalising the transaction terms agreed during the
select-init negotiation cycle.
(Context wrapper stripped; only the message-content portion is inlined.)

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/ConfirmAction/attributes.yaml](https://schema.beckn.io/ConfirmAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/ConfirmAction/v2.0/attributes.yaml](https://schema.beckn.io/ConfirmAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/ConfirmAction/attributes.jsonschema.yaml](https://schema.beckn.io/ConfirmAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/ConfirmAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/ConfirmAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/ConfirmAction/context.jsonld](https://schema.beckn.io/ConfirmAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/ConfirmAction/v2.0/context.jsonld](https://schema.beckn.io/ConfirmAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/ConfirmAction/vocab.jsonld](https://schema.beckn.io/ConfirmAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/ConfirmAction/v2.0/vocab.jsonld](https://schema.beckn.io/ConfirmAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `contract` | yes | $ref: https://schema.beckn.io/Contract/v2.0/attributes.yaml#/components/schemas/Contract | - |
