# OnSelectAction — v2.0

Beckn /beckn/on_select message payload. Sent by a BPP to a BAP in
response to a /beckn/select call, with updated contract terms.
(Context wrapper stripped; only the message-content portion is inlined.)

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/OnSelectAction/attributes.yaml](https://schema.beckn.io/OnSelectAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/OnSelectAction/v2.0/attributes.yaml](https://schema.beckn.io/OnSelectAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/OnSelectAction/attributes.jsonschema.yaml](https://schema.beckn.io/OnSelectAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/OnSelectAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/OnSelectAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/OnSelectAction/context.jsonld](https://schema.beckn.io/OnSelectAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/OnSelectAction/v2.0/context.jsonld](https://schema.beckn.io/OnSelectAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/OnSelectAction/vocab.jsonld](https://schema.beckn.io/OnSelectAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/OnSelectAction/v2.0/vocab.jsonld](https://schema.beckn.io/OnSelectAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `contract` | yes | $ref: https://schema.beckn.io/Contract/v2.0/attributes.yaml#/components/schemas/Contract | - |
