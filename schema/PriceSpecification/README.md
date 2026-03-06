# Price Specification

> **Canonical IRI:** [`https://schema.beckn.io/PriceSpecification`](https://schema.beckn.io/PriceSpecification)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for PriceSpecification in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `currency` | `string` | — | ISO 4217 code |
| `value` | `number` | — | Total value for this price specification |
| `applicableQuantity` | object | — | — |
| `components` | object[] | — | Optional components (tax, shipping, discount, fee, surcharge) |
| `x-jsonld` | any | — | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/PriceSpecification` |
| JSON Schema (latest) | `https://schema.beckn.io/PriceSpecification/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/PriceSpecification/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/PriceSpecification/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
