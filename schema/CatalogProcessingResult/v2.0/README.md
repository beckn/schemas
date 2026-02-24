# CatalogProcessingResult — v2.0

Result of catalog submission to a publishing service.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [CatalogProcessingResult](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `CatalogProcessingResult` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `catalogId` | string | The "id" of the submitted catalog |
| `status` | string | Final processing outcome for this catalog |
| `itemCount` | integer | Number of items indexed (when accepted/partial) |
| `warnings` | [ProcessingNotice](../../ProcessingNotice/README.md)[] | Non-fatal issues encountered |
| `error` | [Error](../../Error/README.md) |  |
