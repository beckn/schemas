# Form — v2.0

A form to be rendered at a checkout terminal.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Form](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Form` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string | CPD |
| `@type` | string |  |
| `data` | object | The form submission data |
| `mimeType` | string | This field indicates the nature and format of the form received by querying the url. MIME types are defined and standardized in IETF's RFC 6838. |
| `submissionId` | string |  |
| `url` | string | The URL from where the form can be fetched. The content fetched from the url must be processed as per the mimeType specified in this object. Once fetched, the rendering platform can choosed to render the form as-is as an embeddable element; or process it further to blend with the theme of the application. In case the interface is non-visual, the the render can process the form data and reproduce it as per the standard specified in the form. |
