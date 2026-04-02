# FulfillmentStageEndpoint — v2.0

A stage boundary endpoint (entry or exit) within a fulfillment, such as pickup, handover, warehouse in/out, border crossing, gate entry/exit, security check, etc. May require one or more proofs/permits/tokens/documents.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FulfillmentStageEndpoint/attributes.yaml](https://schema.beckn.io/FulfillmentStageEndpoint/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FulfillmentStageEndpoint/v2.0/attributes.yaml](https://schema.beckn.io/FulfillmentStageEndpoint/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FulfillmentStageEndpoint/attributes.jsonschema.yaml](https://schema.beckn.io/FulfillmentStageEndpoint/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FulfillmentStageEndpoint/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FulfillmentStageEndpoint/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FulfillmentStageEndpoint/context.jsonld](https://schema.beckn.io/FulfillmentStageEndpoint/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FulfillmentStageEndpoint/v2.0/context.jsonld](https://schema.beckn.io/FulfillmentStageEndpoint/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FulfillmentStageEndpoint/vocab.jsonld](https://schema.beckn.io/FulfillmentStageEndpoint/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FulfillmentStageEndpoint/v2.0/vocab.jsonld](https://schema.beckn.io/FulfillmentStageEndpoint/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | no | string | CPD |
| `@type` | no | string | - |
| `location` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | - |
| `time` | no | $ref: https://schema.beckn.io/TimePeriod/v2.1/attributes.yaml#/components/schemas/TimePeriod | - |
| `authorization` | no | array | One or more credentials required and/or issued at this endpoint. Includes machine-readable tokens (QR/URL/OTP) and manual documents (IDs, permits).  |
