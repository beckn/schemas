# FareMedium — v2.0

The physical or digital medium used to carry or present a fare product, such as a contactless card, mobile app, or paper ticket.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FareMedium/attributes.yaml](https://schema.beckn.io/FareMedium/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FareMedium/v2.0/attributes.yaml](https://schema.beckn.io/FareMedium/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FareMedium/attributes.jsonschema.yaml](https://schema.beckn.io/FareMedium/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FareMedium/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FareMedium/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FareMedium/context.jsonld](https://schema.beckn.io/FareMedium/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FareMedium/v2.0/context.jsonld](https://schema.beckn.io/FareMedium/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FareMedium/vocab.jsonld](https://schema.beckn.io/FareMedium/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FareMedium/v2.0/vocab.jsonld](https://schema.beckn.io/FareMedium/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `mediumType` | no | string | Type of fare medium (e.g. CONTACTLESS_CARD, MOBILE_APP, PAPER_TICKET, QR_CODE) |
| `mediumId` | no | string | Unique identifier or number of the physical or digital medium |
| `id` | no | string | Unique identifier for the entitlement |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable information about the entitlement |
| `resource` | no | $ref: https://schema.beckn.io/ContractItem/v2.0/attributes.yaml#/components/schemas/ContractItem | The resource being accessed against this entitlement |
| `credentials` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Credential descriptors for the entitlement |
