# RetailCoreItemAttributes — v2.0

> **Canonical IRI:** [`https://schema.beckn.io/RetailCoreItemAttributes/v2.0`](https://schema.beckn.io/RetailCoreItemAttributes/v2.0)

Schema definition for RetailCoreItemAttributes v2.0.

## Properties

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
| JSON Schema | `https://schema.beckn.io/RetailCoreItemAttributes/v2.0` |
| context.jsonld | `https://schema.beckn.io/RetailCoreItemAttributes/v2.0/context.jsonld` |
| vocab.jsonld | `https://schema.beckn.io/RetailCoreItemAttributes/v2.0/vocab.jsonld` |
