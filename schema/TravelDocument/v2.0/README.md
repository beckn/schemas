# TravelDocument — v2.0

A document (physical or digital) issued to a passenger proving entitlement to travel, used for validation or inspection.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/TravelDocument/attributes.yaml](https://schema.beckn.io/TravelDocument/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/TravelDocument/v2.0/attributes.yaml](https://schema.beckn.io/TravelDocument/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/TravelDocument/attributes.jsonschema.yaml](https://schema.beckn.io/TravelDocument/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/TravelDocument/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/TravelDocument/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/TravelDocument/context.jsonld](https://schema.beckn.io/TravelDocument/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/TravelDocument/v2.0/context.jsonld](https://schema.beckn.io/TravelDocument/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/TravelDocument/vocab.jsonld](https://schema.beckn.io/TravelDocument/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/TravelDocument/v2.0/vocab.jsonld](https://schema.beckn.io/TravelDocument/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `documentType` | no | string | Type of travel document (e.g. E_TICKET, PDF_TICKET, SMARTCARD, BARCODE) |
| `documentNumber` | no | string | Unique document number or serial |
| `issuingAuthority` | no | $ref: https://schema.beckn.io/Operator/v2.0/attributes.yaml#/components/schemas/Operator | The operator or authority that issued this document |
| `validFrom` | no | string | Start date of the document validity |
| `validUntil` | no | string | Expiry date of the document |
| `id` | no | string | Unique identifier for the entitlement |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable information about the entitlement |
| `resource` | no | $ref: https://schema.beckn.io/ContractItem/v2.0/attributes.yaml#/components/schemas/ContractItem | The resource being accessed against this entitlement |
| `credentials` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Credential descriptors for the entitlement |
