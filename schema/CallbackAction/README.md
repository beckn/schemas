# Callback Action

> **Canonical IRI:** [`https://schema.beckn.io/CallbackAction`](https://schema.beckn.io/CallbackAction)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

DEPRECATED. This schema is structurally invalid and does not validate any payloads — the oneOf keyword was incorrectly nested inside properties, which is not valid JSON Schema. The $id also lacked a version segment. Use https://schema.beckn.io/BecknAction/v2.0 instead. BecknAction is the unified envelope for all Beckn actions (both request and callback directions). Callback actions are those with on_ prefixed endpoints (e.g. beckn/on_discover, beckn/on_confirm) and are validated by the same BecknAction schema via if/then dispatch on context.action. This schema will be removed in a future major version.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/CallbackAction` |
| JSON Schema (latest) | `https://schema.beckn.io/CallbackAction/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/CallbackAction/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/CallbackAction/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
