# Catalog — v2.0

Collection of items and offers provided by a provider.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Catalog](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Catalog` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string | JSON-LD context URI for the core Catalog schema |
| `@type` | string | Type of the catalog |
| `bppId` | string | BPP (Beckn Protocol Provider) identifier that publishes this catalog |
| `bppUri` | string | BPP (Beckn Protocol Provider) URI endpoint |
| `descriptor` | object | A verbal summary of the catalog for humans, AI agents, etc to read and understand the context. |
| `id` | string | Unique identifier for the catalog |
| `isActive` | boolean | Whether the catalog is active |
| `items` | object[] | Array of beckn core Item entities in this catalog |
| `offers` | object[] |  |
| `providerId` | string | Reference to the provider that owns this catalog |
| `validity` | object |  |
