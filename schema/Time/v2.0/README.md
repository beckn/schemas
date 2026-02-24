# Time — v2.0

A time value.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Time](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Time` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string |  |
| `@type` | string |  |
| `timestamp` | string | A specific instant in time (ISO 8601) |
| `duration` | string | ISO 8601 duration (e.g., PT30M for 30 minutes) |
| `range` | [TimePeriod](../../TimePeriod/README.md) | A time range with start and end |
| `label` | string | Human-readable label for this time |
