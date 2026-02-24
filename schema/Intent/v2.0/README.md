# Intent — v2.0

The search intent expressed by a consumer.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Intent](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Intent` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `textSearch` | string | Free text search query for items |
| `filters` | object | Filter criteria for items |
| `spatial` | [SpatialConstraint](../../SpatialConstraint/README.md)[] | Optional array of spatial constraints (CQL2-JSON semantics). |
| `media_search` | [MediaSearch](../../MediaSearch/README.md) |  |
