# Person — v2.0

A person (alive, deceased, or fictional). Modeled after schema.org/Person.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Person/attributes.yaml](https://schema.beckn.io/Person/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Person/v2.0/attributes.yaml](https://schema.beckn.io/Person/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Person/attributes.jsonschema.yaml](https://schema.beckn.io/Person/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Person/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Person/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Person/context.jsonld](https://schema.beckn.io/Person/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Person/v2.0/context.jsonld](https://schema.beckn.io/Person/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Person/vocab.jsonld](https://schema.beckn.io/Person/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Person/v2.0/vocab.jsonld](https://schema.beckn.io/Person/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `id` | yes | string | Unique identifier for the person |
| `name` | no | string | Full name of the person |
| `email` | no | string | Email address |
| `telephone` | no | string | Telephone number |
| `address` | no | any | Physical address |
| `age` | no | integer | Age in years |
| `knowsLanguage` | no | array | Languages known by the person (BCP-47 codes or language names) |
| `worksFor` | no | $ref: https://schema.beckn.io/Organization/v2.0/attributes.yaml#/components/schemas/Organization | Organization the person works for |
| `credentials` | no | array | Credentials held by the person |
| `skills` | no | array | Skills possessed by the person |
| `personAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Extensible attribute pack for jurisdictional or domain-specific person properties |
