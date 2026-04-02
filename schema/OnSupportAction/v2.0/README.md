# OnSupportAction — v2.0

Beckn /beckn/on_support message payload. Sent by a BPP to a BAP in
response to a /beckn/support call, returning support contact details
and available channels.
(Context wrapper stripped; only the message-content portion is inlined.)

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/OnSupportAction/attributes.yaml](https://schema.beckn.io/OnSupportAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/OnSupportAction/v2.0/attributes.yaml](https://schema.beckn.io/OnSupportAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/OnSupportAction/attributes.jsonschema.yaml](https://schema.beckn.io/OnSupportAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/OnSupportAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/OnSupportAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/OnSupportAction/context.jsonld](https://schema.beckn.io/OnSupportAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/OnSupportAction/v2.0/context.jsonld](https://schema.beckn.io/OnSupportAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/OnSupportAction/vocab.jsonld](https://schema.beckn.io/OnSupportAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/OnSupportAction/v2.0/vocab.jsonld](https://schema.beckn.io/OnSupportAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `support` | yes | $ref: https://schema.beckn.io/Support/v2.0/attributes.yaml#/components/schemas/Support | - |
