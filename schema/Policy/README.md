# Policy

> **Canonical IRI:** [`https://schema.beckn.io/Policy`](https://schema.beckn.io/Policy)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for Policy in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | — |
| `@type` | `string` | ✅ | — |
| `descriptor` | any | ✅ | Validity window for this policy version |
| `id` | `string` | ✅ | Identifier for the policy |
| `policyType` | `string` | — | Type/kind of policy (extensible term) |
| `validity` | any | — | Validity window for this policy version |
| `policyAttributes` | object | — | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Policy` |
| JSON Schema (latest) | `https://schema.beckn.io/Policy/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Policy/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Policy/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
