# Constraint — v2.0

A constraint expression applied to an entity.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Constraint](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Constraint` |

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
| `@type` | string |  |
| `constraintType` | string | Type of constraint (extensible term) |
| `id` | string | Identifier for the constraint |
| `operator` | string | Comparator/operator (<=, >=, =, etc.) |
| `unitCode` | string | Unit code (e.g., km, min) |
| `validity` | [TimePeriod](../../TimePeriod/README.md) |  |
| `value` | number | Constraint value |
