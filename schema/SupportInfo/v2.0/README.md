# SupportInfo — v2.0

Canonical support contact for an entity, mapped to schema.org ContactPoint.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/SupportInfo/attributes.yaml](https://schema.beckn.io/SupportInfo/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/SupportInfo/v2.0/attributes.yaml](https://schema.beckn.io/SupportInfo/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/SupportInfo/attributes.jsonschema.yaml](https://schema.beckn.io/SupportInfo/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/SupportInfo/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/SupportInfo/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/SupportInfo/context.jsonld](https://schema.beckn.io/SupportInfo/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/SupportInfo/v2.0/context.jsonld](https://schema.beckn.io/SupportInfo/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/SupportInfo/vocab.jsonld](https://schema.beckn.io/SupportInfo/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/SupportInfo/v2.0/vocab.jsonld](https://schema.beckn.io/SupportInfo/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `name` | no | string | Name of the support organization or contact. |
| `phone` | no | string | Telephone number. |
| `email` | no | string | Support email address. |
| `url` | no | string | Webpage or chat endpoint for support. |
| `hours` | no | string | Human-readable support hours (local time). |
| `channels` | no | array | Available support channels. |
