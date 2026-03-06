# Food And Beverage Item

> **Canonical IRI:** [`https://schema.beckn.io/FoodAndBeverageItem`](https://schema.beckn.io/FoodAndBeverageItem)
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Food & Beverage-specific extensions to RetailCoreItemAttributes. Covers allergens, cuisine classification, and preparation guidance.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `allergens` | string[] | — | List of known allergens present in the item. |
| `cuisine` | `string` | — | Cuisine classification (e.g., Italian, Indian, Mexican). |
| `preparation` | object | — | Preparation and storage guidance. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/FoodAndBeverageItem` |
| JSON Schema (latest) | `https://schema.beckn.io/FoodAndBeverageItem/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/FoodAndBeverageItem/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/FoodAndBeverageItem/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
