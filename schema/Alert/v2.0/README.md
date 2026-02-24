# Alert — v2.0

Notification or alert associated with an entity.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Alert](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Alert` |

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
| `affectedEntities` | string[] | IDs of entities affected (route/order/fulfillment/etc.) |
| `descriptor` | [Descriptor](../../Descriptor/README.md) |  |
| `id` | string |  |
| `severity` | string |  |
| `validity` | [TimePeriod](../../TimePeriod/README.md) |  |
