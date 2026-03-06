# Rating Input

> **Canonical IRI:** [`https://schema.beckn.io/RatingInput`](https://schema.beckn.io/RatingInput)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

A form designed to capture rating and feedback from a user. This can be used by both BAP and BPP to fetch ratings and feedback of their respective users.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | — |
| `@type` | `string` | ✅ | — |
| `target` | object | ✅ | The entity being rated |
| `range` | `object` \| `array` | ✅ | — |
| `feedbackFormSubmission` | any | — | The submission to the feedback form sent along with a rating request |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/RatingInput` |
| JSON Schema (latest) | `https://schema.beckn.io/RatingInput/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/RatingInput/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/RatingInput/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
