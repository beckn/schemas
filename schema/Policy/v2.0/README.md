# Policy — v2.0

A policy applied to a transaction or item.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Policy](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Policy` |

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
| `descriptor` | [Descriptor](../../Descriptor/README.md) | Validity window for this policy version |
| `id` | string | Identifier for the policy |
| `policyType` | string | Type/kind of policy (extensible term) |
| `validity` | [TimePeriod](../../TimePeriod/README.md) | Validity window for this policy version |
| `policyAttributes` | [Attributes](../../Attributes/README.md) |  |
