# RetailItem — v2.1

A minimal retail item schema for use in Contract.commitments[].commitmentAttributes.

RetailItem is the foundational schema for items in retail transactions.
It extends beckn:Resource with the core retail item properties: price, quantity,
and verifiable credentials. Domain-specific schemas (e.g. FoodAndBeverageItem)
extend RetailItem with additional domain-specific attributes.

Inheritance: beckn:Resource ← beckn:RetailItem
Use in: beckn:Commitment.commitmentAttributes for retail orders

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/RetailItem/attributes.yaml](https://schema.beckn.io/RetailItem/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/RetailItem/v2.1/attributes.yaml](https://schema.beckn.io/RetailItem/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/RetailItem/attributes.jsonschema.yaml](https://schema.beckn.io/RetailItem/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/RetailItem/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/RetailItem/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/RetailItem/context.jsonld](https://schema.beckn.io/RetailItem/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/RetailItem/v2.1/context.jsonld](https://schema.beckn.io/RetailItem/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/RetailItem/vocab.jsonld](https://schema.beckn.io/RetailItem/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/RetailItem/v2.1/vocab.jsonld](https://schema.beckn.io/RetailItem/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| _none_ | - | - | - |
