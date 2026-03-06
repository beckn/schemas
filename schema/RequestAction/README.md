# Request Action

> **Canonical IRI:** [`https://schema.beckn.io/RequestAction`](https://schema.beckn.io/RequestAction)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

DEPRECATED. This schema is structurally invalid and does not validate any payloads — the oneOf keyword was incorrectly nested inside properties, which is not valid JSON Schema. Use https://schema.beckn.io/BecknAction/v2.0 instead. BecknAction is the unified envelope for all Beckn actions (both request and callback directions). The request/callback distinction is encoded in context.action (e.g. beckn/discover for requests, beckn/on_discover for callbacks). This schema will be removed in a future major version.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/RequestAction` |
| JSON Schema (latest) | `https://schema.beckn.io/RequestAction/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/RequestAction/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/RequestAction/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
