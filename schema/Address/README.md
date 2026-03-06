# Address

> **Canonical IRI:** [`https://schema.beckn.io/Address`](https://schema.beckn.io/Address)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

**Postal address** aligned with schema.org `PostalAddress`. Use for human-readable addresses. Geometry lives in `Location.geo` as GeoJSON.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `addressCountry` | `string` | — | Country name or ISO-3166-1 alpha-2 code. |
| `addressLocality` | `string` | — | City/locality. |
| `addressRegion` | `string` | — | State/region/province. |
| `extendedAddress` | `string` | — | Address extension (apt/suite/floor, C/O). |
| `postalCode` | `string` | — | Postal/ZIP code. |
| `streetAddress` | `string` | — | Street address (building name/number and street). |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Address` |
| JSON Schema (latest) | `https://schema.beckn.io/Address/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Address/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Address/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
