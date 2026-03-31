# PullResultFile — v2.0

JSON body of `GET /catalog/pull/result/{requestId}/catalogs.json`.
Same structure as the inline `catalog` array in the callback payload —
a list of distribution-envelope catalog objects.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/PullResultFile/attributes.yaml](https://schema.beckn.io/PullResultFile/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/PullResultFile/v2.0/attributes.yaml](https://schema.beckn.io/PullResultFile/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/PullResultFile/attributes.jsonschema.yaml](https://schema.beckn.io/PullResultFile/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/PullResultFile/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/PullResultFile/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/PullResultFile/context.jsonld](https://schema.beckn.io/PullResultFile/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/PullResultFile/v2.0/context.jsonld](https://schema.beckn.io/PullResultFile/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/PullResultFile/vocab.jsonld](https://schema.beckn.io/PullResultFile/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/PullResultFile/v2.0/vocab.jsonld](https://schema.beckn.io/PullResultFile/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `catalogs` | no | array | - |
