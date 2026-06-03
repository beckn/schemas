# CatalogPullCallbackAction — v2.0

The real-world act by which the CS (Cataloging Service) delivers the results of a previously accepted /catalog/pull request to the subscriber's (DS) /catalog/on_pull callback endpoint.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CatalogPullCallbackAction/attributes.yaml](https://schema.beckn.io/CatalogPullCallbackAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CatalogPullCallbackAction/v2.0/attributes.yaml](https://schema.beckn.io/CatalogPullCallbackAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CatalogPullCallbackAction/attributes.jsonschema.yaml](https://schema.beckn.io/CatalogPullCallbackAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CatalogPullCallbackAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/CatalogPullCallbackAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CatalogPullCallbackAction/context.jsonld](https://schema.beckn.io/CatalogPullCallbackAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CatalogPullCallbackAction/v2.0/context.jsonld](https://schema.beckn.io/CatalogPullCallbackAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CatalogPullCallbackAction/vocab.jsonld](https://schema.beckn.io/CatalogPullCallbackAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CatalogPullCallbackAction/v2.0/vocab.jsonld](https://schema.beckn.io/CatalogPullCallbackAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `status` | yes | string | Status of the pull request result assigned by the CS. COMPLETED — the CS successfully assembled the catalog result; the DS MUST process either catalogs[] or downloadManifest. FAILED — the CS could not assemble the result; the DS MUST read the error field and MUST NOT attempt to process catalogs or downloadManifest. |
| `catalogs` | no | array | Requested catalogs inline. Present when status is COMPLETED. |
| `downloadManifest` | no | object | Metadata required to download, verify, and decode the catalog result payload from object storage. Present when status is COMPLETED and the result is too large to return inline in catalogs[]. Mutually exclusive with catalogs[] — exactly one MUST be present when status is COMPLETED. The CN MUST download the object at url, verify the checksum before processing, and MUST NOT process the content if verification fails. |
| `pagination` | no | $ref | - |
| `error` | no | $ref | Present when status is FAILED. |
