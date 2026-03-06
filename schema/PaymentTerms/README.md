# Payment Terms

> **Canonical IRI:** [`https://schema.beckn.io/PaymentTerms`](https://schema.beckn.io/PaymentTerms)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for PaymentTerms in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | — | — |
| `@type` | `string` | — | — |
| `collectedBy` | `string` | — | Describes the entity that first collects the payment from the consumer. This is the actor who is responsible to initiate the settlement process as … |
| `checkoutAt` | object | — | — |
| `settlementTerms` | any[] | — | — |
| `checkoutTrigger` | any | — | The stage in the order lifecycle when the checkout should be triggered |
| `paymentTermsAttributes` | any | — | Rail-specific attribute pack (e.g., UPI: VPA/UTR; CARD: token/3DS; BNPL: plan/schedule) |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/PaymentTerms` |
| JSON Schema (latest) | `https://schema.beckn.io/PaymentTerms/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/PaymentTerms/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/PaymentTerms/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
