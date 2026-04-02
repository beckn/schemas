# PaymentTerms — v2.0

Schema definition for PaymentTerms in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/PaymentTerms/attributes.yaml](https://schema.beckn.io/PaymentTerms/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/PaymentTerms/v2.0/attributes.yaml](https://schema.beckn.io/PaymentTerms/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/PaymentTerms/attributes.jsonschema.yaml](https://schema.beckn.io/PaymentTerms/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/PaymentTerms/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/PaymentTerms/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/PaymentTerms/context.jsonld](https://schema.beckn.io/PaymentTerms/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/PaymentTerms/v2.0/context.jsonld](https://schema.beckn.io/PaymentTerms/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/PaymentTerms/vocab.jsonld](https://schema.beckn.io/PaymentTerms/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/PaymentTerms/v2.0/vocab.jsonld](https://schema.beckn.io/PaymentTerms/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | no | string | - |
| `@type` | no | string | - |
| `collectedBy` | no | string | Describes the entity that first collects the payment from the consumer. This is the actor who is responsible to initiate the settlement process as per the terms described in the settlementTerms property. |
| `checkoutAt` | no | $ref: https://schema.beckn.io/CheckoutTerminal/v2.0/attributes.yaml#/components/schemas/CheckoutTerminal | - |
| `settlementTerms` | no | array | - |
| `checkoutTrigger` | no | $ref: https://schema.beckn.io/PaymentTrigger/v2.0/attributes.yaml#/components/schemas/PaymentTrigger | The stage in the order lifecycle when the checkout should be triggered |
| `paymentTermsAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Rail-specific attribute pack (e.g., UPI: VPA/UTR; CARD: token/3DS; BNPL: plan/schedule) |
