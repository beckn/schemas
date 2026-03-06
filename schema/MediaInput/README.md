# Media Input

> **Canonical IRI:** [`https://schema.beckn.io/MediaInput`](https://schema.beckn.io/MediaInput)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Reference to an image, audio clip, or video used for multimodal search.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | `string` | — | Client-supplied identifier for this media input. |
| `type` | `string` | ✅ | Media category. |
| `url` | `string` (uri) | ✅ | HTTPS URL or data URI pointing to the media resource. |
| `contentType` | `string` | — | MIME type, e.g., image/jpeg, audio/mpeg, video/mp4. |
| `textHint` | `string` | — | Optional pre-extracted text (OCR/ASR) for search augmentation. |
| `language` | `string` | — | Language code (BCP-47) of `textHint` or spoken audio. |
| `startMs` | `integer` | — | Optional start offset in milliseconds (for audio/video segments). |
| `endMs` | `integer` | — | Optional end offset in milliseconds (for audio/video segments). |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/MediaInput` |
| JSON Schema (latest) | `https://schema.beckn.io/MediaInput/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/MediaInput/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/MediaInput/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
