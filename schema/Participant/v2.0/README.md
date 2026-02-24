# Participant — v2.0

A participant in the Beckn network.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Participant](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Participant` |

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
| `credentials` | [Credential](../../Credential/README.md)[] |  |
| `displayName` | string |  |
| `email` | string |  |
| `id` | string |  |
| `rating` | [Rating](../../Rating/README.md) |  |
| `role` | string | Role of participant (consumer, recipient, rider, patient, operator, etc.) |
| `skills` | [Skill](../../Skill/README.md)[] |  |
| `telephone` | string |  |
