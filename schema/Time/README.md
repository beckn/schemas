# Time

> **Canonical IRI:** [`https://schema.beckn.io/Time`](https://schema.beckn.io/Time)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Represents a moment or duration in time. Can express a timestamp, a duration, or a time range.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | — | — |
| `@type` | `string` | — | — |
| `timestamp` | `string` (date-time) | — | A specific instant in time (ISO 8601) |
| `duration` | `string` | — | ISO 8601 duration (e.g., PT30M for 30 minutes) |
| `range` | any | — | A time range with start and end |
| `label` | `string` | — | Human-readable label for this time |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Time` |
| JSON Schema (latest) | `https://schema.beckn.io/Time/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Time/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Time/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
