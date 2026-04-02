# Participant — v2.0

Container schemas fetched from beckn.yaml. This cannot be extended as it is a reserved schema in beckn protocol. Any additional properties added to this schema can only be made using its *Attributes property

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Participant/attributes.yaml](https://schema.beckn.io/Participant/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Participant/v2.0/attributes.yaml](https://schema.beckn.io/Participant/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Participant/attributes.jsonschema.yaml](https://schema.beckn.io/Participant/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Participant/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Participant/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Participant/context.jsonld](https://schema.beckn.io/Participant/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Participant/v2.0/context.jsonld](https://schema.beckn.io/Participant/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Participant/vocab.jsonld](https://schema.beckn.io/Participant/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Participant/v2.0/vocab.jsonld](https://schema.beckn.io/Participant/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | no | string | - |
| `descriptor` | no | $ref: https://schema.beckn.io/Descriptor/v2.1/attributes.yaml#/components/schemas/Descriptor | - |
| `participantAttributes` | no | allOf | Domain-specific extension attributes for this contract. Use beckn:LogisticsContract for hyperlocal physical delivery. Use the generic Attributes schema for other fulfillment types where no well-known domain schema exists. |
