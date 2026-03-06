# Payment Action

> **Canonical IRI:** [`https://schema.beckn.io/PaymentAction`](https://schema.beckn.io/PaymentAction)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for PaymentAction in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | — |
| `@type` | `string` | ✅ | — |
| `amount` | object | — | Amount associated with this payment action |
| `paymentStatus` | `string` | ✅ | Payment lifecycle status (Pending \| Authorized \| Captured \| Failed \| Refunded \| PartialRefund …) |
| `paymentMethod` | object | — | — |
| `paymentUrl` | `string` (uri) | — | URL for payment processing/redirection |
| `state` | object | — | — |
| `txnRef` | `string` | — | PSP/gateway/bank transaction reference |
| `checkoutAt` | object | — | — |
| `paidAt` | `string` (date-time) | — | The time at which the payment was made |
| `paymentActionAttributes` | any | — | Extensible set of attributes containing payment actions specific to each ecosystem. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/PaymentAction` |
| JSON Schema (latest) | `https://schema.beckn.io/PaymentAction/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/PaymentAction/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/PaymentAction/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
