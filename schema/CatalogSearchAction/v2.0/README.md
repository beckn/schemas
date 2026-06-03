# CatalogSearchAction — v2.0

The real-world act by which a caller queries the CS (Cataloging Service) for indexed catalogs, applying optional catalog type, network, and schema type filters with pagination control.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CatalogSearchAction/attributes.yaml](https://schema.beckn.io/CatalogSearchAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CatalogSearchAction/v2.0/attributes.yaml](https://schema.beckn.io/CatalogSearchAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CatalogSearchAction/attributes.jsonschema.yaml](https://schema.beckn.io/CatalogSearchAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CatalogSearchAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/CatalogSearchAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CatalogSearchAction/context.jsonld](https://schema.beckn.io/CatalogSearchAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CatalogSearchAction/v2.0/context.jsonld](https://schema.beckn.io/CatalogSearchAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CatalogSearchAction/vocab.jsonld](https://schema.beckn.io/CatalogSearchAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CatalogSearchAction/v2.0/vocab.jsonld](https://schema.beckn.io/CatalogSearchAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `filters` | no | object | Search filters. All fields are optional; omitting a field matches all values for that dimension. |
| `limit` | no | integer | Maximum number of catalogs to return per page |
| `offset` | no | integer | Zero-based result offset for pagination |
