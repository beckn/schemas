# Media Search

> **Canonical IRI:** [`https://schema.beckn.io/MediaSearch`](https://schema.beckn.io/MediaSearch)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Container for multimodal search inputs and configuration. Supports searching through **images, audio notes, and videos** alongside text, filters, and spatial predicates. For GET, this object should be JSON-encoded and URL-escaped.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `media` | any[] | — | One or more references to **images, audio notes, or videos** supplied as part of a multimodal search. Each entry references a media resource access… |
| `options` | object | — | Options controlling how the discovery engine interprets the supplied media — e.g., whether to perform OCR/ASR, semantic similarity, or object detec… |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/MediaSearch` |
| JSON Schema (latest) | `https://schema.beckn.io/MediaSearch/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/MediaSearch/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/MediaSearch/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
