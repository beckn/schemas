# StopTimeUpdate — v2.0

A real-time update to the predicted arrival or departure time of a vehicle at a specific stop within a journey.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/StopTimeUpdate/attributes.yaml](https://schema.beckn.io/StopTimeUpdate/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/StopTimeUpdate/v2.0/attributes.yaml](https://schema.beckn.io/StopTimeUpdate/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/StopTimeUpdate/attributes.jsonschema.yaml](https://schema.beckn.io/StopTimeUpdate/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/StopTimeUpdate/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/StopTimeUpdate/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/StopTimeUpdate/context.jsonld](https://schema.beckn.io/StopTimeUpdate/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/StopTimeUpdate/v2.0/context.jsonld](https://schema.beckn.io/StopTimeUpdate/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/StopTimeUpdate/vocab.jsonld](https://schema.beckn.io/StopTimeUpdate/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/StopTimeUpdate/v2.0/vocab.jsonld](https://schema.beckn.io/StopTimeUpdate/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `stopId` | no | $ref: https://schema.beckn.io/Stop/v2.0/attributes.yaml#/components/schemas/Stop | Reference to the stop being updated |
| `stopSequence` | no | number | Sequence of this stop in the trip |
| `arrivalDelay` | no | number | Arrival delay in seconds (negative = early) |
| `departureDelay` | no | number | Departure delay in seconds (negative = early) |
| `scheduleRelationship` | no | string | Relationship to schedule (SCHEDULED, SKIPPED, NO_DATA) |
| `id` | no | string | Unique identifier for the tracking record |
| `url` | no | string | URL endpoint for real-time tracking information |
| `status` | no | $ref: https://schema.beckn.io/State/v2.0/attributes.yaml#/components/schemas/State | Current tracking status |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity period for this tracking record |
