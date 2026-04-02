# BookingRule — v2.0

A set of rules governing how and when a demand-responsive transport service must be booked in advance.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/BookingRule/attributes.yaml](https://schema.beckn.io/BookingRule/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/BookingRule/v2.0/attributes.yaml](https://schema.beckn.io/BookingRule/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/BookingRule/attributes.jsonschema.yaml](https://schema.beckn.io/BookingRule/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/BookingRule/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/BookingRule/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/BookingRule/context.jsonld](https://schema.beckn.io/BookingRule/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/BookingRule/v2.0/context.jsonld](https://schema.beckn.io/BookingRule/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/BookingRule/vocab.jsonld](https://schema.beckn.io/BookingRule/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/BookingRule/v2.0/vocab.jsonld](https://schema.beckn.io/BookingRule/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `latestBookingTime` | no | string | Latest time before departure that a booking can be made |
| `earliestBookingTime` | no | string | Earliest time before departure that a booking can be made |
| `priorNoticeDurationMin` | no | number | Minimum advance notice in minutes required for booking |
| `priorNoticeStartDay` | no | number | Earliest day before service when booking opens |
| `priorNoticeStartTime` | no | string | Time of day on the start day when booking opens |
| `message` | no | string | Customer-facing message about booking requirements |
| `phoneNumber` | no | string | Phone number to call for booking |
| `url` | no | string | URL to booking interface |
| `id` | no | string | Unique identifier for the policy |
| `policyType` | no | string | Type of policy (extensible term) |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the policy |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity window for this policy version |
| `policyAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Extensible domain-specific policy attributes |
