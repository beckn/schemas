# FareLegRule — v2.0

A rule defining how a fare is applied to a single leg of a journey based on origin, destination, network, and time.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FareLegRule/attributes.yaml](https://schema.beckn.io/FareLegRule/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FareLegRule/v2.0/attributes.yaml](https://schema.beckn.io/FareLegRule/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FareLegRule/attributes.jsonschema.yaml](https://schema.beckn.io/FareLegRule/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FareLegRule/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FareLegRule/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FareLegRule/context.jsonld](https://schema.beckn.io/FareLegRule/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FareLegRule/v2.0/context.jsonld](https://schema.beckn.io/FareLegRule/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FareLegRule/vocab.jsonld](https://schema.beckn.io/FareLegRule/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FareLegRule/v2.0/vocab.jsonld](https://schema.beckn.io/FareLegRule/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `fareProductId` | no | string | Identifier of the fare product this rule applies to |
| `legGroupId` | no | string | Leg group identifier for grouping related rules |
| `networkId` | no | string | Network to which this rule is restricted |
| `fromAreaId` | no | $ref: https://schema.beckn.io/TariffZone/v2.0/attributes.yaml#/components/schemas/TariffZone | Origin tariff zone for this fare leg rule |
| `toAreaId` | no | $ref: https://schema.beckn.io/TariffZone/v2.0/attributes.yaml#/components/schemas/TariffZone | Destination tariff zone for this fare leg rule |
| `containsServiceId` | no | $ref: https://schema.beckn.io/Route/v2.0/attributes.yaml#/components/schemas/Route | Specific route this rule applies to |
| `id` | no | string | Unique identifier for the policy |
| `policyType` | no | string | Type of policy (extensible term) |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the policy |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity window for this policy version |
| `policyAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Extensible domain-specific policy attributes |
