# SupportResponse

> **Canonical IRI:** [`https://schema.beckn.io/SupportResponse`](https://schema.beckn.io/SupportResponse)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Schema definition for SupportResponse in the Beckn Protocol v2.0.1

Support response payload returned by a BPP to a BAP in the `/beckn/on_support`
callback. Contains the support ticket reference, available contact channels,
SLA commitment, and optional consumer acknowledgement details.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI. |
| `@type` | `string` | ✅ | Must be `beckn:SupportResponse`. |
| `refId` | `string` | — | Reference identifier (typically the order ID) against which support was requested. |
| `ticketId` | `string` | — | Support ticket identifier assigned by the BPP. |
| `descriptor` | `Descriptor` | — | Human-readable label for this support response. |
| `channels` | `array` | — | Available support channels with contact details. |
| `sla` | `object` | — | Service level agreement for this support response. |
| `consumer` | `Consumer` | — | The consumer the support response is addressed to. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/SupportResponse` |
| JSON Schema (latest) | `https://schema.beckn.io/SupportResponse/v2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/SupportResponse/v2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/SupportResponse/v2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
