# Lineage Entry — v2.0

A causal attribution record asserting that the Beckn transaction in which this entry appears was triggered by a specific upstream Beckn interaction. Used in Context.lineage at transaction boundaries — when a new transaction is initiated as a direct consequence of an upstream interaction. MUST NOT be included within subsequent steps of the same transaction, and MUST NOT be propagated by downstream responses.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [LineageEntry](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | JSON Schema 2020-12 definition for `LineageEntry` |
| [context.jsonld](./context.jsonld) | JSON-LD context for `LineageEntry` v2.0 |
| [vocab.jsonld](./vocab.jsonld) | RDF vocabulary for `LineageEntry` v2.0 |

## Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `action` | object | ✅ | The Beckn endpoint of the upstream message that caused this transaction to be initiated. |
| `transactionId` | string (uuid) | ✅ | The transactionId of the upstream Beckn transaction, taken from its Context. |
| `messageId` | string (uuid) | ✅ | The messageId of the specific upstream message that directly triggered the creation of this transaction. |
| `digest` | string | ✅ | BLAKE2b-512 hash of the upstream message body bytes, encoded in Base64 and prefixed with the algorithm identifier. Fo… |
