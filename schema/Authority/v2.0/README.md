# Authority — v2.0

A governmental or administrative body responsible for planning, regulating, and overseeing transport services within a jurisdiction.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Authority/attributes.yaml](https://schema.beckn.io/Authority/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Authority/v2.0/attributes.yaml](https://schema.beckn.io/Authority/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Authority/attributes.jsonschema.yaml](https://schema.beckn.io/Authority/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Authority/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Authority/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Authority/context.jsonld](https://schema.beckn.io/Authority/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Authority/v2.0/context.jsonld](https://schema.beckn.io/Authority/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Authority/vocab.jsonld](https://schema.beckn.io/Authority/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Authority/v2.0/vocab.jsonld](https://schema.beckn.io/Authority/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `authorityId` | no | string | Unique identifier for the authority |
| `jurisdiction` | no | string | Geographic or administrative jurisdiction of this authority |
| `regulatoryScope` | no | string | Scope of regulatory powers (e.g. national, regional, local) |
| `id` | no | string | Unique identifier for the provider |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the provider |
| `categories` | no | $ref: https://schema.beckn.io/CategoryCode/v2.1/attributes.yaml#/components/schemas/CategoryCode | Service categories offered by the provider |
| `locations` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Locations where the provider offers services |
| `items` | no | $ref: https://schema.beckn.io/Item/v2.1/attributes.yaml#/components/schemas/Item | Items available for discovery from this provider |
| `fulfillments` | no | $ref: https://schema.beckn.io/Fulfillment/v2.1/attributes.yaml#/components/schemas/Fulfillment | Fulfillment options offered by this provider |
| `ratingsTotal` | no | number | Total number of ratings received |
| `rating` | no | $ref: https://schema.beckn.io/Rating/v2.0/attributes.yaml#/components/schemas/Rating | Aggregate rating of the provider |
