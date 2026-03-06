# Lineage Entry

> **Canonical IRI:** [`https://schema.beckn.io/LineageEntry`](https://schema.beckn.io/LineageEntry)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

A causal attribution record asserting that the Beckn transaction in which this entry appears was triggered by a specific upstream Beckn interaction. Used in Context.lineage at transaction boundaries — when a new transaction is initiated as a direct consequence of an upstream interaction. MUST NOT be included within subsequent steps of the same transaction, and MUST NOT be propagated by downstream responses.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `action` | object | ✅ | The Beckn endpoint of the upstream message that caused this transaction to be initiated. |
| `transactionId` | `string` (uuid) | ✅ | The transactionId of the upstream Beckn transaction, taken from its Context. |
| `messageId` | `string` (uuid) | ✅ | The messageId of the specific upstream message that directly triggered the creation of this transaction. |
| `digest` | `string` | ✅ | BLAKE2b-512 hash of the upstream message body bytes, encoded in Base64 and prefixed with the algorithm identifier. Format: BLAKE-512={base64Encoded… |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/LineageEntry` |
| JSON Schema (latest) | `https://schema.beckn.io/LineageEntry/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/LineageEntry/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/LineageEntry/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
