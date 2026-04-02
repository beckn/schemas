# OnUpdateAction — v2.0

Beckn /beckn/on_update message payload. Sent by a BPP to a BAP in
response to a /beckn/update call (or as an unsolicited update push),
returning the updated contract state.
(Context wrapper stripped; only the message-content portion is inlined.)

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/OnUpdateAction/attributes.yaml](https://schema.beckn.io/OnUpdateAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/OnUpdateAction/v2.0/attributes.yaml](https://schema.beckn.io/OnUpdateAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/OnUpdateAction/attributes.jsonschema.yaml](https://schema.beckn.io/OnUpdateAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/OnUpdateAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/OnUpdateAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/OnUpdateAction/context.jsonld](https://schema.beckn.io/OnUpdateAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/OnUpdateAction/v2.0/context.jsonld](https://schema.beckn.io/OnUpdateAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/OnUpdateAction/vocab.jsonld](https://schema.beckn.io/OnUpdateAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/OnUpdateAction/v2.0/vocab.jsonld](https://schema.beckn.io/OnUpdateAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `contract` | yes | $ref: https://schema.beckn.io/Contract/v2.0/attributes.yaml#/components/schemas/Contract | - |
