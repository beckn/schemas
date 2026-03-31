# FulfillmentStage — v2.0

Schema definition for FulfillmentStage in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FulfillmentStage/attributes.yaml](https://schema.beckn.io/FulfillmentStage/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FulfillmentStage/v2.0/attributes.yaml](https://schema.beckn.io/FulfillmentStage/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FulfillmentStage/attributes.jsonschema.yaml](https://schema.beckn.io/FulfillmentStage/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FulfillmentStage/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FulfillmentStage/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FulfillmentStage/context.jsonld](https://schema.beckn.io/FulfillmentStage/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FulfillmentStage/v2.0/context.jsonld](https://schema.beckn.io/FulfillmentStage/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FulfillmentStage/vocab.jsonld](https://schema.beckn.io/FulfillmentStage/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FulfillmentStage/v2.0/vocab.jsonld](https://schema.beckn.io/FulfillmentStage/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | CPD |
| `@type` | yes | string | - |
| `id` | yes | string | A unique identifier for this stage of fulfillment |
| `instructions` | no | array | A set of instructions to follow during this stage of fulfillment |
| `preferences` | no | array | A extensible set of attributes that describe the fulfillment preferences |
| `start` | no | $ref: https://schema.beckn.io/FulfillmentStageEndpoint/attributes.yaml#/components/schemas/FulfillmentStageEndpoint | An extensible set of attributes that describe the criteria required to start this stage of fulfillment |
| `end` | no | $ref: https://schema.beckn.io/FulfillmentStageEndpoint/attributes.yaml#/components/schemas/FulfillmentStageEndpoint | An extensible set of attributes that describe the criteria required to end this stage of fulfillment |
| `fulfillmentStageAttributes` | no | $ref: https://schema.beckn.io/Attributes/attributes.yaml#/components/schemas/Attributes | An extensible set of attributes that describe this stage of fulfillment |
