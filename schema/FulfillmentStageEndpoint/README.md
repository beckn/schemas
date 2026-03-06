# Fulfillment Stage Endpoint

> **Canonical IRI:** [`https://schema.beckn.io/FulfillmentStageEndpoint`](https://schema.beckn.io/FulfillmentStageEndpoint)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

A stage boundary endpoint (entry or exit) within a fulfillment, such as pickup, handover, warehouse in/out, border crossing, gate entry/exit, security check, etc. May require one or more proofs/permits/tokens/documents.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | — | CPD |
| `@type` | `string` | — | — |
| `location` | object | — | — |
| `time` | object | — | — |
| `authorization` | any[] | — | One or more credentials required and/or issued at this endpoint. Includes machine-readable tokens (QR/URL/OTP) and manual documents (IDs, permits). |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/FulfillmentStageEndpoint` |
| JSON Schema (latest) | `https://schema.beckn.io/FulfillmentStageEndpoint/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/FulfillmentStageEndpoint/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/FulfillmentStageEndpoint/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
