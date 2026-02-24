# Organization — v2.0

An organisation entity.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Organization](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Organization` |

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
| `id` | string | Unique identifier for the organization |
| `name` | string | Name of the organization |
| `email` | string | Email address |
| `telephone` | string | Telephone number |
| `address` |  | Physical address |
| `credentials` | [Credential](../../Credential/README.md)[] | Credentials held by the organization |
| `skills` | [Skill](../../Skill/README.md)[] | Skills or capabilities of the organization |
| `organizationAttributes` | [Attributes](../../Attributes/README.md) | Extensible attribute pack for jurisdictional or domain-specific organization properties |
