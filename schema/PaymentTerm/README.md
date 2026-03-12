# PaymentTerm

> **Canonical IRI:** [`https://schema.beckn.io/PaymentTerm`](https://schema.beckn.io/PaymentTerm)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for PaymentTerm in the Beckn Protocol v2.0.1

A single payment instruction for an order. Represents one line item in the
`paymentTerms` array of an Order — e.g., a pre-order UPI payment, a cash-on-delivery
amount, or an instalment.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI. |
| `@type` | `string` | ✅ | Must be `beckn:PaymentTerm`. |
| `id` | `string` | — | Unique identifier for this payment term within the order. |
| `type` | `string` (enum) | — | Payment lifecycle stage (PRE_ORDER, ON_FULFILLMENT, POST_FULFILLMENT, INSTALLMENT). |
| `method` | `string` (enum) | — | Payment instrument or rail to use. |
| `amount` | `object` | — | Amount due under this payment term. |
| `due` | `string` (date-time) | — | ISO 8601 date-time by which this payment is due. |
| `payTo` | `object` | — | Payee details for this payment term. |
| `status` | `string` (enum) | — | Payment status. |
| `transactionId` | `string` | — | Payment gateway or bank transaction reference ID. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/PaymentTerm` |
| JSON Schema (latest) | `https://schema.beckn.io/PaymentTerm/v2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/PaymentTerm/v2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/PaymentTerm/v2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
