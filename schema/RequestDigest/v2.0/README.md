# RequestDigest — v2.0

A cryptographic binding that explicitly ties a callback to the
specific inbound request that triggered it. Establishes bilateral non-repudiation
for the asynchronous leg of a Beckn interaction.

Use `lineage` (on `Context`) for cross-transaction causality.

Verification steps:
1. Recompute BLAKE2b-512 digest of the original request body; compare to `digest`.
2. Confirm `messageId` matches the `messageId` from the original request `Context`.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/RequestDigest/attributes.yaml](https://schema.beckn.io/RequestDigest/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/RequestDigest/v2.0/attributes.yaml](https://schema.beckn.io/RequestDigest/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/RequestDigest/attributes.jsonschema.yaml](https://schema.beckn.io/RequestDigest/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/RequestDigest/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/RequestDigest/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/RequestDigest/context.jsonld](https://schema.beckn.io/RequestDigest/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/RequestDigest/v2.0/context.jsonld](https://schema.beckn.io/RequestDigest/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/RequestDigest/vocab.jsonld](https://schema.beckn.io/RequestDigest/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/RequestDigest/v2.0/vocab.jsonld](https://schema.beckn.io/RequestDigest/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `digest` | yes | string | BLAKE2b-512 hash of the parent request body, Base64-encoded with algorithm prefix. Format: `BLAKE-512={base64EncodedHash}` |
