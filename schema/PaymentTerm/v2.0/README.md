# PaymentTerm — v2.0

A single payment instruction for an order. Represents one line item in the paymentTerms array of an Order — e.g., a pre-order UPI payment, a cash-on-delivery amount, or an instalment.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/PaymentTerm/attributes.yaml](https://schema.beckn.io/PaymentTerm/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/PaymentTerm/v2.0/attributes.yaml](https://schema.beckn.io/PaymentTerm/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/PaymentTerm/attributes.jsonschema.yaml](https://schema.beckn.io/PaymentTerm/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/PaymentTerm/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/PaymentTerm/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/PaymentTerm/context.jsonld](https://schema.beckn.io/PaymentTerm/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/PaymentTerm/v2.0/context.jsonld](https://schema.beckn.io/PaymentTerm/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/PaymentTerm/vocab.jsonld](https://schema.beckn.io/PaymentTerm/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/PaymentTerm/v2.0/vocab.jsonld](https://schema.beckn.io/PaymentTerm/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `id` | no | string | Unique identifier for this payment term within the order. |
| `type` | no | string | Payment lifecycle stage. |
| `method` | no | string | Payment instrument or rail to use. |
| `amount` | no | object | Amount due under this payment term. |
| `due` | no | string | ISO 8601 date-time by which this payment is due. |
| `payTo` | no | object | Payee details for this payment term. |
| `status` | no | string | Payment status. |
| `transactionId` | no | string | Payment gateway or bank transaction reference ID. |
