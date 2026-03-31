# MediaInput — v2.0

Reference to an image, audio clip, or video used for multimodal search.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/MediaInput/attributes.yaml](https://schema.beckn.io/MediaInput/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/MediaInput/v2.0/attributes.yaml](https://schema.beckn.io/MediaInput/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/MediaInput/attributes.jsonschema.yaml](https://schema.beckn.io/MediaInput/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/MediaInput/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/MediaInput/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/MediaInput/context.jsonld](https://schema.beckn.io/MediaInput/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/MediaInput/v2.0/context.jsonld](https://schema.beckn.io/MediaInput/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/MediaInput/vocab.jsonld](https://schema.beckn.io/MediaInput/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/MediaInput/v2.0/vocab.jsonld](https://schema.beckn.io/MediaInput/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | no | string | Client-supplied identifier for this media input. |
| `type` | yes | string | Media category. |
| `url` | yes | string | HTTPS URL or data URI pointing to the media resource. |
| `contentType` | no | string | MIME type, e.g., image/jpeg, audio/mpeg, video/mp4. |
| `textHint` | no | string | Optional pre-extracted text (OCR/ASR) for search augmentation. |
| `language` | no | string | Language code (BCP-47) of `textHint` or spoken audio. |
| `startMs` | no | integer | Optional start offset in milliseconds (for audio/video segments). |
| `endMs` | no | integer | Optional end offset in milliseconds (for audio/video segments). |
