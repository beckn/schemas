# Fulfillment Stage Authorization

> **Canonical IRI:** [`https://schema.beckn.io/FulfillmentStageAuthorization`](https://schema.beckn.io/FulfillmentStageAuthorization)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

A credential/document/proof relevant to authorization at a fulfillment stage endpoint. This may be a token to be verified (QR/OTP/URL) or a document to be inspected manually.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | — | CPD |
| `@type` | `string` | — | — |
| `mediaFiles` | any[] | — | Media files required to enter or exit this fulfillment stage. The could be images of delivered packages, recorded video proof of installation, etc |
| `docs` | any[] | — | Documents required to enter or exit this fulfillment stage. The could be entry tickets, boarding passes, waybill, permits, certificates, credential… |
| `authToken` | `string` | — | A human readable string that needs to be provided to enter or exit this fulfillment stage. Like an OTP |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/FulfillmentStageAuthorization` |
| JSON Schema (latest) | `https://schema.beckn.io/FulfillmentStageAuthorization/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/FulfillmentStageAuthorization/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/FulfillmentStageAuthorization/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
