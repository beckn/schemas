# Participant

> **Canonical IRI:** [`https://schema.beckn.io/Participant`](https://schema.beckn.io/Participant)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for Participant in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | — |
| `@type` | `string` | ✅ | — |
| `credentials` | any[] | — | — |
| `displayName` | `string` | — | — |
| `email` | `string` (email) | — | — |
| `id` | `string` | ✅ | — |
| `rating` | object | — | — |
| `role` | `string` | ✅ | Role of participant (consumer, recipient, rider, patient, operator, etc.) |
| `skills` | any[] | — | — |
| `telephone` | `string` | — | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Participant` |
| JSON Schema (latest) | `https://schema.beckn.io/Participant/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Participant/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Participant/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
