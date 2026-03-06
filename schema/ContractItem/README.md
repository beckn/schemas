# Contract Item

> **Canonical IRI:** [`https://schema.beckn.io/ContractItem`](https://schema.beckn.io/ContractItem)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

A line item within a Contract, linking an accepted Offer and ordered Item with quantity and price.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `acceptedOffer` | any | — | Offer applied to this line (if different from contract-level) |
| `itemId` | [id](../id/README.md) | ✅ | — |
| `lineId` | `string` | — | Unique line id within contract |
| `contractItemAttributes` | any | — | Line-level Attribute Pack (options, substitutions, ESG, etc.) |
| `price` | any | — | Line price composition (unit/tax/delivery/discount) |
| `quantity` | any | — | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/ContractItem` |
| JSON Schema (latest) | `https://schema.beckn.io/ContractItem/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/ContractItem/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/ContractItem/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
