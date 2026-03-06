# Recurring Schedule

> **Canonical IRI:** [`https://schema.beckn.io/RecurringSchedule`](https://schema.beckn.io/RecurringSchedule)
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Defines a recurring temporal schedule such as operating hours or serviceability timing windows. Supports day-based recurrence and optional holiday exclusions.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `days` | string[] | — | Days of week on which the schedule applies. |
| `timeRange` | object | — | Daily time window for applicable days. |
| `holidays` | string[] | — | Specific dates excluded from this schedule. |
| `timezone` | `string` | — | IANA timezone identifier (e.g., Asia/Kolkata). |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/RecurringSchedule` |
| JSON Schema (latest) | `https://schema.beckn.io/RecurringSchedule/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/RecurringSchedule/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/RecurringSchedule/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
