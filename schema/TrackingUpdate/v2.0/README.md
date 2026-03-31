# TrackingUpdate — v2.0

A TrackingUpdate is a real-time or periodic update on the status and location of a shipment during transit. Maps to beckn:Event.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/TrackingUpdate/attributes.yaml](https://schema.beckn.io/TrackingUpdate/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/TrackingUpdate/v2.0/attributes.yaml](https://schema.beckn.io/TrackingUpdate/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/TrackingUpdate/attributes.jsonschema.yaml](https://schema.beckn.io/TrackingUpdate/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/TrackingUpdate/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/TrackingUpdate/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/TrackingUpdate/context.jsonld](https://schema.beckn.io/TrackingUpdate/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/TrackingUpdate/v2.0/context.jsonld](https://schema.beckn.io/TrackingUpdate/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/TrackingUpdate/vocab.jsonld](https://schema.beckn.io/TrackingUpdate/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/TrackingUpdate/v2.0/vocab.jsonld](https://schema.beckn.io/TrackingUpdate/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | - |
| `shipmentId` | yes | string | - |
| `status` | yes | string | - |
| `location` | no | object | - |
| `timestamp` | yes | string | - |
| `message` | no | string | Human-readable status message |
| `hub` | no | $ref: https://schema.beckn.io/Hub/attributes.yaml#/components/schemas/Hub | - |
| `driver` | no | $ref: https://schema.beckn.io/Driver/attributes.yaml#/components/schemas/Driver | - |
| `vehicle` | no | $ref: https://schema.beckn.io/Vehicle/attributes.yaml#/components/schemas/Vehicle | - |
| `exceptionDetails` | no | object | Details if this update is an exception |
| `nextAction` | no | string | Next planned action |
| `notificationSent` | no | boolean | Whether customer was notified of this update |
