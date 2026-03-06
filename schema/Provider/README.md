# Provider

> **Canonical IRI:** [`https://schema.beckn.io/Provider`](https://schema.beckn.io/Provider)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for Provider in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | — | CPD |
| `@type` | `string` | — | TPD |
| `alerts` | any[] | — | — |
| `descriptor` | object | ✅ | — |
| `id` | `string` | ✅ | Unique identifier for the provider |
| `locations` | any[] | — | Physical locations where the provider operates |
| `policies` | any[] | — | — |
| `providerAttributes` | object | — | — |
| `rateable` | `boolean` | — | Whether the provider can be rated by customers |
| `rating` | object | — | — |
| `validity` | object | — | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Provider` |
| JSON Schema (latest) | `https://schema.beckn.io/Provider/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Provider/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Provider/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
