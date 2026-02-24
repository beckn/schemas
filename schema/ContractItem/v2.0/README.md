# ContractItem — v2.0

A line item within a Contract.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [ContractItem](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `ContractItem` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `acceptedOffer` | [Offer](../../Offer/README.md) | Offer applied to this line (if different from contract-level) |
| `itemId` | id |  |
| `lineId` | string | Unique line id within contract |
| `contractItemAttributes` | [Attributes](../../Attributes/README.md) | Line-level Attribute Pack (options, substitutions, ESG, etc.) |
| `price` | [PriceSpecification](../../PriceSpecification/README.md) | Line price composition (unit/tax/delivery/discount) |
| `quantity` | [Quantity](../../Quantity/README.md) |  |
