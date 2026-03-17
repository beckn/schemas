# Offer — v2.0

A promotional offer.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Offer](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Offer` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string | JSON-LD context URI for the core offer schema |
| `@type` | string | TPD |
| `acceptedPaymentMethod` | [AcceptedPaymentMethod](../../AcceptedPaymentMethod/README.md) |  |
| `addOnItems` | id[] | Optional extras modeled as items (e.g., toppings, accessories) |
| `addOns` | id[] | Optional extra Offers that can be attached (e.g., warranty, gift wrap) |
| `constraints` | [Constraint](../../Constraint/README.md)[] |  |
| `descriptor` | [Descriptor](../../Descriptor/README.md) |  |
| `eligibleRegion` | [Location](../../Location/README.md)[] | Regions where the offer is eligible |
| `id` | string | Unique id for this offer |
| `isActive` | boolean | Whether the offer is active |
| `items` | id[] | Base item(s) the offer applies to (single or bundle) |
| `offerAttributes` | [Attributes](../../Attributes/README.md) | Attribute Pack attachment (pricing models, discounts, rail terms, etc.) |
| `policies` | [Policy](../../Policy/README.md)[] |  |
| `price` | [PriceSpecification](../../PriceSpecification/README.md) | Price snapshot; detailed models can live in offerAttributes |
| `provider` | id | Seller / provider of this offer |
| `validity` | [TimePeriod](../../TimePeriod/README.md) | Offer validity window |
