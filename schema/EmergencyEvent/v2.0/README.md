# EmergencyEvent — v2.0

A critical safety or operational event requiring immediate response, such as an accident, vehicle breakdown, or passenger emergency.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/EmergencyEvent/attributes.yaml](https://schema.beckn.io/EmergencyEvent/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/EmergencyEvent/v2.0/attributes.yaml](https://schema.beckn.io/EmergencyEvent/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/EmergencyEvent/attributes.jsonschema.yaml](https://schema.beckn.io/EmergencyEvent/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/EmergencyEvent/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/EmergencyEvent/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/EmergencyEvent/context.jsonld](https://schema.beckn.io/EmergencyEvent/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/EmergencyEvent/v2.0/context.jsonld](https://schema.beckn.io/EmergencyEvent/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/EmergencyEvent/vocab.jsonld](https://schema.beckn.io/EmergencyEvent/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/EmergencyEvent/v2.0/vocab.jsonld](https://schema.beckn.io/EmergencyEvent/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `emergencyType` | no | string | Type of emergency (e.g. ACCIDENT, BREAKDOWN, MEDICAL) |
| `severity` | no | string | Severity level of the emergency (LOW, MEDIUM, HIGH, CRITICAL) |
| `reportedAt` | no | string | Timestamp when the emergency was reported |
| `location` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Geographic location of the emergency |
| `id` | no | string | Unique identifier for the alert |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the alert |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Time period during which the alert is active |
| `status` | no | $ref: https://schema.beckn.io/State/v2.0/attributes.yaml#/components/schemas/State | Current status of the alert |
