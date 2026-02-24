# MediaFile — v2.0

A media file attachment.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [MediaFile](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `MediaFile` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `label` | string | The display name of the media file |
| `mimeType` | | MIME type if 'data' is provided (application/pdf, image/png). |
| `uri` | string | URL to the document |
