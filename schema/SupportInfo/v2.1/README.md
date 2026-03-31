# SupportInfo — v2.1

Canonical support contact for an entity, mapped to schema.org ContactPoint.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/SupportInfo/attributes.yaml](https://schema.beckn.io/SupportInfo/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/SupportInfo/v2.1/attributes.yaml](https://schema.beckn.io/SupportInfo/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/SupportInfo/attributes.jsonschema.yaml](https://schema.beckn.io/SupportInfo/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/SupportInfo/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/SupportInfo/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/SupportInfo/context.jsonld](https://schema.beckn.io/SupportInfo/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/SupportInfo/v2.1/context.jsonld](https://schema.beckn.io/SupportInfo/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/SupportInfo/vocab.jsonld](https://schema.beckn.io/SupportInfo/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/SupportInfo/v2.1/vocab.jsonld](https://schema.beckn.io/SupportInfo/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `channels` | no | array | Available support channels. |
| `email` | no | string | Support email address. |
| `hoursAvailable` | no | string | Human-readable support hours (local time) |
| `name` | no | string | Name of the support organization or contact. |
| `telephone` | no | string | Telephone number. |
| `chat` | no | string | Embeddable chat endpoint for support. |
| `url` | no | string | Generic URL to a support page. |
| `callbackStatus` | no | string | Status of a support callback request. Indicates whether a callback has been requested, scheduled, or completed. |
