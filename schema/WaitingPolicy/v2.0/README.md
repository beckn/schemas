# WaitingPolicy — v2.0

Rules governing the maximum time a driver is required to wait for a passenger at the pickup location before being permitted to cancel the booking.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/WaitingPolicy/attributes.yaml](https://schema.beckn.io/WaitingPolicy/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/WaitingPolicy/v2.0/attributes.yaml](https://schema.beckn.io/WaitingPolicy/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/WaitingPolicy/attributes.jsonschema.yaml](https://schema.beckn.io/WaitingPolicy/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/WaitingPolicy/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/WaitingPolicy/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/WaitingPolicy/context.jsonld](https://schema.beckn.io/WaitingPolicy/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/WaitingPolicy/v2.0/context.jsonld](https://schema.beckn.io/WaitingPolicy/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/WaitingPolicy/vocab.jsonld](https://schema.beckn.io/WaitingPolicy/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/WaitingPolicy/v2.0/vocab.jsonld](https://schema.beckn.io/WaitingPolicy/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `freeWaitingTimeMinutes` | no | number | Number of minutes the driver waits for free before charging |
| `maxWaitingTimeMinutes` | no | number | Maximum total minutes the driver will wait before auto-cancelling |
| `chargePerExtraMinute` | no | number | Additional charge per minute beyond the free waiting time |
| `currency` | no | string | ISO 4217 currency code for waiting charges |
| `id` | no | string | Unique identifier for the policy |
| `policyType` | no | string | Type of policy (extensible term) |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the policy |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity window for this policy version |
| `policyAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Extensible domain-specific policy attributes |
