# Time Period

> **Canonical IRI:** [`https://schema.beckn.io/TimePeriod`](https://schema.beckn.io/TimePeriod)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Time window with date-time precision for availability/validity

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@type` | `string` | ✅ | JSON-LD type for a date-time period |
| `startDate` | `string` (date-time) | — | Start instant (inclusive) |
| `endDate` | `string` (date-time) | — | End instant (exclusive or inclusive per domain semantics) |
| `startTime` | `string` (time) | — | Start time of the time period |
| `endTime` | `string` (time) | — | End time of the time period |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/TimePeriod` |
| JSON Schema (latest) | `https://schema.beckn.io/TimePeriod/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/TimePeriod/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/TimePeriod/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
