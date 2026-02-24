# Item — v2.0

A product or service offered by a provider.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Item](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Item` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string | JSON-LD context URI for the core Item schema |
| `@type` | string | Type of the core item |
| `availabilityWindow` | [TimePeriod](../../TimePeriod/README.md)[] | Time periods when the item is available |
| `availableAt` | [Location](../../Location/README.md)[] | Physical locations where the item is available |
| `category` | [CategoryCode](../../CategoryCode/README.md) |  |
| `constraints` | [Constraint](../../Constraint/README.md)[] |  |
| `descriptor` | [Descriptor](../../Descriptor/README.md) |  |
| `id` | string | Unique identifier for the item |
| `isActive` | boolean | Whether the item is active |
| `itemAttributes` | [Attributes](../../Attributes/README.md) |  |
| `networkId` | string[] | Array of network identifiers for the BAP (Beckn App Provider) that offers this item |
| `policies` | [Policy](../../Policy/README.md)[] |  |
| `provider` | [Provider](../../Provider/README.md) |  |
| `rateable` | boolean | Whether the item can be rated by customers |
| `rating` | [Rating](../../Rating/README.md) |  |
