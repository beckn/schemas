# Quantity

> **Canonical IRI:** [`https://schema.beckn.io/Quantity`](https://schema.beckn.io/Quantity)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for Quantity in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `maxQuantity` | `number` | — | Maximum quantity for this price |
| `minQuantity` | `number` | — | Minimum quantity for this price |
| `unitCode` | `string` | — | Unit code for the quoted price (e.g., KWH, MIN, H, MON) |
| `unitQuantity` | `number` | — | Quantity of the unit |
| `unitText` | `string` | — | Unit for the quoted price (e.g., kWh, minute, hour, month) |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Quantity` |
| JSON Schema (latest) | `https://schema.beckn.io/Quantity/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Quantity/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Quantity/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
