# Update Action

> **Canonical IRI:** [`https://schema.beckn.io/UpdateAction`](https://schema.beckn.io/UpdateAction)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Beckn /beckn/update action envelope. Sent by a BAP to a BPP to request changes to an active contract (e.g., update fulfillment address, add items, change quantities). The context.try flag must be true during negotiation.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `context` | `object` | ✅ | — |
| `message` | object | ✅ | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/UpdateAction` |
| JSON Schema (latest) | `https://schema.beckn.io/UpdateAction/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/UpdateAction/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/UpdateAction/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
