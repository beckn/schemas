# Support — v2.0

Describes a support session info

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Support/attributes.yaml](https://schema.beckn.io/Support/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Support/v2.0/attributes.yaml](https://schema.beckn.io/Support/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Support/attributes.jsonschema.yaml](https://schema.beckn.io/Support/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Support/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Support/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Support/context.jsonld](https://schema.beckn.io/Support/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Support/v2.0/context.jsonld](https://schema.beckn.io/Support/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Support/vocab.jsonld](https://schema.beckn.io/Support/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Support/v2.0/vocab.jsonld](https://schema.beckn.io/Support/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `orderId` | no | string | The order against which support is required |
| `descriptor` | no | $ref: https://schema.beckn.io/Descriptor/v2.1/attributes.yaml#/components/schemas/Descriptor | A description of the nature of support needed |
| `channels` | no | array | Available support channels described in individual linked data JSON objects |
