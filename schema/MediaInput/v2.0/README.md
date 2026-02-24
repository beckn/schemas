# MediaInput — v2.0

Media input for visual or audio search.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [MediaInput](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `MediaInput` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Client-supplied identifier for this media input. |
| `type` | string | Media category. |
| `url` | string | HTTPS URL or data URI pointing to the media resource. |
| `contentType` | string | MIME type, e.g., image/jpeg, audio/mpeg, video/mp4. |
| `textHint` | string | Optional pre-extracted text (OCR/ASR) for search augmentation. |
| `language` | string | Language code (BCP-47) of `textHint` or spoken audio. |
| `startMs` | integer | Optional start offset in milliseconds (for audio/video segments). |
| `endMs` | integer | Optional end offset in milliseconds (for audio/video segments). |
