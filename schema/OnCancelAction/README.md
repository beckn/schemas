# On Cancel Action

> **Canonical IRI:** [`https://schema.beckn.io/OnCancelAction`](https://schema.beckn.io/OnCancelAction)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Beckn /beckn/on_cancel callback envelope. Sent by a BPP to a BAP in response to a /beckn/cancel call, returning the contract with status set to CANCELLED and any applicable cancellation outcome.

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
| Canonical IRI | `https://schema.beckn.io/OnCancelAction` |
| JSON Schema (latest) | `https://schema.beckn.io/OnCancelAction/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/OnCancelAction/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/OnCancelAction/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
