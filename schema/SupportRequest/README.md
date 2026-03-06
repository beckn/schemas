# Support Request

> **Canonical IRI:** [`https://schema.beckn.io/SupportRequest`](https://schema.beckn.io/SupportRequest)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Support request by a user. If no field is set, the user can expect a public support contact info

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | — |
| `@type` | `string` | ✅ | — |
| `orderId` | `string` | — | The order against which support is required |
| `ticketIds` | [id](../id/README.md)[] | — | IDs of support ticket if open |
| `callbackPhone` | `string` | — | Telephone number of the user for callback. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/SupportRequest` |
| JSON Schema (latest) | `https://schema.beckn.io/SupportRequest/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/SupportRequest/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/SupportRequest/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
