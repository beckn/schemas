# DiscoverAction — v2.0

Beckn /beckn/discover message payload as published at schema.beckn.io.
Requires all discover qualifiers to be nested inside an `intent`
container object.
(Context wrapper stripped; only the message-content portion is inlined.)

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/DiscoverAction/attributes.yaml](https://schema.beckn.io/DiscoverAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/DiscoverAction/v2.0/attributes.yaml](https://schema.beckn.io/DiscoverAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/DiscoverAction/attributes.jsonschema.yaml](https://schema.beckn.io/DiscoverAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/DiscoverAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/DiscoverAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/DiscoverAction/context.jsonld](https://schema.beckn.io/DiscoverAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/DiscoverAction/v2.0/context.jsonld](https://schema.beckn.io/DiscoverAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/DiscoverAction/vocab.jsonld](https://schema.beckn.io/DiscoverAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/DiscoverAction/v2.0/vocab.jsonld](https://schema.beckn.io/DiscoverAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `intent` | yes | $ref: https://schema.beckn.io/Intent/v2.0/attributes.yaml#/components/schemas/Intent | - |
| `text_search` | no | string | Legacy flat free-text discover query |
| `textSearch` | no | string | Flat free-text discover query |
