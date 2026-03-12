# PaymentTerm — v2.0

A single payment instruction for an order. Represents one line item in the
`paymentTerms` array of an Order — e.g., a pre-order UPI payment, a cash-on-delivery
amount, or an instalment.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [PaymentTerm](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `PaymentTerm` |
| [context.jsonld](./context.jsonld) | JSON-LD context mapping properties to beckn IRIs |
| [vocab.jsonld](./vocab.jsonld) | RDF vocabulary declaration for this schema |

## Properties

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI. |
| `@type` | `string` | ✅ | Must be `beckn:PaymentTerm`. |
| `id` | `string` | — | Unique identifier for this payment term within the order. |
| `type` | `string` (enum) | — | Payment lifecycle stage. |
| `method` | `string` (enum) | — | Payment instrument or rail to use. |
| `amount` | `object` | — | Amount due under this payment term. |
| `due` | `string` (date-time) | — | ISO 8601 date-time by which this payment is due. |
| `payTo` | `object` | — | Payee details for this payment term. |
| `status` | `string` (enum) | — | Payment status. |
| `transactionId` | `string` | — | Payment gateway or bank transaction reference ID. |
