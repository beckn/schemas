# PaymentAction — v2.0

Schema definition for PaymentAction in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/PaymentAction/attributes.yaml](https://schema.beckn.io/PaymentAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/PaymentAction/v2.0/attributes.yaml](https://schema.beckn.io/PaymentAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/PaymentAction/attributes.jsonschema.yaml](https://schema.beckn.io/PaymentAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/PaymentAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/PaymentAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/PaymentAction/context.jsonld](https://schema.beckn.io/PaymentAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/PaymentAction/v2.0/context.jsonld](https://schema.beckn.io/PaymentAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/PaymentAction/vocab.jsonld](https://schema.beckn.io/PaymentAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/PaymentAction/v2.0/vocab.jsonld](https://schema.beckn.io/PaymentAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `amount` | no | object | Amount associated with this payment action |
| `paymentStatus` | yes | string | Payment lifecycle status (Pending \| Authorized \| Captured \| Failed \| Refunded \| PartialRefund …) |
| `paymentMethod` | no | object | - |
| `paymentUrl` | no | string | URL for payment processing/redirection |
| `state` | no | $ref: https://schema.beckn.io/State/v2.0/attributes.yaml#/components/schemas/State | - |
| `txnRef` | no | string | PSP/gateway/bank transaction reference |
| `checkoutAt` | no | $ref: https://schema.beckn.io/CheckoutTerminal/v2.0/attributes.yaml#/components/schemas/CheckoutTerminal | - |
| `paidAt` | no | string | The time at which the payment was made |
| `paymentActionAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Extensible set of attributes containing payment actions specific to each ecosystem. |
