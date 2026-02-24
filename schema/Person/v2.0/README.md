# Person — v2.0

A person entity.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Person](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Person` |

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
| `id` | string | Unique identifier for the person |
| `name` | string | Full name of the person |
| `email` | string | Email address |
| `telephone` | string | Telephone number |
| `address` |  | Physical address |
| `age` | integer | Age in years |
| `knowsLanguage` | string[] | Languages known by the person (BCP-47 codes or language names) |
| `worksFor` | [Organization](../../Organization/README.md) | Organization the person works for |
| `credentials` | [Credential](../../Credential/README.md)[] | Credentials held by the person |
| `skills` | [Skill](../../Skill/README.md)[] | Skills possessed by the person |
| `personAttributes` | [Attributes](../../Attributes/README.md) | Extensible attribute pack for jurisdictional or domain-specific person properties |
