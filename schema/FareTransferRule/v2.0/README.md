# FareTransferRule — v2.0

A rule defining how fares from different legs are combined when a passenger makes a transfer between services.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FareTransferRule/attributes.yaml](https://schema.beckn.io/FareTransferRule/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FareTransferRule/v2.0/attributes.yaml](https://schema.beckn.io/FareTransferRule/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FareTransferRule/attributes.jsonschema.yaml](https://schema.beckn.io/FareTransferRule/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FareTransferRule/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FareTransferRule/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FareTransferRule/context.jsonld](https://schema.beckn.io/FareTransferRule/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FareTransferRule/v2.0/context.jsonld](https://schema.beckn.io/FareTransferRule/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FareTransferRule/vocab.jsonld](https://schema.beckn.io/FareTransferRule/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FareTransferRule/v2.0/vocab.jsonld](https://schema.beckn.io/FareTransferRule/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `fareProductId` | no | string | Identifier of the fare product this transfer rule applies to |
| `transferCount` | no | number | Number of transfers permitted under this rule |
| `durationLimit` | no | number | Maximum duration in minutes for the transfer window |
| `fareTransferType` | no | string | Type of fare adjustment on transfer (e.g. FREE, DISCOUNT, ADDITIONAL_FARE) |
| `id` | no | string | Unique identifier for the policy |
| `policyType` | no | string | Type of policy (extensible term) |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the policy |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity window for this policy version |
| `policyAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Extensible domain-specific policy attributes |
