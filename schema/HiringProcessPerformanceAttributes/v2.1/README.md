# HiringProcessPerformanceAttributes — v2.1

Execution state of the hiring process service. Covers the pipeline from initial screening through to offer acceptance or withdrawal. Includes optional credential verification triggered by the employer during the hiring process.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/HiringProcessPerformanceAttributes/attributes.yaml](https://schema.beckn.io/HiringProcessPerformanceAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/HiringProcessPerformanceAttributes/v2.1/attributes.yaml](https://schema.beckn.io/HiringProcessPerformanceAttributes/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/HiringProcessPerformanceAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/HiringProcessPerformanceAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/HiringProcessPerformanceAttributes/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/HiringProcessPerformanceAttributes/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/HiringProcessPerformanceAttributes/context.jsonld](https://schema.beckn.io/HiringProcessPerformanceAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/HiringProcessPerformanceAttributes/v2.1/context.jsonld](https://schema.beckn.io/HiringProcessPerformanceAttributes/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/HiringProcessPerformanceAttributes/vocab.jsonld](https://schema.beckn.io/HiringProcessPerformanceAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/HiringProcessPerformanceAttributes/v2.1/vocab.jsonld](https://schema.beckn.io/HiringProcessPerformanceAttributes/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `stage` | yes | string | Current stage of the hiring pipeline. |
| `interview_schedule` | no | array | Scheduled interview sessions, if applicable. |
| `assessment_required` | no | boolean | Whether a formal technical or aptitude assessment is required. |
| `assessment_reference` | no | string | External reference ID for the assessment (e.g. a test platform link or reference number). Only present when assessment_required = true.  |
| `verification_requested` | no | boolean | Whether the employer has triggered credential verification for this candidate. |
| `verification_summary` | no | $ref: ../../../VerificationSummary/attributes.jsonschema.yaml#/components/schemas/VerificationSummary | Outcome of employer-triggered credential verification. Only populated when verification_requested = true.  |
