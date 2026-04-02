# SalesOfferPackage — v2.0

A combination of one or more fare products bundled for sale through a specific distribution channel.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/SalesOfferPackage/attributes.yaml](https://schema.beckn.io/SalesOfferPackage/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/SalesOfferPackage/v2.0/attributes.yaml](https://schema.beckn.io/SalesOfferPackage/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/SalesOfferPackage/attributes.jsonschema.yaml](https://schema.beckn.io/SalesOfferPackage/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/SalesOfferPackage/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/SalesOfferPackage/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/SalesOfferPackage/context.jsonld](https://schema.beckn.io/SalesOfferPackage/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/SalesOfferPackage/v2.0/context.jsonld](https://schema.beckn.io/SalesOfferPackage/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/SalesOfferPackage/vocab.jsonld](https://schema.beckn.io/SalesOfferPackage/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/SalesOfferPackage/v2.0/vocab.jsonld](https://schema.beckn.io/SalesOfferPackage/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `fareProducts` | no | $ref: https://schema.beckn.io/FareProduct/v2.0/attributes.yaml#/components/schemas/FareProduct | Fare products included in this sales package |
| `distributions` | no | $ref: https://schema.beckn.io/DistributionChannel/v2.0/attributes.yaml#/components/schemas/DistributionChannel | Channels through which this package can be purchased |
| `conditionsOfTravel` | no | string | Conditions applying to the use of this package |
| `id` | no | string | Unique identifier for the offer |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the offer |
| `price` | no | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | Price specification for this offer |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity period of the offer |
| `tags` | no | string | Tags or labels associated with the offer |
