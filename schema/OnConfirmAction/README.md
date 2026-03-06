# On Confirm Action

> **Canonical IRI:** [`https://schema.beckn.io/OnConfirmAction`](https://schema.beckn.io/OnConfirmAction)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Beckn /beckn/on_confirm callback envelope. Sent by a BPP to a BAP in response to a /beckn/confirm call, returning the confirmed contract with status set to CONFIRMED.

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
| Canonical IRI | `https://schema.beckn.io/OnConfirmAction` |
| JSON Schema (latest) | `https://schema.beckn.io/OnConfirmAction/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/OnConfirmAction/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/OnConfirmAction/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
