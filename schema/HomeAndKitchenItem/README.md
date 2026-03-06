# Home And Kitchen Item

> **Canonical IRI:** [`https://schema.beckn.io/HomeAndKitchenItem`](https://schema.beckn.io/HomeAndKitchenItem)
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Home & Kitchen-specific extensions to RetailCoreItemAttributes. Covers care, installation and usage environment guidance.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `careInstructions` | `string` | — | Cleaning and maintenance guidance. |
| `installation` | object | — | Installation requirements and support information. |
| `usage` | object | — | Usage environment or compatibility constraints. |
| `warranty` | object | — | Warranty information at item level (if generic). |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/HomeAndKitchenItem` |
| JSON Schema (latest) | `https://schema.beckn.io/HomeAndKitchenItem/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/HomeAndKitchenItem/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/HomeAndKitchenItem/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
