# Ack — v2.0

Synchronous receipt acknowledgement returned for every accepted Beckn request.
Supports both the v2.0 format (status + signature CounterSignature) and the
v2.0-rc1 legacy format (ack_status + transaction_id + timestamp) via oneOf
for backward compatibility.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Ack/attributes.yaml](https://schema.beckn.io/Ack/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Ack/v2.0/attributes.yaml](https://schema.beckn.io/Ack/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Ack/attributes.jsonschema.yaml](https://schema.beckn.io/Ack/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Ack/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Ack/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Ack/context.jsonld](https://schema.beckn.io/Ack/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Ack/v2.0/context.jsonld](https://schema.beckn.io/Ack/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Ack/vocab.jsonld](https://schema.beckn.io/Ack/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Ack/v2.0/vocab.jsonld](https://schema.beckn.io/Ack/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| _none_ | - | - | - |
