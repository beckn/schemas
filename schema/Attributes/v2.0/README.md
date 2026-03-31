# Attributes — v2.0

JSON-LD aware container for domain-specific attributes of an Item. MUST include @context (URI) and @type (compact or full IRI). Any additional properties are allowed and interpreted per the provided JSON-LD context.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Attributes/attributes.yaml](https://schema.beckn.io/Attributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Attributes/v2.0/attributes.yaml](https://schema.beckn.io/Attributes/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Attributes/attributes.jsonschema.yaml](https://schema.beckn.io/Attributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Attributes/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Attributes/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Attributes/context.jsonld](https://schema.beckn.io/Attributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Attributes/v2.0/context.jsonld](https://schema.beckn.io/Attributes/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Attributes/vocab.jsonld](https://schema.beckn.io/Attributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Attributes/v2.0/vocab.jsonld](https://schema.beckn.io/Attributes/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | Use case specific JSON-LD context URI |
| `@type` | yes | string | JSON-LD type defined within the context |
