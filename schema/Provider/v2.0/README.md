# Provider — v2.0

A provider of items and services.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Provider](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Provider` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string | CPD |
| `@type` | string | TPD |
| `alerts` | [Alert](../../Alert/README.md)[] |  |
| `descriptor` | [Descriptor](../../Descriptor/README.md) |  |
| `id` | string | Unique identifier for the provider |
| `locations` | [Location](../../Location/README.md)[] | Physical locations where the provider operates |
| `policies` | [Policy](../../Policy/README.md)[] |  |
| `providerAttributes` | [Attributes](../../Attributes/README.md) |  |
| `rateable` | boolean | Whether the provider can be rated by customers |
| `rating` | [Rating](../../Rating/README.md) |  |
| `validity` | [TimePeriod](../../TimePeriod/README.md) |  |
