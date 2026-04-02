# Prognosis — v2.0

A real-time prediction of a vehicle's arrival or departure time at a stop, including an indication of prediction confidence.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Prognosis/attributes.yaml](https://schema.beckn.io/Prognosis/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Prognosis/v2.0/attributes.yaml](https://schema.beckn.io/Prognosis/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Prognosis/attributes.jsonschema.yaml](https://schema.beckn.io/Prognosis/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Prognosis/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Prognosis/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Prognosis/context.jsonld](https://schema.beckn.io/Prognosis/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Prognosis/v2.0/context.jsonld](https://schema.beckn.io/Prognosis/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Prognosis/vocab.jsonld](https://schema.beckn.io/Prognosis/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Prognosis/v2.0/vocab.jsonld](https://schema.beckn.io/Prognosis/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `scheduledTime` | no | string | Timetabled scheduled time |
| `estimatedTime` | no | string | Predicted actual time |
| `certainty` | no | string | Confidence of the prognosis (e.g. real, prognosis, calculated, unknown) |
| `delaySeconds` | no | number | Delay in seconds relative to the scheduled time |
| `id` | no | string | Unique identifier for the tracking record |
| `url` | no | string | URL endpoint for real-time tracking information |
| `status` | no | $ref: https://schema.beckn.io/State/v2.0/attributes.yaml#/components/schemas/State | Current tracking status |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity period for this tracking record |
