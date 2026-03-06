# Support Info

> **Canonical IRI:** [`https://schema.beckn.io/SupportInfo`](https://schema.beckn.io/SupportInfo)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Canonical support contact for an entity, mapped to schema.org ContactPoint.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | — |
| `@type` | `string` | ✅ | — |
| `channels` | string[] | — | Available support channels. |
| `email` | `string` (email) | — | Support email address. |
| `hoursAvailable` | `string` | — | Human-readable support hours (local time) |
| `name` | `string` | — | Name of the support organization or contact. |
| `telephone` | `string` | — | Telephone number. |
| `chat` | `string` (uri) | — | Embeddable chat endpoint for support. |
| `url` | `string` (uri) | — | Generic URL to a support page. |
| `callbackStatus` | `string` | — | Status of a support callback request. Indicates whether a callback has been requested, scheduled, or completed. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/SupportInfo` |
| JSON Schema (latest) | `https://schema.beckn.io/SupportInfo/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/SupportInfo/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/SupportInfo/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
