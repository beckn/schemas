# MediaSearchOptions — v2.0

Options for a media search.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [MediaSearchOptions](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `MediaSearchOptions` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `goals` | string[] | Desired processing goals for the media. |
| `augmentTextSearch` | boolean | Whether to append extracted text from OCR/ASR to `textSearch`. |
| `restrictResultsToMediaProximity` | boolean | Restrict results to spatial proximity of media-derived coordinates (e.g., EXIF GPS tags). |
