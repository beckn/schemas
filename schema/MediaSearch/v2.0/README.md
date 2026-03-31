# MediaSearch — v2.0

Container for multimodal search inputs and configuration. Supports searching through **images, audio notes, and videos** alongside text, filters, and spatial predicates. For GET, this object should be JSON-encoded and URL-escaped.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/MediaSearch/attributes.yaml](https://schema.beckn.io/MediaSearch/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/MediaSearch/v2.0/attributes.yaml](https://schema.beckn.io/MediaSearch/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/MediaSearch/attributes.jsonschema.yaml](https://schema.beckn.io/MediaSearch/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/MediaSearch/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/MediaSearch/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/MediaSearch/context.jsonld](https://schema.beckn.io/MediaSearch/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/MediaSearch/v2.0/context.jsonld](https://schema.beckn.io/MediaSearch/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/MediaSearch/vocab.jsonld](https://schema.beckn.io/MediaSearch/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/MediaSearch/v2.0/vocab.jsonld](https://schema.beckn.io/MediaSearch/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `media` | no | array | One or more references to **images, audio notes, or videos** supplied as part of a multimodal search. Each entry references a media resource accessible via HTTPS or data URI. |
| `options` | no | $ref: https://schema.beckn.io/MediaSearchOptions/attributes.yaml#/components/schemas/MediaSearchOptions | Options controlling how the discovery engine interprets the supplied media — e.g., whether to perform OCR/ASR, semantic similarity, or object detection. |
