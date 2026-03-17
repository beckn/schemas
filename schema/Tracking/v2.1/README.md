# Tracking — v2.0

A tracking record.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Tracking](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Tracking` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string | TBD |
| `@type` | string | TBD |
| `expiresAt` | string | ISO 8601 expiry timestamp for the tracking handle. |
| `trackingStatus` | string |  |
| `url` | string | Link/handle to off-network tracking UI or endpoint. |
