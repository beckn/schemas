# Retail Core Offer

> **Canonical IRI:** [`https://schema.beckn.io/RetailCoreOffer`](https://schema.beckn.io/RetailCoreOffer)
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

The `RetailCoreOffer` schema object.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `policies` | object | — | — |
| `paymentConstraints` | object | — | — |
| `serviceability` | object | — | Additional serviceability constraints beyond geographic eligibility (handled via core Offer.eligibleRegion). |
| `timeRange` | object | — | Daily time window applicable on the specified days. |
| `holidays` | string[] | — | Specific dates excluded from this schedule. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/RetailCoreOffer` |
| JSON Schema (latest) | `https://schema.beckn.io/RetailCoreOffer/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/RetailCoreOffer/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/RetailCoreOffer/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
