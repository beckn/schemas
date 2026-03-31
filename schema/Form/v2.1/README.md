# Form — v2.1

Describes a form

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Form/attributes.yaml](https://schema.beckn.io/Form/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Form/v2.1/attributes.yaml](https://schema.beckn.io/Form/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Form/attributes.jsonschema.yaml](https://schema.beckn.io/Form/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Form/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/Form/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Form/context.jsonld](https://schema.beckn.io/Form/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Form/v2.1/context.jsonld](https://schema.beckn.io/Form/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Form/vocab.jsonld](https://schema.beckn.io/Form/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Form/v2.1/vocab.jsonld](https://schema.beckn.io/Form/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | CPD |
| `@type` | yes | string | - |
| `data` | no | object | The form submission data |
| `mimeType` | no | string | This field indicates the nature and format of the form received by querying the url. MIME types are defined and standardized in IETF's RFC 6838. |
| `submissionId` | no | string | - |
| `url` | no | string | The URL from where the form can be fetched. The content fetched from the url must be processed as per the mimeType specified in this object. Once fetched, the rendering platform can choosed to render the form as-is as an embeddable element; or process it further to blend with the theme of the application. In case the interface is non-visual, the the render can process the form data and reproduce it as per the standard specified in the form. |
