# Quay — v2.0

A specific platform, bay, or boarding area within a Stop Place at which passengers board or alight from a vehicle.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Quay/attributes.yaml](https://schema.beckn.io/Quay/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Quay/v2.0/attributes.yaml](https://schema.beckn.io/Quay/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Quay/attributes.jsonschema.yaml](https://schema.beckn.io/Quay/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Quay/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Quay/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Quay/context.jsonld](https://schema.beckn.io/Quay/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Quay/v2.0/context.jsonld](https://schema.beckn.io/Quay/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Quay/vocab.jsonld](https://schema.beckn.io/Quay/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Quay/v2.0/vocab.jsonld](https://schema.beckn.io/Quay/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `quayId` | no | string | Unique identifier for the quay |
| `publicCode` | no | string | Publicly displayed platform or bay code |
| `quayType` | no | string | Type of quay (e.g. RAIL_PLATFORM, BUS_BAY, FERRY_BERTH) |
| `stopPlaceRef` | no | $ref: https://schema.beckn.io/StopPlace/v2.0/attributes.yaml#/components/schemas/StopPlace | Reference to the parent Stop Place |
| `id` | no | string | Unique identifier for the fulfillment stop |
| `location` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Geographic location of the stop |
| `type` | no | string | Type of stop (start, end, intermediate) |
| `instructions` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Instructions for passengers at this stop |
| `time` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Expected time window at this stop |
