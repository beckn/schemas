# MediaSearchOptions — v2.0

How the discovery engine should use the provided media inputs.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/MediaSearchOptions/attributes.yaml](https://schema.beckn.io/MediaSearchOptions/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/MediaSearchOptions/v2.0/attributes.yaml](https://schema.beckn.io/MediaSearchOptions/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/MediaSearchOptions/attributes.jsonschema.yaml](https://schema.beckn.io/MediaSearchOptions/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/MediaSearchOptions/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/MediaSearchOptions/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/MediaSearchOptions/context.jsonld](https://schema.beckn.io/MediaSearchOptions/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/MediaSearchOptions/v2.0/context.jsonld](https://schema.beckn.io/MediaSearchOptions/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/MediaSearchOptions/vocab.jsonld](https://schema.beckn.io/MediaSearchOptions/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/MediaSearchOptions/v2.0/vocab.jsonld](https://schema.beckn.io/MediaSearchOptions/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `goals` | no | array | Desired processing goals for the media. |
| `augmentTextSearch` | no | boolean | Whether to append extracted text from OCR/ASR to `textSearch`. |
| `restrictResultsToMediaProximity` | no | boolean | Restrict results to spatial proximity of media-derived coordinates (e.g., EXIF GPS tags). |
