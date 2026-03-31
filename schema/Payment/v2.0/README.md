# Payment — v2.0

Schema definition for Payment in the Beckn Protocol

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Payment/attributes.yaml](https://schema.beckn.io/Payment/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Payment/v2.0/attributes.yaml](https://schema.beckn.io/Payment/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Payment/attributes.jsonschema.yaml](https://schema.beckn.io/Payment/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Payment/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Payment/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Payment/context.jsonld](https://schema.beckn.io/Payment/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Payment/v2.0/context.jsonld](https://schema.beckn.io/Payment/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Payment/vocab.jsonld](https://schema.beckn.io/Payment/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Payment/v2.0/vocab.jsonld](https://schema.beckn.io/Payment/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `beckn:id` | no | string | Payment record identifier |
| `beckn:paymentStatus` | yes | string | Payment lifecycle status (Pending \| Authorized \| Captured \| Failed \| Refunded \| PartialRefund …) |
| `beckn:amount` | no | object | Amount associated with this payment action |
| `beckn:paymentURL` | no | string | URL for payment processing/redirection |
| `beckn:txnRef` | no | string | PSP/gateway/bank transaction reference |
| `beckn:paidAt` | no | ['string', 'null'] | When the last terminal event (capture/refund) happened |
| `beckn:acceptedPaymentMethod` | no | $ref: https://schema.beckn.io/AcceptedPaymentMethod/attributes.yaml#/components/schemas/AcceptedPaymentMethod | - |
| `beckn:beneficiary` | no | string | Who will be the beneficiary or recipient of the payment |
| `beckn:paymentAttributes` | no | $ref: https://schema.beckn.io/Attributes/attributes.yaml#/components/schemas/Attributes | Rail-specific attribute pack (e.g., UPI: VPA/UTR; CARD: token/3DS; BNPL: plan/schedule)  |
