# OnStatusAction — v2.0

Beckn /beckn/on_status callback envelope. Sent by a BPP to a BAP in response to a /beckn/status call (or as an unsolicited status push), returning the current state of the contract.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/OnStatusAction/attributes.yaml](https://schema.beckn.io/OnStatusAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/OnStatusAction/v2.0/attributes.yaml](https://schema.beckn.io/OnStatusAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/OnStatusAction/attributes.jsonschema.yaml](https://schema.beckn.io/OnStatusAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/OnStatusAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/OnStatusAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/OnStatusAction/context.jsonld](https://schema.beckn.io/OnStatusAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/OnStatusAction/v2.0/context.jsonld](https://schema.beckn.io/OnStatusAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/OnStatusAction/vocab.jsonld](https://schema.beckn.io/OnStatusAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/OnStatusAction/v2.0/vocab.jsonld](https://schema.beckn.io/OnStatusAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `context` | yes | allOf | - |
| `message` | yes | object | - |
