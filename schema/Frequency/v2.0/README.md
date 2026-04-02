# Frequency — v2.0

A headway-based service specification indicating how often a vehicle runs on a route within a given time window.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Frequency/attributes.yaml](https://schema.beckn.io/Frequency/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Frequency/v2.0/attributes.yaml](https://schema.beckn.io/Frequency/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Frequency/attributes.jsonschema.yaml](https://schema.beckn.io/Frequency/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Frequency/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Frequency/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Frequency/context.jsonld](https://schema.beckn.io/Frequency/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Frequency/v2.0/context.jsonld](https://schema.beckn.io/Frequency/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Frequency/vocab.jsonld](https://schema.beckn.io/Frequency/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Frequency/v2.0/vocab.jsonld](https://schema.beckn.io/Frequency/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `headwaySecs` | no | number | Time in seconds between consecutive vehicle departures |
| `exactTimes` | no | boolean | Whether departures are at exact scheduled times (true) or headway-based (false) |
| `startTime` | no | string | Time at which this frequency period begins (HH:MM:SS) |
| `endTime` | no | string | Time at which this frequency period ends (HH:MM:SS) |
| `id` | no | string | Unique identifier for the constraint |
| `constraintType` | no | string | Type of constraint (extensible term) |
| `operator` | no | string | Comparator operator (e.g. <=, >=, =) |
| `value` | no | number | Numeric value of the constraint |
| `unitCode` | no | string | Unit of measure code (UN/ECE Rec 20) |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity window for this constraint |
