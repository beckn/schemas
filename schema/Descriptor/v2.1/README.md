# Descriptor — v2.1

Schema definition for Descriptor in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Descriptor/attributes.yaml](https://schema.beckn.io/Descriptor/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Descriptor/v2.1/attributes.yaml](https://schema.beckn.io/Descriptor/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Descriptor/attributes.jsonschema.yaml](https://schema.beckn.io/Descriptor/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Descriptor/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/Descriptor/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Descriptor/context.jsonld](https://schema.beckn.io/Descriptor/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Descriptor/v2.1/context.jsonld](https://schema.beckn.io/Descriptor/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Descriptor/vocab.jsonld](https://schema.beckn.io/Descriptor/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Descriptor/v2.1/vocab.jsonld](https://schema.beckn.io/Descriptor/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `code` | no | string | A machine-readable code identifying the state or type of the entity being described. The valid values for this field are defined by the context in which the Descriptor is used (e.g. DRAFT, ACTIVE, CANCELLED, COMPLETE for a Contract status). |
| `longDesc` | no | string | Detailed description of the item |
| `shortDesc` | no | string | Short description of the item |
| `name` | no | string | Name of the entity being described |
| `thumbnailImage` | no | string | Name of the entity being described |
| `docs` | no | array | Links to downloadable business/supporting documents |
| `mediaFile` | no | array | Links to multimedia files and images |
