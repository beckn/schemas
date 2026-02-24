# Document — v2.0

A document or attachment associated with a transaction.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Document](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Document` |

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
| `mimeType` | string | MIME type if 'data' is provided (application/pdf, image/png, application/json). |
| `standard` | string | Describes the schema type in case the document follows a standard schema like a verifiableCredential |
| `url` | string | URL to the document |
| `security` | object |  |
