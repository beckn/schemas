# SupportResponse — v2.0

Support response payload returned by a BPP to a BAP in the /beckn/on_support callback. Contains the support ticket reference, available contact channels, SLA commitment, and optional consumer acknowledgement details.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/SupportResponse/attributes.yaml](https://schema.beckn.io/SupportResponse/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/SupportResponse/v2.0/attributes.yaml](https://schema.beckn.io/SupportResponse/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/SupportResponse/attributes.jsonschema.yaml](https://schema.beckn.io/SupportResponse/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/SupportResponse/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/SupportResponse/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/SupportResponse/context.jsonld](https://schema.beckn.io/SupportResponse/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/SupportResponse/v2.0/context.jsonld](https://schema.beckn.io/SupportResponse/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/SupportResponse/vocab.jsonld](https://schema.beckn.io/SupportResponse/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/SupportResponse/v2.0/vocab.jsonld](https://schema.beckn.io/SupportResponse/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `refId` | no | string | Reference identifier (typically the order ID) against which support was requested. |
| `ticketId` | no | string | Support ticket identifier assigned by the BPP. |
| `descriptor` | no | $ref: https://schema.beckn.io/Descriptor/v2.1/attributes.yaml#/components/schemas/Descriptor | Human-readable label for this support response. |
| `channels` | no | array | Available support channels with contact details. |
| `sla` | no | object | Service level agreement for this support response. |
| `consumer` | no | $ref: https://schema.beckn.io/Consumer/v2.0/attributes.yaml#/components/schemas/Consumer | The consumer the support response is addressed to (optional). |
