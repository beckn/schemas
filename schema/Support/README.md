# Support

> **Canonical IRI:** [`https://schema.beckn.io/Support`](https://schema.beckn.io/Support)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for Support in the Beckn Protocol v2.0.1

Support request payload sent by a BAP to a BPP in the `/beckn/support` call.
Used to request support contact information, report an issue, or open a
support ticket for an existing order.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI. |
| `@type` | `string` | ✅ | Must be `Support`. |
| `orderId` | `string` | — | The order against which support is required. |
| `ticketIds` | `array` | — | IDs of existing support tickets for this order. |
| `callbackPhone` | `string` | — | Telephone number of the user for a support callback. |
| `issue` | `string` | — | Free-text description of the issue requiring support. |
| `issueCode` | `string` | — | Structured issue category code (domain-defined). |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Support` |
| JSON Schema (latest) | `https://schema.beckn.io/Support/v2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Support/v2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Support/v2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
