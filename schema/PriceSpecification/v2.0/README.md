# PriceSpecification — v2.0

A price breakdown specification.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [PriceSpecification](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `PriceSpecification` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `currency` | string | ISO 4217 code |
| `value` | number | Total value for this price specification |
| `applicableQuantity` | [Quantity](../../Quantity/README.md) |  |
| `components` | object[] | Optional components (tax, shipping, discount, fee, surcharge) |
| `x-jsonld` |  |  |
