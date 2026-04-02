# CatalogSubscription — v2.0

Full subscription record

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CatalogSubscription/attributes.yaml](https://schema.beckn.io/CatalogSubscription/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CatalogSubscription/v2.0/attributes.yaml](https://schema.beckn.io/CatalogSubscription/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CatalogSubscription/attributes.jsonschema.yaml](https://schema.beckn.io/CatalogSubscription/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CatalogSubscription/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/CatalogSubscription/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CatalogSubscription/context.jsonld](https://schema.beckn.io/CatalogSubscription/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CatalogSubscription/v2.0/context.jsonld](https://schema.beckn.io/CatalogSubscription/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CatalogSubscription/vocab.jsonld](https://schema.beckn.io/CatalogSubscription/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CatalogSubscription/v2.0/vocab.jsonld](https://schema.beckn.io/CatalogSubscription/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | Subscription UUID |
| `networkIds` | no | array | Network IDs covered by this subscription |
| `schemaTypes` | no | array | Schema type URIs filtered by this subscription (empty = wildcard "*") |
| `callbackUrl` | no | string | Delivery callback URL |
| `status` | yes | string | Lifecycle status of the subscription |
| `deliveryPolicy` | no | $ref: https://schema.beckn.io/DeliveryPolicy/v2.0/attributes.yaml#/components/schemas/DeliveryPolicy | - |
| `createdAt` | no | string | - |
| `updatedAt` | no | string | - |
