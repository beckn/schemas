# TransportObject — v2.0

A generic transport entity in the OSLO mobility ontology representing any object involved in transport operations.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/TransportObject/attributes.yaml](https://schema.beckn.io/TransportObject/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/TransportObject/v2.0/attributes.yaml](https://schema.beckn.io/TransportObject/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/TransportObject/attributes.jsonschema.yaml](https://schema.beckn.io/TransportObject/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/TransportObject/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/TransportObject/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/TransportObject/context.jsonld](https://schema.beckn.io/TransportObject/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/TransportObject/v2.0/context.jsonld](https://schema.beckn.io/TransportObject/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/TransportObject/vocab.jsonld](https://schema.beckn.io/TransportObject/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/TransportObject/v2.0/vocab.jsonld](https://schema.beckn.io/TransportObject/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `objectType` | no | string | Type of transport object (e.g. VEHICLE, INFRASTRUCTURE, ASSET) |
| `attributes` | no | string | Additional extensible attributes for this transport object |
| `id` | no | string | Unique identifier for the item |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the item |
| `categoryId` | no | $ref: https://schema.beckn.io/CategoryCode/v2.1/attributes.yaml#/components/schemas/CategoryCode | Category code classifying the item |
| `price` | no | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | Price specification for this item |
| `quantity` | no | $ref: https://schema.beckn.io/Quantity/v2.0/attributes.yaml#/components/schemas/Quantity | Available quantity of the item |
| `tags` | no | string | Tags associated with the item |
