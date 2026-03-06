# Invoice

> **Canonical IRI:** [`https://schema.beckn.io/Invoice`](https://schema.beckn.io/Invoice)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for Invoice in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | CPD |
| `@type` | `string` | ✅ | TPD |
| `dueDate` | `string` (date) | — | — |
| `id` | `string` | ✅ | Stable invoice identifier (system id) |
| `invoiceAttributes` | any | — | Attribute Pack for tax regime (e.g., GST/VAT), e-invoice refs, legal boilerplate, etc. |
| `issueDate` | `string` (date) | ✅ | — |
| `number` | `string` | ✅ | Human-visible invoice number |
| `payee` | any | ✅ | Seller / issuer of the invoice |
| `payer` | any | ✅ | consumer being invoiced |
| `costBreakup` | any[] | — | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Invoice` |
| JSON Schema (latest) | `https://schema.beckn.io/Invoice/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Invoice/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Invoice/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
