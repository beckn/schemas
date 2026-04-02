# Operator — v2.0

An organization that provides and operates public transport or shared mobility services under a defined service agreement.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Operator/attributes.yaml](https://schema.beckn.io/Operator/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Operator/v2.0/attributes.yaml](https://schema.beckn.io/Operator/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Operator/attributes.jsonschema.yaml](https://schema.beckn.io/Operator/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Operator/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Operator/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Operator/context.jsonld](https://schema.beckn.io/Operator/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Operator/v2.0/context.jsonld](https://schema.beckn.io/Operator/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Operator/vocab.jsonld](https://schema.beckn.io/Operator/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Operator/v2.0/vocab.jsonld](https://schema.beckn.io/Operator/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `operatorId` | no | string | Unique identifier for the operator |
| `operatingRegions` | no | string | Geographic regions where the operator provides services |
| `licenseNumber` | no | string | Regulatory license or accreditation number |
| `contactInfo` | no | string | Public contact information for the operator |
| `id` | no | string | Unique identifier for the provider |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the provider |
| `categories` | no | $ref: https://schema.beckn.io/CategoryCode/v2.1/attributes.yaml#/components/schemas/CategoryCode | Service categories offered by the provider |
| `locations` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Locations where the provider offers services |
| `items` | no | $ref: https://schema.beckn.io/Item/v2.1/attributes.yaml#/components/schemas/Item | Items available for discovery from this provider |
| `fulfillments` | no | $ref: https://schema.beckn.io/Fulfillment/v2.1/attributes.yaml#/components/schemas/Fulfillment | Fulfillment options offered by this provider |
| `ratingsTotal` | no | number | Total number of ratings received |
| `rating` | no | $ref: https://schema.beckn.io/Rating/v2.0/attributes.yaml#/components/schemas/Rating | Aggregate rating of the provider |
