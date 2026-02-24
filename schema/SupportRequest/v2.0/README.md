# SupportRequest — v2.0

A support request raised by a participant.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [SupportRequest](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `SupportRequest` |

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
| `orderId` | string | The order against which support is required |
| `ticketIds` | id[] | IDs of support ticket if open |
| `callbackPhone` | string | Telephone number of the user for callback. |
