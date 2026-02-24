# Quantity — v2.0

A quantity specification.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Quantity](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Quantity` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `maxQuantity` | number | Maximum quantity for this price |
| `minQuantity` | number | Minimum quantity for this price |
| `unitCode` | string | Unit code for the quoted price (e.g., KWH, MIN, H, MON) |
| `unitQuantity` | number | Quantity of the unit |
| `unitText` | string | Unit for the quoted price (e.g., kWh, minute, hour, month) |
