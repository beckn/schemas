# SafetyPolicy — v2.0

A set of rules, protocols, and standards governing safety requirements for drivers, vehicles, and passengers on a mobility platform.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/SafetyPolicy/attributes.yaml](https://schema.beckn.io/SafetyPolicy/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/SafetyPolicy/v2.0/attributes.yaml](https://schema.beckn.io/SafetyPolicy/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/SafetyPolicy/attributes.jsonschema.yaml](https://schema.beckn.io/SafetyPolicy/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/SafetyPolicy/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/SafetyPolicy/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/SafetyPolicy/context.jsonld](https://schema.beckn.io/SafetyPolicy/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/SafetyPolicy/v2.0/context.jsonld](https://schema.beckn.io/SafetyPolicy/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/SafetyPolicy/vocab.jsonld](https://schema.beckn.io/SafetyPolicy/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/SafetyPolicy/v2.0/vocab.jsonld](https://schema.beckn.io/SafetyPolicy/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `safetyInstructions` | no | string | Instructions and guidelines for passenger and driver safety |
| `emergencyContact` | no | $ref: https://schema.beckn.io/ContactHandle/v2.0/attributes.yaml#/components/schemas/ContactHandle | Emergency contact handle for safety incidents |
| `insuranceCoverage` | no | string | Description of insurance coverage under this policy |
| `id` | no | string | Unique identifier for the policy |
| `policyType` | no | string | Type of policy (extensible term) |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the policy |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity window for this policy version |
| `policyAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Extensible domain-specific policy attributes |
