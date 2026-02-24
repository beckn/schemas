# MediaSearch — v2.0

A media-based search request.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [MediaSearch](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `MediaSearch` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `media` | [MediaInput](../../MediaInput/README.md)[] | One or more references to **images, audio notes, or videos** supplied as part of a multimodal search. Each entry references a media resource accessible via HTTPS or data URI. |
| `options` | [MediaSearchOptions](../../MediaSearchOptions/README.md) | Options controlling how the discovery engine interprets the supplied media — e.g., whether to perform OCR/ASR, semantic similarity, or object detection. |
