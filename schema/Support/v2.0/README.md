# Support — v2.0

Support request payload sent by a BAP to a BPP in the /beckn/support call. Used to request support contact information, report an issue, or open a support ticket for an existing order.

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
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `orderId` | no | string | The order against which support is required. |
| `ticketIds` | no | array | IDs of existing support tickets (if open) for this order. |
| `callbackPhone` | no | string | Telephone number of the user for a support callback. |
| `issue` | no | string | Free-text description of the issue requiring support. |
| `issueCode` | no | string | Structured issue category code (domain-defined). |
