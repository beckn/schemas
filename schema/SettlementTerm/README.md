# Settlement Term

> **Canonical IRI:** [`https://schema.beckn.io/SettlementTerm`](https://schema.beckn.io/SettlementTerm)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Describes the terms of settlement associated with a given transaction. This is not to be confused with the PaymentAction as it describes all the places where the money gets disbursed after reconciliation.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | — | — |
| `@type` | `string` | — | — |
| `amount` | object | — | Amount associated with this settlement action |
| `paymentTrigger` | any | — | Describes the event which triggers the payment against this settlement term |
| `settlementStatus` | `string` | — | — |
| `settlementSchedule` | object | — | — |
| `payTo` | `object` \| `object` \| `object` | — | Describes the details of the account where the money must be remited. It could be a bank account, a payment gateway, or a virtual payment address (… |
| `acceptedPaymentMethods` | string[] | — | Describes the methods or mechanisms accepted by the payee (described in the payTo property) for the purpose of this settlement. |
| `settlementTermAttributes` | any | — | Additional use case specific settlement terms that must be adhered to |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/SettlementTerm` |
| JSON Schema (latest) | `https://schema.beckn.io/SettlementTerm/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/SettlementTerm/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/SettlementTerm/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
