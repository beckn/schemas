# Entitlement

> **Canonical IRI:** [`https://schema.beckn.io/Entitlement`](https://schema.beckn.io/Entitlement)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

A contractually granted, policy-governed right that allows a specific party to access, use, or claim a defined economic resource within stated scope and validity constraints. It represents the enforceable permission created by an order, independent of the credential used to exercise it.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | CPD |
| `@type` | `string` | ✅ | The domain-specific type of entitlement that allows domains to extend this schema |
| `id` | `string` | ✅ | A unique identifier for this entitlement within the entitlement provider's namespace |
| `resource` | [lineId](../lineId/README.md) | — | The resource being availed or accessed against this entitlement |
| `descriptor` | any | ✅ | Human-readable information regarding the entitlement like QR-code images, attached documents containing terms and conditions, video or audio files … |
| `credentials` | any[] | — | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Entitlement` |
| JSON Schema (latest) | `https://schema.beckn.io/Entitlement/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Entitlement/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Entitlement/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
