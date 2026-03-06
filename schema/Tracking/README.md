# Tracking

> **Canonical IRI:** [`https://schema.beckn.io/Tracking`](https://schema.beckn.io/Tracking)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Non-streaming tracking handle per legacy semantics (url/transport/status).

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | TBD |
| `@type` | `string` | ✅ | TBD |
| `expiresAt` | `string` (date-time) | — | ISO 8601 expiry timestamp for the tracking handle. |
| `trackingStatus` | `string` | ✅ | — |
| `url` | `string` (uri) | ✅ | Link/handle to off-network tracking UI or endpoint. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Tracking` |
| JSON Schema (latest) | `https://schema.beckn.io/Tracking/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Tracking/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Tracking/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
