# Location

> **Canonical IRI:** [`https://schema.beckn.io/Location`](https://schema.beckn.io/Location)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

A **place** represented by **GeoJSON geometry** (Point/Polygon/Multi*) and optional human-readable `address`. This unifies all Beckn location fields into a single, widely-adopted representation (GeoJSON).

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@type` | `string` | — | — |
| `address` | `string` | — | Optional human-readable address for the same place/area. |
| `geo` | object | ✅ | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Location` |
| JSON Schema (latest) | `https://schema.beckn.io/Location/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Location/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Location/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
