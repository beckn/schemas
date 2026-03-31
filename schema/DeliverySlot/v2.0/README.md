# DeliverySlot — v2.0

A DeliverySlot is a time window offered or agreed upon for delivery of a shipment. Maps to beckn:TimeSlot.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/DeliverySlot/attributes.yaml](https://schema.beckn.io/DeliverySlot/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/DeliverySlot/v2.0/attributes.yaml](https://schema.beckn.io/DeliverySlot/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/DeliverySlot/attributes.jsonschema.yaml](https://schema.beckn.io/DeliverySlot/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/DeliverySlot/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/DeliverySlot/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/DeliverySlot/context.jsonld](https://schema.beckn.io/DeliverySlot/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/DeliverySlot/v2.0/context.jsonld](https://schema.beckn.io/DeliverySlot/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/DeliverySlot/vocab.jsonld](https://schema.beckn.io/DeliverySlot/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/DeliverySlot/v2.0/vocab.jsonld](https://schema.beckn.io/DeliverySlot/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | - |
| `date` | yes | string | - |
| `startTime` | yes | string | - |
| `endTime` | yes | string | - |
| `label` | no | string | Human-readable label |
| `available` | no | boolean | Whether this slot is still available |
| `surcharge` | no | object | Additional charge for this slot (e.g. express slot) |
| `capacity` | no | integer | Maximum deliveries in this slot |
| `remainingCapacity` | no | integer | - |
| `cutoffTime` | no | string | Last time to book this slot |
