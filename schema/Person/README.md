# Person

> **Canonical IRI:** [`https://schema.beckn.io/Person`](https://schema.beckn.io/Person)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

A person (alive, deceased, or fictional). Modeled after schema.org/Person.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | — |
| `@type` | `string` | ✅ | — |
| `id` | `string` | ✅ | Unique identifier for the person |
| `name` | `string` | — | Full name of the person |
| `email` | `string` (email) | — | Email address |
| `telephone` | `string` | — | Telephone number |
| `address` | `string` | — | Physical address |
| `age` | `integer` | — | Age in years |
| `knowsLanguage` | string[] | — | Languages known by the person (BCP-47 codes or language names) |
| `worksFor` | any | — | Organization the person works for |
| `credentials` | any[] | — | Credentials held by the person |
| `skills` | any[] | — | Skills possessed by the person |
| `personAttributes` | any | — | Extensible attribute pack for jurisdictional or domain-specific person properties |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Person` |
| JSON Schema (latest) | `https://schema.beckn.io/Person/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Person/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Person/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
