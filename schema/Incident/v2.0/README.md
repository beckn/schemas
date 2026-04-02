# Incident — v2.0

A reported event on the transport network that affects normal service operations, such as a disruption, roadblock, or infrastructure failure.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Incident/attributes.yaml](https://schema.beckn.io/Incident/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Incident/v2.0/attributes.yaml](https://schema.beckn.io/Incident/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Incident/attributes.jsonschema.yaml](https://schema.beckn.io/Incident/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Incident/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Incident/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Incident/context.jsonld](https://schema.beckn.io/Incident/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Incident/v2.0/context.jsonld](https://schema.beckn.io/Incident/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Incident/vocab.jsonld](https://schema.beckn.io/Incident/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Incident/v2.0/vocab.jsonld](https://schema.beckn.io/Incident/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `incidentType` | no | string | Type of incident (e.g. DISRUPTION, ROADBLOCK, MAINTENANCE) |
| `severity` | no | string | Severity level of the incident (LOW, MEDIUM, HIGH) |
| `affectedArea` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Geographic area affected by the incident |
| `startTime` | no | string | Date and time the incident started |
| `endTime` | no | string | Expected or actual end date and time of the incident |
| `id` | no | string | Unique identifier for the alert |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the alert |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Time period during which the alert is active |
| `status` | no | $ref: https://schema.beckn.io/State/v2.0/attributes.yaml#/components/schemas/State | Current status of the alert |
