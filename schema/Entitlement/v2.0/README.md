# Entitlement — v2.0

An entitlement granted by a provider.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Entitlement](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Entitlement` |

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
| `@type` | string | The domain-specific type of entitlement that allows domains to extend this schema |
| `id` | string | A unique identifier for this entitlement within the entitlement provider's namespace |
| `resource` | lineId | The resource being availed or accessed against this entitlement |
| `descriptor` | [Descriptor](../../Descriptor/README.md) | Human-readable information regarding the entitlement like QR-code images, attached documents containing terms and conditions, video or audio files instructing the user on how to use the entitlement |
| `credentials` | [Descriptor](../../Descriptor/README.md)[] |  |
