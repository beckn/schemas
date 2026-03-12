# RetailCoreItemAttributes

> **Canonical IRI:** [`https://schema.beckn.io/RetailCoreItemAttributes`](https://schema.beckn.io/RetailCoreItemAttributes)
> **Tags:** `retail`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for RetailCoreItemAttributes in the Beckn Protocol v2.0.1

Retail-specific item attribute pack, used as the value of `Item.itemAttributes`
for retail domain items. Covers physical properties, food classification,
regulatory declarations, and verifiable credentials.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI for the retail item schema. |
| `@type` | `string` | ✅ | Must be `beckn:RetailCoreItemAttributes`. |
| `identity` | `object` | — | Brand and origin information. |
| `physical` | `object` | — | Weight, volume, dimensions, and appearance. |
| `food` | `object` | — | Food classification (VEG/NON_VEG/EGG). |
| `packagedGoodsDeclaration` | `object` | — | Jurisdiction-neutral packaged goods declaration. |
| `foodRegulatoryDeclaration` | `object` | — | Jurisdiction-neutral food regulatory declarations. |
| `credentials` | `array` | — | External verifiable credentials or attestations. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/RetailCoreItemAttributes` |
| JSON Schema (latest) | `https://schema.beckn.io/RetailCoreItemAttributes/v2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/RetailCoreItemAttributes/v2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/RetailCoreItemAttributes/v2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
