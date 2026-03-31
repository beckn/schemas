# LineageEntry — v2.0

A causal attribution record asserting that the Beckn transaction in which this entry appears was triggered by a specific upstream Beckn interaction. Used in Context.lineage at transaction boundaries — when a new transaction is initiated as a direct consequence of an upstream interaction. MUST NOT be included within subsequent steps of the same transaction, and MUST NOT be propagated by downstream responses.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/LineageEntry/attributes.yaml](https://schema.beckn.io/LineageEntry/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/LineageEntry/v2.0/attributes.yaml](https://schema.beckn.io/LineageEntry/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/LineageEntry/attributes.jsonschema.yaml](https://schema.beckn.io/LineageEntry/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/LineageEntry/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/LineageEntry/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/LineageEntry/context.jsonld](https://schema.beckn.io/LineageEntry/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/LineageEntry/v2.0/context.jsonld](https://schema.beckn.io/LineageEntry/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/LineageEntry/vocab.jsonld](https://schema.beckn.io/LineageEntry/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/LineageEntry/v2.0/vocab.jsonld](https://schema.beckn.io/LineageEntry/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `action` | yes | $ref: https://schema.beckn.io/BecknEndpoint/attributes.yaml#/components/schemas/BecknEndpoint | The Beckn endpoint of the upstream message that caused this transaction to be initiated. |
| `transactionId` | yes | string | The transactionId of the upstream Beckn transaction, taken from its Context. |
| `messageId` | yes | string | The messageId of the specific upstream message that directly triggered the creation of this transaction. |
| `digest` | yes | string | BLAKE2b-512 hash of the upstream message body bytes, encoded in Base64 and prefixed with the algorithm identifier. Format: BLAKE-512={base64EncodedHash} |
