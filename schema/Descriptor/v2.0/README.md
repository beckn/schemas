# Descriptor — v2.0

Reusable descriptor for display text, images, and tags.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Descriptor](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Descriptor` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string | Use case specific JSON-LD context. This can change from use case to use case, even within a domain. |
| `@type` | string | Type of the descriptor. The type can be overriden with a context-specific type |
| `longDesc` | string | Detailed description of the item |
| `shortDesc` | string | Short description of the item |
| `name` | string | Name of the entity being described |
| `thumbnailImage` | string | Name of the entity being described |
| `docs` | [Document](../../Document/README.md)[] | Links to downloadable documents |
| `mediaFile` | [MediaFile](../../MediaFile/README.md)[] | Links to multimedia files and images |
