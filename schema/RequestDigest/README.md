# RequestDigest

A cryptographic binding that explicitly ties a callback to the
specific inbound request that triggered it. Establishes bilateral non-repudiation
for the asynchronous leg of a Beckn interaction.

Use `lineage` (on `Context`) for cross-transaction causality.

Verification steps:
1. Recompute BLAKE2b-512 digest of the original request body; compare to `digest`.
2. Confirm `messageId` matches the `messageId` from the original request `Context`.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute.

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/RequestDigest/v2.0/attributes.yaml](https://schema.beckn.io/RequestDigest/v2.0/attributes.yaml) | [https://schema.beckn.io/RequestDigest/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/RequestDigest/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/RequestDigest/v2.0/context.jsonld](https://schema.beckn.io/RequestDigest/v2.0/context.jsonld) | [https://schema.beckn.io/RequestDigest/v2.0/vocab.jsonld](https://schema.beckn.io/RequestDigest/v2.0/vocab.jsonld) | [https://schema.beckn.io/RequestDigest/v2.0/README.md](https://schema.beckn.io/RequestDigest/v2.0/README.md) |
