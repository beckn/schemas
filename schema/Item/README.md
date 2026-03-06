# Item

> **Canonical IRI:** [`https://schema.beckn.io/Item`](https://schema.beckn.io/Item)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for Item in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI for the core Item schema |
| `@type` | `string` | ✅ | Type of the core item |
| `availabilityWindow` | any[] | — | Time periods when the item is available |
| `availableAt` | any[] | — | Physical locations where the item is available |
| `category` | object | — | — |
| `constraints` | any[] | — | — |
| `descriptor` | object | ✅ | — |
| `id` | `string` | ✅ | Unique identifier for the item |
| `isActive` | `boolean` | — | Whether the item is active |
| `itemAttributes` | object | ✅ | — |
| `networkId` | string[] | — | Array of network identifiers for the BAP (Beckn App Provider) that offers this item |
| `policies` | any[] | — | — |
| `provider` | object | ✅ | — |
| `rateable` | `boolean` | — | Whether the item can be rated by customers |
| `rating` | object | — | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Item` |
| JSON Schema (latest) | `https://schema.beckn.io/Item/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Item/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Item/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
