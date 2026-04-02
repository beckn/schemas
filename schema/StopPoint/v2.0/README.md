# StopPoint — v2.0

An abstract or scheduled point in a public transport network at which passengers can board or alight from a service.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/StopPoint/attributes.yaml](https://schema.beckn.io/StopPoint/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/StopPoint/v2.0/attributes.yaml](https://schema.beckn.io/StopPoint/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/StopPoint/attributes.jsonschema.yaml](https://schema.beckn.io/StopPoint/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/StopPoint/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/StopPoint/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/StopPoint/context.jsonld](https://schema.beckn.io/StopPoint/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/StopPoint/v2.0/context.jsonld](https://schema.beckn.io/StopPoint/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/StopPoint/vocab.jsonld](https://schema.beckn.io/StopPoint/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/StopPoint/v2.0/vocab.jsonld](https://schema.beckn.io/StopPoint/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `stopPointId` | no | string | Unique identifier for the stop point |
| `shortName` | no | string | Short display name or code |
| `publicCode` | no | string | Publicly visible code displayed at the stop |
| `stopAreaRef` | no | $ref: https://schema.beckn.io/StopArea/v2.0/attributes.yaml#/components/schemas/StopArea | Reference to the stop area this point belongs to |
| `id` | no | string | Unique identifier for the fulfillment stop |
| `location` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Geographic location of the stop |
| `type` | no | string | Type of stop (start, end, intermediate) |
| `instructions` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Instructions for passengers at this stop |
| `time` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Expected time window at this stop |
