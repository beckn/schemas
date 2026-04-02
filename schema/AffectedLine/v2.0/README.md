# AffectedLine — v2.0

A reference to a transport line that is affected by a service disruption or alert.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/AffectedLine/attributes.yaml](https://schema.beckn.io/AffectedLine/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/AffectedLine/v2.0/attributes.yaml](https://schema.beckn.io/AffectedLine/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/AffectedLine/attributes.jsonschema.yaml](https://schema.beckn.io/AffectedLine/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/AffectedLine/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/AffectedLine/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/AffectedLine/context.jsonld](https://schema.beckn.io/AffectedLine/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/AffectedLine/v2.0/context.jsonld](https://schema.beckn.io/AffectedLine/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/AffectedLine/vocab.jsonld](https://schema.beckn.io/AffectedLine/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/AffectedLine/v2.0/vocab.jsonld](https://schema.beckn.io/AffectedLine/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `lineId` | no | string | Identifier of the affected transport line |
| `lineRef` | no | $ref: https://schema.beckn.io/Line/v2.0/attributes.yaml#/components/schemas/Line | Reference to the affected Line entity |
| `affectedStops` | no | $ref: https://schema.beckn.io/Stop/v2.0/attributes.yaml#/components/schemas/Stop | Stops on this line affected by the disruption |
| `cause` | no | string | Cause of the disruption affecting this line |
| `id` | no | string | Unique identifier for the alert |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the alert |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Time period during which the alert is active |
| `status` | no | $ref: https://schema.beckn.io/State/v2.0/attributes.yaml#/components/schemas/State | Current status of the alert |
