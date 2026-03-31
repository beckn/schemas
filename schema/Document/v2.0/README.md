# Document — v2.0

A document, that can be parsed, printed, download or displayed. This has intentionally been kept separate from MediaFile as they may contain additional attributes like signature, schema etc.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Document/attributes.yaml](https://schema.beckn.io/Document/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Document/v2.0/attributes.yaml](https://schema.beckn.io/Document/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Document/attributes.jsonschema.yaml](https://schema.beckn.io/Document/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Document/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Document/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Document/context.jsonld](https://schema.beckn.io/Document/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Document/v2.0/context.jsonld](https://schema.beckn.io/Document/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Document/vocab.jsonld](https://schema.beckn.io/Document/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Document/v2.0/vocab.jsonld](https://schema.beckn.io/Document/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `label` | yes | string | The display name of the media file |
| `mimeType` | yes | string | MIME type if 'data' is provided (application/pdf, image/png, application/json). |
| `standard` | no | string | Describes the schema type in case the document follows a standard schema like a verifiableCredential |
| `url` | yes | string | URL to the document |
| `security` | no | object | - |
