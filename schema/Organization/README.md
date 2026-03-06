# Organization

> **Canonical IRI:** [`https://schema.beckn.io/Organization`](https://schema.beckn.io/Organization)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

An organization such as a company, non-profit, or governmental institution. Modeled after schema.org/Organization.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | — |
| `@type` | `string` | ✅ | — |
| `id` | `string` | ✅ | Unique identifier for the organization |
| `name` | `string` | — | Name of the organization |
| `email` | `string` (email) | — | Email address |
| `telephone` | `string` | — | Telephone number |
| `address` | `string` | — | Physical address |
| `credentials` | any[] | — | Credentials held by the organization |
| `skills` | any[] | — | Skills or capabilities of the organization |
| `organizationAttributes` | any | — | Extensible attribute pack for jurisdictional or domain-specific organization properties |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Organization` |
| JSON Schema (latest) | `https://schema.beckn.io/Organization/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Organization/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Organization/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
