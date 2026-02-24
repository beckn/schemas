# Fulfillment — v2.0

A fulfillment record associated with a contract.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Fulfillment](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Fulfillment` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string | JSON-LD context URI |
| `@type` | string |  |
| `agent` | [FulfillmentAgent](../../FulfillmentAgent/README.md) | The entity that directly performs the fulfillment |
| `fulfillmentAttributes` | [Attributes](../../Attributes/README.md) | Extensible set of domain-specific attributes describing the fulfillment |
| `id` | string | Fulfillment identifier |
| `instructions` | [Descriptor](../../Descriptor/README.md)[] |  |
| `mode` | [FulfillmentMode](../../FulfillmentMode/README.md) | Extensible set of attributes describing the mode of fulfillment. Varies with Industry Use Case |
| `participants` | [Participant](../../Participant/README.md)[] | A list of participants who are entitled to receive the fulfillment of the order. By default, it is the consumer who placed the order |
| `state` | [State](../../State/README.md) | The current state of fulfillment |
| `stages` | [FulfillmentStage](../../FulfillmentStage/README.md)[] | The various stages of the fulfillment |
| `trackingEnabled` | boolean | Whether tracking is enabled / possible for this fulfillment |
