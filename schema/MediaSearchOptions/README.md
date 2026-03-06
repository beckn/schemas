# Media Search Options

> **Canonical IRI:** [`https://schema.beckn.io/MediaSearchOptions`](https://schema.beckn.io/MediaSearchOptions)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

How the discovery engine should use the provided media inputs.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `goals` | string[] | — | Desired processing goals for the media. |
| `augmentTextSearch` | `boolean` | — | Whether to append extracted text from OCR/ASR to `textSearch`. |
| `restrictResultsToMediaProximity` | `boolean` | — | Restrict results to spatial proximity of media-derived coordinates (e.g., EXIF GPS tags). |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/MediaSearchOptions` |
| JSON Schema (latest) | `https://schema.beckn.io/MediaSearchOptions/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/MediaSearchOptions/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/MediaSearchOptions/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
