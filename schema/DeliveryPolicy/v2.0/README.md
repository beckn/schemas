# DeliveryPolicy — v2.0

Callback delivery retry configuration

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/DeliveryPolicy/attributes.yaml](https://schema.beckn.io/DeliveryPolicy/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/DeliveryPolicy/v2.0/attributes.yaml](https://schema.beckn.io/DeliveryPolicy/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/DeliveryPolicy/attributes.jsonschema.yaml](https://schema.beckn.io/DeliveryPolicy/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/DeliveryPolicy/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/DeliveryPolicy/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/DeliveryPolicy/context.jsonld](https://schema.beckn.io/DeliveryPolicy/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/DeliveryPolicy/v2.0/context.jsonld](https://schema.beckn.io/DeliveryPolicy/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/DeliveryPolicy/vocab.jsonld](https://schema.beckn.io/DeliveryPolicy/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/DeliveryPolicy/v2.0/vocab.jsonld](https://schema.beckn.io/DeliveryPolicy/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `timeoutSeconds` | no | integer | Per-request HTTP timeout in seconds |
| `maxPayloadBytes` | no | integer | Maximum callback payload size in bytes |
| `retryPolicy` | no | object | - |
