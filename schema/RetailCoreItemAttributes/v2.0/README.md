# RetailCoreItemAttributes — v2.0

Retail-specific item attribute pack, used as the value of Item.itemAttributes for retail domain items. Covers physical properties, food classification, regulatory declarations, and verifiable credentials.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/RetailCoreItemAttributes/attributes.yaml](https://schema.beckn.io/RetailCoreItemAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/RetailCoreItemAttributes/v2.0/attributes.yaml](https://schema.beckn.io/RetailCoreItemAttributes/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/RetailCoreItemAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/RetailCoreItemAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/RetailCoreItemAttributes/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/RetailCoreItemAttributes/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/RetailCoreItemAttributes/context.jsonld](https://schema.beckn.io/RetailCoreItemAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/RetailCoreItemAttributes/v2.0/context.jsonld](https://schema.beckn.io/RetailCoreItemAttributes/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/RetailCoreItemAttributes/vocab.jsonld](https://schema.beckn.io/RetailCoreItemAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/RetailCoreItemAttributes/v2.0/vocab.jsonld](https://schema.beckn.io/RetailCoreItemAttributes/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | JSON-LD context URI for the retail item schema. |
| `@type` | yes | string | JSON-LD type for this attribute pack. |
| `identity` | no | object | - |
| `physical` | no | object | - |
| `food` | no | object | - |
| `packagedGoodsDeclaration` | no | object | Jurisdiction-neutral packaged goods declaration. |
| `foodRegulatoryDeclaration` | no | object | Jurisdiction-neutral food regulatory declarations. |
| `credentials` | no | array | External verifiable credentials or attestations. |
