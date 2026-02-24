# DisplayedRating — v2.0

Aggregated rating display object.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [DisplayedRating](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `DisplayedRating` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@type` | string | Type of the rating |
| `ratingCount` | integer | Number of ratings |
| `ratingValue` | number | Rating value (0-5) |
