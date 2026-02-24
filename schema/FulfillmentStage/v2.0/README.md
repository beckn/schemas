# FulfillmentStage — v2.0

A stage within a multi-stage fulfillment.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [FulfillmentStage](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `FulfillmentStage` |

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
| `id` | string | A unique identifier for this stage of fulfillment |
| `instructions` | [Instruction](../../Instruction/README.md)[] | A set of instructions to follow during this stage of fulfillment |
| `preferences` | [Attributes](../../Attributes/README.md)[] | A extensible set of attributes that describe the fulfillment preferences |
| `start` | [FulfillmentStageEndpoint](../../FulfillmentStageEndpoint/README.md) | An extensible set of attributes that describe the criteria required to start this stage of fulfillment |
| `end` | [FulfillmentStageEndpoint](../../FulfillmentStageEndpoint/README.md) | An extensible set of attributes that describe the criteria required to end this stage of fulfillment |
| `fulfillmentStageAttributes` | [Attributes](../../Attributes/README.md) | An extensible set of attributes that describe this stage of fulfillment |
