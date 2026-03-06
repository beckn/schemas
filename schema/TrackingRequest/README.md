# Tracking Request

> **Canonical IRI:** [`https://schema.beckn.io/TrackingRequest`](https://schema.beckn.io/TrackingRequest)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for TrackingRequest in the Beckn Protocol v2.0.1

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | `string` | ✅ | Tracking reference identifier |
| `callbackUrl` | `string` (uri) | — | Optional callback URL for streaming tracking coordinates/updates |
| `modeHint` | `string` | — | Optional delivery mode for the tracking handle. |
| `trackingDataSchema` | [schema](../schema/README.md) | — | A JSON Schema (2020-12) that describes the structure of trackingData payloads. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/TrackingRequest` |
| JSON Schema (latest) | `https://schema.beckn.io/TrackingRequest/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/TrackingRequest/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/TrackingRequest/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
