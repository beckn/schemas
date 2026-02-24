# TrackingRequest — v2.0

A tracking request.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [TrackingRequest](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `TrackingRequest` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Tracking reference identifier |
| `callbackUrl` | string | Optional callback URL for streaming tracking coordinates/updates |
| `modeHint` | string | Optional delivery mode for the tracking handle. |
| `trackingDataSchema` | schema | A JSON Schema (2020-12) that describes the structure of trackingData payloads. |
