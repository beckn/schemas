# Hub — v2.0

A Hub is a logistics fulfillment center, sorting facility, or distribution point where goods are consolidated, sorted, and dispatched for onward delivery. Maps to beckn:Location.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Hub/attributes.yaml](https://schema.beckn.io/Hub/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Hub/v2.0/attributes.yaml](https://schema.beckn.io/Hub/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Hub/attributes.jsonschema.yaml](https://schema.beckn.io/Hub/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Hub/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Hub/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Hub/context.jsonld](https://schema.beckn.io/Hub/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Hub/v2.0/context.jsonld](https://schema.beckn.io/Hub/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Hub/vocab.jsonld](https://schema.beckn.io/Hub/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Hub/v2.0/vocab.jsonld](https://schema.beckn.io/Hub/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | - |
| `name` | yes | string | - |
| `code` | no | string | Short hub code |
| `place` | yes | $ref: https://schema.beckn.io/Place/v2.0/attributes.yaml#/components/schemas/Place | - |
| `type` | no | string | - |
| `operator` | no | $ref: https://schema.beckn.io/Operator/v2.0/attributes.yaml#/components/schemas/Operator | - |
| `operatingHours` | no | object | - |
| `processingCapacity` | no | object | Maximum packages processed per day |
| `serviceablePincodes` | no | array | PIN codes serviced from this hub |
| `facilities` | no | array | Facilities available at hub |
| `contactPhone` | no | string | - |
| `active` | no | boolean | - |
