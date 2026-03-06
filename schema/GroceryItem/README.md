# Grocery Item

> **Canonical IRI:** [`https://schema.beckn.io/GroceryItem`](https://schema.beckn.io/GroceryItem)
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Grocery-specific extensions to RetailCoreItemAttributes. Covers nutrition information and fresh produce declarations.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `nutrition` | object[] | — | Nutrition facts per serving or per 100g/100ml. Context of measurement may be specified via unit. |
| `freshProduce` | object | — | Additional declaration applicable for unpackaged or loose produce. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/GroceryItem` |
| JSON Schema (latest) | `https://schema.beckn.io/GroceryItem/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/GroceryItem/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/GroceryItem/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
