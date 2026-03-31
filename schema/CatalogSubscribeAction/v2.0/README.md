# CatalogSubscribeAction — v2.0

Message payload for catalog/subscription.
At least one of `networkIds` or `schemaTypes` must be non-empty.
An empty `schemaTypes` array is treated as the wildcard sentinel `"*"`,
matching all schema types for the specified networks.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CatalogSubscribeAction/attributes.yaml](https://schema.beckn.io/CatalogSubscribeAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CatalogSubscribeAction/v2.0/attributes.yaml](https://schema.beckn.io/CatalogSubscribeAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CatalogSubscribeAction/attributes.jsonschema.yaml](https://schema.beckn.io/CatalogSubscribeAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CatalogSubscribeAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/CatalogSubscribeAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CatalogSubscribeAction/context.jsonld](https://schema.beckn.io/CatalogSubscribeAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CatalogSubscribeAction/v2.0/context.jsonld](https://schema.beckn.io/CatalogSubscribeAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CatalogSubscribeAction/vocab.jsonld](https://schema.beckn.io/CatalogSubscribeAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CatalogSubscribeAction/v2.0/vocab.jsonld](https://schema.beckn.io/CatalogSubscribeAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `subscription` | yes | object | - |
