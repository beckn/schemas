# Ack — v2.0

New v2.0 Ack format carrying an HTTP Counter-Signature proving the receiver authenticated, received, and processed the inbound request.

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
| `status` | yes | string | ACK if the request was accepted; NACK if rejected. |
| `signature` | yes | $ref: https://schema.beckn.io/CounterSignature/v2.0/attributes.yaml#/components/schemas/CounterSignature | Counter-signature proving the receiver authenticated and processed the inbound request. |
